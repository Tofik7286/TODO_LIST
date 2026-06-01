# Spec: Homepage Task Columns Display Properly

## Overview
The homepage task table currently shows only two data columns: Task Name and Created At. The `Task` model already has rich fields — `description`, `category`, `priority`, `status`, and `due_date` — that are never surfaced to the user. This step updates the table to display all meaningful columns so users can see the full context of each task at a glance without opening a detail view.

## Depends on
- Step 01: Homepage Design (table structure and Tailwind layout)
- Step 02: Database Creation (`Task` model with all relevant fields)
- Step 03: Homepage Data Display – Logged-In User (view passes `tasks` queryset to template)

## Routes
No new routes.

## Database changes
No database changes. All required fields already exist on the `Task` model.

## Templates
- **Modify:** `todoapp/templates/todoapp/todo.html`
  - Add table header columns: Category, Priority, Status, Due Date (in addition to existing Task Name and Created At)
  - Add corresponding `<td>` cells in the task row for each new column
  - Apply Tailwind badge/pill styles to Priority and Status values so they are visually distinct
  - Update the `colspan` on the empty-state row to match the new column count
  - Keep the Actions column last

## Files to change
- `todoapp/templates/todoapp/todo.html` — expand table headers and task row cells to include all model fields

## Files to create
No new files.

## New dependencies
No new dependencies.

## Rules for implementation
- Use Django ORM only — no raw SQL
- Use Tailwind CSS only — no custom CSS files, no `<style>` blocks
- Use vanilla JS only — no external JS libraries
- Function-Based Views only — no Class-Based Views
- Follow all conventions in `CLAUDE.md`
- Display `due_date` using Django's `|date:"M d, Y"` filter for consistent formatting
- Use inline Tailwind badge classes for Priority (`Low` → green, `Medium` → yellow, `High` → red) and Status (`Pending` → gray, `In Progress` → blue, `Completed` → green)
- Do not change views, models, migrations, forms, URLs, or admin — template only

## Definition of done
- [ ] The table header row shows columns: Task Name, Category, Priority, Status, Due Date, Created At, Actions
- [ ] Each task row renders the correct value for every column from the `Task` model
- [ ] Priority values are displayed with colored badge/pill styling (Low=green, Medium=yellow, High=red)
- [ ] Status values are displayed with colored badge/pill styling (Pending=gray, In Progress=blue, Completed=green)
- [ ] `due_date` is formatted as `"M d, Y"` (e.g. "Jun 01, 2026")
- [ ] `created_at` remains formatted as `"M d, Y"`
- [ ] The empty-state row's `colspan` matches the total number of columns
- [ ] The page loads without Django template errors or Python exceptions
- [ ] No changes are made to views, models, migrations, forms, URLs, or admin
