import logging
from faker import Faker
import random
import psycopg2
from psycopg2 import DatabaseError

fake = Faker()

# Налаштування підключення до бази даних
conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="goit")
cur = conn.cursor()

# Створення статусів
status_names = ['new', 'in progress', 'completed']
for name in status_names:
    cur.execute("INSERT INTO status (name) VALUES (%s) ON CONFLICT (name) DO NOTHING", (name,))

# Створення користувачів
for _ in range(10):
    cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fake.name(), fake.unique.email()))

# Створення завдань
for _ in range(20):
    title = fake.sentence(nb_words=6)
    description = fake.text(max_nb_chars=200)
    status_id = random.randint(1, 3)  # Припускаємо, що є 3 статуси
    user_id = random.randint(1, 10)   # Припускаємо, що створено 10 користувачів
    cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                (title, description, status_id, user_id))

try:
    # Збереження змін
    conn.commit()
except DatabaseError as e:
    logging.error("Database error occurred: {}".format(e))
    conn.rollback()
finally:
    # Закриття підключення
    cur.close()
    conn.close()
