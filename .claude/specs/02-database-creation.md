# Task Model Specification

**Workflow:** Create model → Create ModelForm → Register in `admin.py`
**Do not do anything else.**

---

## Model

Create a `Task` model in `todoapp/models.py` with the following fields:

| Field        | Type                                              |
|--------------|---------------------------------------------------|
| Title        | `CharField`                                       |
| Description  | `TextField`                                       |
| Category     | `CharField`                                       |
| Priority     | `CharField` — choices: `Low`, `Medium`, `High`    |
| Status       | `CharField` — choices: `Pending`, `In Progress`, `Completed` |
| Created date | `DateTimeField` — auto-set on creation            |
| Due date     | `DateField`                                       |

---

## ModelForm

Create a `TaskForm` using `ModelForm` in `todoapp/forms.py` that includes all the fields above.

---

## Admin

Register the `Task` model in `todoapp/admin.py`.

---

## Acceptance Criteria

- [ ] `Task` model is defined in `todoapp/models.py` with all seven fields.
- [ ] `Priority` field is restricted to choices: `Low`, `Medium`, `High`.
- [ ] `Status` field is restricted to choices: `Pending`, `In Progress`, `Completed`.
- [ ] `Created date` is auto-set on creation — not manually editable.
- [ ] Migration is created and applied without errors.
- [ ] `TaskForm` is a `ModelForm` and includes all seven fields.
- [ ] `Task` model is registered in `admin.py` and visible in the Django admin panel.
- [ ] No views, URLs, or templates are created or modified.