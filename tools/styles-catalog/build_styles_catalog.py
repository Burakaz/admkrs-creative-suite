#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generiert docs/styles.html: animierter NOVA-Ad-Style-Katalog (184 Styles, 9:16-Previews)."""
import json, re, html as H, sys

import os
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = json.load(open(os.path.join(HERE, 'styles_data.json'), encoding='utf-8'))
SPECS = {s['name']: s for s in json.load(open(os.path.join(HERE, 'specs.json'), encoding='utf-8'))}

E = lambda t: H.escape(t or '', quote=True)

def words(t, cls='w'):
    return ''.join(f'<span class="{cls}" style="--i:{i}">{E(w)}</span> ' for i, w in enumerate((t or '').split()))

# ---------- Produkt-Grafiken (CSS-gezeichnet) ----------
def product_gfx(tone, flavor=None):
    flv = f'<i class="flv">{E(flavor)}</i>' if flavor else ''
    if tone == 'hydra':
        return f'<div class="gfx bottle"><i class="cap"></i><i class="lbl">NOVA</i>{flv}</div>'
    if tone == 'box':
        return '<div class="gfx pack"><i class="lbl">NOVA</i><i class="sub2">STARTER BOX</i></div>'
    return f'<div class="gfx can"><i class="band"></i><i class="lbl">NOVA</i>{flv}</div>'

def avatar(initial='L'):
    return f'<span class="ava">{E(initial)}</span>'

# ---------- Archetyp-Renderer (jede fn liefert inneres HTML der 9:16-Szene) ----------
def r_hookcard(s):
    return f'<div class="sc-hook"><div class="hk a1">{E(s["hook"])}</div>' + \
        (f'<div class="sb a2">{E(s.get("sub",""))}</div>' if s.get('sub') else '') + \
        (f'<div class="bdg a3">{E(s["badge"])}</div>' if s.get('badge') else '') + \
        (f'<div class="cta a3">{E(s["cta"])}</div>' if s.get('cta') else '') + '</div>'

def r_product(s):
    return f'<div class="sc-prod"><div class="hk sm a1">{E(s["hook"])}</div>{product_gfx(s["tone"], s.get("flavor"))}' + \
        (f'<div class="bdg a2">{E(s["badge"])}</div>' if s.get('badge') else '') + \
        (f'<div class="cta a3">{E(s["cta"])}</div>' if s.get('cta') else '') + '</div>'

def r_review(s):
    stars = ''.join(f'<i class="st" style="--i:{i}">★</i>' for i in range(5))
    return f'<div class="sc-rev"><div class="strs">{stars}</div><div class="hk sm a1">{E(s["hook"])}</div>' + \
        f'<div class="who a2">{avatar((s.get("label") or "L")[0].upper())}<span>{E(s.get("label") or "Lena · Verified Customer")}</span></div>' + \
        (f'<div class="bdg a3">{E(s["badge"])}</div>' if s.get('badge') else '') + '</div>'

def r_split(s):
    it = (s.get('items') or ['Vorher', 'Nachher'])[:2]
    while len(it) < 2: it.append('')
    return f'<div class="sc-split"><div class="half hL"><span class="hlbl">{E(it[0])}</span><i class="x">✕</i></div>' + \
        f'<div class="half hR"><span class="hlbl">{E(it[1])}</span><i class="ck">✓</i></div><div class="divider"></div>' + \
        f'<div class="hk xs onsplit a1">{E(s["hook"])}</div></div>'

def r_list(s):
    rows = ''.join(f'<div class="li" style="--i:{i}"><i>{i+1}</i><span>{E(x)}</span></div>' for i, x in enumerate(s.get('items') or []))
    return f'<div class="sc-list"><div class="hk sm a1">{E(s["hook"])}</div><div class="lis">{rows}</div>' + \
        (f'<div class="cta a3">{E(s["cta"])}</div>' if s.get('cta') else '') + '</div>'

def r_ui(s):
    k = s.get('ui', 'notes'); lab = E(s.get('label') or '')
    cap = f'<div class="cap-line">{words(s.get("caption") or s.get("sub") or "")}</div>' if (s.get('caption') or s.get('sub')) else ''
    if k == 'notes':
        return f'<div class="sc-ui ui-notes"><div class="statusrow"><span>9:41</span><i>•••</i></div><div class="ui-bar">Notizen</div><div class="ui-body"><div class="nhk">{E(s["hook"])}</div>{cap}</div></div>'
    if k == 'tweet':
        handle = lab if lab.startswith('@') else '@nova.nutrition'
        shown = lab.lstrip('@') if lab and not lab.startswith('@') else 'NOVA'
        return f'<div class="sc-ui ui-tweet"><div class="tw-head">{avatar("N")}<div><b>{shown}</b><span>{handle}</span></div></div><div class="tw-txt">{E(s["hook"])}</div><div class="tw-meta a3">♡ 2.418 · ↺ 312</div></div>'
    if k == 'chat':
        reply = s.get('sub') or s.get('caption') or ''
        bub_out = ('<div class="bub out a2">' + E(reply) + '</div>') if reply else ''
        return f'<div class="sc-ui ui-chat"><div class="statusrow"><span>9:41</span><i>•••</i></div><div class="ui-bar">{lab or "Mara"}</div><div class="ui-body"><div class="bub in a1">{E(s["hook"])}</div>{bub_out}</div></div>'
    if k == 'reddit':
        return f'<div class="sc-ui ui-reddit"><div class="rd-head">{lab or "r/Fitness"} · u/anna_k</div><div class="rd-title">{E(s["hook"])}</div>{cap}<div class="tw-meta a3">▲ 1,2k · 214 Kommentare</div></div>'
    if k == 'search':
        return f'<div class="sc-ui ui-search"><div class="se-box"><i class="loupe"></i><span class="typing">{E(s["hook"])}</span></div><div class="se-sug a2">{E(s.get("sub") or "")}</div></div>'
    if k == 'email':
        return f'<div class="sc-ui ui-email"><div class="statusrow"><span>9:41</span><i>•••</i></div><div class="ui-bar">Posteingang</div><div class="ui-body"><div class="em-from">NOVA <span>09:41</span></div><div class="em-subj">{E(s["hook"])}</div><div class="em-prev">{E(s.get("sub") or "")}</div></div></div>'
    if k == 'calendar':
        return f'<div class="sc-ui ui-cal"><div class="statusrow"><span>9:41</span><i>•••</i></div><div class="ui-bar">Erinnerung</div><div class="ui-body"><div class="cal-dot a1"></div><div class="nhk">{E(s["hook"])}</div>{cap}</div></div>'
    if k == 'poll':
        o = (s.get('items') or ['Ja', 'Nein'])[:2]
        return f'<div class="sc-ui ui-poll"><div class="nhk">{E(s["hook"])}</div><div class="po a1"><span>{E(o[0])}</span><i class="bar" style="--p:.72"></i></div><div class="po a2"><span>{E(o[1] if len(o)>1 else "")}</span><i class="bar" style="--p:.28"></i></div></div>'
    if k == 'playlist':
        return f'<div class="sc-ui ui-play"><div class="pl-art a1"></div><div class="nhk">{E(s["hook"])}</div><div class="em-prev">{E(s.get("sub") or "NOVA · Mix")}</div><div class="pl-bar"><i></i></div></div>'
    if k == 'dating':
        return f'<div class="sc-ui ui-date"><div class="dt-card a1"><div class="dt-ph">{product_gfx(s["tone"])}</div><div class="nhk">{E(s["hook"])}</div></div><div class="dt-acts a3"><i>✕</i><i class="lk">♥</i></div></div>'
    if k == 'maps':
        return f'<div class="sc-ui ui-maps"><div class="mp"></div><i class="cpin a1"></i><div class="nhk">{E(s["hook"])}</div>{cap}</div>'
    # comment
    return f'<div class="sc-ui ui-comment"><div class="cm a1">{avatar("J")}<div><b>jana_m</b> {E(s["hook"])}</div></div><div class="cm reply a2">{avatar("N")}<div><b>nova</b> {E(s.get("sub") or s.get("caption") or "")}</div></div></div>'

RAIL = ('<div class="rail"><i>♥</i><b>12,4k</b><i>💬</i><b>318</b><i>➦</i></div>'
        '<div class="snd"><i></i><i></i><i></i></div>')

def r_talkinghead(s):
    return f'<div class="sc-vid th"><div class="person"><i class="head"></i><i class="body"></i></div>' + \
        (f'<div class="vtag">{E(s.get("label") or "")}</div>' if s.get('label') else '') + RAIL + \
        f'<div class="cap-line">{words(s.get("caption") or s["hook"])}</div><div class="prog"><i></i></div></div>'

def r_broll(s):
    return f'<div class="sc-vid br"><div class="clips"><i class="c1"></i><i class="c2">{product_gfx(s["tone"], s.get("flavor"))}</i><i class="c3"></i></div>' + RAIL + \
        f'<div class="cap-line">{words(s.get("caption") or s["hook"])}</div><div class="prog"><i></i></div></div>'

def r_screencast(s):
    return f'<div class="sc-vid scn"><div class="scr"><div class="scr-bar"><i></i><i></i><i></i></div><div class="scr-row a1"></div><div class="scr-row w2 a2"></div><div class="scr-cur a3">→</div></div>' + \
        f'<div class="cap-line">{words(s.get("caption") or s["hook"])}</div><div class="prog"><i></i></div></div>'

def r_stat(s):
    return f'<div class="sc-stat"><div class="big">{E(s.get("num") or "24g")}</div><div class="hk sm a2">{E(s["hook"])}</div>' + \
        (f'<div class="sb a3">{E(s.get("sub",""))}</div>' if s.get('sub') else '') + '</div>'

def r_offer(s):
    return f'<div class="sc-offer"><div class="big off">{E(s.get("num") or "-30 %")}</div><div class="hk sm a1">{E(s["hook"])}</div>' + \
        (f'<div class="code a2">{E(s.get("badge") or "CODE TRYNOVA")}</div>' if True else '') + \
        (f'<div class="cta a3">{E(s.get("cta") or "Jetzt sichern")}</div>') + '</div>'

def r_carousel(s):
    it = (s.get('items') or [s.get('sub') or '', '', ''])[:3]
    cards = ''.join(f'<div class="cc"><span>{E(x)}</span></div>' for x in it if x is not None)
    return f'<div class="sc-car"><div class="hk xs a1">{E(s["hook"])}</div><div class="strip">{cards}</div><div class="dots"><i class="on"></i><i></i><i></i></div></div>'

def r_editorial(s):
    return f'<div class="sc-edit"><div class="kicker">{E(s.get("label") or "MAGAZIN")}</div><div class="ed-hl">{E(s["hook"])}</div>' + \
        f'<div class="ed-ln a1"></div><div class="ed-ln w2 a2"></div><div class="ed-ln w3 a2"></div>' + \
        (f'<div class="ed-pull a3">„{E(s.get("sub",""))}“</div>' if s.get('sub') else '') + '</div>'

def r_meme(s):
    return f'<div class="sc-meme"><div class="m-top">{E(s["hook"])}</div><div class="m-img">{product_gfx(s["tone"], s.get("flavor"))}</div>' + \
        (f'<div class="m-cap">{E(s.get("sub",""))}</div>' if s.get('sub') else '') + '</div>'

def r_kinetic(s):
    it = (s.get('items') or [s['hook']])[:3]
    ws = ''.join(f'<span class="kw" style="--i:{i}">{E(x)}</span>' for i, x in enumerate(it))
    return f'<div class="sc-kin"><div class="kwrap">{ws}</div>' + \
        (f'<div class="bdg a3">{E(s["badge"])}</div>' if s.get('badge') else '') + '</div>'

def r_collage(s):
    it = (s.get('items') or ['', '', ''])[:3]
    tiles = f'<div class="tile t1">{product_gfx(s["tone"], s.get("flavor"))}</div>' + ''.join(f'<div class="tile t{i+2}"><span>{E(x)}</span></div>' for i, x in enumerate(it[:3]))
    return f'<div class="sc-col"><div class="tiles">{tiles}</div><div class="hk xs a3">{E(s["hook"])}</div></div>'

def r_badges(s):
    it = (s.get('items') or ['★ 4,8', 'VOGUE', 'FAZ'])[:3]
    bs = ''.join(f'<div class="bw" style="--i:{i}">{E(x)}</div>' for i, x in enumerate(it))
    return f'<div class="sc-bdg"><div class="hk sm a1">{E(s["hook"])}</div><div class="bws">{bs}</div>' + \
        (f'<div class="sb a3">{E(s.get("sub",""))}</div>' if s.get('sub') else '') + '</div>'

def r_doc(s):
    return f'<div class="sc-doc"><div class="doc"><div class="doc-tab">{E(s.get("label") or "PDF")}</div><div class="doc-hl">{E(s["hook"])}</div>' + \
        f'<div class="ed-ln a1"></div><div class="ed-ln w2 a2"></div></div>' + \
        (f'<div class="cta a3">{E(s.get("cta") or "Kostenlos laden")}</div>') + '</div>'

ARCH = {'hookcard': r_hookcard, 'product': r_product, 'review': r_review, 'split': r_split, 'list': r_list,
        'ui': r_ui, 'talkinghead': r_talkinghead, 'broll': r_broll, 'screencast': r_screencast, 'stat': r_stat,
        'offer': r_offer, 'carousel': r_carousel, 'editorial': r_editorial, 'meme': r_meme, 'kinetic': r_kinetic,
        'collage': r_collage, 'badges': r_badges, 'doc': r_doc}

FALLBACK = {'static': ('hookcard', 'fadeup'), 'video': ('broll', 'progress'), 'motion': ('kinetic', 'swap'),
            'carousel': ('carousel', 'scrollx'), 'mixed': ('hookcard', 'fadeup')}

# Nur bewegte Medien werden animiert; Statics stehen still (Hausregel).
ANIMATED_ARCHS = {'talkinghead', 'broll', 'screencast', 'kinetic', 'carousel'}

def validate(s):
    w = []
    if s['arch'] == 'ui' and not s.get('ui'):
        w.append('arch=ui ohne ui-Feld -> notes'); s['ui'] = 'notes'
    if s['arch'] in ('list', 'split', 'kinetic', 'carousel') and not s.get('items'):
        w.append(f"{s['arch']} ohne items -> Fallback")
        s['items'] = ['Vorher', 'Nachher'] if s['arch'] == 'split' else [s['hook']]
    if s['arch'] in ('stat', 'offer') and not s.get('num'):
        w.append(f"{s['arch']} ohne num -> Default")
    if s['arch'] in ('talkinghead', 'broll', 'screencast') and not s.get('caption'):
        w.append(f"{s['arch']} ohne caption -> hook")
    if '—' in json.dumps(s, ensure_ascii=False):
        w.append('EM-DASH im Spec!')
    return w

def preview(style, medium):
    s = SPECS.get(style['name'])
    if not s:
        arch, anim = FALLBACK[medium]
        s = {'name': style['name'], 'arch': arch, 'anim': anim, 'tone': 'neutral',
             'hook': style['name'], 'sub': '', 'caption': style['name']}
        preview.missing.append(style['name'])
    for warn in validate(s):
        preview.warnings.append(f"{style['name']}: {warn}")
    inner = ARCH[s['arch']](s)
    animated = ' anim an-' + s['anim'] if s['arch'] in ANIMATED_ARCHS else ''
    return f'<div class="pv t-{s["tone"]}{animated}" data-arch="{s["arch"]}"><div class="safe">{inner}</div><div class="pv-ui"><span class="pv-brand">NOVA</span><span class="pv-916">9:16</span></div></div>'
preview.missing = []
preview.warnings = []

# ---------- Chips ----------
def chips(wofuer):
    found = []
    for tok in ['ToFu', 'MoFu', 'BoFu', 'Retargeting', 'B2B', 'Testing']:
        if re.search(tok, wofuer, re.I): found.append(tok)
    return found

# ---------- Seite ----------
head = open(os.path.join(HERE, 'catalog_head.html'), encoding='utf-8').read()
foot = open(os.path.join(HERE, 'catalog_foot.html'), encoding='utf-8').read()

num = 0
sections = []
gnav_links = []
for gi, g in enumerate(DATA):
    cards = []
    for st in g['styles']:
        num += 1
        q = ' '.join([st['name'], st['erkennung'], st['wofuer'], st['aufbau']]).lower()
        ch = ''.join(f'<span class="chip">{c}</span>' for c in chips(st['wofuer']))
        cards.append(f'''<div class="card" data-q="{E(q)}">
{preview(st, g['medium'])}
<div class="info">
<div class="ihead"><span class="no">{num:03d}</span><h3>{E(st['name'])}</h3></div>
<p class="erk">{E(st['erkennung'])}</p>
<div class="wof">{ch}<span>{E(st['wofuer'])}</span></div>
{'<p class="auf"><b>Aufbau:</b> ' + E(st['aufbau']) + '</p>' if st['aufbau'] else ''}
</div></div>''')
    short = g['kategorie'].replace('Static · ', '').replace('Video · ', '').replace('Motion · ', '')
    gnav_links.append(f'      <a class="g-link" href="#g{gi}">{E(short)}<span class="gc">{len(g["styles"])}</span></a>')
    sections.append(f'''<section class="grp" id="g{gi}" data-medium="{g['medium']}">
<h2>{E(g['kategorie'])} <em class="cnt">{len(g['styles'])}</em></h2>
<div class="grid">{''.join(cards)}</div>
</section>''')

out = head.replace('{{GNAV}}', '\n'.join(gnav_links)) + '\n'.join(sections) + foot
open(os.path.join(HERE, '..', '..', 'docs', 'styles.html'), 'w', encoding='utf-8').write(out)
print(f'OK: {num} Styles geschrieben. Fallback-Previews (Spec fehlte): {len(preview.missing)}')
print(f'Validierungs-Warnungen: {len(preview.warnings)}')
for w in preview.warnings: print('  WARN:', w)
for m in preview.missing: print('  fehlt:', m)
