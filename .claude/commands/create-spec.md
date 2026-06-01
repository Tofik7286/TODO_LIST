# Create Spec

Create a spec file and feature branch for the next step.

**Usage:** `/create-spec <step_number> <feature_name>`
**Example:** `/create-spec 2 registration`

**Allowed tools:** Read, Write, Glob

**User input:** $ARGUMENTS

---

> You are a senior developer spinning up a new feature for the Todo list project. Always follow the rules in `CLAUDE.md`.

---

## Step 1 — Parse Arguments

From `$ARGUMENTS` extract:

1. `step_number` — zero-padded to 2 digits: `2` → `02`, `11` → `11`
2. `feature_title` — human-readable title in Title Case
   - Example: `Registration` or `Login and Logout`
3. `feature_slug` — git and file-safe slug
   - Lowercase, kebab-case
   - Only `a-z`, `0-9`, and `-`
   - Maximum 40 characters
   - Example: `registration`, `login-logout`

If you cannot infer all three from `$ARGUMENTS`, ask the user to clarify before proceeding.

---

## Step 2 — Research the Codebase

Read the following files before writing the spec:

- `CLAUDE.md` — roadmap, conventions, schema
- `todoapp/views.py` — existing routes and structure
- `todoapp/forms.py`
- `todoapp/models.py`
- `todoapp/urls.py`
- Any other files relevant to the feature
- All files in `.claude/specs/` — avoid duplicating existing specs

Check `CLAUDE.md` to confirm the requested step is not already marked complete. If it is, warn the user and stop:

```
Step <step_number> (<feature_title>) is already marked complete in CLAUDE.md. Nothing to do.
```

---

## Step 3 — Write the Spec

Generate a spec document using this exact structure:

```markdown
# Spec: <feature_title>

## Overview
One paragraph describing what this feature does and why it exists at this stage of the project roadmap.

## Depends on
Which previous steps this feature requires to be complete.

## Routes
Every new route needed:
- `METHOD /path` — description — access level (public / logged-in)

If no new routes: state "No new routes."

## Database changes
Any new tables, columns, or constraints needed.
Always verify against the current models before writing this section.

If none: state "No database changes."

## Templates
- **Create:** list new templates with their full path
- **Modify:** list existing templates and what changes

## Files to change
Every file that will be modified.

## Files to create
Every new file that will be created.

## New dependencies
Any new pip packages required.

If none: state "No new dependencies."

## Rules for implementation
Specific constraints Claude must follow during implementation. Always include:
- Use Django ORM only — no raw SQL
- Passwords hashed with `werkzeug.security.generate_password_hash`
- Use Tailwind CSS only — no custom CSS files, no `<style>` blocks
- Use vanilla JS only — no external JS libraries
- Function-Based Views only — no Class-Based Views
- Follow all conventions in `CLAUDE.md`

## Definition of done
A specific, testable checklist. Each item must be something that can be verified by running the app.
- [ ] ...
- [ ] ...
```

---

## Step 4 — Save the Spec

Save the spec to:

```
.claude/specs/<step_number>-<feature_slug>.md
```

Create the `.claude/specs/` directory if it does not exist.

---

## Step 5 — Report to the User

Print a short summary in this exact format:

```
Spec created: .claude/specs/<step_number>-<feature_slug>.md
```

Then tell the user:

```
Review the spec at `.claude/specs/<step_number>-<feature_slug>.md`
then enter Plan Mode with Shift+Tab twice to begin implementation.
```

Do not print the full spec in chat unless explicitly asked.