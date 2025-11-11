---
layout: default
title: SQL for Data Analysis
parent: Core Technical Skills
nav_order: 1
last_reviewed: 2025-11-10
reviewer: Rodrigo (BI Lead)
---

# SQL for Data Analysis – Mastery Module

## Learning Objectives
- Translate business questions into robust SQL solutions that withstand production scrutiny.
- Demonstrate mastery of relational concepts, query composition, joins, aggregations, and window logic.
- Diagnose and optimize query performance using indexes, execution plans, and refactoring patterns.
- Build quality into every step: profiling data, handling anomalies, validating outputs, and documenting assumptions.
- Articulate complex SQL decisions in interview and stakeholder contexts, including storytelling through metrics.

## Prerequisites & Audience
- Comfortable with spreadsheets and basic data concepts.
- Familiar with at least one RDBMS (SQL Server, PostgreSQL, MySQL, Oracle, BigQuery, Snowflake).
- Target audience: BI Analyst candidates preparing for technical interviews or transitioning from reporting roles.

## Role Context & Business Value
The BI Analyst bridges raw data and actionable insight. SQL is the lingua franca for:
- Consolidating data from multiple operational systems into an analytical view.
- Calculating KPIs that influence strategic decisions (revenue, churn, pipeline health, operational efficiency).
- Performing deep-dive investigations when a dashboard shows anomalies.
- Enabling self-service analytics by preparing trusted, well-modeled datasets.
Interviewers expect you to demonstrate situational awareness (why the metric matters) and technical execution (how to query it efficiently and accurately).

---

## 1. Relational Foundations & Best Practices
### 1.1 Data Modeling Concepts
- **Entities and Relationships**: Identify business entities (customers, orders, products) and their relationships (1:many, many:many). Reinforce referential integrity through primary and foreign keys.
- **Normalization vs Denormalization**: Understand 3NF for operational systems; recognize when denormalization (pre-aggregated tables, wide dimensions) accelerates analytics.
- **Surrogate Keys & Natural Keys**: Choose surrogate keys (integers, UUIDs) to ensure stability. Preserve natural keys for business context.
- **Slowly Changing Dimensions (SCDs)**: Explain SCD Types 1–6 and when to use them; highlight SQL patterns for snapshotting history.

### 1.2 Core SQL Data Types & Constraints
- Numeric, character, temporal, and boolean types; precision implications in financial data.
- Constraints: NOT NULL, UNIQUE, CHECK; discuss how they affect query planning and data quality.
- Collation and case sensitivity considerations across platforms.

### 1.3 Metadata & Catalogs
- Using system tables (`INFORMATION_SCHEMA`, `sys.tables`) to discover schemas.
- Documenting assumptions: column descriptions, valid value ranges, update cadence.

---

## 2. Query Anatomy & Execution Order
### 2.1 Logical Processing Order
1. `FROM` / `JOIN`
2. `WHERE`
3. `GROUP BY`
4. `HAVING`
5. `SELECT`
6. `WINDOW`
7. `ORDER BY`
8. `LIMIT / TOP`
Explain how this order drives null handling, aggregate availability, and alias visibility.

### 2.2 SELECT Clause Best Practices
- Explicit column lists vs `*`.
- Column aliasing for readability and downstream use.
- Using expressions (CASE, COALESCE, NULLIF) to embed business logic.

### 2.3 Filtering Strategies
- Predicate pushdown and sargability (avoid wrapping indexed columns with functions).
- Using `WHERE` vs `HAVING` for aggregated filters.
- Handling nulls explicitly (`IS NULL`, `COALESCE`, default values).

### 2.4 Modular Query Design
- Common Table Expressions (CTEs) for clarity; when to materialize intermediate results with temp tables.
- Reusable subqueries and views; pros/cons of views and materialized views.

---

## 3. Joins, Set Operators, and Data Relationships
### 3.1 Join Types & Use Cases
- INNER JOIN: enforce matching rows; typical for intersection analysis.
- LEFT JOIN: preserve base table; essential for measuring absence (e.g., customers without orders).
- RIGHT / FULL OUTER JOIN: symmetrical cases; note they can often be refactored into LEFT/UNION patterns.
- CROSS JOIN: generating combinations; caution about Cartesian explosion.
- SELF JOIN: hierarchical and sequential analysis (e.g., comparisons to previous records).

### 3.2 Join Implementation Checklist
- Confirm join cardinality and uniqueness; explain how duplication occurs.
- Use join predicates with equality where possible; discuss inequality joins (`BETWEEN`, `>`, `<`).
- Document assumptions for unmatched rows; provide default values or filter them intentionally.

### 3.3 Set Operators
- UNION vs UNION ALL: duplicates removal vs performance trade-offs.
- INTERSECT and EXCEPT/MINUS: when validating dataset overlaps or differences.
- Apply consistent column datatypes and ordering across operands.

### 3.4 Relationship Diagrams
Include a diagram of a common retail schema (placeholder: `shared/templates/retail_schema.png`). Highlight join paths and caution about many-to-many bridging tables.

---

## 4. Aggregations, Window Functions, and Analytical Patterns
### 4.1 Aggregations
- Core functions: SUM, COUNT, AVG, MIN, MAX.
- Conditional aggregates: `SUM(CASE WHEN condition THEN value ELSE 0 END)` for KPIs like active users.
- Grouping extensions: `GROUP BY ROLLUP`, `GROUPING SETS`, `CUBE` for multi-level summaries.

### 4.2 Window Functions
- Ranking: `ROW_NUMBER`, `RANK`, `DENSE_RANK` — compare deduping vs tied ranks.
- Offset functions: `LAG`, `LEAD` for period comparisons.
- Running totals and moving averages: `SUM(value) OVER (PARTITION BY ... ORDER BY ... ROWS BETWEEN ...)`.
- Percentiles: `PERCENT_RANK`, `NTILE`, `APPROX_QUANTILES` (platform-dependent).

### 4.3 Advanced Analytical Patterns
- Cohort analysis: define cohort via `MIN(order_date)` per customer; calculate retention.
- Funnel analysis: sequential step conversion with window functions and self-joins.
- Segmentation: clustering results stored in SQL tables; join cluster labels back to fact data.

### 4.4 Time Intelligence
- Date dimension joins vs on-the-fly calculations.
- Handling fiscal calendars, ISO weeks, timezone conversions (e.g., `AT TIME ZONE`).
- Handling late-arriving facts in daily aggregates.

---

## 5. Data Quality, Validation, and Governance
### 5.1 Profiling & Auditing
- Row counts by day/week to catch ingestion issues.
- Null percentage checks per key column.
- Value distribution analysis (`PERCENTILE_CONT`, histograms) to spot outliers.

### 5.2 Reconciliation Patterns
- Compare staging vs production tables using `EXCEPT`/`MINUS`.
- Temporal comparisons to validate updates (Type 2 dimension audits).
- Snapshot tables for month-end reconciliations.

### 5.3 Error Handling & Guardrails
- Defensive coding (`CASE` for divide-by-zero, `TRY_CAST` for data type conversion).
- Logging anomalies to audit tables.
- Documenting assumptions and validation steps in module notes.

### 5.4 Governance Considerations
- Row-Level Security (row filters) at the SQL layer.
- Data classification (PII, GDPR) and obfuscation techniques.
- Change management: versioned views, migration scripts.

---

## 6. Performance Tuning & Optimization
### 6.1 Index Strategies
- Clustered vs non-clustered indexes; composite index order and selectivity.
- Covering indexes and INCLUDE columns.
- Columnstore indexes for analytics (SQL Server) or clustering keys (Snowflake).

### 6.2 Execution Plan Analysis
- Reading estimated vs actual plans.
- Common anti-patterns: nested loops explosion, hash match spills, key lookups.
- Statistics updates and their impact on cardinality estimates.

### 6.3 Query Refactoring Techniques
- Replacing correlated subqueries with joins or window functions.
- Splitting giant queries into modular steps for caching or parallelization.
- Using temp tables vs CTEs when the optimizer struggles.

### 6.4 Platform-Specific Tuning Notes
- BigQuery partition pruning and clustering.
- Snowflake warehouse sizing and result caching.
- Synapse and Databricks: push predicates to Spark/PolyBase.

---

## 7. Advanced Topics & Edge Cases
### 7.1 Semi-Structured Data
- Querying JSON/XML columns (`JSON_VALUE`, `OPENJSON`, `json_extract`).
- `UNNEST` / `CROSS APPLY` patterns for arrays.

### 7.2 Incremental Loads & CDC
- SQL patterns for Change Data Capture (CDC) and watermarks.
- `MERGE` statements: syntax, conflict resolution, idempotency.

### 7.3 Working with Large Tables
- Partitioned tables, bucketing, sharding.
- Batch windowing (e.g., `TOP (10000)` loops for updates).
- Managing fact tables with billions of rows (distribution, compression).

### 7.4 Security & Access Control
- `GRANT`/`REVOKE` basics, role-based access schemas.
- Masking functions for sensitive columns.

---

## 8. BI Storytelling with SQL
### 8.1 From Query to Insight
- Translate query results into stakeholder narratives: set context, highlight trends, recommend actions.
- Annotate SQL outputs with commentary tables for BI tools.

### 8.2 SQL + Visualization Tool Integration
- Publish SQL outputs to Power BI datasets/Tableau extracts.
- Schedule refreshes; ensure row-level security alignment.

### 8.3 Documentation & Hand-off
- Maintain README per dataset: source tables, transformation logic, owners.
- Hand-off checklists when promoting SQL logic to production pipelines.

---

## Hands-on Labs
### Lab 1 – KPI Pipeline (Sales Growth Dashboard)
1. Build monthly revenue, average order value, and order volume metrics.
2. Use window functions to calculate MoM growth and 3-month rolling averages.
3. Export results to a BI tool; create visuals and annotate insights.
4. Deliverables: SQL script, dashboard screenshots, commentary on drivers of change.

### Lab 2 – Data Quality Triage
1. Profile a customer table: identify duplicate keys, invalid emails, null critical fields.
2. Write SQL to surface anomalies; propose cleansing steps.
3. Document root causes and remediation plan.
4. Deliverables: anomaly report query, summary table, remediation memo.

### Lab 3 – Query Optimization Challenge
1. Start with a slow query involving multiple joins and scalar functions.
2. Measure baseline execution plan and runtime.
3. Apply optimizations: index suggestions, refactoring filters, replacing scalar functions with set-based logic.
4. Show performance improvement metrics and explain trade-offs.

### Lab 4 – Cohort Retention Analysis
1. Define signup cohorts using earliest purchase date.
2. Calculate retention matrix (percentage active each month post-signup).
3. Visualize results; discuss retention drivers and anomalies.
4. Deliverables: SQL script, retention heatmap, executive summary.

### Lab 5 – Interview Simulation
1. Work through a case prompt (e.g., revenue drop) using SQL to investigate.
2. Prepare a brief stakeholder presentation with findings, SQL excerpts, and next steps.
3. Practice a live explanation focusing on clarity of reasoning.

---

## Practice Question Bank
1. **Case Question**: Marketing claims a campaign increased weekly active users. Design SQL to validate the claim, outlining tables, filters, success criteria, and potential pitfalls.
2. **Coding Prompt**: Provide a query that returns the top 3 products per category by revenue for the last 90 days, excluding products with fewer than 10 orders.
3. **Debugging**: A dashboard double-counts revenue after introducing a new join. Diagnose the root cause and rewrite the query.
4. **Optimization**: Explain how you would tune a query that filters on `WHERE YEAR(order_date) = 2025` and scans an entire fact table.
5. **Data Quality**: Write SQL to compare yesterday’s orders table with a snapshot to ensure no deletions occurred.
6. **Behavioral**: Describe a time when a SQL change caused a regression. How did you detect, resolve, and prevent recurrence?
7. **Architecture**: Compare materialized views vs scheduled ETL tables for powering BI dashboards. When is each appropriate?

---

## Interview Story Bank (STAR Prompts)
- **Scenario 1 – Performance Rescue**: Share a project where you reduced query runtime drastically. Highlight situation, actions (indexing, refactoring), and impact (report refresh time cut by X%).
- **Scenario 2 – Data Integrity Fire Drill**: Discuss a time you discovered faulty metrics before an executive meeting, detailing investigation SQL, cross-team communication, and the fix.
- **Scenario 3 – Stakeholder Alignment**: Explain a case where ambiguous requirements led to rework; describe how you used SQL prototypes to clarify expectations.
- **Scenario 4 – Innovation**: Outline how you introduced window functions or CTE-based refactors to replace legacy stored procedures, improving maintainability.

Prepare concise bullet points for each story; rehearse narratives emphasizing business outcomes.

---

## Glossary & Cross-References
- Glossary terms: sargable predicate, window function, execution plan, cohort analysis (see `shared/glossary.md`).
- Related modules:
  - `Data_Modeling/module.md` for dimensional modeling refresh.
  - `ETL_ELT_Processes/module.md` for sourcing best practices.
  - `Visualization_and_Tools/module.md` for publishing outputs.

---

## Further Reading & Resources
- `sqlstyle.guide` – comprehensive SQL style conventions.
- Mode Analytics SQL tutorials – advanced window function walkthroughs.
- PostgreSQL docs: Window Functions chapter (applies broadly across RDBMS).
- Microsoft Learn: SQL Server performance tuning guide.
- Snowflake/Spark/BigQuery official optimization docs for platform nuances.
- “High Performance MySQL” (Baron Schwartz) – optimization deep dive.
- Stack Overflow Developer Survey – stay current with prevalent SQL features.

---

## Practice Checklist for Learners
- [ ] Rebuild the sample KPIs using the dataset in `shared/templates/sql/sample_sales_orders.csv`.
- [ ] Write your own window function exercises and validate results with LAG/LEAD.
- [ ] Document SQL quality checks (null handling, reconciliation) for a recent project.
- [ ] Prepare STAR stories using the prompts above; rehearse aloud.
- [ ] Share learnings with your team and identify one optimization opportunity in existing reports.

_Last updated: 2025-11-10_
