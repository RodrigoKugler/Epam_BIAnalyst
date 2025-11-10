---
layout: default
title: Cloud Platforms
parent: Core Technical Skills
nav_order: 6
last_reviewed: 2025-11-10
reviewer: Rodrigo (BI Lead)
---

# Cloud Platforms for Analytics – Mastery Module

## Learning Objectives
- Compare major cloud analytics platforms (AWS, Azure, GCP, Databricks) and map them to BI workloads.
- Design cloud-native data architectures including storage, compute, orchestration, and security components.
- Optimize cost, performance, and scalability across cloud services.
- Implement governance, monitoring, and deployment pipelines in cloud environments.
- Communicate platform selection trade-offs and integration strategies in interviews and stakeholder discussions.

## Prerequisites & Audience
- Understanding of data warehousing, ETL/ELT pipelines, and BI visualization workflows.
- Familiarity with at least one cloud platform or hosted analytics service.
- Audience: BI Analysts, analytics engineers, and aspiring data architects preparing for platform-centric roles or interviews.

## 1. Foundations & Theory
### 1.1 Cloud Analytics Overview
- Shared responsibility model: cloud provider vs customer responsibilities.
- Benefits: elasticity, managed services, consumption-based pricing.
- Challenges: governance, vendor lock-in, skill alignment.

### 1.2 Core Components
- **Storage**: object storage (S3, ADLS, GCS), managed databases.
- **Compute**: serverless (Lambda, Cloud Functions), containers, managed warehouses (Snowflake, BigQuery, Synapse, Redshift).
- **Networking**: VPCs, private endpoints, firewall rules.
- **Security**: IAM roles, service principals, secrets management.

### 1.3 Platform Landscape
- AWS: Redshift, Glue, Athena, EMR, QuickSight, Lake Formation.
- Azure: Synapse, Data Factory, Databricks, Power BI, Azure SQL DB.
- GCP: BigQuery, Dataflow, Dataproc, Looker, Cloud Composer.
- Databricks: Lakehouse platform, Delta Lake, MLflow integration.
- Snowflake: cross-cloud data warehouse, native governance features.

### 1.4 Architectural Patterns
- Lambda architecture (batch + streaming) vs Kappa (streaming only).
- Lakehouse approach (Delta Lake, Iceberg, Hudi) unifying lake + warehouse.
- Data mesh: domain-oriented architecture leveraging cloud services.

---

## 2. Platform Deep Dives & Practices
### 2.1 AWS Analytics Stack
- Storage: S3 data lake, Glue catalogs, Lake Formation governance.
- Compute: Redshift, EMR (Spark/Hadoop), Athena (serverless SQL).
- Orchestration: AWS Glue workflows, Step Functions, Managed Airflow.
- BI: QuickSight, Tableau/Power BI connectivity.
- Security: IAM roles, KMS encryption, PrivateLink.
- Cost management: Reserved instances, usage monitoring (CloudWatch, Cost Explorer).

### 2.2 Azure Analytics Stack
- Storage: Azure Data Lake Storage Gen2, Blob Storage.
- Compute: Synapse SQL pools, Azure Databricks, Azure SQL Database.
- Orchestration: Data Factory, Synapse pipelines, Logic Apps.
- BI: Power BI integration with Synapse/Databricks; Azure Analysis Services.
- Security: Azure Active Directory, Managed Identities, Private Endpoints.
- Cost management: Azure Monitor, cost alerts, reserved capacity.

### 2.3 Google Cloud Analytics Stack
- Storage: Google Cloud Storage, Bigtable.
- Compute: BigQuery, Dataproc (managed Spark), Dataflow (Apache Beam), Cloud Functions.
- Orchestration: Cloud Composer (Airflow), Workflows.
- BI: Looker, Connected Sheets, Data Studio.
- Security: IAM, VPC Service Controls, CMEK.
- Cost management: BigQuery reservations, budget alerts, slot monitoring.

### 2.4 Databricks Lakehouse
- Unified platform: Delta Lake storage, notebooks, jobs, MLflow.
- Multi-cloud deployment (AWS, Azure, GCP) and integration points.
- Photon engine for SQL, SQL warehouse endpoints.
- Governance: Unity Catalog, table ACLs, column-level security.
- Cost control: Auto-scaling clusters, job clusters vs all-purpose clusters.

### 2.5 Snowflake
- Separation of storage/compute, multi-cluster warehouses.
- Data sharing, data marketplace.
- Streams & tasks for ELT; external tables for data lake access.
- Governance: access control, masking policies, row access policies.
- Cost optimization: warehouse sizing, auto-suspend, resource monitors.

---

## 3. Quality, Governance & Operations
### 3.1 Identity & Access Management
- Role-based access (RBAC) across clouds; least privilege principles.
- Service accounts/service principals for pipelines.
- Multi-account/tenant strategies (prod vs dev, domain separation).

### 3.2 Data Governance
- Catalogs: AWS Glue, Azure Purview, GCP Data Catalog, Unity Catalog.
- Data classification and tagging for compliance (GDPR, HIPAA).
- Auditing: cloud-native logging (CloudTrail, Azure Monitor, Cloud Audit Logs).

### 3.3 Monitoring & Observability
- Metrics: job success rates, latency, throughput, cost.
- Tools: CloudWatch, Azure Monitor, Stackdriver, Datadog.
- Logging pipelines; central log storage (Cloud Logging, Log Analytics).

### 3.4 Deployment & Change Management
- Infrastructure as Code (Terraform, CloudFormation, ARM templates).
- CI/CD for data pipelines (GitHub Actions, Azure DevOps, Cloud Build).
- Environment promotion strategies (dev/test/prod projects or resource groups).

---

## 4. Performance & Cost Optimization
### 4.1 Storage Optimization
- Lifecycle policies (S3 Glacier, Azure Archive tier) for cold data.
- Compression formats (Parquet, ORC).
- Partitioning schemes to improve query pruning.

### 4.2 Compute Efficiency
- Right-sizing compute (warehouse size, cluster node types).
- Autoscaling vs manual scaling policies.
- Serverless options vs dedicated capacity (BigQuery on-demand vs reservations).

### 4.3 Query Optimization
- BigQuery slot tuning, materialized views, BI Engine.
- Redshift sort keys/dist keys, concurrency scaling.
- Synapse distribution strategies (hash, round robin, replicate).
- Databricks Delta OPTIMIZE/ZORDER.
- Snowflake clustering, result caching, query profiling.

### 4.4 Cost Governance
- Tagging resources for showback/chargeback.
- Budget alerts, anomaly detection.
- Choosing reserved capacity vs pay-as-you-go.

---

## 5. Advanced & Edge Cases
### 5.1 Multi-Cloud & Hybrid Strategies
- Data replication across clouds (Databricks, Snowflake cross-cloud features).
- Hybrid architectures (on-prem + cloud) using connectors (DirectQuery, VPN, ExpressRoute).
- Vendor lock-in mitigation, portability (open table formats, containerization).

### 5.2 Real-Time & Event-Driven Analytics
- Kinesis/Kafka + Lambda, Azure Event Hubs + Stream Analytics, GCP Pub/Sub + Dataflow.
- Data streaming into warehouses (BigQuery streaming inserts, Snowpipe).

### 5.3 Machine Learning Integration
- Feature stores (SageMaker Feature Store, Vertex AI Feature Store, Databricks Feature Store).
- Model serving integration with BI (batch scoring, real-time predictions in dashboards).

### 5.4 Compliance & Sovereignty
- Regional data residency requirements.
- Cross-border data transfer controls.
- Certifications (ISO, SOC2) and their implications for platform selection.

---

## Hands-on Labs
### Lab 1 – Cloud Platform Selection Matrix
1. Gather requirements (latency, data volume, existing stack, skill set).
2. Compare AWS, Azure, GCP, Databricks on key dimensions (cost, services, integration).
3. Recommend platform(s) with rationale and migration considerations.
4. Deliverables: comparison matrix, decision memo, risk assessment.

### Lab 2 – End-to-End Pipeline on Cloud Platform
1. Choose a platform; implement ingestion → transformation → visualization workflow.
2. Use platform-native tools (e.g., AWS Glue + Redshift + QuickSight, Azure Data Factory + Synapse + Power BI, GCP Dataflow + BigQuery + Looker Studio).
3. Document deployment steps and automation scripts.
4. Deliverables: architecture diagram, pipeline script snippets, deployment guide.

### Lab 3 – Cost Optimization Exercise
1. Analyze sample billing data; identify high-cost services.
2. Propose optimization strategies (reservations, autoscaling, storage tiering).
3. Calculate potential savings and present to stakeholders.
4. Deliverables: cost report, optimization plan, stakeholder presentation.

### Lab 4 – Security & Governance Implementation
1. Configure IAM roles/service accounts, define least privilege access.
2. Implement data classification tagging and access policies.
3. Set up monitoring/alerts for policy violations.
4. Deliverables: security policy document, IAM configuration snapshots, audit checklist.

### Lab 5 – Multi-Region Disaster Recovery Plan
1. Design DR architecture (cross-region replication, failover strategy).
2. Simulate failover steps and recovery time objectives.
3. Document communication plan and testing procedures.
4. Deliverables: DR plan, runbook, test results summary.

---

## Practice Question Bank
1. **Case**: A global company wants to centralize analytics in the cloud. Which platform do you recommend and why?
2. **Design**: Compare designing a BI architecture on Snowflake vs BigQuery for a SaaS company.
3. **Performance**: How would you reduce BigQuery query costs for large ad-hoc analytics workloads?
4. **Governance**: Outline a governance framework for a multi-team Azure Synapse deployment.
5. **Behavioral**: Tell me about a time you influenced a platform decision; what was the impact?
6. **Security**: How do you enforce row-level security when using Snowflake with Power BI?
7. **Advanced**: Explain how Databricks Lakehouse differs from traditional warehouses and when you’d adopt it.
8. **Troubleshooting**: A scheduled pipeline in Cloud Composer keeps failing. Walk through your debugging approach.

---

## Interview Story Bank (STAR Prompts)
- **Platform Migration**: Led migration from on-prem to cloud; detail reasoning, execution, results.
- **Cost Control**: Implemented monitoring/optimization that reduced monthly spend.
- **Security Improvement**: Strengthened IAM and data classification to pass audit.
- **Cross-Cloud Collaboration**: Coordinated teams using different clouds; highlight integration approach.
- **Innovation**: Introduced feature store or real-time architecture driving new capabilities.

Prepare concise bullet narratives emphasizing metrics (cost savings, performance improvements, risk reduction).

---

## Glossary & Cross-References
- Glossary terms: serverless, data lakehouse, IAM, autoscaling, feature store (see `shared/glossary.md`).
- Related modules:
  - `Data_Warehousing_Fundamentals/module.md` for core architecture concepts.
  - `ETL_ELT_Processes/module.md` for pipeline implementation.
  - `Visualization_and_Tools/module.md` for BI consumption layers.

---

## Further Reading & Resources
- AWS Well-Architected Framework (Analytics Lens).
- Azure Architecture Center – analytics reference architectures.
- Google Cloud whitepapers on modern data stack and BigQuery optimization.
- Databricks Lakehouse Fundamentals documentation.
- Snowflake Cost Optimization guide and governance best practices.
- Cloud cost management blogs (FinOps Foundation).

---

## Learner Practice Checklist
- [ ] Complete the platform comparison matrix and produce a recommendation memo for a hypothetical organization.
- [ ] Implement an end-to-end pipeline on your chosen cloud platform and document deployment automation.
- [ ] Analyze sample billing data to identify optimization opportunities and present savings estimates.
- [ ] Configure IAM roles, tagging, and monitoring alerts to demonstrate governance controls.
- [ ] Draft a multi-region disaster recovery plan and simulate failover steps.

_Last updated: 2025-11-10_
