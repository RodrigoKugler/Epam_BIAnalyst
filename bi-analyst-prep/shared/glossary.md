# BI Analyst Training – Glossary

## Data Foundations
- **Fact Table**: Central table storing quantitative measurements of business processes at a defined grain.
- **Dimension Table**: Table containing descriptive attributes used to filter, group, and label facts.
- **Conformed Dimension**: Dimension shared across multiple fact tables to ensure consistent reporting.
- **Grain**: Level of detail represented by a row in a fact or dimension table.
- **Slowly Changing Dimension (SCD)**: Dimension where attribute values change over time; managed with specific update strategies (Type 0–6).

## SQL & Querying
- **Sargable Predicate**: Filter condition that allows the query optimizer to leverage indexes efficiently.
- **Window Function**: SQL function applied across a set of rows related to the current row without collapsing result sets.
- **Execution Plan**: Engine-generated map showing how a database executes a query, including operations and estimated costs.
- **Cohort Analysis**: Technique grouping entities by a shared characteristic (e.g., signup month) to analyze behavior over time.

## ETL/ELT & Governance
- **ETL**: Extract-Transform-Load pattern performing transformations outside the target system before load.
- **ELT**: Extract-Load-Transform pattern loading raw data first, then transforming within the target system.
- **Change Data Capture (CDC)**: Method of identifying and capturing changes in source data to apply incrementally downstream.
- **Idempotent Pipeline**: Pipeline designed to produce consistent results even when executed multiple times with the same inputs.
- **Data Contract**: Formal agreement defining schemas, semantics, and SLAs between data producers and consumers.

## Cloud & Architecture
- **Serverless**: Execution model where the cloud provider manages infrastructure, automatically scaling resources per demand.
- **Data Lakehouse**: Architecture combining flexible storage of a data lake with the governance and performance of a warehouse.
- **Identity and Access Management (IAM)**: Framework controlling authentication and authorization of users and services.
- **Autoscaling**: Automatic adjustment of compute resources to match workload demand.
- **Feature Store**: Managed repository for storing, governing, and serving machine-learning features.

## Agile & Delivery
- **Definition of Ready (DoR)**: Criteria ensuring a backlog item is sufficiently understood before planning.
- **Definition of Done (DoD)**: Agreed-upon checklist confirming work meets quality standards before completion.
- **Velocity**: Amount of work a team completes in a sprint, often measured in story points.
- **Cycle Time**: Time it takes for work to move from start to finish in a Kanban workflow.
- **Cumulative Flow Diagram (CFD)**: Visualization showing quantities of work in different states over time to monitor flow.

## Business Analysis & Change
- **RACI Matrix**: Responsibility assignment chart identifying who is Responsible, Accountable, Consulted, and Informed.
- **MoSCoW**: Prioritization method categorizing requirements as Must, Should, Could, or Won’t have.
- **Requirements Traceability Matrix (RTM)**: Document linking requirements to design, development, and testing artifacts.
- **RAID Log**: Register tracking project Risks, Assumptions, Issues, and Dependencies.
- **ADKAR**: Change management model focusing on Awareness, Desire, Knowledge, Ability, and Reinforcement.
