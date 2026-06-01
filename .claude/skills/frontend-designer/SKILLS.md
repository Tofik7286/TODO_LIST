---
name: frontend-design
description: Design system and UI component guide for the TodoApp Django project. Use this skill whenever building or updating any template in todoapp/templates/todoapp/ — including new pages, forms, tables, flash messages, auth pages, profile pages, task pages, or any UI component. Must be consulted before writing any template HTML. Ensures Tailwind-only styling, vanilla JS, and visual consistency across register.html, login.html, todo.html, add_task.html, and profile.html.
---

# Frontend Design — TodoApp

This skill defines the design system, component patterns, and layout rules for all templates in the project. Read this before writing any template. The goal is a clean, simple, modern UI that is consistent across every page.

## Hard Constraints

- **Tailwind CSS only** — no custom CSS files, no `<style>` blocks, no inline `style=` attributes
- **Vanilla JS only** — no jQuery, no Alpine, no HTMX, no external JS libraries
- **Semantic HTML** — use correct elements (`<nav>`, `<main>`, `<section>`, `<form>`, `<button>`, etc.)
- **Responsive** — every page must work on mobile and desktop
- **No hardcoded hex values** — use only Tailwind palette classes

---

## Color System

| Role              | Tailwind class(es)                              |
|-------------------|-------------------------------------------------|
| Page background   | `bg-gray-50`                                    |
| Surface / card    | `bg-white`                                      |
| Border            | `border-gray-200`                               |
| Primary text      | `text-gray-900`                                 |
| Secondary text    | `text-gray-600`                                 |
| Muted / hint      | `text-gray-400`                                 |
| Primary action    | `bg-blue-600 hover:bg-blue-700`                 |
| Danger action     | `bg-red-600 hover:bg-red-700`                   |
| Focus ring        | `focus:ring-2 focus:ring-blue-500`              |
| Success message   | `bg-green-50 border-green-200 text-green-800`   |
| Error message     | `bg-red-50 border-red-200 text-red-800`         |

---

## Typography

| Role           | Classes                                         |
|----------------|-------------------------------------------------|
| Page title     | `text-2xl font-bold text-gray-900`              |
| Section header | `text-lg font-semibold text-gray-900`           |
| Form label     | `block text-sm font-medium text-gray-700 mb-1`  |
| Body text      | `text-sm text-gray-600`                         |
| Muted text     | `text-sm text-gray-400`                         |
| Link           | `text-blue-600 hover:text-blue-800 font-medium` |

---

## Layout Patterns

### Auth Pages (login, register)
Centered card on a gray background. No header or nav.

```html
<body class="min-h-screen bg-gray-50 flex items-center justify-center px-4">
  <div class="w-full max-w-md">
    <div class="bg-white rounded-2xl shadow-sm border border-gray-200 p-8">
      <!-- page title -->
      <h1 class="text-2xl font-bold text-gray-900 mb-2">Title</h1>
      <p class="text-sm text-gray-500 mb-6">Subtitle</p>
      <!-- form -->
    </div>
  </div>
</body>
```

### App Pages (todo, add_task, profile)
Full-width header + centered content area.

```html
<body class="min-h-screen bg-gray-50">
  <!-- Header -->
  <header class="bg-white border-b border-gray-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
      <h1 class="text-lg font-semibold text-gray-900">TodoApp</h1>
      <!-- right side: user name / logout -->
    </div>
  </header>

  <!-- Content -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- page content -->
  </main>
</body>
```

### Form Pages (add_task, profile)
Narrower content card centered within the app layout.

```html
<main class="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
  <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
    <!-- form -->
  </div>
</main>
```

---

## Components

### Buttons

**Primary:**
```html
<button class="inline-flex items-center px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white text-sm font-medium rounded-lg transition-colors duration-150 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
  Label
</button>
```

**Secondary / Cancel:**
```html
<button class="inline-flex items-center px-4 py-2 bg-white hover:bg-gray-50 text-gray-700 text-sm font-medium rounded-lg border border-gray-300 transition-colors duration-150 focus:outline-none focus:ring-2 focus:ring-gray-300 focus:ring-offset-2">
  Cancel
</button>
```

**Danger (Delete):**
```html
<button class="inline-flex items-center px-4 py-2 bg-red-600 hover:bg-red-700 text-white text-sm font-medium rounded-lg transition-colors duration-150 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2">
  Delete
</button>
```

**Small inline action:**
```html
<button class="text-sm font-medium text-blue-600 hover:text-blue-800 transition-colors">Finish</button>
```

---

### Form Fields

**Text input / email / password:**
```html
<div>
  <label class="block text-sm font-medium text-gray-700 mb-1">Label</label>
  <input type="text" class="w-full px-3 py-2 border border-gray-300 rounded-lg text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors">
  <!-- error state: replace border-gray-300 with border-red-400 and ring-blue-500 with ring-red-500 -->
</div>
```

**Select (dropdown):**
```html
<select class="w-full px-3 py-2 border border-gray-300 rounded-lg text-sm text-gray-900 bg-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors">
  <option>Option</option>
</select>
```

**Textarea:**
```html
<textarea rows="3" class="w-full px-3 py-2 border border-gray-300 rounded-lg text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors resize-none"></textarea>
```

**Field-level error message:**
```html
<p class="mt-1 text-xs text-red-600">Error message here.</p>
```

---

### Flash Messages (Django messages framework)

Place directly below the header, above page content.

**Success:**
```html
<div class="bg-green-50 border border-green-200 text-green-800 text-sm px-4 py-3 rounded-lg flex items-center justify-between">
  <span>{{ message }}</span>
  <button onclick="this.parentElement.remove()" class="text-green-600 hover:text-green-800 ml-4">✕</button>
</div>
```

**Error:**
```html
<div class="bg-red-50 border border-red-200 text-red-800 text-sm px-4 py-3 rounded-lg flex items-center justify-between">
  <span>{{ message }}</span>
  <button onclick="this.parentElement.remove()" class="text-red-600 hover:text-red-800 ml-4">✕</button>
</div>
```

---

### Task Table

```html
<div class="overflow-hidden rounded-xl border border-gray-200">
  <table class="min-w-full divide-y divide-gray-200">
    <thead class="bg-gray-50">
      <tr>
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Task Name</th>
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Created At</th>
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
      </tr>
    </thead>
    <tbody class="bg-white divide-y divide-gray-100">
      <tr class="hover:bg-gray-50 transition-colors">
        <td class="px-6 py-4 text-sm text-gray-900">Task title</td>
        <td class="px-6 py-4 text-sm text-gray-500">Jan 1, 2025</td>
        <td class="px-6 py-4 text-sm flex gap-3">
          <!-- action buttons -->
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

---

### Badges (Priority & Status)

```html
<!-- Priority -->
<span class="bg-green-100 text-green-700 text-xs font-medium px-2.5 py-0.5 rounded-full">Low</span>
<span class="bg-yellow-100 text-yellow-700 text-xs font-medium px-2.5 py-0.5 rounded-full">Medium</span>
<span class="bg-red-100 text-red-700 text-xs font-medium px-2.5 py-0.5 rounded-full">High</span>

<!-- Status -->
<span class="bg-gray-100 text-gray-700 text-xs font-medium px-2.5 py-0.5 rounded-full">Pending</span>
<span class="bg-blue-100 text-blue-700 text-xs font-medium px-2.5 py-0.5 rounded-full">In Progress</span>
<span class="bg-green-100 text-green-700 text-xs font-medium px-2.5 py-0.5 rounded-full">Completed</span>
```

---

### Search Bar

```html
<div class="relative">
  <svg class="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-4.35-4.35M17 11A6 6 0 1 1 5 11a6 6 0 0 1 12 0z"/>
  </svg>
  <input type="text" placeholder="Search tasks..." class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors">
</div>
```

---

### Avatar (Static — same for all users)

```html
<div class="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center">
  <svg class="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M16 7a4 4 0 1 1-8 0 4 4 0 0 1 8 0zM12 14a7 7 0 0 0-7 7h14a7 7 0 0 0-7-7z"/>
  </svg>
</div>
```

---

## Spacing Rules

- Between form fields: `space-y-4`
- Between sections: `space-y-6` or `mt-8`
- Card padding: `p-6` (standard) or `p-8` (auth cards)
- Button group gap: `gap-3`
- Table action gap: `gap-3`

## Consistency Checklist

Before finishing any template, verify:

- [ ] Page background is `bg-gray-50`
- [ ] All surfaces/cards use `bg-white rounded-xl border border-gray-200`
- [ ] All inputs follow the standard field pattern with focus ring
- [ ] All primary buttons use `bg-blue-600 hover:bg-blue-700`
- [ ] Flash messages use the correct color pattern
- [ ] Layout matches the correct pattern (auth vs app vs form page)
- [ ] No custom CSS, no `<style>` blocks, no inline styles
- [ ] No external JS libraries
- [ ] Page is responsive