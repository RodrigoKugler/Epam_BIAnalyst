---
layout: default
title: "Visualization & BI Tools"
parent: Core Technical Skills
nav_order: 5
last_reviewed: 2025-11-10
reviewer: Rodrigo (BI Lead)
---

# Visualization & BI Tools – Mastery Module

## Learning Objectives
- Translate analytical requirements into compelling, accurate visual narratives.
- Evaluate and leverage major BI platforms (Power BI, Tableau, Looker) for different scenarios.
- Design dashboards and reports with user-centric UX, accessibility, and performance in mind.
- Implement governance: data security, row-level security, certification, and deployment workflows.
- Optimize refresh strategies, data models, and visualizations for scalability.
- Communicate design choices and trade-offs effectively in interviews and stakeholder meetings.

## Prerequisites & Audience
- Familiar with SQL queries and fundamental BI concepts (dimensions, measures).
- Experience building basic dashboards in at least one BI tool.
- Audience: BI Analysts seeking advanced visualization mastery and interview readiness.

## Role Context & Business Value
Visualization is where insights meet decision makers. BI Analysts must balance aesthetics, accuracy, and interpretability. Interviewers look for candidates who can articulate why a visualization works, demonstrate tool fluency, and anticipate stakeholder needs while maintaining governance.

## 1. Foundations & Theory
### 1.1 Principles of Data Storytelling
- Context, narrative arc, and actionable takeaways (context → conflict → conclusion).
- Audience analysis: executives vs operators vs analysts.
- Choosing the right chart type for the question (comparison, trend, distribution, relationship, composition).
- Avoiding clutter: decluttering frameworks (remove, emphasize, annotate).

### 1.2 Cognitive Design Principles
- Pre-attentive attributes (color, position, size) to guide attention.
- Gestalt principles (proximity, similarity, continuity) in layout.
- Color theory: sequential vs diverging palettes, color blindness considerations.
- Dashboard layout: F-pattern, storytelling flow, responsive design.

### 1.3 KPI and Metric Design
- SMART KPIs: specific, measurable, attainable, relevant, time-bound.
- Balancing leading vs lagging indicators.
- Defining metrics clearly (business glossary alignment).
- Benchmarking (targets, thresholds, goal lines).

---

## 2. Tool Deep Dives & Practices
### 2.1 Power BI
- Data model optimization (star schema, aggregations, composite models).
- DAX essentials: calculated columns vs measures, CALCULATE context transitions.
- Power Query transformations, parameterized refresh.
- Row-Level Security (RLS), object-level security, app workspaces.
- Deployment pipelines (dev/test/prod), dataset certification.

### 2.2 Tableau
- Data model relationships vs joins; customizing extracts.
- Calculations (LOD expressions, table calculations, window functions).
- Dashboard actions (filter, highlight, URL) for interactivity.
- Performance: extract tuning, context filters, materialized views.
- Server/Online governance: projects, permissions, data source credentials.

### 2.3 Other Tools & Ecosystems
- Looker (LookML modeling, explores, governance).
- Qlik (associative engine, set analysis).
- Superset/Metabase (lightweight open-source options).
- Embedded analytics scenarios.

### 2.4 Cross-Tool Considerations
- Selection matrix: when to pick Power BI vs Tableau vs Looker.
- Integration with data platforms (Snowflake, BigQuery, Synapse, Databricks).
- Export formats, mobile responsiveness, offline capabilities.

### 2.5 Accessibility & Localization
- WCAG compliance basics (color contrast, text alternatives).
- Localization: currency, date formats, language toggles.
- Inclusive design: simplifying navigation, providing raw data downloads.

---

## 3. Quality, Governance & Lifecycle
### 3.1 Visualization Testing
- Validate data accuracy against source queries.
- Visual QA checklist: filter behavior, dynamic titles, conditional formatting.
- Cross-browser/device testing.

### 3.2 Governance Frameworks
- Content lifecycle: draft, certified, deprecated.
- Documentation: data source lineage, refresh schedule, owner metadata.
- Ticketing for change requests and enhancements.

### 3.3 Security & Compliance
- RLS implementation patterns (Power BI roles, Tableau user filters, Looker access grants).
- Sensitive data handling (masking, hidden fields, aggregated views).

### 3.4 Deployment & Operations
- Refresh scheduling, incremental refresh policies.
- Monitoring dashboards: usage metrics, performance logs.
- Incident response for data or refresh failures.

---

## 4. Performance Optimization
### 4.1 Data Model Tuning
- Aggregate tables, import vs DirectQuery/Live connections in Power BI.
- Tableau extract optimization (custom SQL vs logical layer).
- Storage mode trade-offs (Power BI composite models; Tableau Hyper file size).

### 4.2 Visualization Performance
- Limit high-cardinality visuals; pre-aggregate when necessary.
- Use parameters/slicers instead of cross-filtering large visuals.
- Optimize calculations (DAX/LOD) to avoid unnecessary complexity.

### 4.3 Refresh Efficiency
- Partitioned refresh, incremental policies (Power BI incremental refresh, Tableau incremental extracts).
- Caching strategies and scheduled refresh windows to avoid peak load.

### 4.4 Platform Nuances
- Power BI Premium vs Pro capabilities.
- Tableau Server vs Tableau Online cost and admin differences.
- Looker’s persistent derived tables (PDTs) and caching.

---

## 5. Advanced & Edge Cases
### 5.1 Real-Time Dashboards
- Streaming datasets (Power BI push datasets, Tableau Hyper API, Web Data Connectors).
- Handling high-frequency updates; throttling visual refresh.
- Alerting systems integrated with dashboards.

### 5.2 Embedded Analytics & Portals
- Embedding Power BI (REST APIs, Azure AD apps).
- Tableau embedded with JavaScript API.
- Licensing, security, and customization considerations.

### 5.3 Self-Service Enablement
- Curated data sources, certified datasets, semantic layers.
- Training materials and office hours frameworks.
- Governance guardrails: limits on custom SQL, usage monitoring.

### 5.4 A/B Testing & Experimentation Visuals
- Designing experiment dashboards (control vs variant, statistical significance indicators).
- Automating variance calculations and confidence intervals.

---

## Hands-on Labs
### Lab 1 – Executive KPI Dashboard
1. Gather requirements for an executive sales dashboard.
2. Design wireframes (e.g., Figma, PowerPoint) with layout and narrative flow.
3. Build the dashboard in Power BI or Tableau, incorporating dynamic commentary.
4. Deliverables: requirements doc, wireframe, final dashboard, executive briefing notes.

### Lab 2 – Power BI RLS Implementation
1. Create a dataset with regional sales data.
2. Define RLS roles for region managers and execs.
3. Test access using “View as role”; document security matrix.
4. Deliverables: PBIX/TWBX file, RLS documentation, test results.

### Lab 3 – Tableau Performance Tune-Up
1. Start with a slow workbook (sample provided).
2. Diagnose performance using Performance Recorder.
3. Optimize extracts, reduce heavy calculations, adjust filters.
4. Deliverables: before/after performance metrics, optimization checklist.

### Lab 4 – Cross-Tool Comparison
1. Build the same dashboard in Power BI and Tableau.
2. Document differences in workflow, features, and limitations.
3. Recommend tool choice for hypothetical organization scenarios.
4. Deliverables: comparison matrix, recorded walkthrough.

### Lab 5 – Accessibility Audit
1. Evaluate an existing dashboard against WCAG guidelines.
2. Implement improvements (color palette adjustments, alt text, keyboard navigation).
3. Provide inclusive design recommendations.
4. Deliverables: audit report, updated dashboard, accessibility checklist.

---

## Practice Question Bank
1. **Case**: Sales asks for a dashboard showing global performance. Outline discovery questions, design approach, and tool choice rationale.
2. **Design**: When would you choose a bullet chart over a gauge? Provide business scenarios.
3. **Governance**: How do you manage certified vs ad-hoc dashboards in Power BI or Tableau?
4. **Performance**: A dashboard takes 30 seconds to load. How do you diagnose and fix it?
5. **Behavioral**: Describe a time you balanced stakeholder design requests with best practices.
6. **Security**: Explain how you implemented row-level security for a sensitive dataset and validated compliance.
7. **Advanced**: Compare building semantic models in Power BI vs LookML in Looker.
8. **Troubleshooting**: Filters behave unexpectedly after a recent change. Walk through your debugging process.

---

## Interview Story Bank (STAR Prompts)
- **High-Impact Dashboard**: Delivered an executive dashboard driving key decisions (metric impact, adoption).
- **Design Conflict**: Negotiated with stakeholders to maintain clarity over flashy visuals; outcome.
- **Performance Rescue**: Improved dashboard responsiveness significantly.
- **Governance Initiative**: Implemented certification, RLS, or documentation practices.
- **Self-Service Enablement**: Empowered business users with templates and training while maintaining control.

Prepare bullet-point narratives with metrics (time saved, adoption rates, error reduction).

---

## Glossary & Cross-References
- Glossary terms: pre-attentive attributes, row-level security, semantic model, LOD expression, DAX (`shared/glossary.md`).
- Related modules:
  - `SQL_for_Data_Analysis/module.md` for upstream data proficiency.
  - `Data_Modeling/module.md` for star schema design underlying visuals.
  - `ETL_ELT_Processes/module.md` for data refresh pipelines.

---

## Further Reading & Resources
- Cole Nussbaumer Knaflic – *Storytelling with Data*.
- Power BI documentation on best practices, DAX, RLS.
- Tableau Blueprint and Performance Tuning guides.
- Looker Developer documentation (LookML).
- Web Content Accessibility Guidelines (WCAG 2.1).
- Articles by the Information Lab, SQLBI, and Microsoft MVPs on advanced visualization techniques.

---

## Learner Practice Checklist
- [ ] Draft a dashboard brief using the provided template and gather stakeholder sign-off before building.
- [ ] Build an executive KPI dashboard in Power BI or Tableau, incorporating dynamic commentary and RLS.
- [ ] Run a performance tune-up on an existing workbook/report and document before/after metrics.
- [ ] Complete an accessibility audit and implement improvements aligned with WCAG guidelines.
- [ ] Compare two BI tools for the same use case, documenting workflow differences and recommendations.

_Last updated: 2025-11-10_
