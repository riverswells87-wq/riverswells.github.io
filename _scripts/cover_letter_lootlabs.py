from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.platypus.flowables import Flowable

OUTPUT = "/mnt/user-data/outputs/Rivers_Wells_Cover_Letter_LootLabs.pdf"

DARK  = colors.HexColor("#1A2B3C")
MID   = colors.HexColor("#2E5E8E")
LIGHT = colors.HexColor("#5B8DB8")
GRAY  = colors.HexColor("#555555")
LGRAY = colors.HexColor("#888888")

doc = SimpleDocTemplate(OUTPUT, pagesize=letter,
    leftMargin=0.65*inch, rightMargin=0.65*inch,
    topMargin=0.55*inch, bottomMargin=0.55*inch)

def S(name, **kw): return ParagraphStyle(name, **kw)

NAME    = S("Name",   fontName="Helvetica-Bold", fontSize=22, textColor=DARK, spaceAfter=0, leading=26)
TAGLINE = S("Tag",    fontName="Helvetica-Oblique", fontSize=10, textColor=MID, spaceAfter=0, leading=14, alignment=TA_RIGHT)
CONT    = S("Cont",   fontName="Helvetica", fontSize=9, textColor=LGRAY, spaceAfter=6, leading=13)
DATE_S  = S("Date",   fontName="Helvetica", fontSize=10, textColor=GRAY, spaceAfter=16, leading=14)
SALUT   = S("Salut",  fontName="Helvetica-Bold", fontSize=10, textColor=DARK, spaceAfter=12, leading=14)
BODY    = S("Body",   fontName="Helvetica", fontSize=10, textColor=GRAY, spaceAfter=12, leading=15, alignment=TA_JUSTIFY)
CLOSE   = S("Close",  fontName="Helvetica", fontSize=10, textColor=GRAY, spaceAfter=4, leading=14)
SIG     = S("Sig",    fontName="Helvetica-Bold", fontSize=10, textColor=DARK, spaceAfter=0, leading=14)

def rule(): return HRFlowable(width="100%", thickness=0.75, color=LIGHT, spaceAfter=16)

def add_accent_bar(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(MID)
    canvas.rect(0.25*inch, 0, 0.18*inch, 11*inch, fill=1, stroke=0)
    canvas.restoreState()

story = []

# Two-column header
header_table = Table(
    [[Paragraph("M. Rivers Wells", NAME),
      Paragraph("Editorial Lead.  Content Strategist.  Community Builder.", TAGLINE)]],
    colWidths=[3.8*inch, 3.4*inch],
    hAlign="LEFT"
)
header_table.setStyle(TableStyle([
    ("VALIGN",       (0,0), (-1,-1), "BOTTOM"),
    ("LEFTPADDING",  (0,0), (-1,-1), 0),
    ("RIGHTPADDING", (0,0), (-1,-1), 0),
    ("TOPPADDING",   (0,0), (-1,-1), 0),
    ("BOTTOMPADDING",(0,0), (-1,-1), 0),
]))
story.append(header_table)
story.append(Spacer(1, 4))
story.append(Paragraph(
    "205.522.6027  &bull;  riverwells87@gmail.com  &bull;  riverswells.com", CONT))
story.append(rule())
story.append(Paragraph("May 2026", DATE_S))
story.append(Paragraph("Dear Hiring Manager,", SALUT))

# ── EDIT PARAGRAPH TEXT BELOW THIS LINE ──────────────────────────────────────

story.append(Paragraph(
    "I am writing to express my interest in the Senior Editorial Lead role at Loot Labs. "
    "Building an editorial function from the ground up across blog, video, social, and "
    "community channels, with accountability for tying content performance back to "
    "product engagement and revenue retention, is the kind of ownership-oriented role "
    "I have been looking for. I am a published fantasy author, the designer of a "
    "self-published tabletop roleplaying game, and a longtime participant in the "
    "collecting and gaming community. This is not a market I am learning for this "
    "role. It is one I am already part of.",
    BODY))

story.append(Paragraph(
    "My content background spans 9+ years of technical writing, content strategy, and "
    "program management at Amazon, where I owned a content platform serving 350,000 "
    "monthly readers, built editorial standards and intake models from scratch, and "
    "produced video content using Adobe Creative Cloud that accumulated 1.5 million views "
    "at a 55% audience engagement rate. I have managed content across CMS platforms, "
    "maintained style guides, and driven data-informed content improvements that added "
    "measurable basis points to site performance. I understand SEO as a discoverability "
    "discipline, having optimized information architecture and content categorization "
    "to improve how users find content across tools and interfaces.",
    BODY))

story.append(Paragraph(
    "The editorial leadership this role requires is inseparable from program management, "
    "and that is where my professional credentials are strongest. I have managed "
    "cross-functional teams, built and maintained master editorial calendars, coordinated "
    "freelance contributors, and driven campaigns across multiple concurrent channels "
    "without losing quality or momentum. I set clear standards, give specific feedback, "
    "and build the processes that let a small team scale output. I have also built "
    "AI-driven workflow automation that reduced document creation time by 80%, and I "
    "bring that same instinct for operational efficiency to an editorial function that "
    "needs to produce consistently at pace.",
    BODY))

story.append(Paragraph(
    "Loot Labs is building something genuinely fun in a space I care about. "
    "I would welcome the opportunity to discuss how my background fits the team's "
    "needs. Thank you for your time.",
    BODY))

# ── END OF EDITABLE CONTENT ───────────────────────────────────────────────────

story.append(Spacer(1, 16))
story.append(Paragraph("Sincerely,", CLOSE))
story.append(Spacer(1, 28))
story.append(Paragraph("M. Rivers Wells", SIG))

doc.build(story, onFirstPage=add_accent_bar, onLaterPages=add_accent_bar)
print("Done:", OUTPUT)
