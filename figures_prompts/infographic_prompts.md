# ChatGPT image-gen prompts for hand-designed infographics

Three new infographics to be generated externally (ChatGPT image gen / DALL-E / GPT-4o), then dropped into `figures/` (English versions) and `figures_fa/` (Persian versions).

Each prompt is engineered for a single image. Paste the *entire* prompt block into the image-gen UI. The prompts request **flat vector-style design at journal-page resolution**, with the text rendered inside the image (image gen models can render readable text in 2026).

After generation:
1. Save the English PNG as `figures/figXX_<name>.png` (and PDF if available)
2. Save the Persian PNG as `figures_fa/figXX_<name>.png` (RTL layout)
3. Hand me the filenames so I can wire them into the appropriate manuscript at the right caption position

The three infographics replace or augment the corresponding matplotlib figures:
- **Infographic A** (six-stage continuum overview) → augments / replaces `fig1_continuum.pdf`
- **Infographic B** (container-metaphor triad) → replaces `fig6_metaphor_diagram.pdf`
- **Infographic C** (methodology flow diagram) → new figure, no current equivalent

---

## A. Six-stage anger-spectrum continuum (English)

```
Create a horizontal infographic titled "The Qur'anic Anger Spectrum: A Six-Stage Action-Intensity Continuum" on a clean off-white background. Flat vector style. Journal-publication quality. 2400×900 px, landscape.

Render a horizontal flowing ribbon from left to right representing intensity escalation. The ribbon is divided into six labeled stages, with the color gradient deepening from a soft slate-grey at the left to a saturated deep crimson at the right:

  STAGE 1 — Pre-anger displeasure   (pale slate, 8% of width)
  STAGE 2 — Inner pressure          (warm grey, 13%)
  STAGE 3 — Evaluative aversion     (dusty amber, 14%)
  STAGE 4 — Active anger            (burnt orange, 17%)
  STAGE 5 — Compressed rage         (vermillion, 18%)
  STAGE 6 — Behavioural outcomes    (deep crimson, 30%)

Above the ribbon, place 14 lexeme cards (one per root). Each card shows:
  • The Arabic root in large Naskh/Amiri script (e.g.  أ ف ف )
  • The Latin transliteration in italic small caps below it (e.g.  ʾff )
  • The total attestation count as a small badge in the upper-right corner of the card

Stage 1: ʾff (3), krh (41)
Stage 2: ḍyq (13), ḥzn (42), ʾsf (5)
Stage 3: nqm (17), sakh (4), mqt (6)
Stage 4: ghḍb (24), ḥrd (1)
Stage 5: ghyẓ (11)  — annotate "with tamayyuz manifestation, Q. 67:8"
Stage 6: bghy (96), ṭghy (39), ʿtw (10)

Position each card so its horizontal position falls inside its stage band, with the highest-frequency card (bghy, 96) noticeably enlarged. Card size scales with √frequency.

Below the ribbon, a thin axis labeled "Action intensity →" with three benchmark labels: "Verbal displeasure" (under stage 1), "Sealed-container compression" (under stage 5), "Behavioural rupture" (under stage 6).

In the lower-right corner, a small legend reads:
  N = 312 attestations · Quranic Arabic Corpus v0.4 (Dukes 2011)

Typography: serif body (think EB Garamond or Crimson Pro). Use the Amiri or Scheherazade font for Arabic — never substitute. Avoid all decorative flourishes; design should read as a peer-reviewed-journal figure, not a magazine layout.
```

## A-fa. Six-stage anger-spectrum continuum (Persian, RTL)

```
یک اینفوگرافی افقی به سبک تخت و وکتوری در سطح مجله‌ی علمی طراحی کنید، با عنوان «پیوستارِ شش‌مرحله‌ایِ خشمِ قرآنی: محور شدتِ کنش». پس‌زمینه‌ی شیری-سفید. اندازه 2400×900 پیکسل. چیدمان راست-به-چپ (RTL).

روی محور افقی، یک نوار پیوسته از راست به چپ که شدت را افزایش می‌دهد. شیب رنگ از خاکستریِ ملایم (راست) به قرمزِ تندِ گیلاسی (چپ). نوار به شش مرحله تقسیم می‌شود:

  مرحله ۱ — پیش‌ازخشم        (خاکستری روشن، ۸٪ پهنا) — راست‌ترین
  مرحله ۲ — فشارِ درونی       (خاکستریِ گرم، ۱۳٪)
  مرحله ۳ — نفرتِ ارزیابانه   (کهرباییِ غبارآلود، ۱۴٪)
  مرحله ۴ — خشمِ فعّال        (پرتقالیِ سوخته، ۱۷٪)
  مرحله ۵ — خشمِ متراکم       (شنگرفی، ۱۸٪)
  مرحله ۶ — پیامدهای رفتاری   (گیلاسیِ تیره، ۳۰٪) — چپ‌ترین

بالای نوار، چهارده کارت واژگانی (یکی برای هر ریشه). هر کارت:
  • ریشه‌ی عربی به خط نسخ/امیری در اندازه‌ی بزرگ (مثلاً  أ ف ف )
  • بسامد کل به‌صورت نشان کوچک در گوشه‌ی بالا

مرحله ۱: أفّ (۳)، کره (۴۱)
مرحله ۲: ضِیق (۱۳)، حُزن (۴۲)، أسف (۵)
مرحله ۳: نقم (۱۷)، سَخَط (۴)، مَقت (۶)
مرحله ۴: غضب (۲۴)، حَرد (۱)
مرحله ۵: غیظ (۱۱) — یادداشت: «با تجلیِ تمیّز، سوره مُلک: ۸»
مرحله ۶: بَغی (۹۶)، طُغیان (۳۹)، عُتُوّ (۱۰)

اندازه‌ی کارت به جذرِ بسامد متناسب باشد. کارتِ «بَغی» چشمگیرتر باشد.

زیر نوار: یک محور باریک با برچسبِ ←  شدتِ کنش. سه نقطه‌ی شاخص: «ابرازِ کلامیِ ناخشنودی» (زیر مرحله ۱)، «فشارِ ظرفِ مُهرشده» (زیر مرحله ۵)، «گسستِ رفتاری» (زیر مرحله ۶).

در گوشه‌ی پایین: «۳۱۲ بسامد · پیکره‌ی ریخت‌شناختیِ قرآنی، دوکس ۲۰۱۱».

تایپوگرافی: متن فارسی با فونت وزیرمتن یا یکان. متن عربی با امیری یا اسکهرزاده. هیچ تزیین تصویری اضافه نباشد؛ ظاهرِ کلی، شکلِ مجله‌ی داوری‌شده باشد.
```

---

## B. Container-metaphor triad (English)

```
Create a publication-quality three-panel infographic illustrating the ANGER-IS-A-PRESSURIZED-CONTAINER conceptual metaphor as instantiated by three Qur'anic stages. Title: "The Qur'anic Operationalization of the Container Metaphor". Flat editorial-illustration style; muted journal palette. 2400×1100 px.

Three vertical panels side by side, each with a title bar at top and a verse strip at the bottom.

PANEL 1 (left) — "Stage 4: ghaḍab — open container"
  Illustrate an open clay vessel (Mesopotamian / classical Arabian style, narrow neck, plain ochre body) with vapor rising freely from its mouth. The vapor symbolizes affect dissipating into language and action. The body of the vessel is intact and unstrained.
  Caption strip: "غَضَب: anger present, not yet compressed"

PANEL 2 (middle) — "Stage 5a: ghayẓ + kaẓm — sealed pressurized container"
  Same vessel, now with a tied leather cord knotting the neck shut (this is *kaẓm* — etymologically "to tie off a waterskin"). The body of the vessel shows hairline strain lines and a visible internal glow indicating contained heat / pressure. Small inset arrows showing pressure pushing outward against the seal.
  Caption strip in Arabic + English: "وَالْكَاظِمِينَ الْغَيْظَ — Q. 3:134 — 'those who restrain anger'"

PANEL 3 (right) — "Stage 5 manifestation: tamayyuz — structural rupture"
  Same vessel, now splitting along a vertical fault line. CRITICAL: the contents are NOT shown spilling outward (that would be the English "explode" metaphor). Instead, the *body itself* of the vessel is parting in two halves with a jagged crack down the middle. Inside the crack: glowing red fissure. Note: the verb m-y-z means "to part / sever", so the rupture is of the container's structure, not the contents' exit.
  Caption strip in Arabic + English: "تَكَادُ تَمَيَّزُ مِنَ الْغَيْظِ — Sūrat al-Mulk: 8 — 'almost parts asunder from fury'"

Under all three panels, a single explanatory line in italic:
  "The Qur'an renders all four steps of the Lakoff–Kövecses (1987) container schema: present (P1), pressurized (P2), regulated (the leather knot in P2), and ruptured (P3). Crucially, P3 depicts container failure — not content escape — making the Qur'anic instantiation more structurally transparent than its English analogues."

Use a warm, muted palette: terracotta vessels, deep umber backgrounds, ivory ribbon for captions, crimson glow inside the cracked panel. Arabic in Amiri font. No drop shadows. No skeuomorphic textures. Read as a journal figure, not a children's book illustration.
```

## B-fa. Container-metaphor triad (Persian, RTL)

```
یک اینفوگرافی سه‌پنلیِ افقی به سطح کیفیتِ مجله‌ی علمی طراحی کنید، با عنوان «عملیاتی‌سازیِ قرآنیِ استعاره‌ی ظرفِ تحتِ فشار». سبک تخت، تصویرگری ادیتوریال، پالتِ خفه و موقّر. اندازه 2400×1100 پیکسل. چیدمان راست-به-چپ.

سه پنلِ عمودی در کنار هم، هر یک با نوار عنوان بالا و نوار آیه‌ی قرآنی پایین.

پنل ۱ (راست‌ترین) — «مرحله‌ی ۴: غضب — ظرفِ باز»
  ظرفی سفالین به سبک عربیِ کلاسیک، گردنِ تنگ، بدنه‌ی اُخرایی. از دهانه‌ی ظرف بخار آزادانه برمی‌خیزد. بدنه سالم و بدون فشار.
  زیرنویس: «غضب: هیجان حاضر، اما هنوز متراکم نشده»

پنل ۲ (وسط) — «مرحله‌ی ۵ الف: غیظ + کَظم — ظرفِ مُهرشده‌ی پُرفشار»
  همان ظرف، اما گردنش با بندِ چرمی محکم گره خورده (این همان «کَظم» است: در اصل بستنِ دهانه‌ی مَشک). بر بدنه‌ی ظرف خطوطِ مویِی استرس و درخششِ سرخِ درونی. فلش‌های کوچک نشان‌دهنده‌ی فشارِ به‌سویِ بیرون.
  زیرنویس عربی+فارسی: «وَالْكَاظِمِينَ الْغَيْظَ — آل عمران: ۱۳۴ — "آنان که خشم را فرو می‌خورند"»

پنل ۳ (چپ‌ترین) — «تجلیِ مرحله‌ی ۵: تَمَیُّز — فروپاشیِ ساختاری»
  همان ظرف، اما در حالِ گسستن از وسط در امتدادِ یک شکافِ عمودیِ ناصاف. **مهم**: محتوای ظرف به بیرون نمی‌ریزد (آن استعاره‌ی انگلیسی است). به‌جای آن، خودِ بدنه‌ی ظرف به دو نیمه می‌شکافد. درون شکاف: درخششِ سرخ. ریشه‌ی م-ی-ز یعنی «جداشدن، گسستن»؛ گسست از خودِ ظرف است، نه خروجِ محتوا.
  زیرنویس: «تَكَادُ تَمَيَّزُ مِنَ الْغَيْظِ — سوره مُلک: ۸ — "گویی نزدیک است از شدتِ غیظ بگسلد"»

زیرِ هر سه پنل، یک خطِ توضیحی به‌صورت italic:
  «قرآن چهار گامِ طرحواره‌ی لیکاف-کوچش (۱۹۸۷) را عملیاتی می‌سازد: حضور (پنل۱)، تراکم (پنل۲)، مهار (گرهِ چرمی در پنل۲)، و گسست (پنل۳). نکته‌ی محوری: پنل ۳ فروپاشیِ ظرف را تصویر می‌کند — نه خروجِ محتوا — و بنابراین عملیاتی‌سازیِ قرآنی از نمونه‌های انگلیسیِ معاصر شفاف‌تر است.»

پالت: ظرف‌های گِلی به رنگِ زمینی، پس‌زمینه‌ی قهوه‌ای-خاکستری، روبانِ زیرنویس عاجی، درخششِ سرخِ گدازنده در پنلِ شکسته. متن عربی با فونت امیری، متن فارسی با وزیرمتن. بدون سایه و بدون بافتِ تقلیدی.
```

---

## C. Methodology flow diagram (English)

```
Create a clean methodology flow diagram for a Qur'anic corpus-linguistics paper. Title: "Reproducible Pipeline: From Corpus to Findings". 2200×1400 px, portrait-ish. Journal-quality, no decoration.

The diagram has 5 horizontal tiers, connected by directional arrows.

TIER 1 — Sources (top):
  Three rectangular cards side by side:
    [Quranic Arabic Corpus v0.4 (Dukes 2011) — 128,219 morphological segments, GPL license]
    [Tanzil Project Uthmani text — CC-BY-ND 3.0]
    [Nine classical tafāsīr (Ṭabarī, Zamakhsharī, Ṭabrisī, Ṭabāṭabāʾī, Qurṭubī, Ibn Kathīr, Ibn ʿĀshūr, Sayyid Quṭb, Rashīd Riḍā)]

TIER 2 — Ingest & parse:
  One large card:
    [Python QAC parser → Buckwalter normalization → segment-to-word collapse]
    Subscript: "qac_parser.py · buckwalter.py"

TIER 3 — Selection:
  Two cards:
    [14 spectrum roots] — with the Arabic strip ʾff·krh·ḍyq·ḥzn·ʾsf·nqm·sakh·mqt·ghḍb·ḥrd·ghyẓ·bghy·ṭghy·ʿtw
    [5 umbrella moral-evaluation roots for robustness] — ẓlm·jrm·fsq·ʿdw·šnʾ

TIER 4 — Analyses (four parallel sub-cards):
    [A. Distributional statistics] — χ², binomial (Holm), permutation, monotonic trend
    [B. Co-occurrence network] — aya-level edges, PMI-weighted, bootstrap CIs
    [C. Tafsīr-grounded coding] — 145 Stage-6 attestations × 9 mufassirs, κ = 0.79
    [D. Comparative translation analysis] — 5 EN + 5 FA renderings, 30-aya audit

TIER 5 — Outputs (bottom):
  Three cards:
    [312 attestations across 6 stages — Stage totals 44 · 60 · 27 · 25 · 11 · 145]
    [Seven publication figures (PDF + PNG)]
    [Stage-6 causation breakdown: 26% anger-origin / 49% structure-origin / 25% mixed]

Arrow conventions:
  • Solid black arrows for the main pipeline
  • Dashed grey arrows for cross-feeds (e.g., tafsīr sources also feed coding step C)
  • Branching arrows where one source feeds multiple downstream steps

Bottom corner (lower-right) tag:
  "Pipeline deterministic · Identical inputs → byte-identical CSVs and figures · github.com/ali-kin4/quranic-emotion-spectrum"

Typography: serif (EB Garamond) for body, sans-serif (Inter or Source Sans) for card titles, Amiri for Arabic strip. No 3-D effects, no skeumorphism, no gradients. Treat this as a software-architecture diagram in a methods section — visually quiet, functionally explicit.
```

## C-fa. Methodology flow diagram (Persian, RTL)

```
یک نمودارِ گردشِ روش‌شناختی به سطح مجله‌ی علمی طراحی کنید. عنوان: «خط‌لوله‌ی بازتولیدپذیر: از پیکره تا یافته‌ها». اندازه 2200×1400 پیکسل. چیدمان راست-به-چپ. ظاهرِ آرام و حرفه‌ای، بدون تزیین.

پنج لایه‌ی افقی، با فلش‌های جهت‌دار.

لایه ۱ (بالا) — منابع:
  سه کارت در کنار هم:
    [پیکره‌ی ریخت‌شناختیِ قرآن، دوکس ۲۰۱۱ — ۱۲۸٬۲۱۹ پاره‌واژه، مجوزِ GPL]
    [پروژه‌ی تنزیل — متنِ عثمانی، CC-BY-ND 3.0]
    [نُه تفسیرِ کلاسیک: طبری، زمخشری، طبرسی، طباطبایی، قرطبی، ابن‌کثیر، ابن‌عاشور، سیّد قطب، رشید رضا]

لایه ۲ — استخراج و تجزیه:
  یک کارت بزرگ:
    [تجزیه‌گرِ پایتون QAC ← نُرمالیزه‌ی بُکوالتر ← پاره‌واژه به سطحِ کلمه]
    زیرنویس: «qac_parser.py · buckwalter.py»

لایه ۳ — انتخابِ ریشه‌ها:
  دو کارت:
    [۱۴ ریشه‌ی کانونی] — نوار عربی: أفّ·کره·ضِیق·حُزن·أسف·نقم·سَخَط·مَقت·غضب·حَرد·غیظ·بَغی·طُغیان·عُتُوّ
    [۵ ریشه‌ی چترِ مفهومی برای آزمونِ پایداری] — ظلم·جرم·فسق·عداوت·شَنَأ

لایه ۴ — تحلیل‌ها (چهار زیرکارتِ موازی):
    [الف. آمارِ توزیعی] — خی-دو، دوجمله‌ای (هولم)، جایگشتی، روندِ یکنواخت
    [ب. شبکه‌ی هم‌رخدادگیری] — یال‌های آیه‌ای، وزن PMI، فاصله‌های اطمینانِ بوت‌استرپی
    [ج. کدبندیِ تفسیر-بنیاد] — ۱۴۵ بسامدِ مرحله‌ی ۶ × ۹ مفسّر، κ = ۰٫۷۹
    [د. تحلیلِ تطبیقیِ ترجمه‌ها] — ۵ ترجمه‌ی فارسی + ۵ ترجمه‌ی انگلیسی، ممیّزیِ ۳۰‌آیه‌ای

لایه ۵ (پایین) — خروجی‌ها:
  سه کارت:
    [۳۱۲ بسامد در ۶ مرحله — جمع‌های مرحله‌ای: ۴۴ · ۶۰ · ۲۷ · ۲۵ · ۱۱ · ۱۴۵]
    [هفت نمودارِ مقاله (PDF + PNG)]
    [تفکیکِ علّی مرحله‌ی ۶: ۲۶٪ خشم-خاستگاه / ۴۹٪ ساختار-خاستگاه / ۲۵٪ ترکیبی]

فلش‌ها: مشکیِ توپُر برای مسیرِ اصلی؛ خاکستریِ خط‌چین برای ورودی‌های جانبی (مثلاً منابعِ تفسیر به کدبندیِ ج).

پایینِ نمودار: «خط‌لوله قطعی · ورودیِ یکسان → CSV و نمودارِ بایت-به-بایت یکسان · github.com/ali-kin4/quranic-emotion-spectrum»

تایپوگرافی: متن فارسی با وزیرمتن، متن عربی با امیری. بدون افکتِ سه‌بعدی، بدون شیب رنگ.
```

---

## Usage workflow

1. Pick the prompt block you want and paste into ChatGPT / DALL-E / GPT-4o image gen.
2. Generate; iterate the prompt if needed (image-gen models are nondeterministic — the first output may need 1–3 regenerations to land the text accurately).
3. Save:
   - English: `figures/figA_continuum_v2.png`, `figures/figB_container_triad.png`, `figures/figC_methodology_flow.png`
   - Persian: `figures_fa/figA_continuum_v2.png`, etc.
4. Tell me the filenames and which manuscript spots to slot them into — I'll wire them in and update captions.

Note: if image-gen renders Arabic incorrectly (it sometimes does), accept the layout and overlay the Arabic text via a quick GIMP/Photoshop pass before saving. The Amiri TTF is in `paper/fonts/Amiri-Regular.ttf`.
