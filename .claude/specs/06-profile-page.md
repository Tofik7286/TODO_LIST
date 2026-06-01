# Spec: Profile Page

## Overview
Authenticated users currently have no way to view or update their account information. This step adds a dedicated profile page where users can see their name and email, and update their display name and/or password. The page is accessible from the homepage header, giving the user a persistent entry point to account management.

## Depends on
- Step 02: Database Creation (User model and auth backend in place)
- Step 03: Homepage Data Display – Logged-In User (`@login_required` on the `todo` view, `request.user` available)
- Step 05: Logout Feature (header with user name exists in `todo.html`)

## Routes
- `GET /profile/` — display the profile form pre-filled with the user's current name and email — access: logged-in only
- `POST /profile/` — validate and save changes to name and/or password — access: logged-in only

## Database changes
No database changes. The feature uses the existing `django.contrib.auth.models.User` fields:
- `first_name` — displayed and editable as "Name"
- `email` / `username` — displayed (read-only; email change is out of scope)
- `password` — updatable via Django's `set_password()`

## Templates
- **Create:** `todoapp/templates/todoapp/profile.html`
  - Clean, modern design — consistent with the visual style of `todo.html` (same Tailwind palette, same max-width container)
  - Displays a static avatar at the top of the profile card — the same generic avatar for all users (use an inline SVG user icon; no image upload, no external image URL)
  - Shows: current name (pre-filled), current email (read-only display), new name field, current password field, new password field, confirm new password field
  - Inline field-level error messages styled consistently with register/login pages
  - A "Back to Tasks" link that navigates to `/`
  - Success feedback via Django messages framework (flash message at top of form)
- **Modify:** `todoapp/templates/todoapp/todo.html`
  - Wrap the user's name in the header in an `<a>` tag linking to `/profile/` so users can navigate to their profile

## Files to change
- `todoapp/views.py` — add the `profile` view function
- `todoapp/urls.py` — register the `/profile/` route
- `todoapp/forms.py` — add `ProfileForm`
- `todoapp/templates/todoapp/todo.html` — make the user name in the header a link to `/profile/`

## Files to create
- `todoapp/templates/todoapp/profile.html` — the profile page template

## New dependencies
No new dependencies.

## Rules for implementation
- Use Django ORM only — no raw SQL
- Use Tailwind CSS only — no custom CSS files, no `<style>` blocks
- Use vanilla JS only — no external JS libraries
- Function-Based Views only — no Class-Based Views
- Follow all conventions in `CLAUDE.md`
- Decorate `profile` with `@login_required`
- `ProfileForm` must be a `forms.Form` (not `ModelForm`) to handle password fields explicitly
- Name field is optional to change — if left as-is, keep the current value
- Password change is optional — only update if the user fills in the current password field AND the new password fields; if any of the three password fields are filled, all three are required
- Validate current password using `request.user.check_password()` before accepting a new password
- New password and confirm password must match — raise a `ValidationError` in `clean()` if they differ
- After a successful save, call `update_session_auth_hash(request, user)` to keep the user logged in after a password change
- Use Django's messages framework (`messages.success`) for post-save confirmation; display the flash message at the top of the profile template
- Never expose the hashed password or any raw password value in the template context
- Display email as read-only text (not an editable input); email/username change is out of scope
- Ownership is implicit — the view always operates on `request.user`; no object-level lookup needed
- The avatar must be an inline SVG user icon — do not use an external image URL, a user-uploaded image, or any per-user variation; it is identical for every user

## Definition of done
- [ ] `GET /profile/` renders the profile page with the name field pre-filled with `request.user.first_name`
- [ ] A static avatar icon is visible at the top of the profile card and is the same for all users
- [ ] The email is displayed on the page but is not editable
- [ ] Submitting only a new name (leaving password fields blank) updates `first_name` and shows a success message without changing the password
- [ ] Submitting a correct current password plus matching new/confirm password updates the password and keeps the user logged in
- [ ] Submitting a wrong current password shows a field-level error and does not change the password
- [ ] Submitting mismatched new/confirm passwords shows a validation error and does not change the password
- [ ] Filling in only some password fields (partial) shows a validation error prompting the user to complete all three fields
- [ ] An unauthenticated request to `/profile/` redirects to `/login/`
- [ ] The user's name in the `todo.html` header links to `/profile/`
- [ ] The profile page includes a "Back to Tasks" link that navigates to `/`
- [ ] The page loads without Django template errors or Python exceptions
- [ ] No changes are made to models or migrations