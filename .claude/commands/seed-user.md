# Seed Users

Create dummy users in the database.

**Usage:** `/seed-user [count]`

---

## Steps

### 1. Read the User Model

Read `todoapp/models.py` and understand the user schema — field names, types, and how users are created via the register method.

### 2. Generate and Insert Users

Write a Python script and run it with Bash (Python 3). Repeat the following for each user, up to `[count]`:

**Generate realistic user data using your own knowledge of common Indian names across regions:**

- **Name:** a realistic Indian first + last name (vary regions — e.g. North, South, West, East India)
- **Email:** derived from the name, lowercase, dot-separated, with a random 2–3 digit number suffix — e.g. `rahul.sharma91@gmail.com`
- **Password:** the string `"password123"` hashed using `werkzeug.security.generate_password_hash`
- **created_at:** current datetime

**Before inserting:**
- Check if the generated email already exists in the `users` table.
- If it does, regenerate the user (new name + email) until the email is unique.

**Insert** the user into the database using the model's register method.

### 3. Print Confirmation

After each successful insert, print:

```
User created:
  ID:    <id>
  Name:  <name>
  Email: <email>
```

---

## Tools

- `read` — read `todoapp/models.py`
- `bash` — run the Python 3 script

## Notes

- Do not modify any project files. Write and run the seed script entirely in memory via Bash.
- Do not use Django's ORM or `manage.py`. Interact with the SQLite database (`db.sqlite3`) directly via Python.
- Use only Python standard library + `werkzeug` for hashing. Do not install any other packages.
- If `werkzeug` is not available, install it into the venv first: `.\venv\Scripts\activate && pip install werkzeug`