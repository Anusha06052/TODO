---
mode: ask
description: Guide and review the process of generating an Alembic migration for async SQL Server via aioodbc.
---

# RTACCO Prompt: Alembic Migration Generation & Review

**Role:** Senior backend/database engineer

**Task:** Guide the user through generating and reviewing an Alembic migration for recent model changes.

${input:model_changes}

**Audience:** Backend developers and DBAs

**Context:**
- Stack: async Alembic, SQL Server, SQLAlchemy, aioodbc
- Migration must support both upgrade and downgrade paths

**Constraints:**
- Output the exact alembic revision command to generate the migration
- Provide a review checklist covering:
  1. Model changes reviewed and understood
  2. Alembic revision command correct
  3. Migration file implements all changes accurately
  4. Both upgrade() and downgrade() are implemented
  5. Data-loss risk assessed and documented

**Output:**
- The alembic command to run
- A Markdown-formatted checklist for reviewing the migration
