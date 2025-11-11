---
layout: default
title: Data Modeling
parent: Core Technical Skills
nav_order: 2
last_reviewed: 2025-11-10
reviewer: Rodrigo (BI Lead)
---

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
2. **Design**: Explain the grain of an order fact table that supports order-level, item-level, and return analysis simultaneously.
3. **SCD**: How would you handle changes to a salesperson’s region assignment while preserving historical reporting?
4. **Normalization**: Provide examples of update anomalies that occur when a table is insufficiently normalized.
5. **Performance**: When would you create an aggregate fact table? What are the maintenance implications?
6. **Quality**: Describe how you’d detect and correct a multi-source dimension mismatch (customer master vs CRM).
7. **Behavioral**: Tell me about a time you redesigned a model to solve a reporting bottleneck. What metrics improved?
8. **Advanced**: Compare and contrast Kimball and Data Vault approaches in a modern cloud data platform.

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
- Glossary terms: fact table, dimension table, conformed dimension, grain, data vault (refer to `shared/glossary.md`).
- Related modules:
  - `SQL_for_Data_Analysis/module.md` for querying modeled data.
  - `Data_Warehousing_Fundamentals/module.md` for architectural context.
  - `ETL_ELT_Processes/module.md` for load patterns and transformations.

---

## Further Reading & Resources
- Ralph Kimball & Margy Ross – *The Data Warehouse Toolkit* (dimensional modeling guide).
- Bill Inmon – *Building the Data Warehouse*.
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

_Last updated: 2025-11-10_
