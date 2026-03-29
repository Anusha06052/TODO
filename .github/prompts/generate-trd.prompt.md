---
agent: ask
description: Generate a Technical Requirements Document (TRD) from a PRD for a specified feature.
---

# RTACCO Prompt: Generate Technical Requirements Document (TRD)

**Role:** Senior Engineer or Solution Architect

**Task:** Generate a detailed Technical Requirements Document (TRD) for the feature: ${input:feature}, using the provided PRD below.

**Audience:** Engineering team and technical stakeholders

**Context:**
- The product stack includes FastAPI backend, React frontend, SQL Server, and SQLAlchemy async.
- Use the following PRD as the basis for the TRD:

${file:prd}

**Constraints:**
- Output must be in Markdown format with clear H2 sections.
- Address all required TRD sections.
- Be precise, actionable, and technically detailed.

**Output:**
- A Markdown-formatted TRD with these H2 sections:
  - Architecture Decisions
  - API Contract (endpoints, request/response schemas)
  - DB Schema changes
  - Migration plan
  - Test strategy
  - Performance considerations
  - Security considerations
