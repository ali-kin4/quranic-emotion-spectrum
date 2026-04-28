"""Definition of the four-stage emotion-intensity spectrum.

Each entry: (Arabic root, Buckwalter root, transliteration, English gloss,
Persian gloss, stage 1-4, headline verse from the original idea doc).

Stage 1: Pre-anger / internal distress (درگیری درونی)
Stage 2: Explicit anger (خشم آشکار)
Stage 3: Explosive rage (خشم متراکم و انفجاری)
Stage 4: Behavioural rebellion (کنش عصیانگرانه)
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SpectrumRoot:
    arabic: str           # root in scholarly notation, e.g. ض-ي-ق
    bw: str               # Buckwalter transliteration of the root
    translit: str         # ALA-LC style transliteration
    english: str          # English gloss
    persian: str          # Persian gloss
    stage: int            # 1–4
    headline_verse: str   # Sura:aya canonical exemplar from the original idea
    surface: str = ""     # Headline surface word (no dashes), e.g. ضيق

    def display(self) -> str:
        """The cleanest Arabic label for figures and tables."""
        return self.surface or self.arabic.replace("-", "")


SPECTRUM: tuple[SpectrumRoot, ...] = (
    # --- Stage 1: internal distress ---
    SpectrumRoot("ض-ي-ق", "Dyq", "ḍ-y-q", "constriction / inner tightness",
                 "تنگی روانی، فشار درونی", 1, "15:97", "ضَيْق"),
    SpectrumRoot("ح-ز-ن", "Hzn", "ḥ-z-n", "sorrow / persistent grief",
                 "اندوه پایدار", 1, "2:38", "حُزْن"),
    SpectrumRoot("أ-س-ف", "Asf", "ʾ-s-f", "regretful grief edged with anger",
                 "اندوه آمیخته با خشم خفیف", 1, "43:55", "أَسَف"),

    # --- Stage 2: explicit anger ---
    SpectrumRoot("س-خ-ط", "sxT", "s-kh-ṭ", "moral displeasure / disapproval",
                 "ناخشنودی شدید اخلاقی", 2, "47:28", "سَخَط"),
    SpectrumRoot("غ-ض-ب", "gDb", "gh-ḍ-b", "active anger directed at a target",
                 "خشم آشکار", 2, "48:6", "غَضَب"),

    # --- Stage 3: explosive rage ---
    SpectrumRoot("غ-ي-ظ", "gyZ", "gh-y-ẓ", "compressed/boiling rage",
                 "خشم متراکم و فروخفته", 3, "3:134", "غَيْظ"),
    # The phrase تَكَادُ تَمَيَّزُ مِنَ الْغَيْظِ (Mulk 67:8) uses both gyZ
    # and the verbal root myz (separate / burst apart) — we track both.
    SpectrumRoot("م-ي-ز", "myz", "m-y-z", "to split / burst apart (figurative collapse)",
                 "از هم گسستن (در ترکیب «تمیّز من الغیظ»)", 3, "67:8", "تَمَيُّز"),

    # --- Stage 4: behavioural rebellion ---
    SpectrumRoot("ب-غ-ي", "bgy", "b-gh-y", "transgression / aggressive seeking",
                 "تجاوز، ستم", 4, "42:42", "بَغْي"),
    SpectrumRoot("ط-غ-ي", "Tgy", "ṭ-gh-y", "overflowing rebellion / tyranny",
                 "سرکشی، طغیان", 4, "96:6", "طُغْيَان"),
    SpectrumRoot("ع-ت-و", "Etw", "ʿ-t-w", "obstinate, arrogant defiance",
                 "سرکشی لجوجانه", 4, "25:21", "عُتُوّ"),
)


# Optional expansion roots used in robustness checks (Section §4.5 of the paper).
EXPANSION: tuple[SpectrumRoot, ...] = (
    SpectrumRoot("ك-ر-ه", "krh", "k-r-h", "aversion, disliking",
                 "کراهت", 1, "9:81"),
    SpectrumRoot("ش-ن-أ", "$nA", "sh-n-ʾ", "intense hatred",
                 "بغض شدید", 2, "5:8"),
    SpectrumRoot("ج-ر-م", "jrm", "j-r-m", "criminal/sinful action",
                 "جرم، گناه", 4, "10:17"),
    SpectrumRoot("ف-س-ق", "fsq", "f-s-q", "moral deviance / breaking out of bounds",
                 "فسق", 4, "5:25"),
    SpectrumRoot("ظ-ل-م", "Zlm", "ẓ-l-m", "oppression / wrongdoing",
                 "ظلم", 4, "2:35"),
    SpectrumRoot("ع-د-و", "Edw", "ʿ-d-w", "enmity, hostile transgression",
                 "دشمنی، عداوت", 4, "2:194"),
)


def all_roots(include_expansion: bool = False) -> tuple[SpectrumRoot, ...]:
    return SPECTRUM + (EXPANSION if include_expansion else ())


STAGE_LABELS_FA = {
    1: "مرحله ۱ — رنج و تنگی درونی",
    2: "مرحله ۲ — خشم آشکار",
    3: "مرحله ۳ — خشم متراکم و انفجاری",
    4: "مرحله ۴ — کنش عصیانگرانه",
}
STAGE_LABELS_EN = {
    1: "Stage 1 — Internal Distress (Pre-Anger)",
    2: "Stage 2 — Explicit Anger",
    3: "Stage 3 — Explosive Rage",
    4: "Stage 4 — Behavioural Rebellion",
}
