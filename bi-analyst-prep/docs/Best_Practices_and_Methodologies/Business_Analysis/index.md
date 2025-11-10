---
layout: default
title: Business Analysis
parent: Best Practices & Methodologies
nav_order: 2
last_reviewed: 2025-11-10
reviewer: Rodrigo (BI Lead)
---

# Business Analysis for BI Analysts – Mastery Module

## Learning Objectives
- Elicit, document, and refine business requirements for analytics initiatives.
- Translate stakeholder goals into measurable KPIs, user stories, and data specifications.
- Conduct stakeholder interviews, workshops, and process mapping tailored to BI projects.
- Manage scope, prioritize requests, and negotiate trade-offs using structured techniques.
- Communicate analytical findings and requirements effectively across technical and business audiences.
- Showcase end-to-end discovery skills during interviews and project engagements.

## Prerequisites & Audience
- Experience participating in BI or data projects.
- Familiarity with basic agile concepts and data modeling terminology.
- Audience: BI Analysts, analytics product owners, or aspiring business analysts within data teams.

## 1. Foundations & Theory
### 1.1 Business Analysis Lifecycle
- Discovery → Analysis → Solution Design → Validation → Deployment → Evaluation.
- Iterative approach aligned with agile sprints; continuous feedback loops.

### 1.2 Stakeholder Analysis
- Identify personas (executives, managers, analysts, engineers).
- RACI matrices, power-interest grids to prioritize engagement.
- Stakeholder empathy maps to understand motivations and pain points.

### 1.3 Requirement Types
- Business requirements (objectives, outcomes).
- Functional requirements (features, data transformations).
- Non-functional requirements (performance, security, usability).
- Data requirements (granularity, refresh cadence, data quality tolerances).

### 1.4 Problem Definition
- Techniques: problem statements, 5 Whys, fishbone diagrams.
- Aligning BI initiatives with strategic goals (OKRs, KPIs).

---

## 2. Elicitation Techniques & Practices
### 2.1 Interviews & Workshops
- Prepare agendas, discussion guides, follow-up questions.
- Active listening, probing for context, capturing assumptions.
- Collaborative sessions: design thinking workshops, story mapping.

### 2.2 Observation & Process Analysis
- Job shadowing, contextual inquiry.
- Process mapping (AS-IS vs TO-BE, swimlane diagrams).
- Value stream mapping to identify bottlenecks and waste.

### 2.3 Document Analysis
- Review existing reports, SOPs, policy documents.
- Data profiling to validate assumptions.

### 2.4 Surveys & Feedback Tools
- Use when broad input needed; design unbiased questions.
- Tools: Forms, Typeform, in-product feedback loops.

### 2.5 Prototyping & Wireframing
- Low-fidelity sketches to validate requirements quickly.
- Use Power BI mockups, Figma, Tableau storyboards.
- Gather feedback early to avoid misalignment.

---

## 3. Requirements Documentation & Communication
### 3.1 User Stories & Acceptance Criteria
- Format: “As a persona, I want, so that.”
- Acceptance criteria with measurable conditions (include data validation).
- When to use use cases vs user stories.

### 3.2 Requirements Traceability Matrix (RTM)
- Map requirements to source, technical tasks, tests, and deliverables.
- Maintain traceability through changes to ensure coverage.

### 3.3 Data Dictionaries & Specifications
- Define metrics, dimensions, hierarchies, filter logic.
- Include sample queries, data sources, refresh frequency.
- Align with governance standards and glossary entries.

### 3.4 Communication Artifacts
- BRDs, functional specs, one-pagers, dashboard briefs.
- Storytelling memos highlighting context, solutions, impact.
- Stakeholder update cadence (weekly sync, steering committee).

---

## 4. Prioritization, Scope & Change Control
### 4.1 Prioritization Frameworks
- MoSCoW, RICE, Kano analysis.
- Impact vs effort matrices, factoring data availability/complexity.

### 4.2 Scope Management
- Define MVP, iterations, release roadmap.
- Manage scope creep via change request process and trade-offs.
- Document dependencies and constraints.

### 4.3 Risk Assessment
- Identify risks (data quality, adoption, regulatory) with mitigation plans.
- Use RAID logs (Risks, Assumptions, Issues, Dependencies).

### 4.4 Validation & Testing
- UAT plans/test scripts aligning with requirements.
- Pilot programs and phased rollouts.
- Feedback loops post-launch; feed insights into backlog.

---

## 5. Advanced & Edge Cases
### 5.1 Cross-Functional Alignment
- Facilitate alignment across engineering, BI, finance, operations.
- Shared roadmaps with dependency mapping.

### 5.2 Data Literacy & Enablement
- Assess stakeholder data literacy; tailor training.
- Create enablement materials (playbooks, cheat sheets, office hours).

### 5.3 Regulatory & Compliance Considerations
- Integrate compliance requirements (SOX, HIPAA, GDPR) early.
- Document data retention, privacy, audit trail needs.

### 5.4 Measuring Success & ROI
- Define success metrics (adoption, decision cycle time, revenue impact).
- Conduct post-implementation reviews; continuous improvement loops.

### 5.5 Change Management
- Apply ADKAR (Awareness, Desire, Knowledge, Ability, Reinforcement).
- Communication plans, champions network, training schedules.

---

## Hands-on Labs
### Lab 1 – Stakeholder Interview Simulation
1. Prepare interview guide for a new BI initiative.
2. Conduct mock interview (role-play) capturing requirements and follow-ups.
3. Summarize insights, pain points, next steps.
4. Deliverables: interview script, notes, requirement summary.

### Lab 2 – Process Mapping & Gap Analysis
1. Map current reporting process end-to-end.
2. Identify pain points and improvement opportunities.
3. Design TO-BE process aligned with BI solution.
4. Deliverables: AS-IS/TO-BE diagrams, gap analysis report.

### Lab 3 – Requirements Package Creation
1. Convert stakeholder inputs into user stories, data dictionary, RTM.
2. Define acceptance criteria and UAT plan.
3. Validate with stakeholders and incorporate feedback.
4. Deliverables: requirements packet, traceability matrix, approval log.

### Lab 4 – Prioritization Workshop
1. Facilitate workshop using MoSCoW or RICE to prioritize backlog.
2. Document decisions, trade-offs, alignment outcomes.
3. Deliverables: prioritized backlog, decision matrix, communication summary.

### Lab 5 – Change Management Plan
1. Develop change impact assessment for BI dashboard rollout.
2. Create communication, training, reinforcement plan.
3. Measure readiness indicators and track adoption metrics.
4. Deliverables: change plan, communication calendar, adoption dashboard outline.

---

## Practice Question Bank
1. **Case**: Business leader requests a dashboard with unclear metrics. Outline your gathering approach.
2. **Design**: Document requirements to align business stakeholders and data engineers.
3. **Prioritization**: Conflicting metric requests—determine sequencing.
4. **Behavioral**: Project with unclear requirements causing rework—lessons learned.
5. **Communication**: Explain data limitations to stakeholders demanding immediate answers.
6. **Scope Control**: Stakeholders introduce new KPIs mid-project—response strategy.
7. **Validation**: Ensure analytics deliverables meet expectations pre-launch.
8. **Advanced**: Incorporate regulatory requirements into analytics solutions from the start.

---

## Interview Story Bank (STAR Prompts)
- **Requirement Rescue**: Turned ambiguous request into successful BI solution.
- **Stakeholder Alignment**: Navigated conflicting priorities across departments.
- **Process Improvement**: Redesigned reporting process to reduce cycle time.
- **Change Adoption**: Drove adoption of new analytics product via training and communication.
- **Risk Mitigation**: Identified/resolved data governance issue proactively.

---

## Glossary & Cross-References
- Glossary: RACI, MoSCoW, RTM, RAID log, ADKAR (`shared/glossary.md`).
- Related modules:
  - `Agile_Methodologies/module.md` for execution framework.
  - `Visualization_and_Tools/module.md` for deliverable design.
  - `SQL_for_Data_Analysis/module.md` for translating requirements into data queries.

---

## Further Reading & Resources
- IIBA BABOK Guide.
- PMI’s Business Analysis for Practitioners.
- *Communicating Data with Tableau* (Ben Jones).
- Harvard Business Review articles on stakeholder management.
- Change management resources (Prosci, Kotter’s 8-step).

---

## Learner Practice Checklist
- [ ] Conduct a stakeholder interview using the provided guide; summarize insights and action items.
- [ ] Create AS-IS and TO-BE process maps for a BI workflow and identify gaps.
- [ ] Compile a requirements package (user stories, RTM, UAT plan) and secure stakeholder sign-off.
- [ ] Facilitate a prioritization workshop (MoSCoW or RICE) and document trade-offs.
- [ ] Build a change management plan outlining communication, training, and adoption metrics.

_Last updated: 2025-11-10_
