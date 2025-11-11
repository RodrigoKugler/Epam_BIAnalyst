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

## Role Context & Business Value
Effective business analysis ensures analytics teams solve the right problems and deliver usable insights. Interviewers expect examples of requirement gathering, stakeholder alignment, and change management. Mastery here reduces rework, accelerates adoption, and builds trust with decision makers.

---

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
- Preparing agendas, discussion guides, and follow-up questions.
- Active listening, probing for context, capturing assumptions.
- Collaborative sessions: design thinking workshops, story mapping.

### 2.2 Observation & Process Analysis
- Job shadowing, contextual inquiry.
- Process mapping (AS-IS vs TO-BE diagrams, swimlane diagrams).
- Value stream mapping to identify bottlenecks and waste.

### 2.3 Document Analysis
- Reviewing existing reports, SOPs, policy docs.
- Data profiling results to validate assumptions.

### 2.4 Surveys & Feedback Tools
- When mass input needed; design unbiased questions.
- Tools: Forms, Typeform, in-product feedback loops.

### 2.5 Prototyping & Wireframing
- Low-fidelity sketches (paper, Balsamiq) to validate requirements quickly.
- Use Power BI mockups, Figma, or Tableau storyboards.
- Gather feedback early to avoid misalignment.

---

## 3. Requirements Documentation & Communication
### 3.1 User Stories & Acceptance Criteria
- Format: “As a persona, I want, so that.”
- Acceptance criteria with measurable conditions; include data validation steps.
- Use cases vs user stories; when to employ each.

### 3.2 Requirements Traceability Matrix (RTM)
- Map requirements to source, technical tasks, test cases, and deliverables.
- Maintain traceability through changes to ensure coverage.

### 3.3 Data Dictionaries & Specifications
- Define metrics, dimensions, hierarchies, filter logic.
- Include sample queries, data sources, refresh frequency.
- Align with data governance standards and glossary entries.

### 3.4 Communication Artifacts
- BRDs, functional specs, one-pagers, dashboards briefs.
- Storytelling memos highlighting business context, proposed solutions, impact.
- Stakeholder update cadence (weekly sync, steering committee updates).

---

## 4. Prioritization, Scope & Change Control
### 4.1 Prioritization Frameworks
- MoSCoW, RICE, Kano analysis.
- Impact vs effort matrices; include data availability and complexity factors.

### 4.2 Scope Management
- Define MVP, iterations, release roadmap.
- Manage scope creep: change request process, trade-off discussions.
- Document dependencies and constraints (technology, compliance, resources).

### 4.3 Risk Assessment
- Identify risks (data quality, adoption, regulatory) and mitigation plans.
- Use RAID logs (Risks, Assumptions, Issues, Dependencies).

### 4.4 Validation & Testing
- User acceptance testing (UAT) plans, test scripts aligning with requirements.
- Pilot programs and phased rollouts.
- Feedback loops post-launch; incorporate findings into backlog.

---

## 5. Advanced & Edge Cases
### 5.1 Cross-Functional Alignment
- Facilitate alignment between data engineering, BI, finance, and operations.
- Create shared roadmaps incorporating dependencies.

### 5.2 Data Literacy & Enablement
- Assess stakeholder data literacy levels; tailor training.
- Build enablement materials (playbooks, cheat sheets, office hours).

### 5.3 Regulatory & Compliance Considerations
- Incorporate compliance requirements (SOX, HIPAA, GDPR) into requirements.
- Data retention, privacy, audit trail needs documented upfront.

### 5.4 Measuring Success & ROI
- Define success metrics (adoption, decision cycle time, revenue impact).
- Post-implementation reviews; continuous improvement loops.

### 5.5 Change Management
- ADKAR model (Awareness, Desire, Knowledge, Ability, Reinforcement).
- Communication plans, champions network, training schedules.

---

## Hands-on Labs
### Lab 1 – Stakeholder Interview Simulation
1. Prepare interview guide for a new BI initiative.
2. Conduct mock interview (role-play) capturing requirements and follow-ups.
3. Summarize insights, pain points, and proposed next steps.
4. Deliverables: interview script, notes, requirement summary document.

### Lab 2 – Process Mapping & Gap Analysis
1. Map the current reporting process end-to-end.
2. Identify pain points and improvement opportunities.
3. Design TO-BE process aligning with BI solution.
4. Deliverables: AS-IS/TO-BE diagrams, gap analysis report.

### Lab 3 – Requirements Package Creation
1. Convert stakeholder inputs into user stories, data dictionary, and RTM.
2. Define acceptance criteria and UAT plan.
3. Validate with stakeholders and incorporate feedback.
4. Deliverables: requirements packet, traceability matrix, approval log.

### Lab 4 – Prioritization Workshop
1. Facilitate a mock workshop using MoSCoW or RICE to prioritize backlog.
2. Document decisions, trade-offs, and alignment outcomes.
3. Deliverables: prioritized backlog, decision matrix, communication summary.

### Lab 5 – Change Management Plan
1. Develop change impact assessment for new BI dashboard rollout.
2. Create communication, training, and reinforcement plan.
3. Measure readiness indicators and track adoption metrics.
4. Deliverables: change plan, communication calendar, adoption dashboard outline.

---

## Practice Question Bank
1. **Case**: A business leader requests a dashboard with unclear metrics. Walk through your requirement-gathering approach.  
   **Answer:** I start with discovery questions that uncover the decision they’re trying to make, success signals, and pain points with current reporting. I co-create problem statements and capture candidate metrics, then validate data availability with engineering. Before building, I summarize what I heard—personas, KPIs, filters, refresh cadence—and secure sign-off so the request moves from “idea” to scoped requirement.
2. **Design**: How do you document requirements to ensure alignment between business stakeholders and data engineers?  
   **Answer:** I pair narrative artifacts with structured specs: a dashboard brief for business context, user stories with acceptance criteria, and a data dictionary covering sources, transformations, and metric formulas. Everything feeds into a traceability matrix so each requirement maps to development tasks and UAT tests. This keeps business and technical teams reading from the same sheet of music.
3. **Prioritization**: Multiple departments request conflicting metrics. How do you decide what to deliver first?  
   **Answer:** I facilitate a prioritization session using an impact-versus-effort or RICE framework, grounding the discussion in organizational objectives and data readiness. Where conflicts remain, I escalate with a transparent recommendation that outlines trade-offs and dependencies. The goal is a shared roadmap everyone can reference, not a black-box decision.
4. **Behavioral**: Describe a project where unclear requirements caused rework. What would you do differently now?  
   **Answer:** Early in my career I built a sales dashboard assuming “revenue” meant invoiced amounts; finance expected cash receipts and we rebuilt significant portions. Now I insist on a shared glossary, confirm metric formulas in writing, and run a quick wireframe review before development starts. Those checkpoints catch semantic gaps before code is written.
5. **Communication**: How do you explain data limitations to stakeholders who demand immediate solutions?  
   **Answer:** I acknowledge the urgency, then outline the constraint in plain language—what data is missing, why it matters, and what risks come with pushing ahead. I offer alternatives like interim metrics, manual stopgaps, or a phased delivery plan. Framing it as a joint decision, backed by impact analysis, keeps trust intact while we work the constraint.
6. **Scope Control**: Mid-project, stakeholders introduce new KPIs. How do you handle the change?  
   **Answer:** I treat it as a change request: document the new KPI, assess data availability and effort with the team, and show how it affects timeline or other commitments. We decide together whether to swap scope, extend the schedule, or defer to a later release. Capturing the decision in our backlog and comms ensures transparency.
7. **Validation**: Outline your process for ensuring analytics deliverables meet business expectations before launch.  
   **Answer:** I run structured UAT that traces back to acceptance criteria. Stakeholders test real scenarios, we log findings, and I only exit UAT when critical issues are resolved. In parallel we validate numbers against trusted sources, update documentation, and confirm downstream impacts (alerts, exports). A go-live checklist with sign-offs closes the loop.
8. **Advanced**: Discuss how you incorporate regulatory requirements into analytics solutions from the start.  
   **Answer:** During discovery I involve compliance partners to catalogue relevant regulations, required controls, and audit evidence. I embed those into requirements—masking rules, retention windows, approval workflows—and reflect them in technical design (RLS, logging). We track compliance tasks in the backlog and include them in DoD so controls are first-class citizens, not afterthoughts.

---

## Interview Story Bank (STAR Prompts)
- **Requirement Rescue**: Turned ambiguous request into successful BI solution.
- **Stakeholder Alignment**: Navigated conflicting priorities across departments.
- **Process Improvement**: Redesigned reporting process, reducing cycle time.
- **Change Adoption**: Drove adoption of new analytics product through training and communication.
- **Risk Mitigation**: Proactively identified and resolved data governance issue.

Capture bullet points with context, actions, results, and lessons learned.

---

## Glossary & Cross-References
- Update `shared/glossary.md` with:
  - **RACI Matrix**: Chart clarifying who is Responsible, Accountable, Consulted, Informed.
  - **MoSCoW**: Prioritization technique (Must, Should, Could, Won’t).
  - **Requirements Traceability Matrix (RTM)**: Tool linking requirements to deliverables and tests.
  - **RAID Log**: Register tracking Risks, Assumptions, Issues, Dependencies.
  - **ADKAR**: Change management framework.

- Cross-reference modules:
  - `Agile_Methodologies/module.md` for execution framework.
  - `Visualization_and_Tools/module.md` for deliverable design.
  - `SQL_for_Data_Analysis/module.md` for translating requirements into data queries.

---

## Further Reading & Resources
- IIBA BABOK Guide (Business Analysis Body of Knowledge).
- PMI’s Business Analysis for Practitioners.
- *Communicating Data with Tableau* (Ben Jones) for storytelling alignment.
- Harvard Business Review articles on stakeholder management.
- Change management resources (Prosci, Kotter’s 8-step).

---

## Learner Practice Checklist
- [ ] Conduct a stakeholder interview using the provided guide; summarize insights and action items.
- [ ] Create AS-IS and TO-BE process maps for a BI workflow and identify gaps.
- [ ] Compile a requirements package (user stories, RTM, UAT plan) and secure stakeholder sign-off.
- [ ] Facilitate a prioritization workshop (MoSCoW or RICE) and document trade-offs.
- [ ] Build a change management plan outlining communication, training, and adoption metrics.

This module equips BI Analysts to lead discovery, define requirements, and ensure analytics solutions deliver tangible business value.
