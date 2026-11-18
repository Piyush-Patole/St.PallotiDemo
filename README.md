# St. Vincent Pallotti College of Engineering & Technology (SVPCET)
## Modernized Web Portal & Information Architecture Prototype

A modernized, high-performance, mobile-first web portal prototype for **St. Vincent Pallotti College of Engineering & Technology (SVPCET), Nagpur** (Autonomous Institution, NAAC 'A' Grade, NBA Accredited, DTE Code: 4174).

This prototype restructures the legacy architecture into an accessible, institutional design system aligned with the standards of top global engineering universities.

---

## 🚀 Key Improvements Over Legacy Website

| Dimension | Legacy Website (`stvincentngp.edu.in`) | Modernized Prototype |
| :--- | :--- | :--- |
| **Information Architecture** | Chaotic off-canvas drawer with 24 top-level sections and 50+ nested items | Clean **6-Pillar Mega-Menu** (About, Academics, Admissions, Research, Placements, Campus Life) with visual cards |
| **Department Content** | Trapped behind jQuery AJAX `POST` requests (`/programs/get_tab_info`); invisible to search engines | **Crawlable Semantic Tabs & Dedicated Department Portals** (e.g., `department-template.html`) with permalinks |
| **Heading Hierarchy** | Every page hardcoded with `<h1>Menus</h1>` breaking SEO | Proper semantic HTML5 landmarks (`H1` institutional title &rarr; `H2` section &rarr; `H3` sub-elements) |
| **Admissions Experience** | 15 un-responsive horizontal scrolling tables & paper PDF request forms | **Interactive Admissions & Fee Estimator** calculating category-specific fees and eligibility in real time |
| **Exam Cell Portal** | 90+ unstructured PDF links dumped in chronological order | Tabbed, categorized notice board with instant links to regular/backlog timetables, results, and revaluation forms |
| **Performance & Weight** | Over 6.5 MB on homepage (single uncompressed banner was 2.73 MB) | **Under 650 KB total payload**, responsive image sizing, zero render-blocking icon fonts |
| **Accessibility (WCAG 2.1)** | Severe color contrast issues (2.4:1), 20/22 images missing alt text | **WCAG 2.1 AA Compliant (4.5:1+ contrast)**, focus rings, ARIA roles, and `Ctrl+K` instant search |
| **Security & Mixed Content** | Plaintext HTTP links to ERP login and research portals | Enforced HTTPS patterns, secure credential gateways, and sanitized external links |

---

## 📁 Project Structure

```text
StPalloti/
├── index.html                  # Complete Modernized Institutional Homepage
├── department-template.html    # Academic Department Portal (Computer Science & Engg)
├── assets/
│   ├── css/
│   │   └── styles.css          # Design tokens, mega-menu animations, recruiter marquee
│   ├── js/
│   │   └── main.js             # Sticky header, mobile drawer, Ctrl+K search, fee calculator
│   ├── data/
│   │   ├── programs.json       # Structured data for all 13 academic programs & intake
│   │   ├── fees.json           # Fee matrices (Tuition, Development, Category waivers)
│   │   └── notices.json        # Exam notices, campus events, and academic circulars
│   └── img/
│       ├── logo.png            # SVPCET Institutional Crest
│       ├── naac.png            # NAAC Grade 'A' Emblem
│       ├── nba.png             # NBA Tier-I Accreditation Emblem
│       ├── st-vincent.png      # Founder St. Vincent Pallotti
│       ├── campus-hero.jpg     # Main Academic Campus Photography
│       ├── campus-life.jpg     # Student Life & Events
│       └── lab-drone.jpg       # Texcelrators Drone Innovation Lab
├── crawler.py                  # Python script used to crawl and audit the live website
└── README.md                   # Documentation & Deployment Guide
```

---

## 🌐 Hosting on GitHub Pages (Zero-Build Static Hosting)

This prototype has been intentionally engineered with **zero build dependencies** so that it can be hosted directly on GitHub Pages:

1. Initialize git in this directory (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit of modernized SVPCET web prototype"
   ```
2. Push the repository to GitHub:
   ```bash
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   git branch -M main
   git push -u origin main
   ```
3. In GitHub, go to **Settings &rarr; Pages**:
   - Under **Source**, choose `Deploy from a branch`.
   - Branch: `main` / Folder: `/ (root)`.
   - Click **Save**.
4. Your site will be live at `https://<your-username>.github.io/<repo-name>/` within seconds!

---

## 🔌 Decoupled Backend Integration Architecture

Although currently structured as static pages for GitHub Pages compatibility, the data and presentation layers are completely separated. Any modern backend can be plugged in:

### 1. Next.js 15 / Astro Migration
- Convert `assets/data/*.json` into dynamic API routes (`/api/programs`, `/api/fees`, `/api/notices`).
- Turn `index.html` components into React Server Components (RSC) or Astro components.

### 2. Headless CMS (Strapi / Payload / Sanity)
- Replace static JSON files with live GraphQL/REST queries to manage:
  - Department faculty lists and research publications
  - Autonomous examination timetables and revaluation circulars
  - Student event announcements and photo galleries

### 3. Laravel / PHP Backend
- Map `assets/data/` models directly into Eloquent Models (`Program`, `FeeStructure`, `Notice`, `FacultyMember`).
- Render Blade templates with the existing Tailwind CSS and JavaScript architecture.
