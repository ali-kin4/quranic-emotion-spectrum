"""Build the English manuscript.docx with PNG figures and LTR styling."""
from __future__ import annotations
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

MD_IN = HERE / "manuscript.md"
MD_TMP = HERE / "_manuscript_for_docx.md"
OUT_DOCX = HERE / "manuscript.docx"


def preprocess_markdown(text: str) -> str:
    # Convert LaTeX text-formatting to markdown so docx output looks right
    text = re.sub(r'\\textbf\{([^}]+)\}', r'**\1**', text)
    text = re.sub(r'\\textit\{([^}]+)\}', r'*\1*', text)
    text = re.sub(r'\\emph\{([^}]+)\}', r'*\1*', text)
    text = re.sub(r'\\arb\{([^}]+)\}', r'\1', text)
    text = re.sub(r'\\lr\{([^{}]+)\}', r'\1', text)
    # Strip layout-only LaTeX commands
    text = re.sub(r'\\noindent\b', '', text)
    text = re.sub(r'\\itshape\b', '', text)
    text = re.sub(r'\\normalfont\b', '', text)
    text = re.sub(r'\\vspace\{[^}]+\}', '', text)
    text = re.sub(r'\\setstretch\{[^}]+\}', '', text)
    text = re.sub(r'\\begingroup\b', '', text)
    text = re.sub(r'\\endgroup\b', '', text)
    text = re.sub(r'\\everypar\{[^}]+\}', '', text)
    text = re.sub(r'\\setlength\{[^}]+\}\{[^}]+\}', '', text)
    # Figures: swap .pdf -> .png for Word compatibility
    text = re.sub(r'\]\(([^)]+)\.pdf\)\{', r'](\1.png){', text)
    return text


def main():
    print("Preprocessing markdown...")
    md_text = MD_IN.read_text(encoding='utf-8')
    md_text = preprocess_markdown(md_text)
    MD_TMP.write_text(md_text, encoding='utf-8')

    print("Running pandoc...")
    cmd = [
        "pandoc",
        str(MD_TMP),
        "--from", "markdown",
        "--to", "docx",
        "--resource-path",
        str(ROOT / "figures") + ";" + str(HERE),
        "-o", str(OUT_DOCX),
    ]
    subprocess.check_call(cmd, cwd=str(HERE))

    MD_TMP.unlink(missing_ok=True)
    print(f"Wrote {OUT_DOCX}")


if __name__ == "__main__":
    main()
