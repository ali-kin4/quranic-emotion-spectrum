"""Buckwalter ↔ Arabic transliteration utilities.

The Quranic Arabic Corpus (Dukes, 2011) encodes roots and word forms in
Buckwalter transliteration. This module provides round-trip mappings
between Buckwalter ASCII and Arabic Unicode.
"""

BW_TO_AR = {
    "A": "ا",
    "b": "ب",
    "t": "ت",
    "v": "ث",
    "j": "ج",
    "H": "ح",
    "x": "خ",
    "d": "د",
    "*": "ذ",
    "r": "ر",
    "z": "ز",
    "s": "س",
    "$": "ش",
    "S": "ص",
    "D": "ض",
    "T": "ط",
    "Z": "ظ",
    "E": "ع",
    "g": "غ",
    "f": "ف",
    "q": "ق",
    "k": "ك",
    "l": "ل",
    "m": "م",
    "n": "ن",
    "h": "ه",
    "w": "و",
    "y": "ي",
    "Y": "ى",
    "p": "ة",
    "'": "ء",
    "&": "ؤ",
    "}": "ئ",
    ">": "أ",
    "<": "إ",
    "|": "آ",
    "{": "ٱ",
    "`": "ٰ",
    "~": "ّ",
    "a": "َ",
    "u": "ُ",
    "i": "ِ",
    "F": "ً",
    "N": "ٌ",
    "K": "ٍ",
    "o": "ْ",
}

AR_TO_BW = {v: k for k, v in BW_TO_AR.items()}


def bw_to_arabic(s: str) -> str:
    return "".join(BW_TO_AR.get(ch, ch) for ch in s)


def arabic_to_bw(s: str) -> str:
    return "".join(AR_TO_BW.get(ch, ch) for ch in s)
