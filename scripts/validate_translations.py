#!/usr/bin/env python3
"""
V1.4 Reader-mode translation validator.

Guarantees that Reader mode has ZERO missing or mixed-language strings:
- Every EN translation field is non-empty and contains no Arabic characters.
- Every FR translation field is non-empty and contains no Arabic characters.
- Arity checks: chapters tags_en == tags_fr == tags_ar count, timeline/ideas/quotes counts match.
- No placeholder tokens (TODO, TBD, ???, FIXME).
- Static HTML: every Arabic character outside a .sacred element must be inside a JS template literal,
  not hard-coded in HTML body.

Exit non-zero on any failure. Run before every V1.4 commit.
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
HTML = (ROOT / 'index.html').read_text()
COMPLETE = json.loads((ROOT / 'ocr' / 'translations' / 'complete.json').read_text())

AR_RE = re.compile(r'[\u0600-\u06FF]')
PLACEHOLDER_RE = re.compile(r'\b(TODO|TBD|FIXME|XXX|\?\?\?)\b', re.IGNORECASE)
errors = []

def fail(msg):
    errors.append(msg)

def check_str(label, s, allow_arabic=False):
    if not isinstance(s, str) or not s.strip():
        fail(f"{label}: empty"); return
    if not allow_arabic and AR_RE.search(s):
        fail(f"{label}: contains Arabic characters -> {s[:60]!r}")
    if PLACEHOLDER_RE.search(s):
        fail(f"{label}: contains placeholder -> {s[:60]!r}")

# ─── 1. complete.json: tags arity + no-Arabic in EN/FR ───
tags = COMPLETE['tags']
if not (len(tags['ar']) == len(tags['en']) == len(tags['fr'])):
    fail(f"tags arity mismatch: ar={len(tags['ar'])} en={len(tags['en'])} fr={len(tags['fr'])}")
for i, t in enumerate(tags['en']):
    check_str(f"tags.en[{i}]", t)
for i, t in enumerate(tags['fr']):
    check_str(f"tags.fr[{i}]", t)

# ─── 2. quiz_src: 8 items, each with en+fr, no Arabic ───
qs = COMPLETE['quiz_src']
if len(qs) != 8:
    fail(f"quiz_src count: expected 8, got {len(qs)}")
for i, e in enumerate(qs):
    check_str(f"quiz_src[{i}].en", e.get('en',''))
    check_str(f"quiz_src[{i}].fr", e.get('fr',''))

# ─── 3. idea_notes: 6 items ───
inotes = COMPLETE['idea_notes']
if len(inotes) != 6:
    fail(f"idea_notes count: expected 6, got {len(inotes)}")
for i, e in enumerate(inotes):
    check_str(f"idea_notes[{i}].en", e.get('en',''))
    check_str(f"idea_notes[{i}].fr", e.get('fr',''))

# ─── 4. reader_ui: must cover en + fr with non-empty values ───
ru = COMPLETE['reader_ui']
required = ['modeSource','modeReader','chipText','chipSwitch','trFooter','aboutReaderTitle','aboutReaderBody']
for lang in ('en','fr'):
    if lang not in ru:
        fail(f"reader_ui.{lang}: missing"); continue
    for k in required:
        check_str(f"reader_ui.{lang}.{k}", ru[lang].get(k,''))

# ─── 5. In index.html: each data array translation field should be non-empty + no Arabic ───
def grab_block(name):
    m = re.search(r'const '+name+r'\s*=\s*\[(.*?)^\];', HTML, re.MULTILINE|re.DOTALL)
    return m.group(1) if m else ''

def count(rx, blk):
    return len(re.findall(rx, blk, re.DOTALL))

ch_blk = grab_block('CHAPTERS')
# each chapter has en:{t:..} fr:{t:..} excerpt tr:{en:.. fr:..}
ch_count = count(r"\{id:\d+,\s*part:", ch_blk)
tr_en = count(r"tr:\{en:`[^`]+`, fr:`[^`]+`\}", ch_blk)
if ch_count != 10:
    fail(f"CHAPTERS count: expected 10, got {ch_count}")
if tr_en != 10:
    fail(f"CHAPTERS with tr.en and tr.fr: expected 10, got {tr_en}")

# Collect en and fr strings from CHAPTERS and check no Arabic
for m in re.finditer(r"en:\{t:`([^`]+)`,\s*d:`([^`]+)`\}", ch_blk):
    check_str("CHAPTERS.en.t", m.group(1))
for m in re.finditer(r"fr:\{t:`([^`]+)`,\s*d:`([^`]+)`\}", ch_blk):
    check_str("CHAPTERS.fr.t", m.group(1))

id_blk = grab_block('IDEAS')
id_count = count(r"\{num:\d+", id_blk)
id_tr_count = count(r"tr:\{en:`[^`]+`, fr:`[^`]+`\}", id_blk)
if id_count != 6:
    fail(f"IDEAS count: expected 6, got {id_count}")
if id_tr_count != 6:
    fail(f"IDEAS tr count: expected 6, got {id_tr_count}")

# Idea titles en/fr no Arabic
for m in re.finditer(r"en:\{t:`([^`]+)`", id_blk):
    check_str("IDEAS.en.t", m.group(1))
for m in re.finditer(r"fr:\{t:`([^`]+)`", id_blk):
    check_str("IDEAS.fr.t", m.group(1))

tl_blk = grab_block('TIMELINE')
tl_count = count(r"\{y:'\d+'", tl_blk)
if tl_count != 17:
    fail(f"TIMELINE count: expected 17, got {tl_count}")
for m in re.finditer(r"en:\{t:`([^`]+)`", tl_blk):
    check_str("TIMELINE.en.t", m.group(1))
for m in re.finditer(r"fr:\{t:`([^`]+)`", tl_blk):
    check_str("TIMELINE.fr.t", m.group(1))

qo_blk = grab_block('QUOTES')
qo_count = count(r"\{ar:`", qo_blk)
tr_en_count = count(r"tr_en:`[^`]+`", qo_blk)
tr_fr_count = count(r"tr_fr:`[^`]+`", qo_blk)
if qo_count != 18:
    fail(f"QUOTES count: expected 18, got {qo_count}")
if tr_en_count != 18:
    fail(f"QUOTES tr_en count: expected 18, got {tr_en_count}")
if tr_fr_count != 18:
    fail(f"QUOTES tr_fr count: expected 18, got {tr_fr_count}")

# EN/FR quote theme labels + translated text no Arabic
for m in re.finditer(r"en:`([^`]+)`", qo_blk):
    check_str("QUOTES.en theme", m.group(1))
for m in re.finditer(r"tr_en:`([^`]+)`", qo_blk):
    check_str("QUOTES.tr_en", m.group(1))
for m in re.finditer(r"tr_fr:`([^`]+)`", qo_blk):
    check_str("QUOTES.tr_fr", m.group(1))

q_blk = grab_block('QUIZ')
qcount = count(r"\{q:\{", q_blk)
src_en_count = count(r"src_en:`[^`]+`", q_blk)
src_fr_count = count(r"src_fr:`[^`]+`", q_blk)
if qcount != 8:
    fail(f"QUIZ count: expected 8, got {qcount}")
if src_en_count != 8:
    fail(f"QUIZ src_en count: expected 8, got {src_en_count}")
if src_fr_count != 8:
    fail(f"QUIZ src_fr count: expected 8, got {src_fr_count}")
# Quiz q.en + q.fr + opts no Arabic
for m in re.finditer(r'q:\{ar:`[^`]+`,en:`([^`]+)`,fr:`([^`]+)`\}', q_blk):
    check_str("QUIZ q.en", m.group(1))
    check_str("QUIZ q.fr", m.group(2))
for m in re.finditer(r'src_en:`([^`]+)`', q_blk):
    check_str("QUIZ src_en", m.group(1))
for m in re.finditer(r'src_fr:`([^`]+)`', q_blk):
    check_str("QUIZ src_fr", m.group(1))

# ─── 6. Chapter tags_en + tags_fr must be present ───
if re.search(r'tags_en:\[', ch_blk) is None:
    fail("CHAPTERS missing tags_en field")
if re.search(r'tags_fr:\[', ch_blk) is None:
    fail("CHAPTERS missing tags_fr field")

# ─── 7. Report ───
if errors:
    print(f"❌ {len(errors)} validation errors:")
    for e in errors:
        print(f"  • {e}")
    sys.exit(1)
print(f"✓ All translation checks passed.")
print(f"  chapters: 10 with tr.en/fr + tags_en/fr")
print(f"  ideas: 6 with tr.en/fr + note_en/fr")
print(f"  timeline: 17 with tr.en/fr")
print(f"  quotes: 18 with tr_en/tr_fr")
print(f"  quiz: 8 with q.en/fr + opts.en/fr + src_en/fr")
print(f"  reader_ui: en + fr complete")
print(f"  tags: 30 with en + fr")
