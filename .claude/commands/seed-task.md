# Seed Tasks

Seed realistic dummy tasks for a specific user.

**Usage:** `/seed-task <user_id> <count>`

**User input:** $ARGUMENTS

**Allowed tools:** Read, Bash (python3:*)

---

## Step 1 — Parse Arguments

Extract from `$ARGUMENTS`:

- `user_id` — integer
- `count` — integer, number of tasks to create

If any argument is missing or not a valid integer, stop and print:

```
Usage: /seed-task <user_id> <count>
Example: /seed-task 1 50
```

---

## Step 2 — Verify User Exists

Before generating anything, confirm the `user_id` exists in the users table.

If not, stop and print:

```
No user found with id <user_id>.
```

---

## Step 3 — Generate and Insert Tasks

### 3a. Read the Model

Read `todoapp/models.py` and identify every field on the `Task` model.

Before generating any data, verify that the following fields are present on the model:

- `title`
- `description`
- `category`
- `priority`
- `status`
- `created_date`
- `due_date`

If any field is missing, stop and print:

```
Error: The following required fields are missing from the Task model: <field_name>, <field_name>
```

### 3b. Write and Run the Script

Write a Django script and execute it via `manage.py shell`. The script must:

**Use Django ORM exclusively** — do not create a separate database connection or hardcode any database configuration. Access the database through Django's ORM (`create()`, `bulk_create()`, etc.) and project settings only.

**Wrap all inserts in a single `transaction.atomic()` block** — if any task creation fails, all changes are rolled back.

**Generate realistic task data:**

- **Categories** — use the list below, distributed roughly proportionally (Work most common; Health and Finance least common):

  | Category | Relative frequency |
  |----------|--------------------|
  | Work     | Most common        |
  | Personal | Common             |
  | Study    | Common             |
  | Shopping | Moderate           |
  | Other    | Moderate           |
  | Health   | Least common       |
  | Finance  | Least common       |

- **Title** — realistic task title matching the category (e.g. "Review Q3 report" for Work, "Buy weekly groceries" for Shopping)
- **Description** — a short, realistic description matching the title
- **Priority** — randomized across `Low`, `Medium`, `High`
- **Status** — randomized across `Pending`, `In Progress`, `Completed`
- **Created date** — randomly distributed across the past several months
- **Due date** — a realistic future or near-past date relative to the created date

---

## Step 4 — Confirm

After all inserts complete, print:

```
Seeded <count> tasks for user ID <user_id>.

Sample (5 records):
  1. [id] | <title> | <category> | <priority> | <status> | due: <due_date>
  2. [id] | <title> | <category> | <priority> | <status> | due: <due_date>
  3. [id] | <title> | <category> | <priority> | <status> | due: <due_date>
  4. [id] | <title> | <category> | <priority> | <status> | due: <due_date>
  5. [id] | <title> | <category> | <priority> | <status> | due: <due_date>
```