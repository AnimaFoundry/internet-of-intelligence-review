"""Build the original review and schematic; does not fetch or copy source papers."""
import argparse
from functools import partial
from html import escape
import json
from pathlib import Path
import re

from reportlab import rl_config
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Preformatted
from reportlab.graphics.shapes import Drawing, Rect, Line, Polygon, String

ROOT = Path(__file__).resolve().parents[1]
INK = colors.HexColor('#172C3B')
BLUE = colors.HexColor('#235C78')
WIDTH = A4[0] - 104
rl_config.warnOnMissingFontGlyphs = 1


def schematic():
    d = Drawing(WIDTH, 188)
    labels = [(['OBJECT / NODE', 'Transduction, timing', 'Energy and availability'], 0),
              (['GATEWAY / EDGE', 'Align, validate, buffer', 'Provenance and selection'], 170),
              (['LEARNING SYSTEM', 'Train and evaluate', 'Actions and uncertainty'], 340)]
    boxw = 151
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} 188" role="img" aria-label="Observation and capability loop">',
           '<rect width="100%" height="100%" fill="white"/>']
    for words, x in labels:
        d.add(Rect(x, 93, boxw, 76, rx=4, ry=4, fillColor=colors.HexColor('#EDF3F6'), strokeColor=BLUE))
        svg.append(f'<rect x="{x}" y="19" width="{boxw}" height="76" rx="4" fill="#EDF3F6" stroke="#235C78"/>')
        for j, s in enumerate(words):
            y = 150 - 18 * j
            d.add(String(x + boxw / 2, y, s, fontName='Helvetica-Bold' if j == 0 else 'Helvetica', fontSize=8.4, fillColor=INK, textAnchor='middle'))
            svg.append(f'<text x="{x+boxw/2}" y="{188-y}" text-anchor="middle" font-family="sans-serif" font-size="8.4" font-weight="{"bold" if j == 0 else "normal"}">{escape(s)}</text>')
    for x1, x2 in [(151, 170), (321, 340)]:
        d.add(Line(x1 + 2, 131, x2 - 3, 131, strokeColor=BLUE))
        d.add(Polygon([x2 - 7, 134, x2 - 2, 131, x2 - 7, 128], fillColor=BLUE, strokeColor=BLUE))
        svg.append(f'<path d="M{x1+2} 57 H{x2-3} m-4 -3 l5 3 -5 3" fill="none" stroke="#235C78"/>')
    for points in [(415, 93, 415, 48), (415, 48, 75, 48), (75, 48, 75, 91)]:
        d.add(Line(*points, strokeColor=BLUE))
    d.add(Polygon([72, 86, 75, 92, 78, 86], fillColor=BLUE, strokeColor=BLUE))
    svg.append('<path d="M415 95 V140 H75 V97 m-3 5 l3 -6 3 6" fill="none" stroke="#235C78"/>')
    for s, y in [('Validated, compatible capabilities; selective return', 58),
                 ('Some objects only sense. Learning need not run on every node.', 22)]:
        d.add(String(WIDTH / 2, y, s, fontName='Helvetica', fontSize=8.5, textAnchor='middle', fillColor=INK))
        svg.append(f'<text x="{WIDTH/2}" y="{188-y}" text-anchor="middle" font-family="sans-serif" font-size="8.5">{escape(s)}</text>')
    svg.append('</svg>')
    return d, '\n'.join(svg) + '\n'


def render(destination):
    destination.mkdir(parents=True, exist_ok=True)
    (destination / 'figures').mkdir(exist_ok=True)
    source = (ROOT / 'manuscript.md').read_text(encoding='utf-8-sig')
    refs = json.loads((ROOT / 'references.json').read_text(encoding='utf-8-sig'))
    byid = {r['id']: r for r in refs}
    order = list(dict.fromkeys(re.findall(r'\[@([A-Z0-9]+)\]', source)))
    if len(byid) != len(refs) or set(order) != set(byid):
        raise ValueError('Duplicate, missing, or uncited reference')
    nums = {key: i+1 for i, key in enumerate(order)}
    figure, svg = schematic()
    (destination / 'figures' / 'architecture.svg').write_text(svg, encoding='utf-8', newline='\n')

    def citation(match):
        key = match.group(1)
        return f'[{nums[key]}]'

    clean = re.sub(r'\[@([A-Z0-9]+)\]', citation, source)
    bibliography = []
    for key in order:
        r = byid[key]
        bibliography.append(f"[{nums[key]}] {r['authors']}. {r['title']}. {r['publication']}, {r['year']}. {r['url']}")
    (destination / 'paper.md').write_text(clean + '\n## References\n\n' + '\n\n'.join(bibliography) + '\n', encoding='utf-8', newline='\n')

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle('BodyReview', fontName='Times-Roman', fontSize=10.3, leading=14, alignment=TA_JUSTIFY, spaceAfter=7.2, textColor=INK))
    styles.add(ParagraphStyle('TitleReview', fontName='Times-Bold', fontSize=23, leading=27, spaceAfter=9, textColor=INK))
    styles.add(ParagraphStyle('SubtitleReview', fontName='Times-Roman', fontSize=15, leading=19, spaceAfter=12, textColor=BLUE))
    styles.add(ParagraphStyle('H2Review', fontName='Helvetica-Bold', fontSize=12, leading=16, spaceBefore=13, spaceAfter=7, keepWithNext=True, textColor=INK))
    styles.add(ParagraphStyle('H3Review', fontName='Helvetica-Bold', fontSize=10, leading=14, spaceBefore=9, spaceAfter=6, keepWithNext=True, textColor=INK))
    styles.add(ParagraphStyle('CellReview', fontName='Times-Roman', fontSize=8.6, leading=11, textColor=INK))
    styles.add(ParagraphStyle('RefReview', fontName='Times-Roman', fontSize=9, leading=12, spaceAfter=7, textColor=INK))
    styles.add(ParagraphStyle('CaptionReview', fontName='Times-Italic', fontSize=9, leading=12, spaceAfter=9, textColor=INK))
    styles.add(ParagraphStyle('EquationReview', fontName='Courier', fontSize=8.1, leading=13, spaceBefore=5, spaceAfter=9, textColor=INK))

    def inline(s):
        s = escape(s)
        s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
        s = re.sub(r'\[@([A-Z0-9]+)\]', lambda m: f'<link href="#ref-{m.group(1)}" color="#235C78">[{nums[m.group(1)]}]</link>', s)
        return s

    story, lines, i = [], source.splitlines(), 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line.startswith('```'):
            block = []
            i += 1
            while i < len(lines) and not lines[i].startswith('```'):
                block.append(lines[i]); i += 1
            story.append(Preformatted('\n'.join(block), styles['EquationReview']))
        elif line.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                cells = [x.strip() for x in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?', x) for x in cells):
                    rows.append([Paragraph(inline(x), styles['CellReview']) for x in cells])
                i += 1
            table = Table(rows, colWidths=[WIDTH / len(rows[0])] * len(rows[0]), repeatRows=1, hAlign='LEFT')
            table.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#E7EEF2')), ('LINEABOVE',(0,0),(-1,0),0.8,BLUE), ('LINEBELOW',(0,0),(-1,0),0.5,BLUE), ('LINEBELOW',(0,1),(-1,-1),0.3,colors.HexColor('#CED9DF')), ('LEFTPADDING',(0,0),(-1,-1),6), ('RIGHTPADDING',(0,0),(-1,-1),6), ('TOPPADDING',(0,0),(-1,-1),5), ('BOTTOMPADDING',(0,0),(-1,-1),5)]))
            story.extend([table, Spacer(1, 9)])
            continue
        elif line.startswith('!['):
            story.append(figure)
        elif line.startswith('# '):
            story.append(Paragraph(inline(line[2:]), styles['TitleReview']))
        elif line.startswith('### '):
            story.append(Paragraph(inline(line[4:]), styles['H3Review']))
        elif line.startswith('## '):
            name = 'SubtitleReview' if line[3:].startswith('Materials, Distributed') else 'H2Review'
            story.append(Paragraph(inline(line[3:]), styles[name]))
        else:
            block = [line]
            while i + 1 < len(lines) and lines[i+1].strip() and not lines[i+1].startswith(('#','|','```','![')):
                i += 1; block.append(lines[i].strip())
            story.append(Paragraph(inline(' '.join(block)), styles['BodyReview']))
        i += 1
    story.append(Paragraph('References', styles['H2Review']))
    for key, bib in zip(order, bibliography):
        url = byid[key]['url']
        content = escape(bib[:-len(url)]) + f'<link href="{escape(url)}" color="#235C78">{escape(url)}</link>'
        story.append(Paragraph(f'<a name="ref-{key}"/>' + content, styles['RefReview']))

    def decorate(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(BLUE)
        canvas.setFont('Helvetica', 8)
        canvas.drawString(52, 30, 'AnimaFoundry | Review preprint v1.0.0 | Not peer reviewed')
        canvas.drawRightString(A4[0]-52, 30, str(doc.page))
        canvas.restoreState()

    doc = SimpleDocTemplate(str(destination / 'paper.pdf'), pagesize=A4, leftMargin=52, rightMargin=52, topMargin=44, bottomMargin=48, title='Low-Power Sensing for an Internet of Intelligence', author='AnimaFoundry', subject='Critical integrative review; not peer reviewed', pageCompression=1, invariant=1)
    doc.build(story, onFirstPage=decorate, onLaterPages=decorate, canvasmaker=partial(Canvas, invariant=1))
    return {'references': len(order), 'words_approx': len(source.split()), 'output': str(destination)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--destination', type=Path, default=ROOT)
    print(json.dumps(render(parser.parse_args().destination), indent=2))
