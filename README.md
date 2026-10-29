# Django Practice 🐍

A comprehensive, hands-on repository demonstrating daily Django practice, core concepts, design patterns, and progressive feature development.

Author: **[Gagana C P](https://github.com/gaganagana)**

---

## 📌 Architecture & Modules Overview

This repository demonstrates complete mastery of Django web architecture:

```text
django-practice/
├── learning/              # Core Django project settings & URL configuration
│   ├── settings.py       # Configured with custom apps, templates, and middleware
│   ├── urls.py           # Global URL dispatcher
│   ├── wsgi.py / asgi.py # Deployment handlers
├── notes/                 # Production-ready Notes & Productivity app
│   ├── models.py         # Category & Note models (priorities, slug, indexes, methods)
│   ├── views.py          # Both Function-Based Views (FBV) and Generic Class-Based Views (CBV)
│   ├── forms.py          # ModelForms with custom clean validation methods
│   ├── admin.py          # Custom ModelAdmin with search, filters, and batch actions
│   ├── urls.py           # Modular route definitions and reverse lookup patterns
│   ├── signals.py        # Django post_save and post_delete signal handlers
│   ├── templatetags/     # Custom template filters (priority_badge, reading_time)
│   ├── management/       # Custom manage.py commands ('notes_summary')
│   └── tests.py          # Automated unit testing suite for models, forms, and views
└── templates/             # Responsive Bootstrap 5 user interface
    ├── base.html         # Master layout template with navbar, flash alerts, and footer
    └── notes/            # CRUD templates (list, detail, form, confirm_delete)
```

---

## 🚀 Key Django Concepts Practiced

| Topic | Implementation Details |
|---|---|
| **Models & ORM** | Normalized `Category` and `Note` models, Foreign Keys, custom `__str__`, `get_absolute_url`, summary properties, DB indexes |
| **Django Admin** | Custom `ModelAdmin` classes with search fields, list filters, list editable fields, date hierarchy, and bulk actions |
| **Forms & Validation** | `ModelForm` with custom Bootstrap widget styling and custom `clean_title()` validation rules |
| **Class-Based Views** | Generic `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView` with `SuccessMessageMixin` |
| **Function-Based Views** | Explicit request-response cycle handling and manual template rendering for educational clarity |
| **Search & Filtering** | Dynamic QuerySet filtering using Django `Q` objects (`Q(title__icontains=q) \| Q(content__icontains=q)`) |
| **Template Engine** | Template inheritance, custom template tag filters (`priority_badge`, `reading_time`), responsive layout |
| **Signals** | Asynchronous decoupled event listening via `@receiver(post_save)` and `post_delete` |
| **Unit Testing** | `TestCase` suite testing model properties, form validation edges, and HTTP status codes |
| **JSON API** | Lightweight REST endpoints returning JSON responses for decoupled consumers |
| **Management CLI** | Custom `python manage.py notes_summary` command |

---

## 🛠️ Getting Started

### 1. Clone & Set Up Virtual Environment

```bash
git clone https://github.com/gaganagana/django-practice.git
cd django-practice
python -m venv env
# Windows:
.\env\Scriptsctivate
# Linux/macOS:
source env/bin/activate
pip install django
```

### 2. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Run Automated Tests

```bash
python manage.py test notes
```

### 4. Run Custom Management Command

```bash
python manage.py notes_summary
```

### 5. Launch Development Server

```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

---

## 📜 License
MIT License. Created for daily software engineering practice and continuous learning.
