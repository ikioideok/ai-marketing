# AI & MARKETING

This project is a static website that provides information about AI and marketing.  
It has been reorganised to separate content, styling, scripts and images into
dedicated folders. The goal of this structure is to make the site easier to
understand, update and extend.

## Directory structure

```
ai_marketing/
├── index.html                 # Top‑level landing page
├── assets/                    # Static assets used across the site
│   ├── css/                   # Shared style sheets
│   │   ├── article‑style.css
│   │   ├── common.css
│   │   └── style.css
│   ├── images/                # Images used by the site
│   │   └── haikei.png
│   └── js/
│       └── script.js          # Site‑wide JavaScript
├── pages/                     # All second‑level pages live here
│   ├── about.html             # Company information page
│   ├── contact.html           # Contact form
│   ├── privacy‑policy.html    # Privacy policy
│   ├── guides/                # Guides and long‑form articles
│   │   ├── ai‑marketing‑intro.html
│   │   ├── dx‑guide.html
│   │   └── glossary.html
│   └── categories/            # Category landing pages and articles
│       ├── advertising‑customer‑acquisition/
│       │   └── index.html
│       ├── ai‑dx‑strategy/
│       │   ├── ai_marketing_case_studies.html
│       │   ├── ai_marketing_strategy.html
│       │   └── index.html
│       ├── data‑analysis‑improvement/
│       │   └── index.html
│       ├── generative‑ai‑tools/
│       │   └── index.html
│       └── marketing/
│           ├── content_marketing_guide.html
│           └── index.html
├── scripts/                   # Helper scripts
│   └── generate_new_articles.py
└── .gitignore                 # Ignore rules for git

```

## How to use

To view the site locally, open `index.html` in a web browser. All pages and
assets are referenced with relative paths so the site will work when served
directly from the file system or from a simple static file server.

### Updating the “NEW ARTICLES” section

The `scripts/generate_new_articles.py` script can regenerate the contents of
the “NEW ARTICLES” section on the landing page based on existing article
files. It now determines the project root dynamically and does not rely on
hard‑coded absolute paths. Run the script from within the `scripts` folder or
set the `PROJECT_ROOT` environment variable if you need to override the
location of your project.

```
cd scripts
python3 generate_new_articles.py
```

## Contributing

Feel free to open issues or pull requests with suggestions for improvements or
new articles. When adding new content, place HTML files under the appropriate
directory (for example, `pages/guides/` or a category under
`pages/categories/`) and ensure that image and script references use the
`assets` folder.