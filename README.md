# vagadiya_exim_backend

## Steps to install

1. Clone the repository

```bash
git clone https://github.com/abhishek-vagadiya/vagadiya_exim_backend.git
cd vagadiya_exim_backend
```

2. Create virtual environment(Optional but recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux
. venv/bin/activate
```

3. Install requirements

```bash
pip install -r requirements.txt
```

4. Run server

```bash
python manage.py runserver
```

5. Open http://127.0.0.1:8000 in browser

6. If new database is created

```bash
python manage.py makemigrations
python manage.py migrate
```

7. To access admin panel, create superuser

```bash
python manage.py createsuperuser
```
