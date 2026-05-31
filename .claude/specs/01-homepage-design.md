# Home Page Design Specification
 
**File:** `templates/todoapp/todo.html`
 
> **Important:** Do not add any new business logic, backend functionality, JavaScript behavior, or workflow changes. Only update the UI/layout based on the requirements below.
 
---
 
## Design Goals
 
- Simple and clean interface
- Minimal, modern layout
- Easy to scan and use
- Responsive design
---
 
## Tech Constraints
 
- Tailwind CSS only — no custom CSS files, no `<style>` blocks
- Vanilla JS only — no external JS libraries
- No changes to any view, model, form, URL, or backend file
- Only `templates/todoapp/todo.html` is modified
---
 
## Page Components
 
### 1. Header
- Display a page title at the top (e.g. "My Tasks" or similar).
- Keep it simple — no navigation, no extra controls.
### 2. Search Bar
- Positioned prominently below the header, above the task table.
- Used for searching/filtering tasks by name.
- Full-width or appropriately wide input field.
### 3. Add Task Button
- Positioned near the search bar (same row or directly adjacent).
- Clearly visible, easy to access.
- Label: "Add Task".
### 4. Current Tasks Table
Display all current tasks in a structured table.
 
#### Columns
 
| Column     | Description                              |
|------------|------------------------------------------|
| Task Name  | Name/title of the task                   |
| Created At | Date and time the task was created       |
| Actions    | Action buttons for the task              |
 
#### Actions Column
Each row includes two action buttons:
- **Finish**
- **Delete**
Buttons should be visually distinct from each other (e.g. different colors or styles).
 
---
 
## Layout Structure
 
Render the page components in this top-to-bottom order:
 
1. Header / page title
2. Search bar + Add Task button
3. Current Tasks table
---
 
## Visual & Styling Requirements
 
- Consistent spacing and alignment throughout the page.
- Clear visual hierarchy between sections.
- Table rows should be easy to scan (use alternating row shading or clear row borders).
- Action buttons should be compact and not disrupt the table layout.
- The layout must be responsive — usable on both mobile and desktop screen sizes.
- Overall style must be consistent with `register.html` and `login.html`.
---
 
## Acceptance Criteria
 
- [ ] Only `templates/todoapp/todo.html` is modified — no changes to views, models, forms, or URLs.
- [ ] The page renders without errors.
- [ ] Page title/header is visible at the top.
- [ ] A search bar is displayed above the task table.
- [ ] An "Add Task" button is displayed near the search bar.
- [ ] A task table is displayed with columns: Task Name, Created At, Actions.
- [ ] Each row in the Actions column contains a "Finish" button and a "Delete" button.
- [ ] "Finish" and "Delete" buttons are visually distinct from each other.
- [ ] The layout follows the specified top-to-bottom order: header → search + button → table.
- [ ] The page is responsive and displays correctly on mobile and desktop.
- [ ] Tailwind CSS only is used — no custom CSS files, no `<style>` blocks.
- [ ] Vanilla JS only — no external JS libraries introduced.
- [ ] No backend logic, JavaScript behavior, or workflow is added or changed.
- [ ] Visual style is consistent with `register.html` and `login.html`.