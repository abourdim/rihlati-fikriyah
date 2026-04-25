# Rihlati al-Fikriyah — Statut traduction française

> Document de reprise pour démarrer une nouvelle conversation Claude.
> Mis à jour : 2026-04-25 (après pause sur ch07).

---

## 1. Vue d'ensemble

**Projet** : Traduction française intégrale et fidèle de l'autobiographie intellectuelle d'Abdelwahhab al-Massiri (`رحلتي الفكرية في البذور والجذور والثمر`).

**Repo** : https://github.com/abourdim/rihlati-fikriyah · branche `main`
**Workdir local** : `/Users/besma/Desktop/02_choughl/koutoub/55-rihlati-fikriyah`
**GitHub Pages** : https://abourdim.github.io/rihlati-fikriyah/

**Auteur (utilisateur)** : Abdelhak Bourdim — `abdelhak.bourdim@gmail.com` · GitHub `abourdim`

---

## 2. Statut par chapitre (10 chapitres, 197k mots arabes ≈ 276k mots fr au total)

| Ch | Titre AR | Titre FR | Mots AR | Lignes | Statut | Commit |
|---:|---|---|---:|---:|---|---|
| 1 | البذور الأولى | Les Premières Graines | 25 781 | 538 | ✅ Pushé | `545d871` |
| 2 | بدايات الهوية | Débuts de l'identité | 2 369 | 49 | ✅ Pushé | `f1fa90d` |
| 3 | في الولايات المتحدة | Aux États-Unis | 19 666 | 380 | ✅ Pushé | `32d929b` |
| 4 | من بساطة المادية إلى رحابة الإنسانية والإيمان | Du matérialisme simple à l'humanisme et à la foi | 42 953 | 896 | ⏳ À faire | — |
| 5 | النماذج الإدراكية والتحليلية | Modèles cognitifs et analytiques | 1 815 | 36 | ✅ Pushé | `bf8c0cf` |
| 6 | بعض الثمرات الأولى | Quelques premiers fruits | 24 442 | 538 | ⏳ À faire | — |
| 7 | الصهيونية | Le sionisme | 21 216 | 424 | 🟡 **Partiel local** (voir §11) | — |
| 8 | الموسوعة: تاريخها | L'Encyclopédie : son histoire | 9 741 | 201 | ✅ Pushé | `947e319` |
| 9 | الموسوعة: الموضوعات الأساسية | L'Encyclopédie : les thèmes essentiels | 45 491 | 984 | ⏳ À faire | — |
| 10 | في عالم الأدب والفن | Dans le monde de la littérature et de l'art | 29 622 | 797 | ⏳ À faire | — |

**Avancement** : 5/10 pushés (~57k mots arabes traduits / 197k = 29%).
**Ordre d'attaque restant (taille croissante)** : finir ch07 → ch06 → ch10 → ch04 → ch09.

**Vérifié** : Les .txt OCR contiennent ~99,5 % du décompte JSON (cf. `ocr/book_structured.json`). Souvent la dernière phrase est coupée — flagger avec `[NdT: OCR tronqué...]`.

---

## 3. Sources et structure du repo

```
55-rihlati-fikriyah/
├── chapters/
│   ├── ch01.txt … ch10.txt          # Source arabe OCR (À TRADUIRE — c'est la vraie source)
│   ├── ch01_en.txt, ch01_fr.txt     # Anciennes traductions partielles (RÉSUMÉS — IGNORER)
│   ├── ch01_fr.html, ch01_fr.pdf    # Nouvelles traductions FR (livrables)
│   └── ch02_fr.html, ch05_fr.html   # idem
├── ocr/
│   ├── book_structured.json         # Métadonnées : titres, sous-sections, word counts
│   └── translations/                # Anciennes traductions (résumés — ignorer)
├── references/
│   └── source-original.pdf          # PDF arabe original (20 Mo, pour vérification visuelle)
├── index.html                        # App web trilingue (existante, séparée)
└── TRANSLATION_RESUME.md             # CE FICHIER
```

---

## 4. Principes de traduction (validés par l'utilisateur)

| Décision | Choix |
|---|---|
| Langue cible | **Français intégral** (pas de bilingue) |
| Fidélité | **100 % fidèle**, **aucun résumé**, aucun raccourci, aucune réorganisation |
| Format | **HTML d'abord**, PDF généré ensuite (Chrome headless) |
| Parenthèses auteur | **En ligne**, exactement comme l'original `( … )` |
| Notes traducteur | Inline, balises `<span class="ndt">[NdT: …]</span>`, **rares** |
| Translittération | **Phonétique française** (al-Massiri, al-Bayati, Damanhour, Djeddah), pas de macrons académiques |
| Noms propres | Préserver translittérations standard (La Mecque, Gamal Abdel Nasser) |
| Typographie FR | Accents complets, guillemets `« »`, espaces fines avant `:` `;` `?` `!`, em-dashes pour incises |
| Titres bilingues | Headers `<h2>` avec titre FR + titre AR en `<span class="ar">` |
| Usage | **Personnel uniquement** (al-Massiri d. 2008, encore sous copyright) |

---

## 5. Template HTML / CSS (utiliser tel quel pour cohérence)

Voir `chapters/ch01_fr.html`, `chapters/ch02_fr.html`, `chapters/ch05_fr.html` pour exemples complets.

Skeleton minimal :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>Chapitre N — Titre · Rihlati al-Fikriyah · Abdelwahhab al-Massiri</title>
<style>
  :root{--bg:#fbfaf7;--ink:#1a1a1a;--muted:#6b6b6b;--rule:#c9c2b4;--accent:#7a3a1f;--measure:65ch}
  *{box-sizing:border-box}
  html{font-size:17px}
  body{background:var(--bg);color:var(--ink);font-family:"Iowan Old Style","Cardo","Cormorant Garamond","Hoefler Text","Times New Roman",Georgia,serif;line-height:1.7;margin:0;padding:3rem 1.5rem 6rem;text-rendering:optimizeLegibility;font-feature-settings:"kern","liga","onum";hyphens:auto}
  main{max-width:var(--measure);margin:0 auto}
  header.book{border-bottom:1px solid var(--rule);padding-bottom:1.5rem;margin-bottom:2rem;text-align:center}
  header.book .work{font-size:.85rem;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);margin:0 0 .4rem}
  header.book .author{font-size:.95rem;color:var(--muted);margin:0 0 1.2rem;font-style:italic}
  header.book h1{font-size:2rem;font-weight:600;margin:0 0 .3rem;letter-spacing:-.01em;line-height:1.2}
  header.book .ar-title{font-family:"Amiri","Scheherazade New","Geeza Pro",serif;font-size:1.5rem;color:var(--accent);direction:rtl;margin:.3rem 0 0}
  header.book .meta{font-size:.78rem;color:var(--muted);margin-top:1rem;font-style:italic}
  h2{font-size:1.35rem;font-weight:600;margin:3rem 0 .2rem;border-top:1px solid var(--rule);padding-top:2rem}
  h2 .ar{display:block;font-family:"Amiri","Scheherazade New","Geeza Pro",serif;font-size:1.15rem;color:var(--accent);direction:rtl;font-weight:400;margin-top:.2rem}
  h3{font-size:1.05rem;font-weight:600;margin:2rem 0 .8rem;color:var(--accent);font-variant:small-caps;letter-spacing:.04em}
  p{margin:0 0 1.1rem;text-align:justify}
  p.first::first-letter{font-size:3.2rem;float:left;line-height:.85;padding:.3rem .6rem 0 0;font-weight:600;color:var(--accent)}
  .ndt{font-size:.85em;color:var(--muted);font-style:italic}
  footer{margin-top:4rem;padding-top:1.5rem;border-top:1px solid var(--rule);font-size:.78rem;color:var(--muted);text-align:center;font-style:italic}
  @media print{body{background:#fff;padding:1.5cm 2cm;font-size:11pt}h2{page-break-before:always}h2:first-of-type{page-break-before:auto}}
</style>
</head>
<body><main>
<header class="book">
  <p class="work">Rihlati al-Fikriyah · Mon Itinéraire Intellectuel</p>
  <p class="author">Abdelwahhab al-Massiri</p>
  <h1>Chapitre N — Titre français</h1>
  <p class="ar-title">الفصل N — العنوان</p>
  <p class="meta">Traduction française intégrale et fidèle · Usage personnel</p>
</header>

<h2>Sous-section 1<span class="ar">العنوان العربي</span></h2>
<p class="first">Premier paragraphe avec lettrine…</p>
<p>…</p>

<footer>
  Traduction française fidèle au texte arabe original<br>
  Source : <code>chapters/chNN.txt</code><br>
  Fichier de travail · Pour usage personnel uniquement
</footer>
</main></body></html>
```

---

## 6. Workflow par chapitre

```bash
# 1. Récupérer titre + nb sous-sections depuis le JSON
cd /Users/besma/Desktop/02_choughl/koutoub/55-rihlati-fikriyah
/usr/bin/python3 -c "
import json
data = json.load(open('ocr/book_structured.json'))
ch = data['8']  # remplacer par le numéro
print('TITLE:', ch['title'])
print('SUBSECTIONS:')
for s in ch['subsections']:
    print('  -', s.get('heading','?'))
"

# 2. Lire le source — pour gros chapitres, en plusieurs morceaux (Read offset/limit)
#    Note : les .txt > ~25k tokens nécessitent offset/limit obligatoirement.

# 3. Créer chapters/chNN_fr.html avec template ci-dessus
#    Pour les gros chapitres, ouvrir avec Write + paragraphes initiaux,
#    puis Edit successifs pour injecter chaque sous-section avant <footer>

# 4. Générer le PDF
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=chapters/chNN_fr.pdf \
  "file://$PWD/chapters/chNN_fr.html"

# 5. Commit + push
git add chapters/chNN_fr.html chapters/chNN_fr.pdf
git commit -m "Add chapter N French translation — Titre"
git push origin main

# 6. Bip de signal (à exécuter à la fin de chaque chapitre poussé)
/usr/bin/afplay /System/Library/Sounds/Glass.aiff
```

---

## 7. Spécificités à connaître

- **OCR endommagé** : Quelques passages ont du texte arabe corrompu (mots scramblés, chiffres bizarres comme `١4م4` au lieu de `1948`). Reconstruire le sens probable et flagger avec `<span class="ndt">[NdT: OCR endommagé, sens reconstitué]</span>`. Vérifier au besoin avec `references/source-original.pdf`.
- **Chants/poèmes folkloriques** : Garder en translittération phonétique en italique (ex. `<em>« Khashabat mīn / khashabat ḥabasha »</em>`), suivis d'une glose française si pertinent. Ne pas tenter de rimer.
- **Lignes courtes (chiffres seuls comme `5`, `1١7`)** : Numéros de page OCR — ignorer.
- **Sous-sous-sections** : `book_structured.json` ne capture pas toujours toutes les `<h3>` internes. Préserver tout titre arabe centré qui apparaît seul sur sa ligne dans le source.
- **Préserver la 1<sup>re</sup> personne et le ton autobiographique** d'al-Massiri partout.
- **Hapax al-Massiri** : il invente des mots (ex. *حوسلة* « ḥawsala » → instrumentaliser). Garder le mot en italique + glose entre parenthèses.
- **Citations bibliques/hadiths** : Format italique entre guillemets ; bénédictions « que Dieu lui fasse miséricorde » (رحمه الله), « que la prière et la paix soient sur lui » (صلى الله عليه وسلم) toujours préservées.

---

## 8. Tooling et environnement

- **macOS** : 13.7.8 Ventura (Intel)
- **Chrome** : `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome` (pour PDF headless)
- **Python** : `/usr/bin/python3` (pour parsing JSON)
- **Git** : remote `origin` = `https://github.com/abourdim/rihlati-fikriyah.git`
- **PATH zshrc** : OK (l'ancienne diagnostic de "PATH cassé" était fausse)
- **Pas besoin** : aucune dépendance externe (pas de WeasyPrint, pas de pandoc — Chrome headless suffit)

---

## 9. Mémoire Claude (contexte conservé entre sessions)

Memory file : `/Users/besma/.claude/projects/-Users-besma-Desktop-00-work-repos/memory/MEMORY.md`

Entrée pertinente : `project_choughl_alghirbal.md` (al-Ghirbal — projet voisin sur Capacitor).

Préférences utilisateur enregistrées :
- **Toujours demander avant toute action** qui change l'état (writes, push, serveurs, commandes)
- **Préfère les playbooks complets** plutôt que sélections curées
- Réponses **en français** (validé en cours de session)

---

## 10. Pour démarrer une nouvelle conversation

Coller ce prompt :

```
Je continue la traduction française de Rihlati al-Fikriyah.
Lis /Users/besma/Desktop/02_choughl/koutoub/55-rihlati-fikriyah/TRANSLATION_RESUME.md
puis reprends à partir du prochain chapitre non traduit.

Workflow : traduire intégralement et fidèlement → générer PDF → commit → push → bip
(/usr/bin/afplay /System/Library/Sounds/Glass.aiff) après chaque chapitre poussé.
Mode autonome jusqu'à terminer tous les chapitres restants.
Ne demande pas de confirmation entre chapitres.
```

---

## 11. État de pause sur ch07 (2026-04-25)

**Fichier local non commité** : `chapters/ch07_fr.html`
- Couvre approximativement les **lignes source 1-95** sur 424 (≈ 22% du chapitre).
- Contient : skeleton HTML complet + sous-section `<h2>` « Le sionisme : déconstruire et recomposer » + sous-section `<h3>` « L'objectivité réceptive et l'université ».
- Thèmes traduits : critique de l'objectivité photographique/informationnelle, pragmatisme superficiel, exemples (Bloomingdale's, Camp David, ONU, etc.), influence Marx/Weber/Bauman, problèmes académiques (dictée, polycopiés, examens, recherches sans pensée, soutenance, critères de promotion).
- **Reste à traduire** : lignes ~96-424 source, soit environ 78% du chapitre.

**Sections restantes à injecter avant le `<footer>`** (ordre dans la source) :
1. Inscription au doctorat / questionnaires / méthode des recherches (lignes ~96-115)
2. Critique de la dictée et des polycopiés (déjà partiellement couvert — vérifier le chevauchement)
3. **`<h2>` La carte cognitive (الخريطة الادراكية)** — exemple Marie-Antoinette, sionisme, Bosnie/Bin Laden, Iran/Shah, Irak (lignes ~191-241)
4. **`<h2>` Tchomsky au Caire (تشومسكي في القاهرة)** — analyse de sa pensée, dialogue (lignes ~242-287)
5. **`<h2>` Les modèles comme outil analytique (النماذج كأداة تحليلية)** — modèles d'images, allégorie de la fontaine, hadiths sur le chat et le chien, formation des modèles, exemples (lignes ~288-380)
6. **`<h3>` La séquence modélique (المتتالية النماذجية)** — application aux États-Unis, retour Égypte (lignes ~414-fin)

**Pour reprendre** :
- Soit continuer le `ch07_fr.html` existant (lire les lignes source restantes en plusieurs `Read offset/limit` puisque le fichier est gros, traduire et `Edit` injection avant `<footer>`).
- Soit recommencer à zéro si jugé plus simple.

**Avertissement OCR** : ch07 contient de nombreux artefacts OCR (lignes courtes comme « نرف », « خض », « إخرضا » etc. — ce sont des numéros de page corrompus, à ignorer). Le texte arabe lui-même contient parfois des mots scramblés ; reconstituer le sens et flagger avec `<span class="ndt">[NdT: OCR endommagé]</span>` au besoin.
