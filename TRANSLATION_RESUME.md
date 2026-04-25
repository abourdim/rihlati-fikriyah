# Rihlati al-Fikriyah — Statut traduction française

> Document de reprise pour démarrer une nouvelle conversation Claude.
> Mis à jour : 2026-04-25 (ch06 poussé · ch10 source lue, traduction non commencée — reste ch10, ch04, ch09).

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
| 6 | بعض الثمرات الأولى | Quelques premiers fruits | 24 442 | 538 | ✅ Pushé | `569efc7` |
| 7 | الصهيونية | Le sionisme | 21 216 | 424 | ✅ Pushé | `6d7a327` |
| 8 | الموسوعة: تاريخها | L'Encyclopédie : son histoire | 9 741 | 201 | ✅ Pushé | `947e319` |
| 9 | الموسوعة: الموضوعات الأساسية | L'Encyclopédie : les thèmes essentiels | 45 491 | 984 | ⏳ À faire | — |
| 10 | في عالم الأدب والفن | Dans le monde de la littérature et de l'art | 29 622 | 797 | ⏳ À faire | — |

**Avancement** : 7/10 pushés (~105k mots arabes traduits / 197k = 53%).
**Ordre d'attaque restant (taille croissante)** : ch10 → ch04 → ch09.

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

## 11. État de pause sur ch10 (2026-04-25, shutdown)

**Aucun fichier `chapters/ch10_fr.html` créé pour l'instant.** ch06 est entièrement poussé (commit `569efc7`).

**Chapitre 10 — « Dans le monde de la littérature et de l'art » / في عالم الأدب والفن**
- Source : `chapters/ch10.txt` — 797 lignes / ~29,6k mots arabes
- **Contenu réel à traduire : lignes 1-585** (au-delà = bibliographie + légendes de photos + colophon, voir ci-dessous)
- Les 3 sous-sections JSON officielles + sous-sections additionnelles que l'OCR révèle :

| # | `<h2>` Titre FR proposé | `<h2>` Titre AR | Lignes source |
|---|---|---|---|
| 1 | Ma vie à l'université | حياتي في الجامعة | 2-62 |
| 2 | La littérature : mon premier et ancien amour | الأدب: حبي الأول والقديم | 63-151 |
| 3 | Écrits académiques littéraires | كتابات أكاديمية أدبية | 152-209 |
| 4 | Études en linguistique | دراسات في اللغة | 210-235 |
| 5 | Amis et connaissances parmi les littéraires | أصدقاء ومعارف من الأدباء | 236-269 |
| 6 | Histoires pour enfants | قصص الأطفال | 270-360 |
| 7 | L'architecture intérieure | المعمار الداخلي | 361-456 |
| 8 | Les autres arts | الفنون الأخرى | 457-534 |
| 9 | Réflexions finales sur le sujet/objet | تأملات أخيرة في الذات/الموضوع | 535-585 |

**Lignes 586-797 = à NE PAS traduire dans ch10_fr.html** :
- 587-654 : Liste des œuvres publiées de l'auteur (AR + EN), traductions, études sur lui — typiquement traitée en annexe séparée du livre, pas dans le chapitre.
- 657-785 : Légendes des photos (« Rihlati en images »).
- 786-796 : 4ᵉ de couverture / colophon.

**Décision suggérée pour la reprise** : ne traduire que les lignes 1-585 (les 9 sections du chapitre), et terminer le chapitre par un `<footer>` standard. Si l'utilisateur souhaite ensuite une bibliographie globale ou un index séparé, ce sera un livrable dédié (pas du périmètre ch10).

**Notes accumulées en lisant la source ch10** :
- Dr Latifa Achour / Dr Latifa al-Zayyat (présidentes successives du département) : préserver les noms tels quels.
- Anecdote disciplinaire après mort de Nasser (1970) — sujet sensible, traduire fidèlement, sans euphémisme.
- Thèse de doctorat Jihan Farouq Fouad (sous direction al-Massiri, jury Fadila Fattouh + Mohamed Anani + Ayman Bekhit) : section pédagogique importante.
- Anecdote Faber & Faber / Susan Zaslow / Fiona Macrae sur le rejet du recueil de nouvelles palestiniennes : à traduire intégralement, charge politique.
- Étude « Sermons narratifs sur la nécessité et la liberté » (Franklin's Tale de Chaucer vs Brecht *Die Ausnahme und die Regel*) : longue analyse comparative — préserver les citations en bloc-quotes.
- Dialogues avec Hillis Miller, Charles Jencks, Jacques Derrida (Le Caire, sur la déconstruction) : restituer les échanges au discours direct.
- Section enfance : Khala Sittita, contes du « Shater Hassan », SCUM-like critiques de Barbie/Teddy bear, création du personnage du chameau Zarif.
- Section architecture intérieure : longue série d'anecdotes pratiques (granolite, mhandis Mohieb, Dr Abdel Halim Ibrahim Abdel Halim, dalle « Diwan al-Mudiriyya » 1882/1300H, etc.) — préserver le concept de « ma'mar tahwili » (architecture transformatrice).
- Section arts : longue galerie (Guggenheim, Metropolitan, MET Cloisters, Kandinsky, Chagall, Bonnard, Pissarro, Mark Rothko jamais cité mais Pollock × 2, Boulez, Béjart converti à l'islam, Garaudy, Gonzalo Endara Crow, Mostafa al-Razzaz « al-Mukhalliṣ ») — beaucoup de noms propres occidentaux à transcrire fidèlement.
- Section musique : Telemann, Mozart, Tchaïkovski, Brahms, Vivaldi, Beatles, Abdel Halim Hafez, Magda al-Roumi, Kazem el-Saher, Latifa, Ghada Ragab, Salah Jahin, Sayed Hegab, anecdote Abdel Halim Nuwaira/dur "Kādanī al-hawā" de Mohamed Othman.
- Section finale : longue allégorie de Thoreau (Walden) sur l'artiste de Kuru — à traduire en bloc-quote intégrale, c'est la conclusion symbolique du livre tout entier.

**Pour reprendre dans une nouvelle conversation** :
1. Lire ce §11.
2. Lire `chapters/ch10.txt` par tranches (≤ 100 lignes par lecture).
3. Créer `chapters/ch10_fr.html` avec le squelette CSS standard (cf. §5) : `Chapitre X — Dans le monde de la littérature et de l'art / الفصل العاشر — في عالم الأدب والفن`.
4. Injecter chacune des 9 sections via `Edit` avant le `<footer>` (ou écrire d'un seul `Write` initial si la première section est petite, puis `Edit` pour les suivantes).
5. Workflow standard : PDF Chrome headless → `git add` + `git commit` + `git push` → `/usr/bin/afplay /System/Library/Sounds/Glass.aiff`.
6. Mettre à jour §2 et §11 du présent document.

Une fois ch10 poussé : reste ch04 (43k mots) puis ch09 (45,5k mots) — les deux plus gros, bien aborder en plusieurs phases.

---

## 11.b Archive de l'ancien §11 (ch06, résolu le 2026-04-25)

**Fichier local non commité** : `chapters/ch06_fr.html` (188 lignes, taille = Phase 1 uniquement)

**Couverture actuelle = lignes source 1-145 sur 538 (≈ 27 % du chapitre)**

Sections déjà traduites et présentes dans le HTML, dans cet ordre :
- Header complet : « Chapitre VI — Quelques premiers fruits / بعض الثمرات الأولى »
- Préambule (lignes 1-15) : séquence modélique, instant modélique, définition par termes voisins
- `<h2>` **L'immanentisme / الحلولية** (lignes 16-76) : sonnet de Wordsworth, deux types d'unité de l'Être (spirituelle / matérielle), séquence en 4 étapes de l'immanentisme matérialiste, anecdote de la nuit de Sayyed al-Badawi
- `<h2>` **La sécularisation totale / العلمانية الشاملة** (lignes 77-145) : laïcité partielle vs totale, anecdote John Keane « post-secularism », exemple du photographe Araki, exemple du sport, séquence de sécularisation, Bauman, Spinoza-Hegel, plan de l'Encyclopédie en 4 volumes, livres de dialogue avec al-Azmeh et al-Triki

Le fichier se termine actuellement par `<footer>...</footer>` (lignes 180-184). **Phase 2+ doit injecter le contenu AVANT le `<footer>` via `Edit`.**

**Reste à traduire et injecter — lignes source 146-538 (≈ 73 %), 7 sections** :

| # | `<h2>` Titre FR | `<h2>` Titre AR | Lignes source |
|---|---|---|---|
| 1 | Le capitalisme et l'idée du retour à la nature | الرأسمالية وفكرة العودة للطبيعة | 146-170 |
| 2 | Thèse de doctorat : préambule | رسالة الدكتوراه: تمهيد | 171-204 |
| 3 | La conscience historique et la conscience anti-historique | الوجدان التاريخي والوجدان المعادي للتاريخ | 205-251 |
| 4 | Le Paradis terrestre : le progrès et le darwinisme | الفردوس الأرضي: التقدم والداروينية | 252-294 |
| 5 | Le Paradis terrestre : la nouvelle Sion en Israël et aux États-Unis | الفردوس الأرضي: صهيون الجديدة في إسرائيل والولايات المتحدة | 295-330 |
| 6 | Le Paradis terrestre : le contrat de mariage exhaustif | الفردوس الأرضي: عقد الزواج الشامل | 331-389 |
| 7 | La problématique du biais : mes expériences personnelles | إشكالية التحيز: تجاربي الخاصة | 390-463 |
| 8 | La problématique du biais : la reconstruction civilisationnelle | إشكالية التحيز: التعمير الحضاري | 464-498 |
| 9 | La problématique du biais : la conférence et le livre | إشكالية التحيز: المؤتمر والكتاب | 499-535 |

(Lignes 536-538 = début du Chapitre 7 — **NE PAS** inclure dans ch06.)

**Pour reprendre — étapes** :
1. Lire le source en plusieurs `Read offset/limit` (≤ 100 lignes par lecture pour rester sous la limite de tokens).
2. Pour chaque section, traduire intégralement (aucun résumé) et `Edit`-injecter le bloc `<h2>...</h2>` + paragraphes **juste avant** la balise `<footer>` du fichier `ch06_fr.html`.
3. Une fois TOUTES les 9 sections injectées :
   ```bash
   cd /Users/besma/Desktop/02_choughl/koutoub/55-rihlati-fikriyah
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf=chapters/ch06_fr.pdf "file://$PWD/chapters/ch06_fr.html"
   git add chapters/ch06_fr.html chapters/ch06_fr.pdf
   git commit -m "Add chapter 6 French translation — Quelques premiers fruits"
   git push origin main
   /usr/bin/afplay /System/Library/Sounds/Glass.aiff
   ```
4. Mettre à jour ce document (§2 et §11), passer à ch10.

**Notes utiles déjà accumulées en lisant la source** :
- Ligne 148 : titre original anglais du premier essai = *Competitive Capitalism and Natural Man*, paru en arabe dans *Al-Tali'a* (févr. 1976) sous le titre « La capitalisme et l'idée du retour à la nature ».
- Concept-clé inventé : *« regulating myth »* / `الأسطورة الحاكمة` ou `المعتقدات الشائعة` — distinguer d'idéologie ; garder en italique + glose.
- Thèse de doctorat = *Les œuvres critiques de William Wordsworth et Walt Whitman : étude de la conscience historique et anti-historique* (Rutgers, dir. Pr. David Weimer ; jurés : Paul Fussell, Marius Bewley, William Phillips).
- Anecdote Fussell (homosexualité, divorce, etc.) — traduire sans euphémisme, l'auteur l'expose explicitement.
- Sections « Paradis terrestre » = renvois au livre *Al-Firdaws al-Ardi* (1979) ; nombreuses citations longues du livre — traduire en bloc, pas de résumé.
- Section SCUM Manifesto + New York Radical Women : citations longues à conserver intégralement.
- Lignée P. Godwin / Mary Wollstonecraft : préserver toute l'anecdote du contrat de mariage et la satire d'al-Massiri.
- Comité de reconstruction civilisationnelle al-Ahram (post-1973) : noms à transcrire — Mahmoud Fawzi, Zaki Naguib Mahmoud, Hussein Fawzi, Louis Awad, Tawfiq al-Hakim, Ahmed Bahaa al-Din, Jamil Matar, Mohamed Hassanein Heikal.
- Section finale (livre *Ishkaliyyat al-Tahayyuz*, 1995) : noms du cercle Adel Hussein — Galal Amin, Abdel Halim Ibrahim, Gouda Abdel Khaleq, Karima Karam, Tareq al-Bishri, Hoda Hegazi (épouse de l'auteur), Hamed al-Mosly, Mamdouh Fahmi, Mohamed Imara ; cercle Riyad — Saad al-Bazei, Ezzat Khattab, Mansour al-Hazimi, Aziz al-Azmeh, Mahmoud al-Zoubidi, Saad al-Suwayan ; cercle jeunes Caire — Heba Raouf, Ahmed Abdallah, Hisham Jaafar, Osama al-Qaffash, Fouad al-Saïd, Ibrahim al-Bayoumi Ghanem, Hossam al-Sayed, Hazem Salem.
- Avertissement OCR ch06 : nombreux mots scramblés (ex. `الغمصحى` pour `الفصحى`, `العنصى` pour `العصى`, et chiffres déformés). Reconstituer silencieusement quand le sens est évident ; flagger avec `<span class="ndt">[NdT: OCR endommagé]</span>` seulement si reconstitution incertaine.

**Phase 1 du ch06 (déjà dans le fichier) — ne pas retraduire** : lignes 1-145 source = de l'introduction « Avant d'aborder mes œuvres principales… » jusqu'à la phrase finissant par « *Modernité et postmodernité* » (livre dialogué avec Fathi al-Triki).
