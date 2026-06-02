# Spec: Add Filters and Search Functionality

## Overview
This feature activates the currently non-functional search input on the main todo page and adds filter dropdowns for status, priority, and category. Filtering and searching are handled server-side via GET query parameters on the existing `/` route, keeping the implementation simple and bookmarkable. The UI works consistently on both mobile (card layout) and desktop (table layout).

## Depends on
- Step 02: Database and Task model exist
- Step 07: Add Task (tasks exist to filter)
- Step 08: Edit Task (task fields are stable)

## Routes
No new routes. The existing `GET /` route is extended to read optional query parameters:
- `?q=` — search term (matches title or description, case-insensitive)
- `?status=` — filter by status (Pending / In Progress / Completed)
- `?priority=` — filter by priority (Low / Medium / High)
- `?category=` — filter by category (free-form, matched exactly)

## Database changes
No database changes.

## Templates
- **Modify:** `todoapp/templates/todoapp/todo.html`
  - Wire the existing search `<input>` inside a `<form method="GET">` that submits to `/`
  - Add three filter `<select>` dropdowns (Status, Priority, Category) to the same GET form
  - Show an active-filters summary / "Clear filters" link when any filter is active
  - Pass `categories`, `current_filters` context from the view so dropdowns reflect current selection
  - Empty-state message should distinguish "no tasks at all" from "no tasks match current filters"

## Files to change
- `todoapp/views.py` — extend the `todo` view to read GET params and apply ORM filters
- `todoapp/templates/todoapp/todo.html` — wire search + add filter dropdowns

## Files to create
No new files.

## New dependencies
No new dependencies.

## Rules for implementation
- Use Django ORM only — no raw SQL
- Filter with `.filter()` chaining; never build raw query strings
- Passwords hashed with `werkzeug.security.generate_password_hash`
- Use Tailwind CSS only — no custom CSS files, no `<style>` blocks
- Use vanilla JS only — no external JS libraries
- Function-Based Views only — no Class-Based Views
- Follow all conventions in `CLAUDE.md`
- Preserve all existing functionality: bulk select, bulk delete, single delete modal, edit link
- Categories dropdown must be built dynamically from the logged-in user's distinct task categories
- GET form submission must not break the logout POST form (keep them separate)
- Filters must be scoped to `user=request.user` — never expose another user's data
- Retain filter state in dropdowns after the page reloads (selected value must match query param)

## Definition of done
- [ ] Typing in the search box and submitting filters the task list by title or description (case-insensitive), on both mobile and desktop
- [ ] The Status dropdown filters tasks to only the selected status; selecting "All" shows all statuses
- [ ] The Priority dropdown filters tasks to only the selected priority; selecting "All" shows all priorities
- [ ] The Category dropdown lists only categories the logged-in user has used; selecting one filters correctly
- [ ] All three filters can be combined simultaneously (e.g. High priority + Pending + "Work")
- [ ] After filtering, the dropdowns and search input retain their selected/entered values
- [ ] A "Clear filters" link appears when any filter is active; clicking it resets all filters
- [ ] When filters match zero tasks, a message like "No tasks match your filters" is shown (different from the "no tasks yet" empty state)
- [ ] Bulk select, bulk delete, single delete modal, and edit actions all work correctly on filtered results
- [ ] Filter UI is visible and usable on mobile (card view) and desktop (table view)
- [ ] No task from another user is ever returned regardless of query parameters
