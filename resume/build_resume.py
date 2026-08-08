#!/usr/bin/env python3
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.enums import TA_LEFT

ACCENT = colors.HexColor("#0E8C5A")
INK = colors.HexColor("#101914")
MUTED = colors.HexColor("#54615A")
LINE = colors.HexColor("#DCE5DF")

doc = SimpleDocTemplate(
    "Md_Safayet_Ullah_Resume.pdf",
    pagesize=LETTER,
    leftMargin=0.75 * inch, rightMargin=0.75 * inch,
    topMargin=0.65 * inch, bottomMargin=0.65 * inch,
    title="Md Safayet Ullah — Resume",
    author="Md Safayet Ullah",
)

name_style = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=22, textColor=INK, spaceAfter=2, leading=25)
role_style = ParagraphStyle("role", fontName="Helvetica", fontSize=11.5, textColor=ACCENT, spaceAfter=8, leading=14)
contact_style = ParagraphStyle("contact", fontName="Helvetica", fontSize=9.3, textColor=MUTED, spaceAfter=10, leading=12)
h2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=10.8, textColor=INK, spaceBefore=11, spaceAfter=5, leading=13)
body = ParagraphStyle("body", fontName="Helvetica", fontSize=9.4, textColor=INK, leading=12.6, alignment=TA_LEFT, spaceAfter=3)
muted = ParagraphStyle("muted", fontName="Helvetica-Oblique", fontSize=8.9, textColor=MUTED, leading=11.5, spaceAfter=5)
role_line = ParagraphStyle("role_line", fontName="Helvetica-Bold", fontSize=9.6, textColor=INK, leading=12, spaceAfter=0)
date_line = ParagraphStyle("date_line", fontName="Helvetica", fontSize=8.7, textColor=MUTED, leading=11)
bullet = ParagraphStyle("bullet", fontName="Helvetica", fontSize=9.2, textColor=INK, leading=12, leftIndent=12, spaceAfter=2)

story = []

story.append(Paragraph("Md Safayet Ullah", name_style))
story.append(Paragraph("Web Developer &amp; AI / Web Projects", role_style))
story.append(Paragraph(
    "safayetsifat117@gmail.com &nbsp;&nbsp;|&nbsp;&nbsp; github.com/sifat-ech &nbsp;&nbsp;|&nbsp;&nbsp; linkedin.com/in/safayet117 &nbsp;&nbsp;|&nbsp;&nbsp; Chattogram, Bangladesh",
    contact_style
))
story.append(HRFlowable(width="100%", thickness=1, color=LINE, spaceAfter=4))

# Summary
story.append(Paragraph("SUMMARY", h2))
story.append(Paragraph(
    "Computer Science and Engineering graduate with a solid understanding of programming and software "
    "development fundamentals, and a strong interest in problem-solving and learning new technologies. "
    "Passionate about creating websites and modern web development, especially using AI tools to turn ideas "
    "into practical, creative projects. Eager to experiment, improve technical skills, and take on new "
    "challenges while growing as a developer.",
    body
))

# Education
story.append(Paragraph("EDUCATION", h2))
edu = [
    ("Bachelor of Science in Computer Science and Engineering (CSE)", "Jan 2020 – Sept 2025",
     "Rajshahi University of Engineering &amp; Technology (RUET)", ""),
    ("Higher Secondary Certificate (HSC)", "June 2017 – May 2019",
     "Notre Dame College, Dhaka", "GPA 5.0 · Government Scholarship"),
    ("Secondary School Certificate (SSC)", "Completed 2017",
     "Chattogram Collegiate School", "GPA 5.0 · Government Scholarship"),
]
for title, date, org, extra in edu:
    t = Table([[Paragraph(title, role_line), Paragraph(date, date_line)]], colWidths=[4.5 * inch, 1.75 * inch])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(t)
    story.append(Paragraph(org + (f" &middot; {extra}" if extra else ""), muted))

# Projects
story.append(Paragraph("PROJECTS", h2))
projects = [
    ("Online Food Order System", "PHP, MySQL, CSS",
     "Online food ordering system allowing users to browse menus and place orders.",
     "github.com/sifat-ech/Online-Food-Order-System-Project"),
    ("Online Gym Management System", "PHP, MySQL, CSS",
     "Web interface to manage gym memberships and bookings.",
     "github.com/sifat-ech/Online-Gym-Management-System"),
    ("Hospital Appointment System", "Python, SQLite",
     "Appointment scheduling and patient records management.",
     "github.com/sifat-ech/Hospital-Appointment-System"),
]
for title, tech, desc, link in projects:
    t = Table([[Paragraph(title, role_line), Paragraph(tech, date_line)]], colWidths=[4.5 * inch, 1.75 * inch])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(t)
    story.append(Paragraph(desc, body))
    story.append(Paragraph(link, muted))

# Research
story.append(Paragraph("RESEARCH", h2))
story.append(Paragraph(
    "A Comparative Study of Traditional and Transformer-Based Models for Detecting Cyberbullying "
    "in Bengali Social Media Comments", role_line
))
story.append(Paragraph(
    "Developed a hybrid framework using Naive Bayes, CNN, GRU and BanglaBERT to detect cyberbullying "
    "in Bengali social media comments.", body
))
story.append(Spacer(1, 4))

# Certifications
story.append(Paragraph("CERTIFICATIONS &amp; RECOGNITION", h2))
story.append(Paragraph("&#8226; Python Django Course — EDGE Project (World Bank &amp; Government of Bangladesh Initiative)", bullet))
story.append(Paragraph("&#8226; Recognition for participation in Round One Assessment of IYS2020", bullet))

# Skills
story.append(Paragraph("SKILLS", h2))
skills_rows = [
    ("Programming Languages", "C, C++, Python, Java"),
    ("Web Technologies", "HTML, CSS, PHP, Django"),
    ("Databases", "MySQL, SQLite"),
    ("Machine Learning / AI", "Classical ML, Transformer-based models (BanglaBERT), CNN, GRU"),
    ("Languages", "Bengali, English"),
]
for label, val in skills_rows:
    story.append(Paragraph(f"<b>{label}:</b> {val}", body))

doc.build(story)
print("Resume PDF generated.")
