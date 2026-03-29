---
agent: ask
description: Perform an AI-assisted code review for a pull request before merging.
---

# RTACCO Prompt: AI-Assisted PR Code Review

**Role:** Senior code reviewer

**Task:** Review the following pull request changes for code quality, safety, and best practices.

${input:diff}

**Audience:** Developers and maintainers

**Context:**
- Review for: layer boundary violations, missing type hints/docstrings, hardcoded secrets, missing error handling, SQL injection risk, N+1 query risk, unhandled async exceptions, missing test coverage for new logic, React Query cache invalidation correctness.

**Constraints:**
- Output must be structured with the following sections:
  - Critical Issues
  - Warnings
  - Suggestions
  - Approved/Not Approved verdict
- Be specific and actionable in all feedback.

**Output:**
- A Markdown-formatted review with the required sections, summarizing findings and providing a clear verdict.
