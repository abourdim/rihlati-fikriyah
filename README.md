# Rihlati al-Fikriyah · Mon Itinéraire Intellectuel

**Autobiographie intellectuelle d'Abdelwahhab al-Massiri (1938–2008).**
Application web trilingue interactive **+** traduction française intégrale et fidèle des dix chapitres.

🌐 **Démo** : https://abourdim.github.io/rihlati-fikriyah/
📖 **Lecture en français** : [`lecture_fr.html`](lecture_fr.html)
📕 **PDF complet (FR, 723 pages)** : [`rihlati-fikriyah_fr_complet.pdf`](rihlati-fikriyah_fr_complet.pdf)
📕 **PDF arabe original** : [`references/source-original.pdf`](references/source-original.pdf)

---

## Ce que contient le repo

### 🅰️ App trilingue interactive — `index.html`
Application web autonome (single-file, ~325 Ko) qui présente l'ouvrage en
**arabe / anglais / français** : chapitres, idées clés, chronologie, lecteur
intégré avec narrateur TTS, citations, glossaire, quiz, recherche plein texte,
mode sombre, splash bismillah, etc. Conçue pour un usage hors-ligne.

### 🇫🇷 Lecteur français autonome — `lecture_fr.html`
Page indépendante au design serif/livre (Cormorant Garamond) qui présente la
**traduction française intégrale et fidèle** des dix chapitres. Sidebar de
navigation, iframe par chapitre, raccourcis clavier (← →), URLs partageables
(`#ch04`), boutons de téléchargement PDF.

### 📄 Traduction française par chapitre — `chapters/chNN_fr.{html,pdf}`
Pour chaque chapitre, deux livrables :
- `chNN_fr.html` — page autonome, typographie soignée (lettrines, citations
  bloc, italique pour les concepts arabes translittérés, NdT en marge).
- `chNN_fr.pdf` — PDF imprimable avec pagination cuivre et titre du chapitre.

| #  | Titre français                                          | Titre arabe                                          |  Pages PDF |
|----|---------------------------------------------------------|------------------------------------------------------|-----------:|
| 1  | Les Premières Graines                                   | البذور الأولى                                         |         83 |
| 2  | Débuts de l'identité                                    | بدايات الهوية                                         |          9 |
| 3  | Aux États-Unis                                          | في الولايات المتحدة                                   |         60 |
| 4  | Du matérialisme simple à l'humanisme et à la foi        | من بساطة المادية إلى رحابة الإنسانية والإيمان         |        145 |
| 5  | Modèles cognitifs et analytiques                        | النماذج الإدراكية والتحليلية                          |          7 |
| 6  | Quelques premiers fruits                                | بعض الثمرات الأولى                                    |         83 |
| 7  | Le sionisme                                             | الصهيونية                                             |         65 |
| 8  | L'Encyclopédie : son histoire                           | الموسوعة: تاريخها                                     |         32 |
| 9  | L'Encyclopédie : les thèmes essentiels                  | الموسوعة: الموضوعات الأساسية                           |        144 |
| 10 | Dans le monde de la littérature et de l'art             | في عالم الأدب والفن                                   |         95 |
|    | **Total**                                               |                                                       |    **723** |

### 📕 PDF arabe original — `references/source-original.pdf`
Le scan complet de l'édition Dar al-Shorouk (~20 Mo, avec couche OCR).

### 📚 Bibliographie complète — `sources.html`
Inventaire des ~30 œuvres d'al-Massiri disponibles sur
[archive.org/details/Almissiri_Abdel_wahab](https://archive.org/details/Almissiri_Abdel_wahab),
classées par catégorie : Encyclopédies, Sionisme & conflit, Épistémologie & biais,
Modernité & sécularisme, Autobiographie & divers. Titres en arabe avec
traduction française indicative.

### 🛠️ Sources & matières premières
- `chapters/chNN.txt` — texte arabe brut OCR (ce qui a servi à la traduction)
- `ocr/book_structured.json` — métadonnées (titres, sous-sections, nombre de mots)
- `scripts/` — utilitaires d'export

---

## Principes de la traduction française

| Décision               | Choix                                                                |
|------------------------|----------------------------------------------------------------------|
| Fidélité               | **100 %**, aucun résumé, aucune réorganisation                        |
| Translittération       | Phonétique française (al-Massiri, al-Bayati…), pas de macrons         |
| Notes du traducteur    | Inline `<span class="ndt">[NdT : …]</span>`, rares                    |
| Concepts al-Massiri    | Préservés en italique avec glose : *ḥulūl* (immanentisme), *ḥawsala* (instrumentalisation), *fiṭra*… |
| Citations religieuses  | Italique entre guillemets, bénédictions préservées (ﷺ, ﷭)            |
| Typographie            | Guillemets « », espaces fines avant `:` `;` `?` `!`, em-dashes        |
| Usage                  | **Personnel uniquement** — al-Massiri d. 2008, encore sous copyright  |

Volumes : ~197 000 mots arabes traduits → ~276 000 mots français.

---

## Génération des PDFs

```bash
# Per-chapter (Chrome headless)
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=chapters/chNN_fr.pdf \
  "file://$PWD/chapters/chNN_fr.html"

# Combined PDF + page numbering overlay (pypdf + reportlab)
# voir scripts/build_complete_pdf.py
```

Le PDF combiné est généré avec :
- Sommaire cliquable (bookmarks pypdf, un par chapitre)
- Pagination continue 1/723 → 723/723 en cuivre
- Footer gauche italique avec titre du chapitre courant
- Compression `compress_content_streams()` pour limiter la taille (6,5 Mo)

---

## Historique des versions

Voir [CHANGELOG.md](CHANGELOG.md).

**Version actuelle : v4.1 — Bibliography**
- v4.0 : 10/10 chapitres traduits, PDFs paginés, lecteur français autonome,
  mode sombre par défaut, onglet « Le Livre » par défaut sur l'app trilingue
- v4.1 : ajout de `sources.html` (inventaire des ~30 œuvres d'al-Massiri sur
  archive.org), liens depuis l'app trilingue (3 langues) et le lecteur FR

---

## Sources & crédits

- Texte arabe original : *رحلتي الفكرية في البذور والجذور والثمر* — Dar al-Shorouk
- Couche OCR : [archive.org/details/Almissiri_Abdel_wahab](https://archive.org/details/Almissiri_Abdel_wahab)
- Auteur de l'app et du projet de traduction : Abdelhak Bourdim ([@abourdim](https://github.com/abourdim))
- Traduction française : assistée par Claude (Anthropic), relue et validée

**Ce projet n'est pas une publication commerciale.** Il vise à rendre l'œuvre
intellectuelle d'al-Massiri accessible aux lecteurs francophones et
arabophones de la diaspora, sans se substituer à l'édition imprimée originale
(*Dar al-Shorouk* — qu'il est recommandé d'acheter pour soutenir l'éditeur).
