from __future__ import annotations

import html
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    ListFlowable,
    ListItem,
    PageBreak,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


ROOT = Path(__file__).resolve().parents[1]
LESSON_DIR = ROOT / "Network_Engineering_Foundation_20_Lessons"
OUTPUT_DIR = ROOT / "output" / "pdf" / "Network_Engineering_Foundation_20_Lessons"


def register_fonts() -> tuple[str, str, str, str]:
    fonts_dir = Path("C:/Windows/Fonts")
    regular = fonts_dir / "arial.ttf"
    bold = fonts_dir / "arialbd.ttf"
    italic = fonts_dir / "ariali.ttf"
    mono = fonts_dir / "consola.ttf"

    if regular.exists() and bold.exists():
        pdfmetrics.registerFont(TTFont("CourseSans", str(regular)))
        pdfmetrics.registerFont(TTFont("CourseSans-Bold", str(bold)))
        if italic.exists():
            pdfmetrics.registerFont(TTFont("CourseSans-Italic", str(italic)))
        else:
            pdfmetrics.registerFont(TTFont("CourseSans-Italic", str(regular)))
        if mono.exists():
            pdfmetrics.registerFont(TTFont("CourseMono", str(mono)))
        else:
            pdfmetrics.registerFont(TTFont("CourseMono", str(regular)))
        return "CourseSans", "CourseSans-Bold", "CourseSans-Italic", "CourseMono"

    return "Helvetica", "Helvetica-Bold", "Helvetica-Oblique", "Courier"


FONT, FONT_BOLD, FONT_ITALIC, FONT_MONO = register_fonts()


def build_styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "CourseTitle",
            parent=base["Title"],
            fontName=FONT_BOLD,
            fontSize=20,
            leading=25,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#17324D"),
            spaceAfter=10,
        ),
        "h2": ParagraphStyle(
            "CourseH2",
            parent=base["Heading2"],
            fontName=FONT_BOLD,
            fontSize=13.5,
            leading=17,
            textColor=colors.HexColor("#17324D"),
            spaceBefore=11,
            spaceAfter=6,
            keepWithNext=True,
        ),
        "h3": ParagraphStyle(
            "CourseH3",
            parent=base["Heading3"],
            fontName=FONT_BOLD,
            fontSize=11.5,
            leading=15,
            textColor=colors.HexColor("#255C7A"),
            spaceBefore=8,
            spaceAfter=4,
            keepWithNext=True,
        ),
        "body": ParagraphStyle(
            "CourseBody",
            parent=base["BodyText"],
            fontName=FONT,
            fontSize=9.7,
            leading=14.2,
            alignment=TA_LEFT,
            spaceAfter=5.5,
        ),
        "bullet": ParagraphStyle(
            "CourseBullet",
            parent=base["BodyText"],
            fontName=FONT,
            fontSize=9.5,
            leading=13.5,
            leftIndent=4,
            firstLineIndent=0,
            spaceAfter=2.5,
        ),
        "code": ParagraphStyle(
            "CourseCode",
            parent=base["Code"],
            fontName=FONT_MONO,
            fontSize=7.6,
            leading=9.5,
            textColor=colors.HexColor("#1F2933"),
            backColor=colors.HexColor("#F4F6F8"),
            borderColor=colors.HexColor("#D7DEE5"),
            borderWidth=0.4,
            borderPadding=5,
            spaceBefore=4,
            spaceAfter=8,
            splitLongWords=True,
        ),
        "table": ParagraphStyle(
            "CourseTableCell",
            parent=base["BodyText"],
            fontName=FONT,
            fontSize=7.8,
            leading=9.6,
        ),
        "table_header": ParagraphStyle(
            "CourseTableHeader",
            parent=base["BodyText"],
            fontName=FONT_BOLD,
            fontSize=7.9,
            leading=9.7,
            textColor=colors.white,
        ),
        "footer": ParagraphStyle(
            "CourseFooter",
            parent=base["BodyText"],
            fontName=FONT,
            fontSize=7.5,
            leading=9,
            textColor=colors.HexColor("#6B7280"),
        ),
    }


STYLES = build_styles()


def xml_text(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", f'<font face="{FONT_MONO}">\\1</font>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    return text


def normalize_line(line: str) -> str:
    return line.replace("\ufeff", "").rstrip().replace("\t", "    ")


def wrap_code_line(line: str, width: int = 92) -> list[str]:
    if len(line) <= width:
        return [line]
    chunks = []
    current = line
    indent = re.match(r"^\s*", line).group(0)
    while len(current) > width:
        cut = current.rfind(" ", 0, width)
        if cut < max(20, len(indent) + 12):
            cut = width
        chunks.append(current[:cut].rstrip())
        current = indent + "  " + current[cut:].lstrip()
    chunks.append(current)
    return chunks


def make_table(rows: list[list[str]]) -> Table:
    max_cols = max(len(r) for r in rows)
    clean_rows = [r + [""] * (max_cols - len(r)) for r in rows]
    data = []
    for row_index, row in enumerate(clean_rows):
        style = STYLES["table_header"] if row_index == 0 else STYLES["table"]
        data.append([Paragraph(xml_text(cell.strip()), style) for cell in row])

    page_width = A4[0] - 36 * mm
    col_width = page_width / max_cols
    table = Table(data, colWidths=[col_width] * max_cols, hAlign="LEFT", repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#17324D")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), FONT_BOLD),
                ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#FFFFFF")),
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#CAD2D9")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return table


def clean_mermaid_label(value: str) -> str:
    value = value.strip()
    value = re.sub(r"^\|(.+)\|$", r"\1", value).strip()
    value = re.sub(r"^[A-Za-z0-9_]+\s*(?:\[\s*\"?|{\s*\"?)?", "", value).strip()
    value = re.sub(r"\"?\s*(?:\]|})$", "", value).strip()
    value = value.replace("<br/>", "; ").replace("<br>", "; ")
    return value or "connects to"


def mermaid_node_id(token: str) -> str:
    match = re.match(r"\s*([A-Za-z0-9_]+)", token.strip())
    return match.group(1) if match else token.strip()


def mermaid_node_label(token: str) -> str:
    token = token.strip()
    quoted = re.match(r"([A-Za-z0-9_]+)\s*(?:\[|{)\s*\"(.+?)\"\s*(?:\]|})", token)
    if quoted:
        return quoted.group(2).replace("<br/>", "; ").replace("<br>", "; ")
    plain = re.match(r"([A-Za-z0-9_]+)\s*(?:\[|{)\s*(.+?)\s*(?:\]|})", token)
    if plain:
        return plain.group(2).replace("<br/>", "; ").replace("<br>", "; ").strip('"')
    return mermaid_node_id(token)


def mermaid_to_flow_table(code_lines: list[str]) -> Table | None:
    labels: dict[str, str] = {}
    edges: list[tuple[str, str, str]] = []

    for raw in code_lines:
        line = raw.strip()
        if not line or line.startswith("flowchart") or line.startswith("graph"):
            continue

        for match in re.finditer(r"([A-Za-z0-9_]+)\s*(?:\[|{)\s*\"(.+?)\"\s*(?:\]|})", line):
            labels[match.group(1)] = match.group(2).replace("<br/>", "; ").replace("<br>", "; ")

        if "-->" in line:
            left, right = line.split("-->", 1)
        elif "-.->" in line:
            left, right = line.split("-.->", 1)
        else:
            continue

        relation = "connects to"
        right = right.strip()
        if right.startswith("|"):
            end = right.find("|", 1)
            if end != -1:
                relation = right[1:end].strip() or relation
                right = right[end + 1 :].strip()

        left_id = mermaid_node_id(left)
        right_id = mermaid_node_id(right)
        labels.setdefault(left_id, mermaid_node_label(left))
        labels.setdefault(right_id, mermaid_node_label(right))
        edges.append((labels[left_id], relation, labels[right_id]))

    if not edges:
        return None

    rows = [["From", "Relationship", "To"]]
    rows.extend([list(edge) for edge in edges])
    return make_table(rows)


def parse_table(lines: list[str], start: int) -> tuple[Table | None, int]:
    table_lines = []
    i = start
    while i < len(lines) and lines[i].strip().startswith("|") and lines[i].strip().endswith("|"):
        table_lines.append(lines[i].strip())
        i += 1

    if len(table_lines) < 2:
        return None, start

    rows: list[list[str]] = []
    for idx, line in enumerate(table_lines):
        cells = [c.strip() for c in line.strip("|").split("|")]
        if idx == 1 and all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells):
            continue
        rows.append(cells)

    if len(rows) < 1:
        return None, start
    return make_table(rows), i


def flush_paragraph(story: list, paragraph_lines: list[str]) -> None:
    if not paragraph_lines:
        return
    text = " ".join(line.strip() for line in paragraph_lines if line.strip())
    if text:
        story.append(Paragraph(xml_text(text), STYLES["body"]))
    paragraph_lines.clear()


def flush_bullets(story: list, bullet_items: list[str]) -> None:
    if not bullet_items:
        return
    items = [
        ListItem(Paragraph(xml_text(item), STYLES["bullet"]), leftIndent=10)
        for item in bullet_items
    ]
    story.append(
        ListFlowable(
            items,
            bulletType="bullet",
            start="circle",
            leftIndent=14,
            bulletFontName=FONT,
            bulletFontSize=7,
        )
    )
    story.append(Spacer(1, 2))
    bullet_items.clear()


def markdown_to_story(markdown: str) -> list:
    story: list = []
    lines = [normalize_line(line) for line in markdown.splitlines()]
    paragraph_lines: list[str] = []
    bullet_items: list[str] = []
    i = 0
    first_heading = True

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            flush_paragraph(story, paragraph_lines)
            flush_bullets(story, bullet_items)
            i += 1
            continue

        if stripped.startswith("```"):
            flush_paragraph(story, paragraph_lines)
            flush_bullets(story, bullet_items)
            language = stripped.strip("`").strip()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.extend(wrap_code_line(lines[i]))
                i += 1
            if language == "mermaid":
                diagram_table = mermaid_to_flow_table(code_lines)
                if diagram_table is not None:
                    story.append(Paragraph("Visual flow", STYLES["h3"]))
                    story.append(diagram_table)
                    story.append(Spacer(1, 8))
                else:
                    story.append(Paragraph("Visual diagram notes", STYLES["h3"]))
                    story.append(Preformatted("\n".join(code_lines), STYLES["code"], maxLineLength=100))
            else:
                story.append(Paragraph("Command / configuration block", STYLES["h3"]))
                story.append(Preformatted("\n".join(code_lines), STYLES["code"], maxLineLength=100))
            i += 1
            continue

        if stripped in {"---", "***", "___"}:
            flush_paragraph(story, paragraph_lines)
            flush_bullets(story, bullet_items)
            story.append(HRFlowable(width="100%", thickness=0.45, color=colors.HexColor("#CAD2D9"), spaceBefore=4, spaceAfter=8))
            i += 1
            continue

        if stripped.startswith("|") and stripped.endswith("|"):
            flush_paragraph(story, paragraph_lines)
            flush_bullets(story, bullet_items)
            table, new_i = parse_table(lines, i)
            if table is not None:
                story.append(table)
                story.append(Spacer(1, 8))
                i = new_i
                continue

        if stripped.startswith("#"):
            flush_paragraph(story, paragraph_lines)
            flush_bullets(story, bullet_items)
            level = len(stripped) - len(stripped.lstrip("#"))
            heading = stripped[level:].strip()
            if level == 1:
                if not first_heading:
                    story.append(PageBreak())
                story.append(Paragraph(xml_text(heading), STYLES["title"]))
                story.append(HRFlowable(width="100%", thickness=0.7, color=colors.HexColor("#17324D"), spaceAfter=8))
                first_heading = False
            elif level == 2:
                story.append(Paragraph(xml_text(heading), STYLES["h2"]))
            else:
                story.append(Paragraph(xml_text(heading), STYLES["h3"]))
            i += 1
            continue

        bullet_match = re.match(r"^[-*]\s+(.*)$", stripped)
        if bullet_match:
            flush_paragraph(story, paragraph_lines)
            bullet_items.append(bullet_match.group(1).strip())
            i += 1
            continue

        numbered_match = re.match(r"^\d+\.\s+(.*)$", stripped)
        if numbered_match and len(stripped) < 180:
            flush_paragraph(story, paragraph_lines)
            flush_bullets(story, bullet_items)
            story.append(Paragraph(xml_text(stripped), STYLES["body"]))
            i += 1
            continue

        flush_bullets(story, bullet_items)
        paragraph_lines.append(line)
        i += 1

    flush_paragraph(story, paragraph_lines)
    flush_bullets(story, bullet_items)
    return story


class LessonDocTemplate(BaseDocTemplate):
    def __init__(self, filename: str, lesson_title: str):
        self.lesson_title = lesson_title
        super().__init__(
            filename,
            pagesize=A4,
            leftMargin=18 * mm,
            rightMargin=18 * mm,
            topMargin=18 * mm,
            bottomMargin=16 * mm,
            title=lesson_title,
            author="FEMTECT",
        )
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            id="normal",
            showBoundary=0,
        )
        self.addPageTemplates([PageTemplate(id="CoursePage", frames=[frame], onPage=self.draw_header_footer)])

    def draw_header_footer(self, canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(colors.HexColor("#CAD2D9"))
        canvas.setLineWidth(0.35)
        canvas.line(self.leftMargin, A4[1] - 12 * mm, A4[0] - self.rightMargin, A4[1] - 12 * mm)
        canvas.line(self.leftMargin, 11 * mm, A4[0] - self.rightMargin, 11 * mm)
        canvas.setFont(FONT, 7.5)
        canvas.setFillColor(colors.HexColor("#6B7280"))
        canvas.drawString(self.leftMargin, A4[1] - 9 * mm, "FEMTECT Network Engineering Foundation Course")
        canvas.drawRightString(A4[0] - self.rightMargin, 7 * mm, f"Page {doc.page}")
        canvas.restoreState()


def build_pdf(markdown_file: Path) -> Path:
    text = markdown_file.read_text(encoding="utf-8")
    title = next((line.lstrip("# ").strip() for line in text.splitlines() if line.startswith("# ")), markdown_file.stem)
    output = OUTPUT_DIR / f"{markdown_file.stem}.pdf"
    story = markdown_to_story(text)
    doc = LessonDocTemplate(str(output), title)
    doc.build(story)
    return output


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    lessons = sorted(LESSON_DIR.glob("Lesson_*.md"))
    if len(lessons) != 20:
        raise SystemExit(f"Expected 20 lesson files, found {len(lessons)}")
    built = [build_pdf(path) for path in lessons]
    for path in built:
        print(path)


if __name__ == "__main__":
    main()
