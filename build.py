#!/usr/bin/env python3
"""Generates the static HTML pages for the portfolio from shared partials.
Run: python3 build.py
This is a dev convenience script only — GitHub Pages serves the generated
.html files directly, no build step is required at deploy time.
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

ICONS = {
    "github": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 2C6.48 2 2 6.58 2 12.25c0 4.53 2.87 8.37 6.84 9.73.5.1.68-.22.68-.49v-1.91c-2.78.62-3.37-1.19-3.37-1.19-.46-1.2-1.11-1.52-1.11-1.52-.9-.63.07-.62.07-.62 1 .07 1.53 1.05 1.53 1.05.9 1.57 2.34 1.12 2.91.86.09-.66.35-1.12.63-1.38-2.22-.26-4.56-1.14-4.56-5.05 0-1.12.39-2.03 1.03-2.74-.1-.26-.45-1.32.1-2.75 0 0 .84-.28 2.75 1.05a9.3 9.3 0 0 1 5 0c1.91-1.33 2.75-1.05 2.75-1.05.55 1.43.2 2.49.1 2.75.64.71 1.03 1.62 1.03 2.74 0 3.92-2.34 4.78-4.57 5.04.36.32.68.94.68 1.9v2.82c0 .27.18.6.69.49A10.26 10.26 0 0 0 22 12.25C22 6.58 17.52 2 12 2Z"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="3" width="18" height="18" rx="3"/><path d="M7.5 10v7M7.5 7.2v.1M11.5 17v-4c0-1.5 1-2.5 2.5-2.5s2.5 1 2.5 2.5v4"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m4 7 8 6 8-6"/></svg>',
    "sun": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="12" cy="12" r="4"/><path d="M12 2v2.4M12 19.6V22M4.9 4.9l1.7 1.7M17.4 17.4l1.7 1.7M2 12h2.4M19.6 12H22M4.9 19.1l1.7-1.7M17.4 6.6l1.7-1.7"/></svg>',
    "moon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M20 14.5A8.5 8.5 0 1 1 9.5 4a6.8 6.8 0 0 0 10.5 10.5Z"/></svg>',
    "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 6h16M4 12h16M4 18h16"/></svg>',
    "user": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="12" cy="8" r="4"/><path d="M4 20c1.8-4 5-6 8-6s6.2 2 8 6"/></svg>',
    "code": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="m8 6-5 6 5 6M16 6l5 6-5 6M13 4l-2 16"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
}

NAV_ITEMS = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("projects.html", "Projects"),
    ("research.html", "Research"),
    ("skills.html", "Skills"),
    ("resume.html", "Resume"),
    ("contact.html", "Contact"),
]

def nav_links_html():
    items = []
    for href, label in NAV_ITEMS:
        items.append(f'<a href="{href}">{label}</a>')
    return "\n        ".join(items)

def header_html(active=""):
    return f"""  <header class="site-header">
    <div class="container nav">
      <a href="index.html" class="brand" aria-label="Md Safayet Ullah — Home">
        <span class="brand-mark">MS</span>
        <span class="brand-name">Md Safayet Ullah</span>
      </a>
      <nav class="nav-links" aria-label="Primary">
        {nav_links_html()}
      </nav>
      <div class="nav-right">
        <button class="theme-toggle" type="button" aria-pressed="false" aria-label="Toggle dark and light mode">
          {ICONS['moon']}
        </button>
        <button class="nav-toggle" type="button" aria-expanded="false" aria-label="Toggle menu">
          {ICONS['menu']}
        </button>
      </div>
    </div>
  </header>
"""

FOOTER = f"""  <footer class="site-footer">
    <div class="container footer-grid">
      <div>
        <p class="footer-brand">Md Safayet Ullah</p>
        <p class="footer-sub">Computer Science &amp; Engineering Graduate &middot; Web Development &middot; AI-Powered Projects</p>
        <p class="footer-sub small-note">Resume available for download. No phone number is listed on this site. &copy; <span id="year"></span></p>
      </div>
      <div class="footer-social">
        <a class="icon-btn" href="https://github.com/sifat-ech" target="_blank" rel="noopener noreferrer" aria-label="GitHub profile">{ICONS['github']}</a>
        <a class="icon-btn" href="https://linkedin.com/in/safayet117" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn profile">{ICONS['linkedin']}</a>
        <a class="icon-btn" href="mailto:safayetsifat117@gmail.com" aria-label="Send email">{ICONS['mail']}</a>
      </div>
    </div>
  </footer>
"""

def page(title, description, body, extra_head="", canonical=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#0B0F0D">
<link rel="canonical" href="{canonical}">

<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="assets/img/og-image.svg">
<meta name="twitter:card" content="summary_large_image">

<link rel="icon" type="image/svg+xml" href="assets/img/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
<script>document.documentElement.classList.add('js');</script>
{extra_head}</head>
<body>
<a class="visually-hidden" href="#main" style="position:absolute;left:-9999px;top:0;">Skip to content</a>
{header_html()}
<main id="main">
{body}
</main>
{FOOTER}
<script src="assets/js/main.js"></script>
</body>
</html>
"""

# ---------------------------------------------------------------------------
# PAGE CONTENT
# ---------------------------------------------------------------------------

JSONLD = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Md Safayet Ullah",
  "url": "https://sifat-ech.github.io/portfolio/",
  "email": "mailto:safayetsifat117@gmail.com",
  "jobTitle": "Web Developer",
  "alumniOf": "Rajshahi University of Engineering & Technology (RUET)",
  "sameAs": [
    "https://github.com/sifat-ech",
    "https://linkedin.com/in/safayet117"
  ]
}
</script>
"""

# ---------- HOME ----------
home_body = f"""
  <section class="hero container">
    <div class="hero-grid">
      <div>
        <p class="eyebrow hero-kicker reveal">Web Developer &middot; AI &amp; Web Projects</p>
        <h1 class="reveal">Hi — I'm Md Safayet Ullah.<br>I build websites and experiment with <span class="accent">AI-powered projects.</span></h1>
        <p class="hero-sub reveal">Computer Science &amp; Engineering graduate focused on web development and practical AI applications. Explore my projects and research.</p>
        <div class="hero-cta reveal">
          <a class="btn btn-primary" href="projects.html">View Projects</a>
          <a class="btn btn-outline" href="resume/Md_Safayet_Ullah_Resume.pdf" target="_blank" rel="noopener">Download Resume</a>
        </div>
        <div class="hero-social reveal">
          <a class="icon-btn" href="https://github.com/sifat-ech" target="_blank" rel="noopener noreferrer" aria-label="GitHub">{ICONS['github']}</a>
          <a class="icon-btn" href="https://linkedin.com/in/safayet117" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">{ICONS['linkedin']}</a>
          <a class="icon-btn" href="mailto:safayetsifat117@gmail.com" aria-label="Email">{ICONS['mail']}</a>
        </div>
      </div>
      <div class="hero-portrait reveal">
        <div class="portrait-ring">
          <div class="portrait-avatar">{ICONS['user']}</div>
        </div>
        <span class="portrait-tag">Based in <b>Chattogram, BD</b></span>
      </div>
    </div>
  </section>

  <section class="section section-tight">
    <div class="container">
      <div class="section-head reveal">
        <p class="eyebrow">Snapshot</p>
        <h2>A quick look at what I do</h2>
      </div>
      <div class="grid-3">
        <div class="card reveal">
          <h3>Full-stack web systems</h3>
          <p>PHP, MySQL and Python-based applications — from food ordering to gym and hospital management platforms.</p>
          <div class="tag-row"><span class="tag">PHP</span><span class="tag">MySQL</span><span class="tag">Python</span></div>
        </div>
        <div class="card reveal">
          <h3>NLP &amp; AI research</h3>
          <p>Comparative study of classical ML and transformer models (BanglaBERT) for Bengali cyberbullying detection.</p>
          <div class="tag-row"><span class="tag accent">NLP</span><span class="tag">Transformers</span><span class="tag">CNN/GRU</span></div>
        </div>
        <div class="card reveal">
          <h3>Always learning</h3>
          <p>Currently exploring modern web development and AI tooling to turn ideas into practical, creative projects.</p>
          <div class="tag-row"><span class="tag">Django</span><span class="tag">C/C++</span><span class="tag">Java</span></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head reveal">
        <p class="eyebrow">Featured</p>
        <h2>Selected work</h2>
      </div>
      <div class="project-card reveal">
        <div class="project-thumb">{ICONS['code']}</div>
        <div class="project-body">
          <h3>Online Food Order System</h3>
          <p>Online food ordering system allowing users to browse menus and place orders.</p>
          <div class="tag-row" style="margin-bottom:14px;"><span class="tag">PHP</span><span class="tag">MySQL</span><span class="tag">CSS</span></div>
          <div class="project-actions">
            <a class="btn btn-sm btn-outline" href="https://github.com/sifat-ech/Online-Food-Order-System-Project" target="_blank" rel="noopener noreferrer">View on GitHub</a>
            <a class="btn btn-sm btn-primary" href="projects.html">All projects</a>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

# ---------- ABOUT ----------
about_body = f"""
  <section class="page-hero container reveal">
    <p class="eyebrow">About</p>
    <h1>Building for the web, learning in public.</h1>
    <p class="lead">Computer Science and Engineering graduate with a solid understanding of programming and software development fundamentals, and a strong interest in problem-solving and learning new technologies.</p>
  </section>

  <section class="section section-tight">
    <div class="container research-block">
      <div class="reveal">
        <p>Computer Science and Engineering graduate with a solid understanding of programming and software development fundamentals, and a strong interest in problem-solving and learning new technologies.</p>
        <p>Passionate about creating websites and modern web development, especially using AI tools to turn ideas into practical, creative projects.</p>
        <p>Eager to experiment, improve technical skills, and take on new challenges while growing as a developer — from full-stack web systems to research combining classical machine learning with transformer-based models.</p>

        <h2 style="margin-top:44px; font-size:1.3rem;">Education</h2>
        <div class="timeline" style="margin-top:22px;">
          <div class="timeline-item">
            <span class="timeline-date">Jan 2020 &ndash; Sept 2025</span>
            <h3>Bachelor of Science in Computer Science and Engineering (CSE)</h3>
            <p class="org">Rajshahi University of Engineering &amp; Technology (RUET)</p>
          </div>
          <div class="timeline-item">
            <span class="timeline-date">June 2017 &ndash; May 2019</span>
            <h3>Higher Secondary Certificate (HSC)</h3>
            <p class="org">Notre Dame College, Dhaka</p>
            <div class="tag-row"><span class="tag accent">GPA 5.0</span><span class="tag accent">Government Scholarship</span></div>
          </div>
          <div class="timeline-item">
            <span class="timeline-date">Completed 2017</span>
            <h3>Secondary School Certificate (SSC)</h3>
            <p class="org">Chattogram Collegiate School</p>
            <div class="tag-row"><span class="tag accent">GPA 5.0</span><span class="tag accent">Government Scholarship</span></div>
          </div>
        </div>
      </div>

      <aside class="reveal">
        <div class="side-card">
          <h3>Certifications &amp; recognition</h3>
          <ul class="side-list">
            <li><b>Python Django Course</b>EDGE Project (World Bank &amp; Government of Bangladesh Initiative)</li>
            <li><b>Round One Assessment</b>Recognition for participation in IYS2020</li>
          </ul>
        </div>
        <div class="side-card">
          <h3>Languages &amp; hobbies</h3>
          <p style="font-size:13.5px; margin-bottom:12px;">Bengali, English</p>
          <div class="tag-row">
            <span class="tag">Watching documentaries</span>
            <span class="tag">Exploring emerging tech trends</span>
          </div>
        </div>
      </aside>
    </div>
  </section>
"""

# ---------- PROJECTS ----------
def project_card(title, desc, tech, link):
    tags = "".join(f'<span class="tag">{t}</span>' for t in tech)
    return f"""      <div class="project-card reveal">
        <div class="project-thumb">{ICONS['code']}</div>
        <div class="project-body">
          <h3>{title}</h3>
          <p>{desc}</p>
          <div class="tag-row" style="margin-bottom:14px;">{tags}</div>
          <div class="project-actions">
            <a class="btn btn-sm btn-outline" href="{link}" target="_blank" rel="noopener noreferrer">View on GitHub</a>
          </div>
        </div>
      </div>
"""

projects_body = f"""
  <section class="page-hero container reveal">
    <p class="eyebrow">Projects</p>
    <h1>Things I've built.</h1>
    <p class="lead">A selection of full-stack web systems built to solve practical, everyday problems.</p>
  </section>

  <section class="section section-tight">
    <div class="container">
{project_card("Online Food Order System", "Online food ordering system allowing users to browse menus and place orders.", ["PHP","MySQL","CSS"], "https://github.com/sifat-ech/Online-Food-Order-System-Project")}
{project_card("Online Gym Management System", "Web interface to manage gym memberships and bookings.", ["PHP","MySQL","CSS"], "https://github.com/sifat-ech/Online-Gym-Management-System")}
{project_card("Hospital Appointment System", "Appointment scheduling and patient records management.", ["Python","SQLite"], "https://github.com/sifat-ech/Hospital-Appointment-System")}
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head reveal">
        <p class="eyebrow">Research</p>
        <h2>Featured research project</h2>
      </div>
      <div class="card reveal" style="max-width:760px;">
        <h3>A Comparative Study of Traditional and Transformer-Based Models for Detecting Cyberbullying in Bengali Social Media Comments</h3>
        <p>Developed a hybrid framework using Naive Bayes, CNN, GRU and BanglaBERT to detect cyberbullying in Bengali social media comments.</p>
        <div class="tag-row" style="margin-bottom:16px;"><span class="tag accent">NLP</span><span class="tag">BanglaBERT</span><span class="tag">CNN</span><span class="tag">GRU</span><span class="tag">Naive Bayes</span></div>
        <a class="btn btn-sm btn-outline" href="research.html">Read more</a>
      </div>
    </div>
  </section>
"""

# ---------- RESEARCH ----------
research_body = f"""
  <section class="page-hero container reveal">
    <p class="eyebrow">Research</p>
    <h1>Detecting cyberbullying in Bengali, responsibly.</h1>
    <p class="lead">A comparative study of traditional and transformer-based models for detecting cyberbullying in Bengali social media comments.</p>
  </section>

  <section class="section section-tight">
    <div class="container research-block">
      <div class="reveal">
        <h2 style="font-size:1.2rem;">Overview</h2>
        <p>Bengali social media platforms have seen a rise in harmful and abusive comments, yet most cyberbullying-detection research focuses on high-resource languages such as English. This project set out to build and compare detection models designed specifically for Bengali text, where informal spelling, code-mixing, and limited labelled data make the task especially difficult.</p>

        <h2 style="font-size:1.2rem; margin-top:32px;">Methods</h2>
        <p>A hybrid framework was developed spanning both classical machine learning and modern transformer-based approaches, allowing a direct comparison of accuracy, generalisation, and computational cost across model families.</p>
        <div class="method-list">
          <span class="tag accent">Naive Bayes</span>
          <span class="tag accent">CNN</span>
          <span class="tag accent">GRU</span>
          <span class="tag accent">BanglaBERT</span>
        </div>

        <h2 style="font-size:1.2rem;">Highlights</h2>
        <ul class="timeline" style="padding-left:0; list-style:none;">
          <li style="padding:10px 0; border-bottom:1px solid var(--border-soft); color:var(--text-muted); font-size:14px;">Compared classical (Naive Bayes) and deep-learning (CNN, GRU) baselines against a transformer-based BanglaBERT model on Bengali comment data.</li>
          <li style="padding:10px 0; border-bottom:1px solid var(--border-soft); color:var(--text-muted); font-size:14px;">Explored preprocessing strategies suited to Bengali's script and informal online writing style.</li>
          <li style="padding:10px 0; color:var(--text-muted); font-size:14px;">Evaluated trade-offs between transformer-based accuracy and the lighter compute footprint of classical/CNN-GRU approaches.</li>
        </ul>
      </div>

      <aside class="reveal">
        <div class="side-card">
          <h3>At a glance</h3>
          <ul class="side-list">
            <li><b>Type</b>Undergraduate thesis</li>
            <li><b>Focus</b>Bengali NLP &middot; Cyberbullying detection</li>
            <li><b>Models</b>Naive Bayes, CNN, GRU, BanglaBERT</li>
          </ul>
        </div>
        <div class="side-card">
          <h3>Links</h3>
          <p style="font-size:13px; margin-bottom:0;">Paper, code, and dataset links will be added here once publicly available. In the meantime, reach out via <a style="color:var(--accent);" href="mailto:safayetsifat117@gmail.com">email</a> for details.</p>
        </div>
      </aside>
    </div>
  </section>
"""

# ---------- SKILLS ----------
def chips(items):
    return "".join(f'<span class="chip">{i}</span>' for i in items)

skills_body = f"""
  <section class="page-hero container reveal">
    <p class="eyebrow">Skills</p>
    <h1>Tools I build with.</h1>
    <p class="lead">A working toolkit spanning full-stack web development, databases, and AI/ML research.</p>
  </section>

  <section class="section section-tight">
    <div class="container">
      <div class="skill-group reveal">
        <h3>Programming languages</h3>
        <div class="skill-chips">{chips(["C","C++","Python","Java"])}</div>
      </div>
      <div class="skill-group reveal">
        <h3>Web technologies</h3>
        <div class="skill-chips">{chips(["HTML","CSS","PHP","Django"])}</div>
      </div>
      <div class="skill-group reveal">
        <h3>Databases</h3>
        <div class="skill-chips">{chips(["MySQL","SQLite"])}</div>
      </div>
      <div class="skill-group reveal">
        <h3>Machine learning / AI</h3>
        <div class="skill-chips">{chips(["Classical ML","Transformer-based models (BanglaBERT)","CNN","GRU"])}</div>
      </div>
      <div class="skill-group reveal">
        <h3>Languages</h3>
        <div class="skill-chips">{chips(["Bengali","English"])}</div>
      </div>
    </div>
  </section>
"""

# ---------- RESUME ----------
resume_body = f"""
  <section class="page-hero container reveal">
    <p class="eyebrow">Resume</p>
    <h1>Resume</h1>
    <p class="lead">A web-friendly summary of my education, projects, and skills — or download the full PDF.</p>
  </section>

  <section class="section section-tight">
    <div class="container">
      <div class="resume-cta reveal">
        <div>
          <h3 style="margin-bottom:4px;">Md Safayet Ullah — Resume</h3>
          <p>PDF &middot; stored in this repository at <code>/resume/Md_Safayet_Ullah_Resume.pdf</code></p>
        </div>
        <a class="btn btn-primary" href="resume/Md_Safayet_Ullah_Resume.pdf" target="_blank" rel="noopener">Download Resume (PDF)</a>
      </div>

      <div class="resume-block reveal">
        <h2>Education</h2>
        <div class="resume-line"><span class="role">Bachelor of Science in Computer Science and Engineering (CSE)</span><span class="date">Jan 2020 &ndash; Sept 2025</span></div>
        <p class="resume-sub">Rajshahi University of Engineering &amp; Technology (RUET)</p>
        <div class="resume-line"><span class="role">Higher Secondary Certificate (HSC)</span><span class="date">June 2017 &ndash; May 2019</span></div>
        <p class="resume-sub">Notre Dame College, Dhaka &middot; GPA 5.0 &middot; Government Scholarship</p>
        <div class="resume-line"><span class="role">Secondary School Certificate (SSC)</span><span class="date">Completed 2017</span></div>
        <p class="resume-sub">Chattogram Collegiate School &middot; GPA 5.0 &middot; Government Scholarship</p>
      </div>

      <div class="resume-block reveal">
        <h2>Projects</h2>
        <div class="resume-line"><span class="role">Online Food Order System</span></div>
        <p class="resume-sub">PHP, MySQL, CSS &middot; github.com/sifat-ech/Online-Food-Order-System-Project</p>
        <div class="resume-line"><span class="role">Online Gym Management System</span></div>
        <p class="resume-sub">PHP, MySQL, CSS &middot; github.com/sifat-ech/Online-Gym-Management-System</p>
        <div class="resume-line"><span class="role">Hospital Appointment System</span></div>
        <p class="resume-sub">Python, SQLite &middot; github.com/sifat-ech/Hospital-Appointment-System</p>
      </div>

      <div class="resume-block reveal">
        <h2>Research</h2>
        <div class="resume-line"><span class="role">A Comparative Study of Traditional and Transformer-Based Models for Detecting Cyberbullying in Bengali Social Media Comments</span></div>
        <p class="resume-sub">Hybrid framework using Naive Bayes, CNN, GRU and BanglaBERT.</p>
      </div>

      <div class="resume-block reveal">
        <h2>Certifications &amp; recognition</h2>
        <div class="resume-line"><span class="role">Python Django Course</span></div>
        <p class="resume-sub">EDGE Project (World Bank &amp; Government of Bangladesh Initiative)</p>
        <div class="resume-line"><span class="role">Round One Assessment, IYS2020</span></div>
        <p class="resume-sub">Recognition for participation</p>
      </div>

      <div class="resume-block reveal">
        <h2>Skills</h2>
        <div class="skill-chips">{chips(["C","C++","Python","Java","HTML","CSS","PHP","Django","MySQL","SQLite","Classical ML","BanglaBERT","CNN","GRU","Bengali","English"])}</div>
      </div>
    </div>
  </section>
"""

# ---------- CONTACT ----------
contact_body = f"""
  <section class="page-hero container reveal">
    <p class="eyebrow">Contact</p>
    <h1>Let's talk.</h1>
    <p class="lead">The fastest way to reach me is by email. You can also find me on GitHub and LinkedIn.</p>
  </section>

  <section class="section section-tight">
    <div class="container">
      <div class="contact-grid">
        <a class="contact-card reveal" href="mailto:safayetsifat117@gmail.com">
          <span class="icon-btn">{ICONS['mail']}</span>
          <h3>Email</h3>
          <p style="margin:0; font-size:13.5px;">safayetsifat117@gmail.com</p>
        </a>
        <a class="contact-card reveal" href="https://github.com/sifat-ech" target="_blank" rel="noopener noreferrer">
          <span class="icon-btn">{ICONS['github']}</span>
          <h3>GitHub</h3>
          <p style="margin:0; font-size:13.5px;">github.com/sifat-ech</p>
        </a>
        <a class="contact-card reveal" href="https://linkedin.com/in/safayet117" target="_blank" rel="noopener noreferrer">
          <span class="icon-btn">{ICONS['linkedin']}</span>
          <h3>LinkedIn</h3>
          <p style="margin:0; font-size:13.5px;">linkedin.com/in/safayet117</p>
        </a>
      </div>
      <p class="contact-note reveal">No phone number is listed on this site. Resume available for download from the <a style="color:var(--accent);" href="resume.html">Resume page</a>.</p>
    </div>
  </section>
"""

PAGES = [
    ("index.html", "Md Safayet Ullah — Web Developer | AI & Web Projects",
     "Portfolio of Md Safayet Ullah — Computer Science & Engineering graduate exploring web development and AI-powered projects. View projects, research, and download resume.",
     home_body, JSONLD, "https://sifat-ech.github.io/portfolio/"),
    ("about.html", "About — Md Safayet Ullah",
     "About Md Safayet Ullah: CSE graduate from RUET, education, certifications, languages and hobbies.",
     about_body, "", "https://sifat-ech.github.io/portfolio/about.html"),
    ("projects.html", "Projects — Md Safayet Ullah",
     "Selected web development projects by Md Safayet Ullah, including a food ordering system, gym management system, and hospital appointment system.",
     projects_body, "", "https://sifat-ech.github.io/portfolio/projects.html"),
    ("research.html", "Research — Md Safayet Ullah",
     "Research by Md Safayet Ullah on detecting cyberbullying in Bengali social media comments using classical ML and transformer-based models.",
     research_body, "", "https://sifat-ech.github.io/portfolio/research.html"),
    ("skills.html", "Skills — Md Safayet Ullah",
     "Technical skills of Md Safayet Ullah: programming languages, web technologies, databases, and machine learning.",
     skills_body, "", "https://sifat-ech.github.io/portfolio/skills.html"),
    ("resume.html", "Resume — Md Safayet Ullah",
     "Web-friendly resume of Md Safayet Ullah with a downloadable PDF version.",
     resume_body, "", "https://sifat-ech.github.io/portfolio/resume.html"),
    ("contact.html", "Contact — Md Safayet Ullah",
     "Contact Md Safayet Ullah via email, GitHub, or LinkedIn.",
     contact_body, "", "https://sifat-ech.github.io/portfolio/contact.html"),
]

def main():
    for filename, title, desc, body, extra_head, canonical in PAGES:
        html = page(title, desc, body, extra_head, canonical)
        with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote", filename)

if __name__ == "__main__":
    main()
