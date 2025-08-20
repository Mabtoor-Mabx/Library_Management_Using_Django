
# 📚 Library_Management_Using_Django

A simple **Library Management System** built with Django that demonstrates the use of **Model Relations (One-to-Many: Author → Books)** and **Forms (ModelForm)** for creating and managing records.

---

## 📂 Project Structure

```
Library_Management_Using_Django/
│── library_project/          # Main project folder
│   │── settings.py           # Project settings
│   │── urls.py               # Global URL configurations
│   │── wsgi.py
│   │── asgi.py
│
│── library_app/              # Main application
│   │── migrations/           # Database migrations
│   │── templates/            # HTML templates
│   │   │── author_list.html  # List of authors and books
│   │   │── add_book.html     # Form to add a new book
│   │── models.py             # Database models (Author, Book)
│   │── forms.py              # Django forms (BookForm)
│   │── views.py              # Views (author list, add book)
│   │── urls.py               # App URL configurations
│   │── admin.py              # Register models in admin
│
│── manage.py                 # Django management script
│── README.md                 # Project documentation
```

---

## ⚙️ Important Libraries & Dependencies

* **Django** – Web framework
* **SQLite3** – Default database (can be changed to PostgreSQL/MySQL)
* **Bootstrap (optional)** – For styling templates
* **Python 3.x**

Install dependencies:

```bash
pip install django
```

---

## 🚀 How Project Works

1. **Author Model** → Stores author details.
2. **Book Model** → Stores books with a `ForeignKey` relation to Author.
3. **Forms (ModelForm)** → Used to add new books linked to authors.
4. **Views** →

   * `author_list` → Displays authors and their books.
   * `add_book` → Provides form to add a new book.
5. **Templates** → Simple HTML pages to render forms and display data.
6. **Admin Panel** → Manage Authors & Books quickly.

---

## 🔄 Project Workflow

1. **Create & Apply Migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
2. **Create Superuser** (to manage authors in admin panel)

   ```bash
   python manage.py createsuperuser
   ```
3. **Run Server**

   ```bash
   python manage.py runserver
   ```
4. **Add Authors** via Admin (`/admin/`).
5. **Add Books** via `/add-book/` form.
6. **View Authors & Books** via `/`.

---

## 📑 Example Features

* **Author → Books (One-to-Many Relation)**
* **Add Book Form** (Django ModelForm with Date Picker)
* **Author List Page** shows all books per author
* **Admin Panel Support** for easy management
* **HTML Templates** with CSRF protection

---

## 🖥️ Screenshots (Optional)

* `author_list.html` → Displays all authors with their books.
* `add_book.html` → Form to add a new book with an HTML5 date picker.

---

## 🔧 Future Enhancements

* Add **CRUD (Update/Delete)** for books.
* Add **Many-to-Many Relation** (e.g., Student ↔ Courses).
* Add **Search & Filters** (search books by title, filter by author).
* Add **Bootstrap styling** for modern UI.

---

## 📌 Summary

This project is a **beginner-friendly Django application** to understand:
✔️ **Model Relations (ForeignKey)**
✔️ **Forms (ModelForm)**
✔️ **Views & Templates**
✔️ **Admin Panel Integration**

It can serve as a **base project** for building a more complete Library Management System.


