# Spec: Add Task

## Overview
The homepage currently displays tasks and has a placeholder "Add Task" button that does nothing. This step wires up that button to navigate to a dedicated Add Task page containing a task creation form. On submission, the task is saved to the database, associated with the logged-in user, and the user is returned to the homepage with the new task visible in the list. This is the first piece of CRUD functionality and establishes the pattern for future edit/delete operations.

## Depends on
- Step 02: Database Creation (Task model and migrations in place)
- Step 03: Homepage Data Display – Logged-In User (`@login_required`, `request.user` available)
- Step 04: Homepage Task Columns Display (task table layout already rendered)

## Routes
- `GET /tasks/add/` — render the Add Task form page — access: logged-in only
- `POST /tasks/add/` — create a new task for the logged-in user — access: logged-in only

## Database changes
No database changes. The `Task` model already has all required fields:
- `user` (ForeignKey to User)
- `title` (CharField)
- `description` (TextField)
- `category` (CharField)
- `priority` (TextChoices: Low / Medium / High)
- `status` (TextChoices: Pending / In Progress / Completed — default: Pending)
- `due_date` (DateField)
- `created_at` (auto_now_add)

## Templates
- **Create:** `todoapp/templates/todoapp/add_task.html`
  - Dedicated page for the task creation form
  - Clean, modern design consistent with the rest of the app (same Tailwind palette, same max-width container)
  - Form fields: Title, Description, Category, Priority (dropdown), Status (dropdown, default Pending), Due Date
  - Inline field-level validation errors displayed on the page if the form is invalid
  - A "Cancel" button that navigates back to `/` without saving
- **Modify:** `todoapp/templates/todoapp/todo.html`
  - Update the existing "Add Task" button to link to `/tasks/add/` instead of its current placeholder behaviour

## Files to change
- `todoapp/views.py` — add the `add_task` view function
- `todoapp/urls.py` — register the `GET /tasks/add/` and `POST /tasks/add/` routes
- `todoapp/templates/todoapp/todo.html` — update the "Add Task" button to link to `/tasks/add/`

## Files to create
- `todoapp/templates/todoapp/add_task.html` — the dedicated Add Task page

## New dependencies
No new dependencies.

## Rules for implementation
- Use Django ORM only — no raw SQL
- Use Tailwind CSS only — no custom CSS files, no `<style>` blocks
- Use vanilla JS only — no external JS libraries
- Function-Based Views only — no Class-Based Views
- Follow all conventions in `CLAUDE.md`
- Decorate `add_task` with `@login_required`
- `GET` renders the empty task form; `POST` processes the submission
- Always set `task.user = request.user` before saving — never trust user input for ownership
- Use the existing `TaskForm` from `forms.py` — do not read `request.POST` directly
- If the form is invalid, re-render `add_task.html` with the form and inline errors visible
- After a valid save, use `redirect('todo')` (POST-Redirect-GET pattern) to prevent duplicate submissions on browser refresh
- Use Django's messages framework (`messages.success`) to confirm task creation after the redirect
- Display the flash success message on `todo.html` (brief banner, auto-dismisses or user can close)
- `due_date` input must use `type="date"` — no third-party date picker
- `priority` and `status` must render as `<select>` dropdowns populated from `Task.Priority.choices` and `Task.Status.choices`
- `description` renders as `<textarea>`
- All fields are required unless the model explicitly allows blank/null
- Do not alter the task list query in the `todo` view; it already orders by `-created_at`

## Definition of done
- [ ] Clicking "Add Task" on the homepage navigates to `/tasks/add/`
- [ ] `GET /tasks/add/` renders the Add Task page with an empty form
- [ ] Clicking "Cancel" on the Add Task page navigates back to `/` without saving anything
- [ ] Submitting the form with all valid fields creates a new task owned by the logged-in user and redirects to `/`
- [ ] The newly created task appears at the top of the task list immediately after the redirect
- [ ] A success flash message is displayed after task creation
- [ ] Submitting the form with missing or invalid fields re-renders the Add Task page with inline error messages visible
- [ ] The `add_task` view redirects unauthenticated requests to the login page
- [ ] No task is created if the form is invalid (no partial saves)
- [ ] Priority and Status dropdowns are populated from the model's `TextChoices`
- [ ] Due Date uses a native date input
- [ ] The page loads without Django template errors or Python exceptions
- [ ] No changes are made to models or migrations