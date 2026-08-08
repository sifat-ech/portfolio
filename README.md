# Md Safayet Ullah — Portfolio

Live site: **https://sifat-ech.github.io/portfolio/**

A clean, dark, green-accented portfolio for Md Safayet Ullah — CSE graduate, web developer, and AI/ML researcher. Plain HTML/CSS/JS, no build step, no framework, ready to host on GitHub Pages.

## Contents

```
portfolio/
├── index.html          Home / hero
├── about.html           About, education, certifications
├── projects.html        Project cards (GitHub links)
├── research.html        Thesis / research write-up
├── skills.html          Skills & tools
├── resume.html          Web-friendly resume + PDF download button
├── contact.html         Email / GitHub / LinkedIn links (no form)
├── resume/
│   └── Md_Safayet_Ullah_Resume.pdf
├── assets/
│   ├── css/style.css
│   ├── js/main.js
│   └── img/ (favicon, social share image)
├── build.py              Dev convenience script that generated the HTML
│                          (not needed to deploy — the .html files are final)
└── .github/workflows/deploy.yml   Optional GitHub Actions auto-deploy
```

## Run locally

No install needed — it's static HTML. Either:

1. Double-click `index.html` to open it in a browser, or
2. Serve it properly (recommended, avoids relative-path quirks):
   ```bash
   cd portfolio
   python3 -m http.server 8000
   # open http://localhost:8000
   ```

## Deploy to GitHub Pages

See the step-by-step walkthrough in the chat response, or the short version:

1. Create a GitHub repo named `portfolio` under the `sifat-ech` account.
2. Push everything in this folder to the `main` branch.
3. In the repo, go to **Settings → Pages** and set Source to the `main` branch (or let the included GitHub Actions workflow deploy it automatically).
4. The site publishes at `https://sifat-ech.github.io/portfolio/`.

## Updating content

All text lives directly in the `.html` files — edit them and re-push. If you'd rather edit the Python source of truth and regenerate all pages at once, edit `build.py` and run `python3 build.py`.

To replace the resume PDF, drop a new file at `resume/Md_Safayet_Ullah_Resume.pdf` (keep the exact filename, or update the links in `index.html` and `resume.html`).

## Notes

- No contact form is included, per request — the Contact page links directly to email, GitHub, and LinkedIn.
- No phone number appears anywhere on the site.
- Dark/light mode toggle is in the header and remembers the visitor's choice (`localStorage`).
- Content is fully visible without JavaScript (progressive enhancement) — the scroll-reveal animation is a JS-only enhancement layered on top.

## License

MIT — see `LICENSE`.
