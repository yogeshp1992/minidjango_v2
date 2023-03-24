### Django models

- A model is the single, definitive source of information about your data.
- In short model class is your DDL

### django database
- django uses `sqlite3` as default database (shipped along with django)
- `sqlite3` is lightweight database and it is called as in-memory database
- `sqlite3` is typically used for development (not for production)
- If we want to change default database in django...
- We go to settings.py file and update DB engine
- TODO refer - https://docs.djangoproject.com/en/4.1/ref/databases/#mysql-notes
- 


### migrations
- When you add any new table OR alter any existing table...
- `python manage.py makemigrations` (detection)
- `python manage.py migrate` (apply)


### ORM (Object Relational Mapper)
- Flexibility

