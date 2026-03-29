---
agent: ask
description: Generate a conventional commit message from staged git changes.
---

# RTACCO Prompt: Generate Conventional Commit Message

**Role:** Git commit message generator

**Task:** Write a conventional commit message for the following staged changes (git diff):

${input:diff}

**Audience:** Developers and code reviewers

**Context:**
- The commit message must summarize the semantic intent of the changes, not list files or code details.
- Use the conventional commit format: subject line (≤72 chars) with feat/fix/chore/test/docs/refactor prefix, optional body for rationale, and optional footer for breaking changes.

**Constraints:**
- Do not include file lists or code snippets.
- Focus on the purpose and impact of the change.
- Subject line must be ≤72 characters.

**Output:**
- A conventional commit message with:
  - Subject line (feat/fix/chore/test/docs/refactor prefix)
  - Optional body paragraph explaining WHY (not what)
  - Optional footer for breaking changes
