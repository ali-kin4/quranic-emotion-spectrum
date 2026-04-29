"""Definition of the six-stage anger-intensity spectrum.

Revised 2026-04-29 in response to reviewer comments. The paper's focus is
the *anger* spectrum specifically (not negative emotions in general).

Each entry: (Arabic root, Buckwalter root, transliteration, English gloss,
Persian gloss, stage 1-6, headline verse, surface form, plus optional
notes flagging where a root has non-anger uses that the manuscript
discusses explicitly).

Stage 1: Pre-anger displeasure (ناخشنودیِ پیش‌خشم) — uff, karh
Stage 2: Inner pressure / contraction (فشار درونی و انقباض) — ḍyq, ḥzn,
         asaf [with caveats: ḥzn is not necessarily anger-derived; ḍyq
         can be both pre-anger AND inhibited-aggression]
Stage 3: Evaluative aversion (انزجار ارزیابانه) — naqm, sakhaṭ, maqt
Stage 4: Active anger (خشم فعال) — ghaḍab, ḥard
Stage 5: Compressed/explosive rage (خشم متراکم/انفجاری) — ghayẓ
         [tamayyuz is a manifestation of ghayẓ at its peak, not a
         separate root: تَمَيَّزَ مِن الغَيْظِ = تَقَطَّعَ]
Stage 6: Behavioural outcomes (پیامدهای رفتاری) — baghy, ṭughyān, ʿutuww
         [reviewer caveat: these often arise from supremacism / power-
         seeking rather than as direct outputs of an anger process]
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class SpectrumRoot:
    arabic: str           # root in scholarly notation, e.g. ض-ي-ق
    bw: str               # Buckwalter transliteration of the root
    translit: str         # ALA-LC style transliteration
    english: str          # English gloss
    persian: str          # Persian gloss
    stage: int            # 1–6
    headline_verse: str   # Sura:aya canonical exemplar
    surface: str = ""     # Headline surface word (no dashes), e.g. ضيق
    note: str = ""        # Reviewer-prompted caveat flag (optional)

    def display(self) -> str:
        """The cleanest Arabic label for figures and tables."""
        return self.surface or self.arabic.replace("-", "")


SPECTRUM: tuple[SpectrumRoot, ...] = (
    # --- Stage 1: pre-anger displeasure ---
    SpectrumRoot("أ-ف-ف", "Aff", "ʾ-f-f",
                 "vocal expression of irritation, mild displeasure",
                 "تضجر، ابراز ناخشنودی خفیف",
                 1, "17:23", "أُفّ",
                 note="Lowest tier; Q. 17:23 prohibits saying it to parents."),
    SpectrumRoot("ك-ر-ه", "krh", "k-r-h",
                 "aversion, inner disliking",
                 "کراهت، بی‌میلی درونی",
                 1, "2:216", "كَرْه",
                 note="Cognitive-evaluative; Q. 2:216 reframes karāha through "
                      "wisdom; karāha → ikrāh is the path from emotion to "
                      "structural coercion."),

    # --- Stage 2: inner pressure & contraction ---
    SpectrumRoot("ض-ي-ق", "Dyq", "ḍ-y-q",
                 "inner constriction / pressure",
                 "تنگی و فشار درونی",
                 2, "15:97", "ضَيْق",
                 note="Dual valence: pre-anger affective contraction (Q. 15:97) "
                      "AND inhibited aggression when agency is blocked "
                      "(Lot, Q. 11:77 ضاق بهم ذرعاً)."),
    SpectrumRoot("ح-ز-ن", "Hzn", "ḥ-z-n",
                 "persistent grief / sorrow",
                 "اندوه پایدار",
                 2, "2:38", "حُزْن",
                 note="NOT necessarily anger-derived. Can be standalone grief, "
                      "externally-induced sorrow, or even a positive moral "
                      "compunction. Included in the wider field but flagged "
                      "as semantically transversal."),
    SpectrumRoot("أ-س-ف", "Asf", "ʾ-s-f",
                 "regretful grief edged with anger",
                 "اندوه آمیخته با خشم",
                 2, "43:55", "أَسَف",
                 note="Standalone: regret-grief (Q. 18:6). Compound: غضبان "
                      "أسفاً (Moses, Q. 7:150 / 20:86) where asaf is the "
                      "compassionate inner ground of 'sacred anger'."),

    # --- Stage 3: evaluative aversion ---
    SpectrumRoot("ن-ق-م", "nqm", "n-q-m",
                 "vengeful anger / disapproval seeking retribution",
                 "خشم انتقام‌جویانه و تخطئه‌گر",
                 3, "7:126", "نَقْم",
                 note="Q. 7:126 وَمَا نَقَمُوا مِنَّا إِلَّا أَنْ آمَنَّا — "
                      "between sakhaṭ and ghaḍab on the action axis."),
    SpectrumRoot("س-خ-ط", "sxT", "s-kh-ṭ",
                 "comprehensive moral displeasure",
                 "ناخشنودی فراگیر اخلاقی",
                 3, "47:28", "سَخَط"),
    SpectrumRoot("م-ق-ت", "mqt", "m-q-t",
                 "intense moral aversion / contempt-rejection",
                 "انزجار اخلاقی حداکثری",
                 3, "40:10", "مَقْت",
                 note="Lexically أَشَدُّ الإِبْغاضِ (Zajjāj). Specifically "
                      "directed at observed reprehensible conduct. Q. 40:10 "
                      "لَمَقْتُ اللَّهِ أَكْبَرُ مِن مَّقْتِكُمْ أَنْفُسَكُمْ; "
                      "Q. 4:22; Q. 35:39; Q. 61:3."),

    # --- Stage 4: active anger ---
    SpectrumRoot("غ-ض-ب", "gDb", "gh-ḍ-b",
                 "active anger directed at a target",
                 "خشم آشکار و هدفمند",
                 4, "48:6", "غَضَب"),
    SpectrumRoot("ح-ر-د", "Hrd", "ḥ-r-d",
                 "purposeful punitive anger combined with stinginess",
                 "خشم هدفمند توأم با بخل و منع",
                 4, "68:25", "حَرْد",
                 note="Hapax — Q. 68:25 وَغَدَوْا عَلَى حَرْدٍ قَادِرِينَ. "
                      "Garden-owners' anger combined with miserly intent to "
                      "deny the poor. Tafsir tradition glosses ḥard as both "
                      "anger and intent (al-Ṭabarsī, al-Mīzān)."),

    # --- Stage 5: compressed/explosive rage ---
    SpectrumRoot("غ-ي-ظ", "gyZ", "gh-y-ẓ",
                 "compressed / boiling rage",
                 "خشم متراکم و فروخفته",
                 5, "3:134", "غَيْظ",
                 note="Manifestations: kaẓm (Q. 3:134, restraint), tamayyuz "
                      "(Q. 67:8, container collapse, تَمَيَّزَ = تَقَطَّعَ), "
                      "and divine consummation (Q. 3:119 مُوتُوا بِغَيْظِكُمْ). "
                      "tamayyuz is a manifestation, not a separate root."),

    # --- Stage 6: behavioural outcomes (with caveats) ---
    SpectrumRoot("ب-غ-ي", "bgy", "b-gh-y",
                 "transgression / aggressive seeking",
                 "تجاوز، ستم",
                 6, "42:42", "بَغْي",
                 note="Caveat: baghy frequently arises from greed, supremacism "
                      "or oppressive self-interest, not from anger directly. "
                      "Treated here as a behavioural outcome that *can* "
                      "complete the anger trajectory but is not exclusively "
                      "anger-driven."),
    SpectrumRoot("ط-غ-ي", "Tgy", "ṭ-gh-y",
                 "overflowing rebellion / tyranny",
                 "سرکشی، طغیان",
                 6, "96:6", "طُغْيَان",
                 note="Caveat: ṭughyān often roots in power-seeking or "
                      "structural arrogance (Pharaonic ṭughyān, Q. 79:17). "
                      "Anger may emerge from ṭughyān (Q. 26:55 إنهم لنا "
                      "لغائظون) but is not its source."),
    SpectrumRoot("ع-ت-و", "Etw", "ʿ-t-w",
                 "obstinate, arrogant defiance",
                 "سرکشی لجوجانه",
                 6, "25:21", "عُتُوّ",
                 note="Caveat: ʿutuww typically attaches to istikbār "
                      "(arrogance) rather than acute anger. Persistent, "
                      "settled defiance — an entrenched character trait."),
)


# Expansion roots used in cross-field robustness checks (umbrella moral
# evaluation field; see §4.7 of the paper).
EXPANSION: tuple[SpectrumRoot, ...] = (
    SpectrumRoot("ش-ن-أ", "$nA", "sh-n-ʾ", "intense hatred",
                 "بغض شدید", 3, "5:8"),
    SpectrumRoot("ج-ر-م", "jrm", "j-r-m", "criminal/sinful action",
                 "جرم، گناه", 6, "10:17"),
    SpectrumRoot("ف-س-ق", "fsq", "f-s-q", "moral deviance / breaking out of bounds",
                 "فسق", 6, "5:25"),
    SpectrumRoot("ظ-ل-م", "Zlm", "ẓ-l-m", "oppression / wrongdoing",
                 "ظلم", 6, "2:35"),
    SpectrumRoot("ع-د-و", "Edw", "ʿ-d-w", "enmity, hostile transgression",
                 "دشمنی، عداوت", 6, "2:194"),
)


# Deprecated: the verb m-y-z is retained in concordance scripts as a
# diagnostic for the ghayẓ peak ("تَمَيَّزَ مِن الغَيْظِ", Q. 67:8). It is
# NOT a separate root in the spectrum: lexically تَمَيَّزَ = تَقَطَّعَ
# (Lisān, Mufradāt, al-Mīzān ad loc.). Keep the row only so that
# extract_concordance.py can still emit a per-root file for legacy
# comparison; visualisations and statistics use SPECTRUM only.
DIAGNOSTIC_TAMAYYUZ = SpectrumRoot(
    "م-ي-ز", "myz", "m-y-z",
    "diagnostic verb of ghayẓ at peak (تَمَيَّزَ = تَقَطَّعَ)",
    "ابزار تشخیصِ اوجِ غیظ", 5, "67:8", "تَمَيُّز",
    note="Not a separate root; folded into ghayẓ analysis per reviewer.",
)


def all_roots(include_expansion: bool = False,
              include_diagnostic: bool = False) -> tuple[SpectrumRoot, ...]:
    out = SPECTRUM
    if include_expansion:
        out = out + EXPANSION
    if include_diagnostic:
        out = out + (DIAGNOSTIC_TAMAYYUZ,)
    return out


STAGE_LABELS_FA = {
    1: "مرحله ۱ — تضجر و ناخشنودیِ خفیف",
    2: "مرحله ۲ — فشار درونی و انقباض",
    3: "مرحله ۳ — انزجارِ ارزیابانه",
    4: "مرحله ۴ — خشم فعال",
    5: "مرحله ۵ — خشمِ متراکم و انفجاری",
    6: "مرحله ۶ — پیامدهای رفتاری",
}
STAGE_LABELS_EN = {
    1: "Stage 1 — Pre-Anger Displeasure",
    2: "Stage 2 — Inner Pressure & Contraction",
    3: "Stage 3 — Evaluative Aversion",
    4: "Stage 4 — Active Anger",
    5: "Stage 5 — Compressed Rage",
    6: "Stage 6 — Behavioural Outcomes",
}
