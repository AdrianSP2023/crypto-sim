"""Robustez del modelo de precursores: umbral fijado en validación (2022), test 2023-2026, deslizamiento, por año/activo, sin los 10 mejores días.
Uso: python3 tools/precursores_robustez.py > datos/eventos/precursores_robustez.txt"""
import sys; sys.path.insert(0,'tools')
import numpy as np, pandas as pd
import precursores_subidas as P
from sklearn.ensemble import HistGradientBoostingClassifier
from analisis_historico import cluster_t
panel,_=P.load_panel("USD"); X=P.build(panel)
cols=[c for c in X.columns if c not in("fwd","activo")]
X["y5"]=(X.fwd>=5).astype(int)
tr=X[X.index<"2022-01-01"]; va=X[(X.index>="2022-01-01")&(X.index<"2023-01-01")]; te=X[X.index>="2023-01-01"].copy()
rng=np.random.RandomState(0); trn=tr[(tr.y5==1)|(rng.rand(len(tr))<0.15)]
m=HistGradientBoostingClassifier(max_depth=4,learning_rate=0.06,max_iter=250,l2_regularization=1.0,random_state=0).fit(trn[cols],trn.y5)
va=va.copy(); va["p"]=m.predict_proba(va[cols])[:,1]; te["p"]=m.predict_proba(te[cols])[:,1]
for top in (0.005,0.001):
    thr=va.p.quantile(1-top)   # umbral fijado SOLO con validación
    s=te[te.p>=thr]
    print(f"\n### umbral de VALIDACIÓN top {top*100:.1f}% (p>={thr:.3f}) -> {len(s)/len(te)*100:.2f}% de horas del test")
    s=s.copy(); s["ts"]=s.index
    keep=[]
    for a,g in s.groupby("activo"):
        last=None
        for t in g.sort_values("ts").ts:
            if last is None or (t-last)>=pd.Timedelta(hours=4): keep.append((a,t)); last=t
    e=s.set_index(["activo","ts"]).loc[pd.MultiIndex.from_tuples(keep)].reset_index()
    e["day"]=e.ts.dt.strftime("%Y-%m-%d"); e["year"]=e.ts.dt.year
    mm,t=cluster_t(e.fwd,e.day); print(f"n={len(e)} bruto {mm:+.2f} (mediana {e.fwd.median():+.2f}, t {t:+.1f}) · neto1,1 {mm-1.1:+.2f}")
    for slip in (0.3,0.6,1.0):
        print(f"  con deslizamiento extra {slip}%: neto1,1 {mm-1.1-slip:+.2f} · neto0,5 {mm-0.5-slip:+.2f}")
    print(" por año:",{y:(len(g),round(g.fwd.mean(),2)) for y,g in e.groupby('year')})
    ga=e.groupby('activo').fwd.agg(['count','mean']).sort_values('count',ascending=False)
    print(" top activos por nº entradas:",ga.head(6).round(2).to_dict('index'))
    print(" activos con media>0:",(ga['mean']>0).sum(),"de",len(ga))
    d=e.groupby('day').fwd.sum().sort_values(ascending=False)
    e2=e[~e.day.isin(d.index[:10])]; mm2,t2=cluster_t(e2.fwd,e2.day)
    print(f" sin los 10 mejores días: n={len(e2)} bruto {mm2:+.2f} (t {t2:+.1f}); días distintos {e.day.nunique()}")
    print(" distribución fwd: p10 %.1f p25 %.1f p50 %.1f p75 %.1f p90 %.1f"%tuple(np.percentile(e.fwd,[10,25,50,75,90])))
    print(" nº de entradas/día medio:",round(len(e)/e.day.nunique(),2))
