# Spec: Logout Feature

## Overview
Authenticated users currently have no way to sign out of the application. This step wires up Django's built-in `logout` view, adds a logout button to the homepage header, and ensures the session is cleanly terminated and the user is redirected to the login page. It also surfaces the logged-in user's name in the header so the logout button is clearly contextual.

## Depends on
- Step 02: Database Creation (User model and auth backend in place)
- Step 03: Homepage Data Display – Logged-In User (`@login_required` on the `todo` view, `request.user` available in the template)

## Routes
- `POST /logout/` — logs out the authenticated user and redirects to `/login/` — access: logged-in only

## Database changes
No database changes.

## Templates
- **Modify:** `todoapp/templates/todoapp/todo.html`
  - Add a top navigation bar (or update the existing header block) that shows the logged-in user's name (`request.user.first_name`) on the left and a "Logout" button on the right
  - The logout button must submit a POST form to `/logout/` with the CSRF token
  - No GET link — logout must be a POST to protect against CSRF

## Files to change
- `todoapp/views.py` — add the `logout_view` function
- `todoapp/urls.py` — register the `/logout/` route
- `todoapp/templates/todoapp/todo.html` — add user name display and logout button to the header

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
- Use `django.contrib.auth.logout` to terminate the session
- Decorate `logout_view` with `@login_required` so unauthenticated GET/POST to `/logout/` redirects to login
- After logout, redirect to the named URL `login` — do not hardcode the path
- Logout must be triggered via a POST form, not a plain `<a>` link, to prevent CSRF/logout CSRF attacks
- Include `{% csrf_token %}` inside the logout form
- Display `request.user.first_name` in the header; fall back to `request.user.email` if `first_name` is blank (use a template `if` check)

## Definition of done
- [ ] A `POST /logout/` route exists and is reachable
- [ ] Submitting the logout form ends the session and redirects the user to `/login/`
- [ ] After logout, navigating to `/` redirects to `/login/` (the `@login_required` guard on `todo` is still intact)
- [ ] The homepage header shows the logged-in user's name (or email as fallback)
- [ ] The logout button is a POST form with a CSRF token — not a plain link
- [ ] An unauthenticated request to `/logout/` redirects to the login page (not a 403 or 500)
- [ ] No changes are made to models, migrations, or admin
- [ ] The page loads without Django template errors or Python exceptions
