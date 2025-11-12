# VI. Sample Interview Questions

## 1. SQL

- **Write a query to find the top 5 products by revenue.**  
  In an analytics-ready schema, revenue usually lives in a fact table (for example, `fact_order_lines`) that captures one row per order line item while product details reside in a dimension such as `dim_product`. Joining on the surrogate key preserves the appropriate grain and avoids double counting. A typical solution looks like this:

```sql
SELECT
    p.product_name,
    SUM(f.quantity * f.unit_price) AS total_revenue
FROM fact_order_lines f
JOIN dim_product p
  ON f.product_key = p.product_key
GROUP BY p.product_name
ORDER BY total_revenue DESC
FETCH FIRST 5 ROWS ONLY;
```

  This pattern highlights a few best practices from the SQL module: calculate measures in the warehouse rather than the BI tool, keep the grain explicit (one row per order line), and lean on warehouse-native syntax (`FETCH FIRST` or `LIMIT`) for clarity.

- **Explain UNION vs UNION ALL.**  
  `UNION` removes duplicates across result sets, which means the engine performs a distinct sort that adds cost but ensures uniqueness. `UNION ALL` simply stacks the rows, preserving duplicates and running faster. In production SQL you pick based on intent: use `UNION` when deduplicating is required (for example, merging curated dimensions from two pipelines) and `UNION ALL` when you’re intentionally combining already distinct sets (like monthly snapshots). The SQL module calls this out under set operators—always match column order and datatypes regardless of which you choose.

## 2. Data Modeling

- **What is the difference between star and snowflake schemas?**  
  A star schema keeps dimensions denormalized so facts link to a single-hop set of descriptive tables. It favors simplicity and fast BI queries at the cost of some redundancy. A snowflake schema normalizes dimension hierarchies into additional tables (for example, `dim_product` → `dim_category` → `dim_department`), which reduces duplication but introduces more joins and maintenance. The Data Modeling module recommends defaulting to star schemas for analytics teams because they align with stakeholder mental models and perform well, reaching for snowflake structures only when governance, extremely high-cardinality attributes, or shared hierarchies make normalization worth the overhead.

- **Explain Slowly Changing Dimensions (SCD) and their types.**  
  SCD techniques capture how descriptive attributes evolve so historical reports stay accurate. The module outlines the common types:

  - Type 0: never update past values (useful for immutable attributes).
  - Type 1: overwrite values—simple, but history is lost; ideal for data corrections.
  - Type 2: create a new row with effective dates and a current flag, preserving history in a Type 2 dimension table.
  - Type 3: add extra columns for previous/current values when you only need limited history.
  - Hybrid types (like Type 6) blend approaches to meet nuanced requirements.

  Implementations typically rely on `MERGE` statements with surrogate keys, `effective_start`/`effective_end` timestamps, and `is_current` flags, all emphasized in the modeling labs.

## 3. Data Warehousing (DWH)

- **Compare Data Warehousing with Data Lakes.**  
  The warehousing module frames warehouses as curated, schema-on-write environments optimized for BI workloads—subject-oriented, integrated, non-volatile, and time-variant. Data lakes store raw, often semi-structured data with schema-on-read flexibility; they shine for exploratory or data science use cases but require strong governance. Modern teams often land raw data in a lake (or lakehouse) and promote curated, conformed datasets into the warehouse layers to power analytics, balancing agility with trust.

- **Explain Kimball vs Inmon modeling approaches.**  
  Kimball advocates building dimensional data marts (facts and conformed dimensions) that plug into a bus architecture—fast to deliver and highly consumable for BI. Inmon’s Corporate Information Factory starts with an enterprise-wide, normalized data warehouse (the integration layer) and publishes marts downstream. The module notes many cloud-native teams blend both, sometimes layering Data Vault for raw history capture, then publishing Kimball-style marts for consumption.

## 4. ETL/ELT

- **Describe the ETL process and its applications.**  
  ETL (Extract → Transform → Load) pulls data from sources, applies business logic outside the warehouse (for example, in an ETL server or Spark job), and loads cleansed results into target tables. It’s valuable when compliance demands data masking before landing in shared storage, when source systems lack compute, or when you deliver tightly controlled curated datasets. The ELT alternative loads raw data first and transforms inside the warehouse—ideal in cloud platforms with elastic compute. Pipelines typically include orchestration (Airflow, Data Factory), change data capture, quality checks, and runbooks so BI analysts trust their datasets.

## 5. Agile

- **What are the main ceremonies in Scrum?**  
  Scrum structures work through four recurring events:

  - Sprint Planning: confirm Definition of Ready, break stories into slices, and set the sprint goal.
  - Daily Scrum: quick alignment on progress, plans, and blockers (including data access or validation status).
  - Sprint Review: showcase increments—dashboards, models, pipelines—and gather feedback.
  - Sprint Retrospective: inspect the process, agree on improvements (for example, tightening data validation gates or clarifying dependencies).

  These ceremonies give BI teams cadence, transparency, and continuous improvement, all highlighted in the Agile module.

- **How does Kanban differ from Scrum?**  
  Kanban visualizes flow on a board with explicit WIP limits, optimizing cycle time for steady streams of ad-hoc or support work. There are no fixed-length sprints; you pull new work once capacity frees up. Scrum time-boxes delivery in sprints, uses velocity for forecasting, and fits project-style efforts like launching a new KPI suite. Many analytics teams run a hybrid (“Scrumban”), sprinting core initiatives while reserving a Kanban swimlane for urgent data requests.

## 6. Business Analysis

- **How would you prioritize requirements in a project?**  
  The Business Analysis module recommends blending qualitative insight with structured frameworks. Start by mapping stakeholders, understanding strategic goals, and cataloging dependencies. Then apply methods like MoSCoW or RICE to score requests on impact, reach, confidence, and effort. Facilitate workshops so sponsors see trade-offs transparently; document decisions in a backlog or roadmap and keep a RAID log for risks. This approach ensures the BI team delivers the highest-value analytics first and sets expectations when resource constraints bite.

- **Explain the lifecycle of a requirement.**  
  Requirements typically move through Discovery → Analysis → Solution Design → Validation → Deployment → Evaluation. In practice: elicit needs via interviews or process mapping, translate them into user stories with acceptance criteria and data specs, trace them to development tasks, run UAT tied to those criteria, and finally measure adoption post-launch. Continuous feedback loops—captured in retrospectives or stakeholder syncs—feed improvements back into the backlog, keeping analytics solutions aligned with evolving business goals.

