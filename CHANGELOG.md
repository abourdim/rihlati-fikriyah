# Changelog

Toutes les versions notables du projet *Rihlati al-Fikriyah*, depuis la
référence v1.0 jusqu'à la version actuelle v4.1.

---

## v4.1 — Bibliography · 2026-04-26

### Ajouts
- **`sources.html`** — page inventaire des ~30 œuvres d'al-Massiri disponibles
  sur [archive.org/details/Almissiri_Abdel_wahab](https://archive.org/details/Almissiri_Abdel_wahab),
  classées par catégorie (Encyclopédies, Sionisme & conflit, Épistémologie & biais,
  Modernité & sécularisme, Autobiographie & divers). Titres en arabe avec
  traduction française.
- Lien **« 📚 Bibliographie complète »** ajouté dans la section *Sources* de
  l'app trilingue (AR / EN / FR).
- Lien **« 📚 Bibliographie d'al-Massiri »** ajouté dans la zone *Ressources*
  de la sidebar du lecteur français.
- README et CHANGELOG mis à jour.

---

## v4.0 — French Complete · 2026-04-26

🎉 **Première version « livre complet en français ».**

### Ajouts
- **Traduction française intégrale** des 10 chapitres (~276 000 mots français
  depuis ~197 000 mots arabes). Voir `chapters/chNN_fr.html` et `chNN_fr.pdf`.
- **PDF complet** `rihlati-fikriyah_fr_complet.pdf` (723 pages, 6,5 Mo) avec
  sommaire cliquable et pagination continue cuivre.
- **Lecteur français autonome** `lecture_fr.html` : design serif (Cormorant
  Garamond), sidebar avec badges romains (I–X) et titres bilingues, iframe
  par chapitre, navigation clavier ← →, URLs partageables (`#chNN`),
  responsive mobile (menu hamburger).
- **PDFs paginés** : footer cuivre `— page / total —` à droite + titre du
  chapitre en italique gris à gauche, sur tous les PDFs (combiné + chapitres).
- **README.md** & **CHANGELOG.md** publics.

### Modifications de l'app trilingue (`index.html`)
- Onglet **« Le Livre » actif par défaut** après le splash (au lieu d'« Accueil »).
- **Mode sombre par défaut** (`<html data-theme="dark">` + fallback localStorage).
- Lien **« 📖 Lecture en français »** ajouté dans la section *Sources* des trois
  langues (AR / EN / FR), pointant vers `lecture_fr.html`.

### Tooling
- `pypdf` pour la fusion + bookmarks + compression des content streams
- `reportlab` pour les overlays de pagination

---

## v3.0 — Enriched · 2026-04-25 (`TAG-V3.0-ENRICHED`)

7 fonctionnalités d'enrichissement de l'app trilingue : glossaire des termes
développés par al-Massiri, recherche plein texte, carte des lieux, signets,
personnages clés, bibliographie complète, citation du jour.

---

## v2.2 — Immersive · 2026-04-25 (`TAG-V2.2-IMMERSIVE`)

Mode lecture immersif : vue manuscrit, annotations, vigne décorative, mode
*stargazing*, ambient audio.

---

## v2.1 — Trilingual Read · 2026-04-25 (`TAG-V2.1-TRILINGUAL-READ`)

Onglet *Lecture* trilingue (AR / EN / FR) avec contenu verbatim.

---

## v2.0 — Full Book · 2026-04-25 (`TAG-V2.0-FULL-BOOK`)

Le livre complet (928 pages OCR) lisible dans l'app, plus 51 citations et
17 questions de quiz.

---

## v1.6 — Narrator · 2026-04-25 (`TAG-V1.6-NARRATOR`)

Narrateur audio : TTS avec mise en surbrillance karaoké, lecture en duo,
choix de voix, contrôles depuis l'écran de verrouillage.

---

## v1.5 — KISS · 2026-04-25 (`TAG-V1.5-KISS`)

Simplification : 3 drapeaux pour 3 langues, pas de toggle, ~315 lignes
supprimées.

---

## v1.4 — Reader · 2026-04-25 (`TAG-V1.4-READER`)

Mode lecteur entièrement traduit EN/FR — garantie zéro chaîne non traduite.

---

## v1.3.1 — Audit · 2026-04-25 (`TAG-V1.3.1-AUDIT`)

Audit profond : suppression d'une traduction de chronologie redondante,
inversion du label *Show/Hide*.

---

## v1.3 — Bilingual · 2026-04-25 (`TAG-V1.3-BILINGUAL`)

Bilingue : traductions EN+FR à côté de chaque bloc arabe verbatim
(repliable).

---

## v1.2 — No Generic · 2026-04-25 (`TAG-V1.2-NO-GENERIC`)

Aucun contenu générique — chaque chaîne descriptive est verbatim depuis
l'OCR du PDF.

---

## v1.1 — Faithful · 2026-04-25 (`TAG-V1.1-FAITHFUL`)

Pleine fidélité : tous les tableaux de données reconstruits à partir du
texte OCR du PDF.

---

## v1.0 — Reference · 2026-04-25 (`TAG-V1.0-REF`)

Version de référence 1.0 — app trilingue al-Massiri avec extraits PDF
fidèles.
