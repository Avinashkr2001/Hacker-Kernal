# Online Library System

The Online Library System is a web application for managing a library. Admins can add books and authors, assign books to authors, and export library data to an Excel sheet.

## Features

- Add books and authors.
- Assign books to users.
- Export library data to an Excel sheet.

## Installation

1. **Create a folder and navigate into it:**
   ```sh
   mkdir online-library-system
   cd online-library-system
   git clone https://github.com/Avinashkr2001/Hacker-Kernal.git
   ```
   
2. **Create and activate a virtual environment:**
   ```sh
      python -m venv env
      # On Windows
      .\env\Scripts\activate
      # On macOS and Linux
      source env/bin/activate
   ```
3. **Go to Project Directory:**
   ```sh
   cd project
   ```
    
4. **Install Django and additional dependencies:**
   ```sh
   pip install django
   pip install pandas openpyxl
   ```

   
5. **Initialize Django project:**
   ```sh
     python manage.py makemigrations
     python manage.py migrate
     python manage.py createsuperuser
   ```

6. **Start the development server:**
   ```sh
     python manage.py runserver
   ```





