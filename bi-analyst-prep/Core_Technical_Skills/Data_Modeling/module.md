# Data Modeling for BI Analysts – Mastery Module

## Learning Objectives
- Design relational and dimensional models that align with business processes and analytical needs.
- Translate stakeholder requirements into well-structured entities, attributes, and relationships.
- Apply normalization and denormalization techniques judiciously to balance data integrity and performance.
- Construct and manage slowly changing dimensions (SCDs), snapshots, and history-tracking patterns.
- Evaluate modeling approaches (Inmon, Kimball, Data Vault, wide tables) in modern cloud ecosystems.
- Communicate model decisions effectively to engineers, analysts, and business stakeholders.

## Prerequisites & Audience
- Familiar with SQL querying and basic relational database concepts.
- Exposure to BI tools (Power BI, Tableau) and ETL/ELT pipelines.
- Audience: BI Analysts transitioning from reporting to modeling responsibilities or preparing for technical interviews.

## Role Context & Business Value
Robust data models are the backbone of reliable analytics. BI Analysts anchor conversations around which metrics exist, how they’re calculated, and what data quality safeguards are in place. Interviewers expect you to:
- Interpret ambiguous requirements and map them to logical/physical structures.
- Collaborate with engineers on data pipeline design and documentation.
- Anticipate how models will scale—both in data volume and stakeholder complexity.
Strong modeling skill improves time-to-insight, reduces rework, and boosts trust in BI outputs.

---

## 1. Foundations & Theory
### 1.1 Conceptual, Logical, and Physical Models
- **Conceptual Model**: high-level entities and relationships; stakeholder-friendly diagrams (e.g., customers, orders, products).
- **Logical Model**: detailed attributes, keys, and cardinality; independent of technology.
- **Physical Model**: platform-specific implementation (table structures, partitions, distributions).
- Emphasize iterative refinement; start conceptual, validate with SMEs, then progress to logical/physical.

### 1.2 Normalization Principles
- Objectives: eliminate redundancy, enforce data integrity.
- Normal forms (1NF through 5NF); practical emphasis on 3NF for OLTP.
- Identify anomalies: update, insert, delete anomalies when normalization is lacking.
- Create entity relationship diagrams (ERDs) to highlight dependencies.

### 1.3 Dimensional Modeling Basics
- Fact tables: transactional, periodic snapshot, accumulating snapshot.
- Dimension tables: slow-changing attributes, hierarchies, degenerate dimensions.
- Star vs snowflake schemas; trade-offs in query performance vs maintenance.
- Grain definition: explicit statement of what a single row in a fact table represents.

### 1.4 Business Process Modeling
- Align facts to business processes (orders, subscriptions, support tickets).
- Capture measures and additive/semi-additive/non-additive metrics.
- Document conformed dimensions for consistent cross-domain reporting.

---

## 2. Patterns, Practices & Modeling Techniques
### 2.1 Fact Table Design
- Define grain, primary key strategy (surrogate keys, composite keys).
- Additive vs semi-additive metrics: e.g., inventory levels require special handling.
- Audit columns: load timestamps, source system identifiers, record lineage.
- Bridge tables for many-to-many relationships (e.g., customer ↔ campaign).

### 2.2 Dimension Table Design
- Surrogate keys, natural keys, business keys; when to use each.
- Attributes and hierarchies (date dimension, geography, product categories).
- Junk dimensions: bundling low-cardinality flags into a single dimension.
- Role-playing dimensions: using the same dimension multiple times within a fact (e.g., order date, ship date).

### 2.3 Slowly Changing Dimensions (SCD)
- **Type 0**: retain original value (no change).
- **Type 1**: overwrite; suited for non-historical attributes (name typos).
- **Type 2**: add new row with effective dates; track history.
- **Type 3**: add separate columns for previous/current values.
- **Hybrid Types**: combine for complex requirements (Type 6: 1+2+3).
- Discuss implementation patterns (effective_start/end, current_flag) and SQL MERGE strategies.

### 2.4 Advanced Patterns
- Data Vault modeling: hubs, links, satellites; when to choose for agility and auditability.
- Wide tables / One Big Table (OBT): benefits for self-service analytics; caution about maintenance overhead.
- Anchor modeling for highly dynamic schemas.
- Modeling semi-structured data (JSON, nested structures) in columnar warehouses.

### 2.5 Metadata & Documentation
- Data dictionaries: table/column descriptions, allowed values, calculation notes.
- Model diagrams (Lucidchart, dbdiagram.io) versioned alongside code.
- Capturing business definitions in glossaries; aligning with data governance efforts.

---

## 3. Quality, Governance & Lifecycle
### 3.1 Data Quality Integration
- Profiling during model design: completeness, uniqueness, range checks.
- Surrogate key generation rules and collision detection.
- Default values vs null handling guidelines.
- Reconciliation with source systems post-load.

### 3.2 Governance Alignment
- Collaborate with data stewards to classify data (sensitive vs public).
- Row-Level Security considerations in dimensional models (RLS filters by dimension attributes).
- Naming conventions, schema segmentation (staging, curated, presentation layers).

### 3.3 Lifecycle & Change Management
- Versioning models (semver for schema changes).
- Backward compatibility strategies (views, compatibility layers).
- Migration playbooks: deploy scripts, rollback plans, communication templates.
- Monitoring model drift: detect when assumptions (grain, relationship cardinality) no longer hold due to business changes.

---

## 4. Performance & Optimization Considerations
### 4.1 Physical Design Choices
- Partitioning strategies (date-based for facts, hash for large dimensions).
- Clustering/ordering keys to accelerate common queries.
- Index patterns for BI workloads (covering indexes, columnstore indexes, sort keys).

### 4.2 Minimizing Load & Query Costs
- Incremental loads vs full refresh; storing change timestamps.
- Summary tables / aggregates: when to model aggregated facts to avoid heavy runtime computation.
- Materialized views and caching strategies in cloud warehouses.

### 4.3 Scalability & Storage
- Handling high-cardinality dimensions (e.g., `customer_id`): surrogate key mapping, lookup optimization.
- Dealing with late-arriving facts (open orders, delayed shipments).
- Purging/archive strategies; aligning with compliance requirements.

### 4.4 Platform Nuances
- **Snowflake**: micro-partition clustering and resource monitors.
- **BigQuery**: partitioned and clustered tables, cost of repeated CROSS JOINs, BQML integration.
- **Synapse/SQL DW**: table distribution styles (hash, round-robin, replicate).
- **Databricks**: Delta Lake schema evolution, Z-Ordering, optimize commands.

---

## 5. Advanced & Edge Case Scenarios
### 5.1 Multi-Source Convergence
- Reconciling disparate source systems: mapping keys, resolving conflicts.
- Consolidating hierarchies (e.g., differing product taxonomies).
- Aligning granularity across streaming vs batch sources.

### 5.2 Real-Time & Near Real-Time Models
- Lambda/Kappa architecture: combining batch models with streaming enhancements.
- Handling late and out-of-order events; watermarking strategies.
- Querying CDC streams and merging into presentation models.

### 5.3 Unstructured & Semi-Structured Data
- Modeling text analytics outputs (sentiment scores) as dimensions/facts.
- Handling nested arrays from APIs; flattening strategies for reporting.

### 5.4 Regulatory & Compliance Variants
- GDPR/CCPA implications: right-to-be-forgotten; strategies for pseudonymization.
- Audit trails: storing change history for regulated industries (finance, healthcare).

---

## Hands-on Labs
### Lab 1 – Dimensional Model from Scratch
1. Interview stakeholders for a subscription analytics use case.
2. Define fact tables (subscription events, billing) and conformed dimensions (customer, plan, date).
3. Produce conceptual, logical, and physical diagrams.
4. Deliverables: ERD, grain statements, data dictionary excerpt.

### Lab 2 – SCD Type 2 Implementation
1. Given a customer dimension with changing attributes, design a Type 2 schema.
2. Write SQL MERGE statements to insert/update history.
3. Validate using sample change events; ensure only current rows flagged.
4. Deliverables: DDL + DML scripts, test cases, sample data.

### Lab 3 – Normalize vs Denormalize Debate
1. Start with a highly denormalized report table.
2. Normalize to 3NF; analyze pros/cons for transactional workloads.
3. Re-denormalize into a star schema for analytics.
4. Deliverables: before/after schemas, performance comparison notes.

### Lab 4 – Performance Optimization
1. Analyze a slow dashboard query against a fact table.
2. Introduce aggregate tables or partitioning; measure improvement.
3. Document trade-offs and governance implications.
4. Deliverables: optimization plan, execution plan screenshots, communication template for stakeholders.

### Lab 5 – Data Vault Pilot
1. Model a small domain using Data Vault (hub/link/satellite).
2. Map to star schema outputs for BI consumption.
3. Discuss when this pattern adds value vs overhead.
4. Deliverables: Data Vault schema, transformation logic to dimensional model, pros/cons summary.

---

## Practice Question Bank
1. **Case**: Marketing wants to segment customers by engagement; outline the data model supporting the initiative, detailing facts, dimensions, and conformed attributes.  
   **Answer:** I’d model a behavioral fact table at the customer-by-period grain capturing interactions (emails opened, sessions, purchases) sourced from multiple systems. Dimensions would include a conformed customer dimension enriched with demographic attributes, a calendar dimension, and campaign and product dimensions. Engagement scores become measures, and conformed dimensions ensure the same customer definition is used across marketing and sales analytics.
2. **Design**: Explain the grain of an order fact table that supports order-level, item-level, and return analysis simultaneously.  
   **Answer:** I set the grain at one row per order line item, enabling item-level metrics while still rolling up to order totals via degenerate order keys. Returns can be modeled either as negative quantities in the same fact with a return indicator or as a related fact linked through the same surrogate keys, giving flexibility to analyze both original sales and reverse logistics.
3. **SCD**: How would you handle changes to a salesperson’s region assignment while preserving historical reporting?  
   **Answer:** A Type 2 SCD dimension fits: each salesperson has surrogate-keyed rows with effective start/end dates and a current flag. When a region changes, I close the old record, insert a new one, and downstream facts join on the surrogate key captured at transaction time. Reports using date filters automatically respect history, while current assignments are available via the current flag.
4. **Normalization**: Provide examples of update anomalies that occur when a table is insufficiently normalized.  
   **Answer:** If customer contact details live in every order row, updating a phone number risks inconsistent values (update anomaly). Inserting a new customer without an order may fail because required order fields are missing (insert anomaly). Deleting the last order could remove the only record of the customer (delete anomaly). Normalization separates these concerns to avoid such pitfalls.
5. **Performance**: When would you create an aggregate fact table? What are the maintenance implications?  
   **Answer:** I build aggregate facts when dashboards repeatedly query the same heavy joins at higher grain (e.g., daily sales by region). Aggregates pre-summarize data, slashing query cost and latency. Maintenance means incremental refreshes aligned with the base fact, validation to ensure aggregates reconcile, and versioning when business definitions shift.
6. **Quality**: Describe how you’d detect and correct a multi-source dimension mismatch (customer master vs CRM).  
   **Answer:** I profile both sources, compare keys and critical attributes, and surface discrepancies in a reconciliation report. For mismatches I create mapping rules or golden records—often via a mastering process that selects the authoritative value per field. Automated data quality tests watch for drift, and any manual overrides are documented so downstream consumers trust the dimension.
7. **Behavioral**: Tell me about a time you redesigned a model to solve a reporting bottleneck. What metrics improved?  
   **Answer:** At a SaaS firm, renewal reporting relied on a tangled view hitting multiple OLTP tables. I introduced a clean star schema with a subscription fact and conformed customer/product dimensions. Query time dropped from minutes to seconds, finance gained confidence in ARR metrics, and stakeholder satisfaction scores jumped because monthly close reports were no longer a fire drill.
8. **Advanced**: Compare and contrast Kimball and Data Vault approaches in a modern cloud data platform.  
   **Answer:** Kimball focuses on business-friendly dimensional models optimized for analytics; it’s quick to deliver but less flexible when sources churn. Data Vault prioritizes agility and auditability with hubs, links, and satellites that capture raw lineage but require downstream marts for usability. In cloud environments I often land raw data via Data Vault for resilience and then publish Kimball-style marts for consumption, leveraging cloud compute to automate both layers.

---

## Interview Story Bank (STAR Prompts)
- **Model Redesign Success**: Situation where legacy tables blocked reporting; describe redesign, stakeholder coordination, and measurable impact.
- **SCD Challenge**: Handling rapidly changing product portfolios; explain your Type 2 solution and rollout.
- **Cross-Team Collaboration**: Partnering with engineering to align on physical model choices; emphasize communication of trade-offs.
- **Quality Incident**: Discovery of inconsistent customer IDs across systems; how you reconciled and prevented recurrence.
- **Scalability Win**: Introduced partitioning or aggregates to handle growth; discuss metrics before/after and lessons learned.

Prepare concise bullet notes for each story, highlighting business outcomes and technical depth.

---

## Glossary & Cross-References
- Update `shared/glossary.md` with:
  - **Fact Table**: Central table storing measurements of business processes at a defined grain.
  - **Dimension Table**: Descriptive attributes used to filter, group, and label facts.
  - **Conformed Dimension**: Dimension shared across multiple fact tables to ensure consistent reporting.
  - **Grain**: The level of detail or granularity represented by a row.
  - **Data Vault**: Modeling methodology using hubs, links, and satellites for agility and auditability.

- Cross-reference modules:
  - `SQL_for_Data_Analysis/module.md` for querying modeled data.
  - `Data_Warehousing_Fundamentals/module.md` for architectural context.
  - `ETL_ELT_Processes/module.md` for load patterns and transformations.

---

## Further Reading & Resources
- Ralph Kimball & Margy Ross – *The Data Warehouse Toolkit* (definitive dimensional modeling guide).
- Bill Inmon – *Building the Data Warehouse* (corporate information factory approach).
- Dan Linstedt – *Building a Scalable Data Warehouse with Data Vault 2.0*.
- Microsoft Learn: Data modeling best practices for Power BI and Synapse.
- Snowflake, BigQuery, and Databricks documentation on modeling patterns.
- dbdiagram.io, draw.io for ERD creation.
- Articles on modern data stack modeling (e.g., dbt best practices blogs).

---

## Learner Practice Checklist
- [ ] Complete the dimensional model outline using `shared/templates/data_modeling/dimensional_model_outline.md` for a domain of your choice.
- [ ] Implement a Type 2 dimension with sample data and validate effective dates.
- [ ] Normalize a denormalized report table, then re-denormalize into a star schema and compare results.
- [ ] Document a modeling decision log capturing assumptions, data quality checks, and stakeholder sign-offs.
- [ ] Present a modeling trade-off (Kimball vs Data Vault vs wide table) to peers and gather feedback.

Use this module as the single comprehensive reference for Data Modeling in the BI Analyst training program. Expand with domain-specific examples (finance, retail, SaaS) as new requirements emerge.
