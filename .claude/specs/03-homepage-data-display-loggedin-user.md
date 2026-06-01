# Spec: Homepage Data Display Logged In User

## Overview
Wire up the homepage (`/`) to display real task data for the authenticated user. The `todo` view currently passes no context to the template — the table already uses `{% for task in tasks %}` but `tasks` is never provided. This step fetches the logged-in user's tasks from the database and passes them to the template, so the homepage shows live data instead of the empty-state message.

## Depends on
- Step 01: Homepage Design (template structure with `{% for task in tasks %}` loop)
- Step 02: Database Creation (`Task` model with `user`, `title`, `created_at` fields)

## Routes
No new routes. The existing `GET /` route (`todo` view) is updated to supply context.

## Database changes
No database changes. The `Task` model already has all required fields.

## Templates
- **Modify:** `todoapp/templates/todoapp/todo.html`
  - Format `created_at` using Django's `|date` template filter for a readable display (e.g. `"M d, Y"`)
  - No structural changes — the loop and empty-state are already in place

## Files to change
- `todoapp/views.py` — update the `todo` view to query the logged-in user's tasks and pass them as `tasks` context
- `todoapp/templates/todoapp/todo.html` — apply `|date:"M d, Y"` filter to `created_at`

## Files to create
No new files.

## New dependencies
No new dependencies.

## Rules for implementation
- Use Django ORM only — no raw SQL
- Filter tasks by `request.user` to enforce ownership — never expose other users' tasks
- Use `select_related` or retrieve only what is needed; avoid N+1 queries
- Order tasks by `created_at` descending so the newest appear first
- Use Tailwind CSS only — no custom CSS files, no `<style>` blocks
- Use vanilla JS only — no external JS libraries
- Function-Based Views only — no Class-Based Views
- Follow all conventions in `CLAUDE.md`
- Do not add, remove, or restructure any template components — only wire in real data

## Definition of done
- [ ] The `todo` view queries `Task.objects.filter(user=request.user)` (or equivalent) and passes the result as `tasks` to the template
- [ ] Tasks are ordered newest-first (`-created_at`)
- [ ] Only tasks belonging to the logged-in user are displayed — visiting as a different user shows only that user's tasks
- [ ] The task table renders each task's `title` and formatted `created_at` correctly
- [ ] When the user has no tasks the empty-state row ("No tasks yet…") is shown
- [ ] The page loads without Django template errors or Python exceptions
- [ ] No changes are made to models, migrations, forms, URLs, or admin
