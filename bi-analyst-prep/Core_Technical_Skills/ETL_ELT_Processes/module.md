# ETL & ELT Processes – Mastery Module

## Learning Objectives
- Differentiate ETL and ELT architectures and choose the right approach for BI use cases.
- Design resilient extraction, transformation, and load pipelines that maintain data fidelity and governance.
- Implement incremental loads, CDC, and automation patterns across modern cloud platforms.
- Diagnose and remediate pipeline failures using observability, validation, and documentation best practices.
- Communicate pipeline design decisions clearly to stakeholders and in interview scenarios.

## Prerequisites & Audience
- Intermediate SQL skills and familiarity with data warehousing concepts.
- Exposure to scripting or orchestration tools (dbt, Airflow, Azure Data Factory, Informatica, etc.).
- Audience: BI Analysts, analytics engineers, or data engineers preparing for interviews or responsible for data pipeline delivery.

## Role Context & Business Value
Effective pipelines power reliable dashboards and decision-making. BI Analysts frequently collaborate with engineers or own ELT transformations in tools like dbt or SQL-based pipelines. Interviewers expect you to justify architecture decisions, demonstrate attention to data quality, and describe recovery strategies when pipelines break.

---

## 1. Foundations & Theory
### 1.1 ETL vs ELT
- **ETL (Extract-Transform-Load)**: transform data outside the warehouse (e.g., ETL tool/server) before loading curated results.
- **ELT (Extract-Load-Transform)**: load raw data first, then transform within the warehouse using its compute power.
- Discuss hybrid approaches and when each is appropriate (legacy systems, low latency, compliance).

### 1.2 Pipeline Components
- **Extract**: connectors, APIs, file processing, handling rate limits.
- **Transform**: cleansing, enrichment, normalization, conforming business rules.
- **Load**: append, overwrite, merge, upsert strategies; dependency management.
- Metadata management: capturing lineage, data dictionary, schema changes.

### 1.3 Batch vs Streaming
- Batch: scheduled intervals, typical for nightly updates.
- Streaming: continuous processing using Kafka, Kinesis, Pub/Sub; near-real-time insights.
- Micro-batching: compromise between real-time and batch.

### 1.4 Architecture Layers
- Landing zone (raw files), staging tables, curated layer, presentation marts.
- Orchestration layer coordinating tasks (Airflow DAGs, ADF pipelines, Step Functions).

---

## 2. Patterns, Practices & Techniques
### 2.1 Extraction Patterns
- Full extracts for small datasets; incremental extracts using timestamps, change flags.
- API extraction considerations: pagination, rate limiting, retries, backoff strategies.
- File ingestion: CSV, JSON, Parquet; schema detection and validation.

### 2.2 Transformation Patterns
- SQL-based transformations (dbt, stored procedures) vs code-based (PySpark, Scala, Dataflow).
- Set-based operations vs row-by-row loops.
- Standardization: naming, data types, business rules.
- Auditing columns (created_at, updated_at, source_system, hash keys).

### 2.3 Load Strategies
- Append-only tables vs merge/upsert logic using surrogate keys.
- Slowly Changing Dimensions integration during load (Type 1/2/3).
- Idempotency: ensure rerunning pipelines produces consistent results.
- Handling late arriving data (watermarks, delta detection).

### 2.4 Tooling Landscape
- **Orchestration**: Airflow, Prefect, Dagster, Azure Data Factory, AWS Step Functions.
- **Transformation**: dbt, SQL scripts, Spark/Databricks, Stored Procedures.
- **Extraction**: Fivetran, Stitch, custom scripts, CDC tools (Debezium).
- **Monitoring**: Monte Carlo, Datadog, Prometheus, built-in cloud monitors.

### 2.5 Documentation & Templates
- Pipeline runbooks including context, inputs, outputs, SLAs, escalation contact.
- Data contracts with upstream teams defining schemas and change management.

---

## 3. Quality, Governance & Observability
### 3.1 Data Quality Integration
- Unit tests and assertions (dbt tests, Great Expectations, custom SQL checks).
- Row counts, null/duplicate detection, referential integrity checks post-load.
- Business rule validation (e.g., revenue >= 0, date ranges valid).

### 3.2 Pipeline Monitoring
- Metrics: job duration, success rates, data latency, freshness.
- Alerting: immediate notifications on failures, anomalies.
- Logging: structured logs capturing job parameters, row counts, errors.

### 3.3 Governance & Security
- Credential management (key vaults, secret managers, service principals).
- Least privilege access for pipeline service accounts.
- Compliance with data classification; pipeline-level masking when pulling sensitive data.

### 3.4 Change Management
- Version control for pipeline definitions (Git).
- CI/CD pipelines for transformations (dbt Cloud CI, GitHub Actions, Azure DevOps).
- Blue/green or canary deployments for critical pipelines.

---

## 4. Performance & Optimization
### 4.1 Efficient Extraction
- Parallelizing API calls while respecting limits.
- Using incremental snapshots to avoid full reloads.
- Caching frequently accessed reference data.

### 4.2 Optimized Transformations
- Use warehouse-native features (window functions, partition pruning) to reduce cost.
- Refactor loops into set-based operations and leverage temporary tables where beneficial.
- Deduplicate using hash keys or window functions.

### 4.3 Load Performance
- Bulk load utilities (COPY INTO, LOAD DATA, bq load).
- Batch sizing for merges (chunk large upserts).
- Partitioning target tables to minimize write conflicts.

### 4.4 Platform-Specific Tips
- **Snowflake**: Snowpipe, streams/tasks for incremental processing.
- **BigQuery**: Dataflow/Dataproc integration, partitioned tables, automatic schema evolution.
- **Databricks**: Auto Loader, Delta Lake MERGE, structured streaming.
- **Synapse**: PolyBase for ingestion, pipeline activities, materialized views.

---

## 5. Advanced & Edge Cases
### 5.1 Near Real-Time BI Pipelines
- Combining streaming (Kafka, Kinesis) with ELT to update dashboards within minutes.
- Managing exactly-once processing, deduplication, and late events.

### 5.2 Multi-Source Harmonization
- Align schemas from different systems: data type casting, reference data mapping.
- Business rule reconciliation (e.g., inconsistent status codes across ERPs).

### 5.3 Error Handling Strategies
- Retry policies, dead-letter queues, quarantine tables for problematic records.
- Automated ticket creation/escalation for high-impact failures.

### 5.4 Cost Management
- Autoscaling compute clusters, suspending idle warehouses.
- Optimize job schedules to avoid peak rates.
- Evaluate managed ELT services (Fivetran) vs self-managed workloads.

---

## Hands-on Labs
### Lab 1 – Full ELT Pipeline with dbt
1. Load raw sales data into staging.
2. Build dbt models for cleaned dimensions and facts.
3. Implement tests (unique, not null, accepted values).
4. Deliverables: dbt project structure, run results, documentation snapshot.

### Lab 2 – Incremental Load with MERGE
1. Design incremental ingestion from an orders source using modified timestamp.
2. Implement `MERGE` logic with deduplication and audit columns.
3. Simulate reruns to validate idempotency.
4. Deliverables: SQL scripts, runbook entry, test cases.

### Lab 3 – Pipeline Monitoring Setup
1. Instrument pipeline metrics (success/failure counts, duration).
2. Configure alerts for threshold breaches (e.g., no data in 24 hours).
3. Visualize metrics in a monitoring dashboard.
4. Deliverables: monitoring configuration, screenshot, alert policy document.

### Lab 4 – API Extraction Resilience
1. Build script to extract paginated API data with retry logic.
2. Handle rate limits gracefully; log failed segments for reprocessing.
3. Integrate with orchestration tool (cron/Airflow DAG).
4. Deliverables: code sample, retry/backoff strategy doc, sample logs.

### Lab 5 – Streaming Extension
1. Capture CDC events into staging with Kafka.
2. Merge incremental events into curated warehouse tables.
3. Evaluate latency vs accuracy trade-offs.
4. Deliverables: architecture overview, sample SQL, monitoring plan.

---

## Practice Question Bank
1. **Case**: An executive dashboard is frequently stale. Outline how you’d redesign the pipeline for fresher data while managing cost.
2. **Design**: Compare ETL and ELT for a legacy ERP integration. What factors drive your choice?
3. **Troubleshooting**: A nightly job succeeded but produced fewer rows than expected. How do you investigate?
4. **Performance**: Large `MERGE` operations time out. Describe optimization strategies.
5. **Governance**: How do you enforce data contracts with upstream teams to avoid breaking downstream pipelines?
6. **Behavioral**: Discuss a time when you automated error recovery. What tools and processes did you implement?
7. **Advanced**: Explain how dbt fits into an ELT pipeline. What are its strengths/limitations compared to traditional ETL tools?
8. **Security**: Ensure PII stays protected during extraction and transformation. What controls do you put in place?

---

## Interview Story Bank (STAR Prompts)
- **Pipeline Modernization**: Migrated from manual scripts to an orchestrated ELT stack; highlight reliability gains.
- **Failure Recovery**: Responded to a critical pipeline outage; emphasize communication, root cause, prevention.
- **Data Quality Champion**: Introduced automated tests catching issues before they hit dashboards.
- **Cost Optimization**: Refined scheduling or resource usage to cut warehouse costs significantly.
- **Cross-Team Collaboration**: Worked with engineering to standardize CDC pipelines across products.

Prepare bullet-point narratives with metrics (downtime reduced, refresh frequency improved, errors prevented).

---

## Glossary & Cross-References
- Update `shared/glossary.md` with:
  - **ETL**: Data pipeline pattern extracting from source, transforming externally, loading into target.
  - **ELT**: Pipeline pattern loading raw data first, transforming within the target system.
  - **CDC (Change Data Capture)**: Technique for tracking incremental changes in source systems.
  - **Idempotent Pipeline**: Pipeline that can run multiple times without inconsistent results.
  - **Data Contract**: Agreement defining expected schemas, semantics, and SLAs between data producers and consumers.

- Cross-reference modules:
  - `Data_Warehousing_Fundamentals/module.md` for architectural context.
  - `SQL_for_Data_Analysis/module.md` for downstream querying patterns.
  - `Visualization_and_Tools/module.md` for consuming pipeline outputs.

---

## Further Reading & Resources
- *Fundamentals of Data Engineering* (Joe Reis, Matt Housley) – modern pipeline practices.
- dbt Documentation and dbt Labs blog for ELT transformations.
- Google Cloud, AWS, Azure best-practice guides for data pipeline design.
- Netflix Tech Blog, Airbnb Engineering blog – pipeline reliability case studies.
- Great Expectations documentation for data validation.
- OpenLineage project for metadata and lineage tracking.

---

## Learner Practice Checklist
- [ ] Build a dbt project using the provided template and run validation tests end to end.
- [ ] Implement an incremental `MERGE` pipeline against sample data and prove idempotency with reruns.
- [ ] Instrument pipeline metrics, configure alerts, and capture screenshots/logs for documentation.
- [ ] Develop an API extraction script with resiliency features (retry/backoff, logging, alerting).
- [ ] Prototype a streaming extension that merges CDC events with batch data, documenting latency trade-offs.

Use this module as the end-to-end guide for designing, operating, and explaining ETL/ELT pipelines within the BI Analyst training program.
