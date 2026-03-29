---
agent: ask
description: Generate a Product Requirements Document (PRD) for a specified feature in RTACCO format.
---

# RTACCO Prompt: Generate Product Requirements Document (PRD)

**Role:** Product Owner or Business Analyst

**Task:** Generate a comprehensive Product Requirements Document (PRD) for the feature: ${input:feature}

**Audience:** Engineering team and product stakeholders

**Context:**
- The PRD is for a new or updated feature in the product.
- The document will guide design, development, and QA.

**Constraints:**
- Use Markdown format with clear H2 sections.
- Include the following sections: Overview, User Stories, Acceptance Criteria, Out of Scope, Open Questions.
- Be concise, clear, and actionable.

**Output:**
- A Markdown-formatted PRD with these H2 sections:
  - Overview
  - User Stories
  - Acceptance Criteria
  - Out of Scope
  - Open Questions
