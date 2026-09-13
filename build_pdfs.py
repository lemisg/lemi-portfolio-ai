"""Generates lemi_resume.pdf (1-page) and lemi_cv.pdf from structured content."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, ListFlowable, ListItem, Table, TableStyle
from reportlab.lib import colors

FONT = "Times-Roman"
FONT_B = "Times-Bold"

name_style = ParagraphStyle("name", fontName=FONT_B, fontSize=16, alignment=TA_CENTER, spaceAfter=2)
contact_style = ParagraphStyle("contact", fontName=FONT, fontSize=9.5, alignment=TA_CENTER, spaceAfter=8, textColor=colors.HexColor("#1a1a1a"))
section_style = ParagraphStyle("section", fontName=FONT_B, fontSize=11, spaceBefore=8, spaceAfter=2)
job_title_style = ParagraphStyle("job_title", fontName=FONT_B, fontSize=10, spaceBefore=5, spaceAfter=0, leading=13)
job_meta_style = ParagraphStyle("job_meta", fontName=FONT, fontSize=9.5, fontStyle="italic", spaceAfter=2, leading=12, textColor=colors.HexColor("#333333"))
body_style = ParagraphStyle("body", fontName=FONT, fontSize=9.5, alignment=TA_LEFT, leading=12.5, spaceAfter=3)
bullet_style = ParagraphStyle("bullet", fontName=FONT, fontSize=9.5, alignment=TA_LEFT, leading=12.5, leftIndent=14, bulletIndent=2, spaceAfter=2)
summary_style = ParagraphStyle("summary", fontName=FONT, fontSize=9.5, alignment=TA_LEFT, leading=13, spaceAfter=6)

# Compact variants for the 1-page resume
r_section_style = ParagraphStyle("r_section", fontName=FONT_B, fontSize=10.5, spaceBefore=6, spaceAfter=1)
r_job_title_style = ParagraphStyle("r_job_title", fontName=FONT_B, fontSize=9.5, spaceBefore=4, spaceAfter=0, leading=12)
r_job_meta_style = ParagraphStyle("r_job_meta", fontName=FONT, fontSize=9, spaceAfter=1, leading=11, textColor=colors.HexColor("#333333"))
r_body_style = ParagraphStyle("r_body", fontName=FONT, fontSize=9, alignment=TA_LEFT, leading=11, spaceAfter=2)
r_bullet_style = ParagraphStyle("r_bullet", fontName=FONT, fontSize=9, alignment=TA_LEFT, leading=11, leftIndent=12, bulletIndent=1, spaceAfter=1)


def r_hr():
    return HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#666666"), spaceBefore=0.5, spaceAfter=3)


def r_section(title):
    return [Paragraph(title, r_section_style), r_hr()]


def r_job(title, meta, bullets):
    flow = [Paragraph(title, r_job_title_style)]
    if meta:
        flow.append(Paragraph(meta, r_job_meta_style))
    items = [ListItem(Paragraph(b, r_bullet_style), leftIndent=12, value="•") for b in bullets]
    flow.append(ListFlowable(items, bulletType="bullet", start="•", leftIndent=8))
    return flow


def hr():
    return HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#666666"), spaceBefore=1, spaceAfter=4)


def section(title):
    return [Paragraph(title, section_style), hr()]


def job(title, meta, bullets):
    flow = [Paragraph(title, job_title_style), Paragraph(meta, job_meta_style)]
    items = [ListItem(Paragraph(b, bullet_style), leftIndent=14, value="•") for b in bullets]
    flow.append(ListFlowable(items, bulletType="bullet", start="•", leftIndent=10))
    return flow


def header(story):
    story.append(Paragraph("Lemi Gemedi", name_style))
    story.append(Paragraph(
        '678-973-7066 | <a href="mailto:lemikind@gmail.com" color="blue">lemikind@gmail.com</a> | Corvallis, OR | '
        '<a href="http://www.linkedin.com/in/lemi-gemedi-4202023JAN51911" color="blue">linkedin.com/in/lemi-gemedi</a> | '
        '<a href="https://github.com/lemisg" color="blue">github.com/lemisg</a>',
        contact_style))


# ============================= RESUME (1-page) =============================
resume = SimpleDocTemplate(
    "lemi_resume.pdf", pagesize=letter,
    topMargin=0.45 * inch, bottomMargin=0.4 * inch, leftMargin=0.65 * inch, rightMargin=0.65 * inch,
)
s = []
header(s)

s += r_section("EDUCATION")
s.append(Paragraph("<b>Oregon State University</b>, Corvallis, OR &nbsp;&nbsp;|&nbsp;&nbsp; Bachelor of Science in Electrical and Computer Engineering &nbsp;|&nbsp; Expected: Early 2028", r_body_style))
s.append(Paragraph("Minor in Management and Computer Science &nbsp;|&nbsp; Relevant Coursework: ECE 310 &ndash; Semiconductor Processing", r_body_style))

s += r_section("PROFICIENCIES")
s.append(Paragraph("<b>Software:</b> MATLAB, AutoCAD, LaTeX, C/C++, Microsoft Office, macOS, Computer Proficiency (MS Office Suite), Canva, Machine Learning", r_body_style))
s.append(Paragraph("<b>Languages:</b> English (Advanced), Oromo (Native), Amharic (Native), Spanish (Intermediate)", r_body_style))

s += r_section("EXPERIENCE")
s += r_job("IT Project Management Intern &mdash; Multnomah County, Dept. of County Assets, Portland, OR &nbsp;(2026 &ndash; Present)",
           "",
           ["Coordinated project schedules, tracked deliverables, and maintained documentation for county IT initiatives.",
            "Facilitated communication between technical staff and stakeholders to gather system requirements."])
s += r_job("Wafer Fab Operator &mdash; Intel (via Manpower), Beaverton, OR &nbsp;(Summers 2025 &ndash; Present)",
           "",
           ["Operated semiconductor equipment and managed wafer handling under strict safety procedures.",
            "Oversaw the full production cycle (dicing, final packaging, shipping) and quality control inspections."])
s += r_job("Diversity Learning Assistant &mdash; OSU, UHDS, Corvallis, OR &nbsp;(2024 &ndash; Present, during school year)",
           "",
           ["Execute social justice education programming for a diverse residential community of 400+ residents."])
s += r_job("Community Relations Representative &mdash; Lonnie B. Harris Black Cultural Center, Corvallis, OR &nbsp;(2024 &ndash; Present)",
           "",
           ["Connect students to campus resources; coordinate events and outreach for community programs."])
s += r_job("Beaver Connect Peer Mentor &mdash; Oregon State University, Corvallis, OR &nbsp;(2024 &ndash; 2025)",
           "",
           ["Helped incoming freshman students with their college adjustment and connected with engineering faculty."])
s += r_job("Caregiver &mdash; Kirubeti Teen Home Care / Yilma Gamachu, Tame and Yilma LLC &nbsp;(2025 &ndash; Present, school breaks)",
           "",
           ["Assisted clients with anger management, emotional control, and daily living needs."])
s += r_job("Plumbing Sales Associate &mdash; The Home Depot, Inc., Beaverton, OR &nbsp;(2022 &ndash; 2024, summers)",
           "",
           ["Leveraged product knowledge and communication to engage customers and drive sales."])

mini_header = ParagraphStyle("mini", fontName=FONT_B, fontSize=9, spaceBefore=0, spaceAfter=1)
left_col = [Paragraph("COMMUNITY SERVICE & LEADERSHIP", mini_header),
            ListFlowable([ListItem(Paragraph(t, r_bullet_style), leftIndent=12, value="•") for t in [
                "Yearly Volunteer, Oregon Hood to Coast",
                "OSU National Society of Black Engineers",
                "East African Student Association: Officer",
                "Kappa Alpha Psi Fraternity Inc.: VP",
                "Biweekly Volunteer, Linn Benton Food Share",
            ]], bulletType="bullet", leftIndent=8)]
right_col = [Paragraph("CERTIFICATIONS", mini_header),
             ListFlowable([ListItem(Paragraph(t, r_bullet_style), leftIndent=12, value="•") for t in [
                "ISSA Certified Personal Trainer (CPT)",
                "ISSA Strength &amp; Conditioning Specialist",
                "ISSA Nutrition Coach",
                "ISSA Business of Personal Training",
                "CPR/AED Certification",
                "Oregon Intervention System (OIS) Training",
             ]], bulletType="bullet", leftIndent=8)]
s.append(r_hr())
combo = Table([[left_col, right_col]], colWidths=[3.15 * inch, 3.15 * inch])
combo.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 6), ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
s.append(combo)

s += r_section("PROJECTS")
items = [ListItem(Paragraph(t, r_bullet_style), leftIndent=12, value="•") for t in [
    "<b>Semiconductor &amp; Device Fab:</b> Fabricated NMOS transistors and MOS capacitors from raw Si wafers in a cleanroom; managed thin-film deposition and four-layer photolithographic masking.",
    "<b>AI Portfolio Website:</b> Full-stack site (Flask + Gemini API) with an interactive AI assistant trained on my resume and CV.",
    "<b>Hunt the Wumpus:</b> A grid-based adventure game using polymorphism and inheritance to manage interactive hazards.",
    "<b>Connect Four:</b> A terminal-based game for human-vs-computer play with alternating-turn and win-condition logic.",
]]
s.append(ListFlowable(items, bulletType="bullet", leftIndent=8))

resume.build(s)
print("wrote lemi_resume.pdf")

# ============================= CV (full) =============================
cv = SimpleDocTemplate(
    "lemi_cv.pdf", pagesize=letter,
    topMargin=0.6 * inch, bottomMargin=0.6 * inch, leftMargin=0.75 * inch, rightMargin=0.75 * inch,
)
c = []
header(c)

c += section("PROFESSIONAL SUMMARY")
c.append(Paragraph(
    "Quadrilingual computer electrical engineering student with a minor in computer science, and hands-on "
    "experience in IT project management and semiconductor processing, driven to be the first college graduate "
    "in the family. Seeking to leverage a strong technical foundation in C++, HTML, and semiconductor process "
    "fundamentals, proven project coordination and leadership skills, and cross-cultural communication to "
    "contribute to innovative engineering projects in an engineering internship or academic research role. "
    "Successfully managed complex logistics, coordinated IT project deliverables, fostered inclusive community "
    "environments, and provided high-level consultative sales support.", summary_style))

c += section("EDUCATION")
c.append(Paragraph("<b>Oregon State University</b>, Corvallis, OR", body_style))
c.append(Paragraph("B.S. in Computer Electrical Engineering | Expected Graduation: June 2027", body_style))
c.append(Paragraph("Minor in Management and Computer Science", body_style))
c.append(Paragraph("Relevant Coursework: ECE 310 &ndash; Semiconductor Processing (theory and practice of semiconductor processing techniques and process simulation)", body_style))

c += section("TECHNICAL SKILLS")
c.append(Paragraph("<b>Programming:</b> C++, HTML", body_style))
c.append(Paragraph("<b>Tools/Concepts:</b> Project Coordination, Semiconductor Process Simulation, Digital and Physical Research, Computer Proficiency (MS Office Suite), Canva", body_style))

c += section("LANGUAGES")
c.append(Paragraph("<b>Quadrilingual Fluency:</b> Oromo (Native), Amharic (Native), English (Advanced), Spanish (Intermediate)", body_style))

c += section("EXPERIENCE & LEADERSHIP")
c += job("IT Project Management Intern &mdash; Multnomah County, Department of County Assets, Portland, OR",
         "2026 &ndash; Present",
         ["Coordinated project schedules, tracked deliverables, and maintained documentation for county IT initiatives.",
          "Facilitated communication between technical staff and department stakeholders to gather system requirements and align project scope.",
          "Supported planning and status reporting for multiple concurrent IT projects within a government agency setting."])
c += job("Wafer Fab Operator &mdash; Intel (via Manpower), Beaverton, OR",
         "June 2025 &ndash; September 2025",
         ["Operated specialized semiconductor production equipment according to manufacturing priorities in a highly regulated cleanroom environment.",
          "Managed the end-to-end production cycle, including processing customer orders, wafer dicing, and final packaging and shipping logistics.",
          "Conducted visual quality control inspections and performed accurate data entry to track production progress.",
          "Managed the safe transport and handling of silicon wafer lots, strictly following cleanroom, chemical, and wafer handling procedures.",
          "Collaborated with the production team to troubleshoot and resolve quality challenges."])
c += job("OSU Student Ambassador for The Script &mdash; Oregon State University, Corvallis, OR",
         "Oct 2025 &ndash; Present",
         ["Served as the primary student ambassador for the Script Internship Program, executing on-campus outreach and recruitment strategies.",
          "Tasked with driving a minimum of 40 program applications from underrepresented communities.",
          "Managed monthly digital marketing campaigns on Instagram and LinkedIn."])
c += job("Diversity Learning Assistant &mdash; Oregon State University, UHDS, Corvallis, OR",
         "2024 &ndash; Present",
         ["Executed social justice education programming (dialogues, bulletin boards, hall engagement) for a diverse residential community of 400+ residents.",
          "Served as a key university ambassador, connecting residents to academic advising and mental health services.",
          "Collaborated with the Assistant Director and hall staff to maintain community standards and promote social equity initiatives."])
c += job("Community Relation Rep (CRR) &mdash; Lonnie B. Harris Black Cultural Center, Corvallis, OR",
         "2024 &ndash; Present",
         ["Directly connected peers to critical campus resources (e.g., Academic Success Center, tutoring services).",
          "Executed logistical and outreach efforts for community programming, including history and heritage month celebrations.",
          "Managed daily center operations and maintained a welcoming, inclusive physical space."])
c += job("Caregiver &mdash; Kirubeti Teen Home Care, Beaverton, OR",
         "June 2025 &ndash; Present (during school breaks)",
         ["Assisted clients with anger management and emotional control.",
          "Assisted clients with daily living needs and provided emotional support and companionship."])
c += job("Plumbing Sales Associate &mdash; The Home Depot, Inc., Beaverton, OR",
         "2022 &ndash; 2024",
         ["Engaged proactively with contractors, builders, and professional plumbers to drive departmental sales.",
          "Provided expert product consultation for a wide range of plumbing tools and materials."])
c += job("Caregiver, Elderly Homecare (Hospice) &mdash; Yilma Gamachu, Tame and Yilma LLC",
         "2022 &ndash; 2023",
         ["Assisted clients in hospice with daily living needs and built strong relationships to deliver emotional support."])

c += section("COMMUNITY SERVICE")
c += job("Volunteer Exchange Leader &mdash; Oregon Hood to Coast", "",
         ["Led and managed a team of over 30 volunteers at a major race checkpoint.",
          "Coordinated on-site logistics, equipment management, and vehicle parking control.",
          "Enforced race rules and safety protocols; served as primary point of contact for emergencies."])
c += job("Community Outreach Volunteer &mdash; Kappa Alpha Psi Fraternity Inc.", "",
         ["Coordinated the annual “Shop with Kappas” event, a sponsored shopping spree for underprivileged children."])
c += job("Literacy Volunteer &mdash; Kappa Alpha Psi Fraternity Inc.", "",
         ["Partnered with a local elementary school to read to children and promote early literacy.",
          "Paid student peer mentor for incoming freshman students through Beaver Connect (2024-25)."])
c += job("Community Service Volunteer &mdash; Kappa Alpha Psi Fraternity Inc.", "",
         ["Participated in a fraternity-led program addressing food insecurity; prepared and served meals to the local homeless population."])

c += section("UNIVERSITY INVOLVEMENT & ACTIVITIES")
items = [ListItem(Paragraph(t, bullet_style), leftIndent=14, value="•") for t in [
    "<b>OSU National Society of Black Engineers (NSBE):</b> Board Member",
    "<b>Kappa Alpha Psi Fraternity Inc.:</b> Vice President",
    "<b>East African Student Association (EASA):</b> Community Relations Officer",
    "<b>African Student Association (ASA):</b> Community Relations Officer",
    "<b>OSU Global Formula Racing Team:</b> Member",
]]
c.append(ListFlowable(items, bulletType="bullet", leftIndent=10))

c += section("CERTIFICATIONS")
items = [ListItem(Paragraph(t, bullet_style), leftIndent=14, value="•") for t in [
    "ISSA Certified Personal Trainer (CPT)",
    "ISSA Strength &amp; Conditioning Specialist",
    "ISSA Nutrition Coach",
    "ISSA Business of Personal Training",
    "CPR/AED Certification",
    "First Aid Certificate",
    "Pre-Service Dementia Care Training for Direct Care Staff",
    "Kognito Certificate",
    "Oregon Intervention System (OIS) Training",
    "Direct Support Professional (DSP) Core Competencies &ndash; Tier 1 Program",
]]
c.append(ListFlowable(items, bulletType="bullet", leftIndent=10))

cv.build(c)
print("wrote lemi_cv.pdf")
