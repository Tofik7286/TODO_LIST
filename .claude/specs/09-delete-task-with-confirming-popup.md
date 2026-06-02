# Spec: Delete Task With Confirming Popup

## Overview
This feature adds the ability for authenticated users to delete their own tasks from the todo list. To prevent accidental deletion, a confirmation modal popup appears when the user clicks the delete button. The modal asks the user to confirm before the delete request is sent to the server. This is a critical CRUD operation that completes the full task management lifecycle alongside add and edit.

## Depends on
- Step 01: Homepage Design
- Step 02: Database Creation (Task model)
- Step 03: Homepage data display for logged-in user
- Step 07: Add Task
- Step 08: Edit Task

## Routes
- `POST /tasks/<int:task_id>/delete/` — delete a task owned by the current user — logged-in

## Database changes
No database changes.

## Templates
- **Create:** none
- **Modify:**
  - `todoapp/templates/todoapp/todo.html` — add a Delete button to each task card; add a confirmation modal component; add vanilla JS to wire the modal to the correct task's delete form

## Files to change
- `todoapp/views.py` — add `delete_task` view
- `todoapp/urls.py` — add URL pattern for delete
- `todoapp/templates/todoapp/todo.html` — add delete button, modal, and JS

## Files to create
No new files.

## New dependencies
No new dependencies.

## Rules for implementation
- Use Django ORM only — no raw SQL
- Use Tailwind CSS only — no custom CSS files, no `<style>` blocks
- Use vanilla JS only — no external JS libraries
- Function-Based Views only — no Class-Based Views
- The delete view must use `POST` (not GET) to prevent CSRF-unsafe deletion via link
- Always verify ownership with `get_object_or_404(Task, pk=task_id, user=request.user)` before deleting
- The confirmation modal must be rendered entirely in the template — no separate template file needed
- The modal is triggered by JS; no page navigation occurs until the user confirms
- Each task's delete button must target only that task's delete URL via a hidden form
- Use Django's messages framework to show a success message after deletion
- Follow all conventions in `CLAUDE.md`

## Definition of done
- [ ] Clicking the Delete button on any task card opens the confirmation modal
- [ ] The modal clearly identifies the action (e.g., "Are you sure you want to delete this task?")
- [ ] Clicking "Cancel" (or closing the modal) dismisses it without deleting the task
- [ ] Clicking "Delete" in the modal submits a POST request and deletes the task
- [ ] After deletion, the user is redirected to the todo page and a success message is shown
- [ ] A user cannot delete another user's task (ownership enforced server-side — returns 404)
- [ ] CSRF token is included in the delete form
- [ ] The modal works correctly for every task on the page, not just the first one
- [ ] No JavaScript errors appear in the browser console during normal use
