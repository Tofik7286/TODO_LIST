
## Project Overview

A Django 6.x todo application. The stack is Django + SQLite on the backend, with HTML, Tailwind CSS, and vanilla JavaScript on the frontend.

This project uses **Function-Based Views (FBVs)** as the standard. Do not convert FBVs to Class-Based Views unless explicitly asked. Always match the existing codebase patterns. The goal is clean, maintainable, scalable, production-ready code following Django best practices.

## Commands

Always activate the virtual environment before running Django commands:

```powershell
.\venv\Scripts\activate
```

**Run the development server:**
```powershell
python manage.py runserver
```

**Apply migrations:**
```powershell
python manage.py makemigrations
python manage.py migrate
```

**Run tests:**
```powershell
python manage.py test todoapp
```

**Create a superuser:**
```powershell
python manage.py createsuperuser
```

## Architecture

This is a Django 6.x project with a single app `todoapp`. The project layout follows standard Django conventions:

- `todo_list/` — project config package (settings, root URL conf, wsgi/asgi)
- `todoapp/` — the sole Django app; contains views, models, URLs, templates, and migrations

**URL routing:** `todo_list/urls.py` includes all routes from `todoapp/urls.py` at the root path (`""`).

**Current routes:**
| URL | View | Template |
|-----|------|----------|
| `/` | `todo` | `todoapp/todo.html` |
| `/register/` | `register` | `todoapp/register.html` |
| `/login/` | `login` | `todoapp/login.html` |

**Templates** live in `todoapp/templates/todoapp/` and are loaded via `APP_DIRS = True`.

**Database:** SQLite (`db.sqlite3` at project root). No models are defined yet — `todoapp/models.py` is empty and migrations only contain the initial empty migration.

**Auth:** Django's built-in `django.contrib.auth` is installed but not yet wired to the register/login views (views currently just render placeholder templates).

## Development Workflow

When building a new feature, follow this order unless there's a strong reason not to:

1. Plan the feature and clarify requirements.
2. Create or update models.
3. Create and run migrations.
4. Register models in `admin.py`.
5. Create forms when needed.
6. Implement views and business logic as Function-Based Views.
7. Configure URLs.
8. Build templates (HTML + Tailwind + JS).
9. Refactor and optimize if needed.
10. Finalize.

## Views (Function-Based)

- Use Function-Based Views, not Class-Based Views, unless explicitly requested.
- Keep views concise and readable.
- Move complex logic into helper functions, services, or model methods.
- Separate database operations from presentation logic.

## Database

- Use `select_related()` for ForeignKey access; `prefetch_related()` for ManyToMany and reverse relationships.
- Avoid N+1 queries and avoid DB hits inside loops.
- Retrieve only the data you need.
- Use indexes where appropriate.
- Prefer the ORM over raw SQL.
- Keep migrations clean and organized.

## Forms

Always use `forms.Form` or `forms.ModelForm` for user input.

- GET → display form. POST → validate; if valid, save/process and redirect; if invalid, re-render with errors.
- Put validation in `clean()` and `clean_<field>()` methods; keep it centralized.
- Never read `request.POST` directly for business logic or bypass form validation.

## Security

- `@login_required` on authenticated pages.
- **Verify ownership** before any read/update/delete of user-specific data — never let users touch objects they don't own.
- Enforce object-level permissions where needed.
- Keep CSRF protection on; validate and escape all user input.
- Use the Django messages framework for user feedback.
- Never hardcode secrets, keys, or credentials in committed code.
- Never rely on client-side validation alone or expose sensitive data in templates.
- Avoid `|safe` unless absolutely necessary and approved.

## Frontend & Templates

- Build responsive, semantic, accessible markup.
- Use template inheritance, reusable partials/includes, and consistent Tailwind utility patterns.
- Keep templates focused on presentation — no business logic, no DB queries, no deep conditional nesting.
- Keep JavaScript lightweight and maintainable.

## Code Quality

- Modular, DRY, single-responsibility functions.
- Meaningful, consistent naming.
- Readability over cleverness; avoid overengineering.
- Reuse existing components and conventions.
- Comments only when they add real value.

## Guardrails — Ask Before Acting

Before any significant change: (1) explain the proposed change, (2) explain why, (3) get approval, (4) then proceed.

Do **not**, without explicit approval:

- Change or refactor existing code without first explaining why.
- Make major architectural changes or replace existing patterns.
- Introduce new dependencies without justification.
- Convert FBVs to CBVs.
- Add tests or testing-related code unless asked.
- Remove existing functionality.
- Assume requirements that weren't stated — if unclear, ask first.

## Reviewing Code

Check for: security issues, ownership/permission gaps, query optimization, maintainability, Django best practices, and frontend consistency. Suggest improvements only when they add meaningful value, and preserve existing conventions.

## Development notes

- `SECRET_KEY` is hardcoded and `DEBUG = True` — this is a local-only development setup.
- No `requirements.txt` is present; the `venv/` directory is the dependency source. When adding packages, install into the venv and document them here or generate a `requirements.txt`.
