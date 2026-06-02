# Spec: Edit Task

## Overview
This feature adds the ability for a logged-in user to edit an existing task they own. A dedicated edit page pre-fills a form with the task's current data, allowing the user to update any field (title, description, category, priority, status, due date) and save the changes. This is a natural follow-on to the Add Task feature (step 07) and completes the core CRUD lifecycle for tasks.

## Depends on
- Step 02: Database creation (Task model exists)
- Step 07: Add Task (TaskForm exists and is reusable)

## Routes
- `GET  /tasks/<int:task_id>/edit/` — display pre-filled edit form for the task — logged-in only
- `POST /tasks/<int:task_id>/edit/` — process form submission and save updated task — logged-in only

## Database changes
No database changes. The existing `Task` model has all required fields.

## Templates

### Create
- `todoapp/templates/todoapp/edit_task.html` — edit form page, mirrors `add_task.html` layout but pre-filled and with an "Update Task" heading and submit button

### Modify
- `todoapp/templates/todoapp/todo.html` — add an "Edit" button/link per task row that points to the edit URL

## Files to change
- `todoapp/views.py` — add `edit_task` view function
- `todoapp/urls.py` — add URL pattern for the edit route
- `todoapp/templates/todoapp/todo.html` — add "Edit" button per task row

## Files to create
- `todoapp/templates/todoapp/edit_task.html`

## New dependencies
None.

## Rules for implementation
- FBVs only — no Class-Based Views
- `@login_required` on the view
- Use `get_object_or_404(Task, pk=task_id, user=request.user)` to fetch the task — enforces ownership and returns 404 for tasks the user does not own
- Reuse the existing `TaskForm` (ModelForm) — do not create a separate form class
- Bind the form with `instance=task` to pre-fill all fields
- On valid POST: save, redirect to `/` with `messages.success` confirmation (POST-Redirect-GET)
- On invalid POST: re-render form with validation errors, no data saved
- Tailwind CSS only — no `<style>` blocks, no inline styles, no hex values
- Vanilla JS only — no external JS libraries
- ORM only — no raw SQL
- `{% url %}` tags in templates — no hardcoded URL strings
- Follow all conventions in `CLAUDE.md`

## Definition of done
- [ ] Navigating to `/tasks/<id>/edit/` while logged in renders the edit form with all fields pre-filled from the existing task
- [ ] Submitting valid changes updates the task in the database and redirects to `/` with a success message
- [ ] Submitting invalid data re-renders the form with validation errors — no data is saved
- [ ] Attempting to edit another user's task returns a 404 (not a redirect or permission error)
- [ ] Visiting `/tasks/<id>/edit/` while logged out redirects to `/login/`
- [ ] An "Edit" button is visible on each task row in `todo.html` and points to the correct URL
- [ ] The edit page is visually consistent with `add_task.html` (same layout, Tailwind styling)