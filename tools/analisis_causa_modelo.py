"""Tarea 6 (paso 2 de Maestro): separar por CAUSA las horas que elige el modelo de precursores.
¿La señal funciona igual cuando el movimiento es propio del activo (noticia/flujo específico) que cuando es del mercado entero?

Sin catálogos a posteriori: todo se calcula con información hasta el cierre de la hora de disparo (misma que ve el modelo).
No hay noticias en los datos: 'noticia propia' es un PROXY de precio y volumen (movimiento del activo sobre el mercado,
con mercado plano y volumen propio disparado). [Suposición] que ese proxy capta noticia específica.

Rasgos de causa (hora t, solo pasado):
  mkt_ret6   mediana entre activos del retorno a 6 h (mercado entero)
  breadth3   fracción de activos con retorno a 3 h > 0
  rel6       retorno a 6 h del activo menos mkt_ret6 (parte propia)
  own_share  rel6 / (|rel6| + |mkt_ret6|) (0..1: cuánto del movimiento es propio)
  vol_own    volumen del activo / su mediana de 168 h  ;  vol_mkt: mediana de esa razón entre activos
Particiones declaradas ANTES de mirar resultados (primarias): mediana de own_share; mediana de breadth3.
Todo lo demás (terciles, cruce 2x2) es exploratorio y se marca como tal. Cortes por mediana de las propias 1.056 horas
(no usan el resultado). Resultado: fwd_4h_pct (referencia horaria) y tp8_slx (TP 8 % sin stop, salida 4 h, con velas de 1 min).
Control: la misma partición aplicada a TODAS las horas del test (¿el corte importa fuera del modelo?).
Uso: python3 tools/analisis_causa_modelo.py -> datos/eventos/causa_modelo_informe.txt y causa_modelo_eventos.csv
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import precursores_subidas as P  # noqa: E402
from analisis_historico import load_panel, cluster_t  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "datos" / "eventos"


def add_cause(X):
    X = X.copy()
    X["tt"] = X.index
    g = X.groupby(level=0)
    X["mkt_ret6"] = g.ret6.transform("median")
    X["mkt_ret1"] = g.ret1.transform("median")
    X["rel6"] = X.ret6 - X.mkt_ret6
    X["rel1"] = X.ret1 - X.mkt_ret1
    X["own_share"] = X.rel6 / (X.rel6.abs() + X.mkt_ret6.abs()).replace(0, np.nan)
    X["idio_abs"] = X.rel6.abs() / (X.rel6.abs() + X.mkt_ret6.abs()).replace(0, np.nan)
    X["vol_mkt"] = g.vol_z.transform("median")
    X["vol_rel"] = X.vol_z / X.vol_mkt
    return X


def stats(v, days, years):
    v = pd.Series(np.asarray(v, dtype=float))
    days = pd.Series(np.asarray(days))
    years = pd.Series(np.asarray(years))
    if len(v) < 10:
        return f"n={len(v):4d} (muestra insuficiente)"
    m, t = cluster_t(v, days)
    by_day = v.groupby(days).sum().sort_values(ascending=False)
    top10 = set(by_day.index[:10])
    v2 = v[~days.isin(top10)]
    yy = " ".join(f"{y}:{v[years == y].mean():+.1f}" for y in sorted(years.unique()) if (years == y).sum() >= 5)
    return (f"n={len(v):4d} bruto {m:+.2f} (med {v.median():+.2f}, {100*(v>0).mean():.0f}% >0, t {t:+.1f}) "
            f"neto0,5 {m-0.5:+.2f} neto1,1 {m-1.1:+.2f} | sin 10 mejores días {v2.mean():+.2f} | años {yy}")


def main():
    panel, _ = load_panel("USD")
    X = add_cause(P.build(panel))
    te = X[X.index >= "2023-01-01"]
    h = pd.read_csv(OUT / "horas_modelo.csv", parse_dates=["t_utc"])
    m1 = pd.read_csv(OUT / "modelo_1m_eventos.csv", parse_dates=["t"])
    m1 = m1.rename(columns={"asset": "asset"})[["asset", "t", "tp8_slx"]]
    h = h.merge(m1, left_on=["asset", "t_utc"], right_on=["asset", "t"], how="left").drop(columns="t")
    cols = ["idio_abs", "ret6_own", "mkt_ret6", "breadth3", "rel6", "own_share", "vol_own", "vol_mkt", "vol_rel", "rel1", "mkt_ret1"]
    te = te.assign(vol_own=te.vol_z, ret6_own=te.ret6)
    key = te.reset_index(names="ts").set_index(["activo", "ts"])[[c for c in cols if c in te.columns]]
    idx = list(zip(h.asset, h.t_utc))
    F = key.reindex(idx)
    F.index = h.index
    d = pd.concat([h, F], axis=1)
    d["day"] = d.t_utc.dt.strftime("%Y-%m-%d")
    d["year"] = d.t_utc.dt.year
    L = [f"Horas del modelo: {len(d)} (con rasgos de causa: {int(d.own_share.notna().sum())}) · con 1 min: {int(d.tp8_slx.notna().sum())}",
         "Medianas de las horas del modelo: " + " · ".join(f"{c} {d[c].median():+.3f}" for c in ["ret6_own", "mkt_ret6", "breadth3", "rel6", "own_share", "vol_own", "vol_rel"]),
         "Todas las horas del test (control): " + " · ".join(f"{c} {te[c].median():+.3f}" for c in ["mkt_ret6", "breadth3", "rel6", "own_share", "vol_z", "vol_rel"]),
         ""]
    L.append("== Referencia: todas las horas del modelo ==")
    L.append("  fwd 4 h : " + stats(d.fwd_4h_pct, d.day, d.year))
    L.append("  tp8_slx : " + stats(d.tp8_slx.dropna(), d.loc[d.tp8_slx.notna(), "day"], d.loc[d.tp8_slx.notna(), "year"]))
    L.append("")

    def block(title, mask_a, la, mask_b, lb, primary):
        L.append(f"== {title} ({'PRIMARIA' if primary else 'exploratoria'}) ==")
        for lab, mk in ((la, mask_a), (lb, mask_b)):
            s = d[mk]
            L.append(f"  {lab:34s} fwd 4h: " + stats(s.fwd_4h_pct, s.day, s.year))
            s1 = s[s.tp8_slx.notna()]
            L.append(f"  {'':34s} tp8_slx: " + stats(s1.tp8_slx, s1.day, s1.year))
        a, b = d[mask_a].fwd_4h_pct, d[mask_b].fwd_4h_pct
        ea = d[mask_a].groupby("day").fwd_4h_pct.mean(); eb = d[mask_b].groupby("day").fwd_4h_pct.mean()
        L.append(f"  Diferencia de medias (fwd 4 h): {a.mean()-b.mean():+.2f} pts · "
                 f"error típico aprox {np.sqrt(a.var()/len(a)+b.var()/len(b)):.2f} (días distintos: {len(ea)} vs {len(eb)})")
        L.append("")

    med_os = d.own_share.median(); med_br = d.breadth3.median()
    block("Activo frente al mercado, con signo (own_share; 1ª versión)", d.own_share >= med_os, f"activo rinde MÁS que mercado (own_share >= {med_os:+.2f})",
          d.own_share < med_os, "activo rinde MENOS que mercado (cae más)", True)
    block("Amplitud del mercado (breadth3): la mediana es ~0,06, casi todas las horas son de caída generalizada", d.breadth3 >= med_br, f"mercado menos débil (breadth3 >= {med_br:.2f})",
          d.breadth3 < med_br, "caída generalizada (breadth3 bajo)", True)
    med_ia = d.idio_abs.median()
    L.append(f"(Añadido tras ver la 1ª pasada: own_share con signo mezcla 'cae menos' y 'sube solo'; se añade la versión simétrica idio_abs = |rel6|/(|rel6|+|mkt_ret6|). "
             f"Horas del modelo con retorno 6 h del activo < 0: {100*(d.ret6_own<0).mean():.0f} % · con mercado (mediana) < 0: {100*(d.mkt_ret6<0).mean():.0f} %)")
    L.append("")
    block("Movimiento propio vs de mercado, simétrico (idio_abs; añadida tras 1ª pasada)", d.idio_abs >= med_ia,
          f"movimiento PROPIO (idio_abs >= {med_ia:.2f})", d.idio_abs < med_ia, "movimiento de MERCADO (idio_abs bajo)", False)
    # exploratorias
    med_vr = d.vol_rel.median()
    block("Volumen propio frente al del mercado (vol_rel)", d.vol_rel >= med_vr, f"volumen propio alto (>= {med_vr:.2f})",
          d.vol_rel < med_vr, "volumen propio normal", False)
    prop = (d.own_share >= med_os) & (d.breadth3 < med_br)
    merc = (d.own_share < med_os) & (d.breadth3 >= med_br)
    block("Cruce: 'noticia propia' (propia + mercado flojo) vs 'mercado entero' (mercado + alcista)", prop, "propia + mercado flojo",
          merc, "mercado entero + alcista", False)
    cross = {"propia+alcista": (d.own_share >= med_os) & (d.breadth3 >= med_br),
             "mercado+flojo": (d.own_share < med_os) & (d.breadth3 < med_br)}
    for k, mk in cross.items():
        s = d[mk]
        L.append(f"  (cruce restante) {k:22s} fwd 4h: " + stats(s.fwd_4h_pct, s.day, s.year))
    L.append("")
    # terciles de own_share
    q = d.own_share.quantile([1/3, 2/3]).values
    L.append("== Terciles de own_share (exploratorio) ==")
    for lab, mk in (("T1 mercado", d.own_share < q[0]), ("T2", (d.own_share >= q[0]) & (d.own_share < q[1])), ("T3 propia", d.own_share >= q[1])):
        s = d[mk]
        L.append(f"  {lab:12s} fwd 4h: " + stats(s.fwd_4h_pct, s.day, s.year))
    L.append("")
    # Control: la misma partición en todas las horas del test (no solo las del modelo)
    ctrl = te.dropna(subset=["own_share", "breadth3", "fwd"])
    L.append("== Control: mismas particiones en TODAS las horas del test (con solape, solo media y mediana) ==")
    for lab, mk in ((f"own_share >= {med_os:+.2f}", ctrl.own_share >= med_os), ("own_share bajo", ctrl.own_share < med_os),
                    (f"breadth3 >= {med_br:.2f}", ctrl.breadth3 >= med_br), ("breadth3 bajo", ctrl.breadth3 < med_br)):
        s = ctrl[mk]
        L.append(f"  {lab:22s} n={len(s):7d} fwd 4h medio {s.fwd.mean():+.3f} (mediana {s.fwd.median():+.3f})")
    L.append("")
    # Confirmación con umbrales fijados en VALIDACIÓN (2022), no en las horas de test
    from sklearn.ensemble import HistGradientBoostingClassifier
    Xa = X.copy()
    mcols = [c for c in P.build(panel).columns if c not in ("fwd", "activo")]
    Xa["y5"] = (Xa.fwd >= 5).astype(int)
    tr = Xa[Xa.index < "2022-01-01"]; va = Xa[(Xa.index >= "2022-01-01") & (Xa.index < "2023-01-01")].copy()
    rng = np.random.RandomState(0); trn = tr[(tr.y5 == 1) | (rng.rand(len(tr)) < 0.15)]
    mdl = HistGradientBoostingClassifier(max_depth=4, learning_rate=0.06, max_iter=250, l2_regularization=1.0, random_state=0).fit(trn[mcols], trn.y5)
    va["p"] = mdl.predict_proba(va[mcols])[:, 1]
    vs = va[va.p >= va.p.quantile(0.995)]
    v_ia, v_br = vs.idio_abs.median(), vs.breadth3.median()
    L.append(f"== Confirmación con cortes fijados en VALIDACIÓN 2022 (horas top 0,5 %: n={len(vs)}; mediana idio_abs {v_ia:.2f}, breadth3 {v_br:.2f}) ==")
    for lab, mk in ((f"idio_abs < {v_ia:.2f} (mercado)", d.idio_abs < v_ia), (f"idio_abs >= {v_ia:.2f} (propio)", d.idio_abs >= v_ia),
                    (f"breadth3 <= {v_br:.2f} (caída generalizada)", d.breadth3 <= v_br), (f"breadth3 > {v_br:.2f}", d.breadth3 > v_br),
                    ("ambos: mercado Y caída generalizada", (d.idio_abs < v_ia) & (d.breadth3 <= v_br))):
        sx = d[mk]; s1 = sx[sx.tp8_slx.notna()]
        L.append(f"  {lab:42s} fwd 4h: " + stats(sx.fwd_4h_pct, sx.day, sx.year))
        L.append(f"  {'':42s} tp8_slx: " + stats(s1.tp8_slx, s1.day, s1.year))
    L.append("")
    L.append("Notas: cortes por mediana de las horas del modelo (no usan el resultado); n pequeños en cruces: leer como pista, no como prueba. "
             "Sin fuente de noticias en los datos: 'propia' es proxy de precio/volumen.")
    txt = "\n".join(L)
    (OUT / "causa_modelo_informe.txt").write_text(txt + "\n", encoding="utf-8")
    d.drop(columns=["quote"], errors="ignore").to_csv(OUT / "causa_modelo_eventos.csv", index=False)
    print(txt)


if __name__ == "__main__":
    main()
