import json,sys,collections,datetime
R='/home/claude/crypto-sim/'
s=json.load(open(R+'state/state.json')); lp=s['last_prices']
ev=[json.loads(l) for l in open(R+'state/events.jsonl')]
ex=sum(1 for e in ev if e['type']=='exit'); cl_tot=sum(len(v['closed']) for v in s['strategies'].values())
key=lambda e:(e['type'],e.get('asset'),e.get('strategy'),e.get('ts'),e.get('exit_ts'))
dup=len([k for k,v in collections.Counter(key(e) for e in ev).items() if v>1 and k[0]!='universe'])
reading=open(sys.argv[1]).read() if len(sys.argv)>1 else ''
now=datetime.datetime.now(datetime.timezone.utc)
mad=now+datetime.timedelta(hours=2)
def stats(n):
    st=s['strategies'][n]; cl=st['closed']; k=len(cl)
    w=sum(1 for c in cl if c['net_pct']>0)
    return k,(100*w/k if k else 0),(sum(c['gross_pct'] for c in cl)/k if k else 0),(sum(c['net_pct'] for c in cl)/k if k else 0),sum(c['pnl_eur'] for c in cl),len(st['positions']),st.get('blocked_filter',0)+st.get('blocked_exposure',0)
def ab(names,T0):
    out=[]
    for n in names:
        st=s['strategies'][n]
        cl=[c for c in st['closed'] if c['entry_ts']>=T0]
        real=sum(c['pnl_eur'] for c in cl)
        op=[(x,p) for x,p in st['positions'].items() if p['entry_candle']>=T0]
        un=sum(p['qty']*(lp[x]/p['entry_price']-1) for x,p in op if x in lp)
        m=len(cl)+len(op)
        out.append(f"| {n} | {len(cl)} + {len(op)} | {real+un:+.2f} | {((real+un)/m if m else 0):+.3f} | {st.get('blocked_exposure',0)} |")
    return "\n".join(out)
rows="\n".join("| %s | %d | %.0f%% | %+.2f%% | %+.2f%% | %+.2f | %d | %d |"%((n,)+stats(n)) for n in s['strategies'])
hdr="| Estrategia | Cierres | Acierto | Bruto medio | Neto medio | PnL realizado € | Abiertas | Bloqueadas |\n|---|---|---|---|---|---|---|---|\n"
ah="| Estrategia | Cerradas + abiertas | Total € | €/op | Bloqueos por tope |\n|---|---|---|---|---|\n"
print(f"""# Estado de P1 en vivo (se reescribe en cada actualización)

**Última actualización:** {now:%d/%m/%Y, %H:%M} UTC ({mad:%H:%M} Madrid). Config {json.load(open(R+'config.json'))['version']}, vuelta {s['loops']}, última vuelta {s['last_loop'][:16].replace('T',' ')} UTC, avisos: {len(s['last_warnings'])}. Integridad: {cl_tot} cierres en `state.json` y {ex} eventos `exit`, {dup} duplicados.

Contexto y decisiones: `claude/traspaso-chat-P1.md` y `claude/traspaso-actualizacion-29-09.md`. Criterio de paso a P7: `claude/plan-trading.md`. Números calculados con `state/state.json` del repo `AdrianSP2023/crypto-sim` (abiertas valoradas como `qty*(last_prices/entry_price-1)`, con `qty` en EUR). "Bloqueadas" = entradas frenadas por el filtro de amplitud o por el tope de exposición.

## Acumulado por estrategia (desde el arranque de P1, 08:49 UTC del 28/09)

{hdr}{rows}

## A/B abiertos (solo operaciones con `entry_ts ≥ T0`, realizado + no realizado)

**(b) `ruptura_estricta` frente a `ruptura_volumen`** (T0 = 1790616660, 17:31 UTC del 28/09)

{ah}{ab(['ruptura_estricta','ruptura_volumen'],1790616660)}

**(c) `macd_sin_salida` frente a `macd_momentum`** (T0 = 1790622720, 19:12 UTC del 28/09)

{ah}{ab(['macd_sin_salida','macd_momentum'],1790622720)}

**(d) tope de exposición `max_open=5`: `*_tope` frente a la original** (T0 = 1790645700, 01:35 UTC del 29/09)

{ah}{ab(['c_banda_atr_tope','c_banda_atr','ruptura_volumen_tope','ruptura_volumen'],1790645700)}

## Lectura (Claude)

{reading}""")
