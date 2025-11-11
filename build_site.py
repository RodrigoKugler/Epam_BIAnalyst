from __future__ import annotations

from pathlib import Path
from textwrap import dedent

OUTPUT_PATH = Path("dist/index.html")

PILLARS = [
    {
        "name": "Core Technical Skills",
        "summary": "Master the analytics engineering stack end-to-end.",
        "modules": [
            {
                "title": "SQL for Data Analysis",
                "status": "Published",
                "summary": (
                    "Advanced joins, window functions, optimization patterns, and interview labs "
                    "that move from discovery questions to production-ready reporting."
                ),
                "cta": "Practice bank, labs, and STAR prompts",
            },
            {
                "title": "Data Modeling",
                "status": "Published",
                "summary": (
                    "Dimensional, Data Vault, and semantic layer playbooks with governance guardrails "
                    "and patterns for slowly changing dimensions."
                ),
                "cta": "Templates, ERD outlines, roadmap examples",
            },
            {
                "title": "Data Warehousing Fundamentals",
                "status": "Published",
                "summary": (
                    "Architecture tradeoffs, ELT vs ETL decision trees, data quality controls, "
                    "and cost/performance tuning for BI workloads."
                ),
                "cta": "Incremental load labs, cost calculators",
            },
            {
                "title": "ETL & ELT Processes",
                "status": "Published",
                "summary": (
                    "Pipeline design principles, observability, recovery runbooks, and automation strategies "
                    "for analytics engineering teams."
                ),
                "cta": "dbt workflows, CDC scenarios, runbook templates",
            },
            {
                "title": "Visualization & BI Tools",
                "status": "Published",
                "summary": (
                    "Story-first dashboarding across Power BI, Tableau, and Looker with accessibility, "
                    "adoption, and performance benchmarks."
                ),
                "cta": "Accessibility checklist, comparison labs",
            },
            {
                "title": "Cloud Platforms",
                "status": "Published",
                "summary": (
                    "Reference architectures and governance lenses for AWS, Azure, GCP, Databricks, "
                    "and Snowflake in BI programs."
                ),
                "cta": "Selection matrices, architecture blueprints",
            },
        ],
    },
    {
        "name": "Best Practices & Methodologies",
        "summary": "Translate technical wins into business impact.",
        "modules": [
            {
                "title": "Agile Methodologies",
                "status": "Published",
                "summary": (
                    "Scrum, Kanban, and hybrid cadences tailored to analytics teams with sprint playbooks "
                    "and experiment backlogs."
                ),
                "cta": "Simulation labs, retro templates, delivery metrics",
            },
            {
                "title": "Business Analysis",
                "status": "Published",
                "summary": (
                    "Stakeholder discovery, prioritization frameworks, and change management tactics "
                    "built for BI engagements."
                ),
                "cta": "Interview guides, process maps, value cases",
            },
        ],
    },
]

TIMELINE = [
    {
        "title": "Review & Understand",
        "body": (
            "Digest focused briefs that unpack context, anti-patterns, and success signals so you know "
            "how hiring teams evaluate BI work."
        ),
    },
    {
        "title": "Practice & Apply",
        "body": (
            "Work through SQL drills, modeling outlines, pipeline runbooks, and dashboard briefs to prove concepts "
            "under realistic constraints."
        ),
    },
    {
        "title": "Tell the Story",
        "body": (
            "Translate project outcomes into STAR narratives, measurable impact metrics, and stakeholder-ready language."
        ),
    },
    {
        "title": "Share & Iterate",
        "body": (
            "Use review checklists and feedback cadences to tighten your answers, iterate visuals, and level up with peers."
        ),
    },
]

RESOURCES = [
    {
        "label": "Clone Repository",
        "href": "https://github.com/your-org/bi-analyst-training",
        "style": "solid",
    },
    {
        "label": "Download Templates Pack",
        "href": "https://example.com/bi-analyst-templates.zip",
        "style": "ghost",
    },
    {
        "label": "Print Curriculum (PDF)",
        "href": "https://example.com/bi-analyst-curriculum.pdf",
        "style": "ghost",
    },
]


def render_pillars() -> str:
    sections = []
    for pillar in PILLARS:
        cards_html = "\n".join(
            dedent(
                f"""
                <article class="card">
                  <header class="card__header">
                    <h4>{module['title']}</h4>
                    <span class="card__badge">✅ {module['status']}</span>
                  </header>
                  <p class="card__body">{module['summary']}</p>
                  <p class="card__meta">{module['cta']}</p>
                </article>
                """
            ).strip()
            for module in pillar["modules"]
        )

        sections.append(
            dedent(
                f"""
                <section class="pillar">
                  <div class="pillar__heading">
                    <h3>{pillar['name']}</h3>
                    <p>{pillar['summary']}</p>
                  </div>
                  <div class="card-grid">
                    {cards_html}
                  </div>
                </section>
                """
            ).strip()
        )
    return "\n".join(sections)


def render_timeline() -> str:
    return "\n".join(
        dedent(
            f"""
            <article class="timeline__item">
              <div class="timeline__marker" aria-hidden="true"></div>
              <div>
                <h3>{item['title']}</h3>
                <p>{item['body']}</p>
              </div>
            </article>
            """
        ).strip()
        for item in TIMELINE
    )


def render_resources() -> str:
    buttons = "\n".join(
        f'<a class="btn btn--{res["style"]}" href="{res["href"]}" target="_blank" rel="noopener">{res["label"]}</a>'
        for res in RESOURCES
    )
    return buttons


def build_html() -> str:
    curriculum_html = render_pillars()
    timeline_html = render_timeline()
    resource_buttons = render_resources()

    html = f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>BI Analyst Interview Training</title>
    <meta name="description" content="BI analyst interview prep with SQL, modeling, warehousing, pipelines, visualization, cloud, agile, and business analysis content.">
    <style>
      :root {{
        --navy-950: #070f2b;
        --navy-900: #0b1739;
        --navy-700: #1e2f5c;
        --navy-400: #4a5d91;
        --slate-050: #f6f8fb;
        --slate-100: #eef2fb;
        --slate-300: #c7d2ee;
        --teal-400: #1dd3b0;
        --teal-500: #16b79a;
        --teal-600: #118c7a;
        --max-width: 1180px;
        --radius-lg: 22px;
        --radius-md: 16px;
        --transition: 200ms ease;
        color-scheme: light;
      }}

      *, *::before, *::after {{
        box-sizing: border-box;
      }}

      html {{
        scroll-behavior: smooth;
      }}

      body {{
        margin: 0;
        font-family: "Inter", "Segoe UI", system-ui, -apple-system, sans-serif;
        background: var(--slate-050);
        color: var(--navy-900);
        line-height: 1.6;
      }}

      a {{
        color: inherit;
      }}

      a:focus-visible, button:focus-visible {{
        outline: 3px solid var(--teal-400);
        outline-offset: 4px;
      }}

      .skip-link {{
        position: absolute;
        left: 1.5rem;
        top: -40px;
        padding: 0.6rem 1.2rem;
        border-radius: 999px;
        background: var(--navy-900);
        color: white;
        text-decoration: none;
        z-index: 50;
        transition: top var(--transition);
      }}

      .skip-link:focus {{
        top: 1.5rem;
      }}

      header {{
        background: radial-gradient(circle at top left, rgba(29, 211, 176, 0.18), transparent 55%), var(--navy-950);
        color: white;
        padding: clamp(2.6rem, 7vw, 4.5rem) clamp(1.5rem, 6vw, 4rem);
        position: relative;
        overflow: hidden;
      }}

      header::after {{
        content: "";
        position: absolute;
        inset: 0;
        background: linear-gradient(120deg, rgba(255, 255, 255, 0.06), transparent 60%);
      }}

      .hero {{
        position: relative;
        max-width: var(--max-width);
        margin: 0 auto;
        z-index: 1;
      }}

      .hero__eyebrow {{
        text-transform: uppercase;
        letter-spacing: 0.24rem;
        font-size: 0.78rem;
        color: rgba(255, 255, 255, 0.64);
        margin-bottom: 0.85rem;
        font-weight: 600;
      }}

      .hero h1 {{
        margin: 0 0 1.2rem;
        font-size: clamp(2.5rem, 6vw, 3.8rem);
        line-height: 1.08;
        max-width: 780px;
      }}

      .hero__body {{
        max-width: 680px;
        margin-bottom: clamp(1.8rem, 6vw, 2.8rem);
        color: rgba(218, 230, 255, 0.95);
        font-size: clamp(1.05rem, 3vw, 1.2rem);
      }}

      .hero__cta {{
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
      }}

      .btn {{
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 0.45rem;
        font-weight: 600;
        border-radius: 999px;
        padding: 0.85rem 1.8rem;
        text-decoration: none;
        transition: transform var(--transition), box-shadow var(--transition), background var(--transition), color var(--transition);
      }}

      .btn--solid {{
        background: var(--teal-400);
        color: var(--navy-950);
        box-shadow: 0 18px 30px rgba(16, 139, 122, 0.28);
      }}

      .btn--solid:hover {{
        background: var(--teal-500);
        transform: translateY(-3px);
      }}

      .btn--ghost {{
        border: 1px solid rgba(255, 255, 255, 0.55);
        color: white;
        background: rgba(255, 255, 255, 0.12);
      }}

      .btn--ghost:hover {{
        background: rgba(255, 255, 255, 0.2);
        transform: translateY(-3px);
      }}

      .top-nav {{
        position: sticky;
        top: 1rem;
        margin: clamp(-2.2rem, -5vw, -3rem) auto clamp(3rem, 7vw, 4rem);
        max-width: var(--max-width);
        padding: 0.75rem 1rem;
        background: rgba(255, 255, 255, 0.92);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(11, 23, 57, 0.08);
        border-radius: 999px;
        box-shadow: 0 16px 40px rgba(11, 23, 57, 0.1);
        display: flex;
        gap: 1rem;
        justify-content: center;
        flex-wrap: wrap;
        z-index: 10;
      }}

      .top-nav a {{
        text-decoration: none;
        font-weight: 600;
        color: var(--navy-700);
        font-size: 0.95rem;
        position: relative;
        padding: 0.25rem 0.75rem;
        border-radius: 999px;
        transition: color var(--transition), background var(--transition);
      }}

      .top-nav a:hover {{
        color: var(--navy-950);
        background: rgba(29, 211, 176, 0.18);
      }}

      main {{
        padding: 0 clamp(1.5rem, 6vw, 4rem) clamp(4rem, 10vw, 5.5rem);
      }}

      .section {{
        max-width: var(--max-width);
        margin: 0 auto clamp(3.5rem, 8vw, 5.5rem);
        background: white;
        border-radius: var(--radius-lg);
        padding: clamp(2.2rem, 6vw, 3rem);
        box-shadow: 0 24px 60px rgba(11, 23, 57, 0.12);
        border: 1px solid rgba(11, 23, 57, 0.05);
        scroll-margin-top: 7rem;
      }}

      .section__label {{
        text-transform: uppercase;
        letter-spacing: 0.22rem;
        font-size: 0.78rem;
        color: var(--teal-600);
        font-weight: 600;
        margin-bottom: 0.5rem;
      }}

      .section h2 {{
        margin: 0 0 1rem;
        font-size: clamp(2rem, 4vw, 2.45rem);
        color: var(--navy-900);
      }}

      .section__intro {{
        margin: 0 0 clamp(2rem, 5vw, 2.8rem);
        max-width: 760px;
        color: var(--navy-400);
        font-size: 1.05rem;
      }}

      .pillar + .pillar {{
        margin-top: clamp(2.4rem, 6vw, 3.4rem);
      }}

      .pillar__heading {{
        margin-bottom: clamp(1.2rem, 4vw, 1.8rem);
      }}

      .pillar__heading h3 {{
        margin: 0 0 0.35rem;
        font-size: clamp(1.5rem, 3vw, 1.9rem);
        color: var(--navy-950);
      }}

      .pillar__heading p {{
        margin: 0;
        color: var(--navy-400);
      }}

      .card-grid {{
        display: grid;
        gap: clamp(1.25rem, 4vw, 1.75rem);
        grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      }}

      .card {{
        padding: 1.9rem;
        background: linear-gradient(180deg, white 0%, var(--slate-100) 100%);
        border-radius: var(--radius-md);
        border: 1px solid rgba(11, 23, 57, 0.08);
        box-shadow: 0 18px 36px rgba(11, 23, 57, 0.12);
        display: flex;
        flex-direction: column;
        gap: 0.9rem;
        transition: transform var(--transition), box-shadow var(--transition);
      }}

      .card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 26px 50px rgba(11, 23, 57, 0.18);
      }}

      .card__header {{
        display: flex;
        justify-content: space-between;
        gap: 1rem;
        align-items: baseline;
      }}

      .card__header h4 {{
        margin: 0;
        font-size: 1.1rem;
        color: var(--navy-900);
      }}

      .card__badge {{
        background: rgba(29, 211, 176, 0.16);
        color: var(--teal-600);
        font-size: 0.75rem;
        padding: 0.25rem 0.65rem;
        border-radius: 999px;
        font-weight: 600;
        white-space: nowrap;
      }}

      .card__body {{
        margin: 0;
        color: var(--navy-400);
        flex-grow: 1;
      }}

      .card__meta {{
        margin: 0;
        font-size: 0.9rem;
        color: var(--navy-700);
        font-weight: 500;
      }}

      .timeline {{
        display: grid;
        gap: clamp(1.4rem, 4vw, 2rem);
        position: relative;
      }}

      .timeline__item {{
        padding: 1.6rem 1.8rem 1.6rem 3.4rem;
        background: linear-gradient(135deg, white 0%, var(--slate-100) 100%);
        border-radius: var(--radius-md);
        border: 1px solid rgba(11, 23, 57, 0.08);
        position: relative;
        box-shadow: 0 18px 36px rgba(11, 23, 57, 0.12);
      }}

      .timeline__marker {{
        position: absolute;
        left: 1.4rem;
        top: 1.8rem;
        width: 0.85rem;
        height: 0.85rem;
        border-radius: 50%;
        background: var(--teal-400);
        box-shadow: 0 0 0 8px rgba(29, 211, 176, 0.18);
      }}

      .timeline__item::before {{
        content: "";
        position: absolute;
        left: 1.78rem;
        top: 2.55rem;
        bottom: -2rem;
        width: 2px;
        background: linear-gradient(180deg, rgba(11, 23, 57, 0.12), rgba(11, 23, 57, 0));
      }}

      .timeline__item:last-child::before {{
        display: none;
      }}

      .timeline__item h3 {{
        margin: 0 0 0.55rem;
        color: var(--navy-900);
        font-size: 1.2rem;
      }}

      .timeline__item p {{
        margin: 0;
        color: var(--navy-400);
      }}

      .resource-band {{
        background: linear-gradient(135deg, rgba(29, 211, 176, 0.14), rgba(17, 140, 122, 0.14));
        border-radius: var(--radius-lg);
        padding: clamp(1.9rem, 5vw, 2.6rem);
        display: grid;
        gap: 1.2rem;
        border: 1px solid rgba(17, 140, 122, 0.22);
        box-shadow: 0 20px 40px rgba(11, 23, 57, 0.1);
      }}

      .resource-band h3 {{
        margin: 0 0 0.5rem;
        font-size: clamp(1.45rem, 4vw, 1.7rem);
        color: var(--navy-900);
      }}

      .resource-band p {{
        margin: 0;
        color: var(--navy-400);
        max-width: 620px;
      }}

      .resource-actions {{
        display: flex;
        flex-wrap: wrap;
        gap: 0.9rem;
      }}

      footer {{
        padding: clamp(2.4rem, 7vw, 3.2rem) clamp(1.5rem, 6vw, 4rem);
        text-align: center;
        color: rgba(255, 255, 255, 0.72);
        background: var(--navy-950);
        font-size: 0.95rem;
      }}

      footer a {{
        color: var(--teal-400);
        text-decoration: none;
        font-weight: 600;
      }}

      @media (max-width: 720px) {{
        header {{
          padding-bottom: clamp(2.4rem, 9vw, 3rem);
        }}

        .top-nav {{
          position: static;
          margin: clamp(1.5rem, 6vw, 2rem) auto clamp(2.5rem, 7vw, 3.5rem);
        }}

        .section {{
          padding: clamp(1.6rem, 6vw, 2rem);
        }}

        .timeline__item {{
          padding-left: 2.6rem;
        }}

        .timeline__marker {{
          left: 1rem;
        }}

        .timeline__item::before {{
          left: 1.4rem;
        }}
      }}
    </style>
  </head>
  <body>
    <a class="skip-link" href="#main">Skip to main content</a>
    <header>
      <div class="hero">
        <p class="hero__eyebrow">BI Analyst Learning Journey</p>
        <h1>Master the mix of technical depth and stakeholder storytelling BI interviews demand.</h1>
        <p class="hero__body">
          A ready-to-use curriculum covering SQL, modeling, pipelines, warehousing, visualization, cloud strategy, agile delivery, and business analysis—distilled from real hiring loops so your prep time hits what matters.
        </p>
        <div class="hero__cta">
          <a class="btn btn--solid" href="#curriculum">Explore the curriculum</a>
          <a class="btn btn--ghost" href="#resources">Download assets</a>
        </div>
      </div>
    </header>

    <nav class="top-nav" aria-label="Primary">
      <a href="#curriculum">Curriculum</a>
      <a href="#experience">Experience</a>
      <a href="#resources">Next Steps</a>
    </nav>

    <main id="main">
      <section class="section" id="curriculum">
        <p class="section__label">Curriculum Highlights</p>
        <h2>Every pillar a BI interviewer expects, organized for deep work and quick refreshers.</h2>
        <p class="section__intro">
          Each module is already written, peer-reviewed, and packaged with labs, prompts, and templates. Mix and match to create study sprints, team workshops, or onboarding guides without reinventing the wheel.
        </p>
        {curriculum_html}
      </section>

      <section class="section" id="experience">
        <p class="section__label">Learning Experience</p>
        <h2>A loop that keeps your prep balanced between technical credibility and business value.</h2>
        <p class="section__intro">
          Cycle through these four moves to cement skills, produce proof, and translate results into stories that land with hiring managers.
        </p>
        <div class="timeline">
          {timeline_html}
        </div>
      </section>

      <section class="section" id="resources">
        <p class="section__label">Next Steps</p>
        <h2>Clone it, customize it, and share it with your peers or team.</h2>
        <div class="resource-band">
          <div>
            <h3>Ready to tailor the toolkit?</h3>
            <p>
              Bring the modules into your own repo, add your company context, and export to slides, PDFs, or knowledge bases. All supporting assets are ready for remixing so you can focus on the signal, not formatting.
            </p>
          </div>
          <div class="resource-actions">
            {resource_buttons}
          </div>
        </div>
      </section>
    </main>

    <footer>
      Built for BI candidates bridging analytics engineering and stakeholder partnership. Questions? Reach the team at
      <a href="mailto:analytics@example.com">analytics@example.com</a>.
    </footer>
  </body>
</html>
"""
    return html


def write_html(destination: Path = OUTPUT_PATH) -> Path:
    html = build_html()
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(html, encoding="utf-8")
    return destination


def main() -> None:
    output_file = write_html()
    try:
        display_path = output_file.relative_to(Path.cwd())
    except ValueError:
        display_path = output_file.resolve()
    print(f"✅ Wrote {display_path}")


if __name__ == "__main__":
    main()


