# Розумна тепличка (Фітобокс) - Проєкт IoT

Цей проєкт є веб-додатком для моніторингу та управління параметрами розумної теплиці. Розроблено в рамках лабораторних робіт з дисципліни «Проєктування та моделювання IoT-систем».

## 🏗️ Архітектура рішення
Система побудована за архітектурою MTV (Model-Template-View) на базі Django. 
Серверна частина розгорнута за допомогою стеку: Django, uWSGI, Supervisor, Nginx.

## ⚙️ Керівництво програміста (Як запустити)

Існує два способи запуску проєкту. 

### Варіант 1: Швидкий запуск (Перевірка працездатності)
Цей спосіб не потребує налаштування серверів і підходить для будь-якої ОС.

1. Клонуйте репозиторій та перейдіть у папку:
   ```bash
   git clone https://github.com/Lika-25/GreenBox.git
   cd GreenBox
2. Створіть віртуальне середовище та встановіть залежності:
   ```bash
   python3 -m venv env
   source env/bin/activate  # Для Windows: env\Scripts\activate
   pip install -r requirements.txt
3. Виконайте міграції бази даних:
   ```bash
   python manage.py migrate
4. Запустіть сервер розробки:
   ```bash
   python manage.py runserver
Додаток буде доступний за адресою: http://127.0.0.1:8000/

### Варіант 2: Production-запуск (через Nginx та uWSGI)
Увага! Цей спосіб вимагає Linux-середовища.

**Перед запуском обов'язково відредагуйте шляхи у файлах конфігурації!**
У файлах uwsgi.ini та deploy/supervisor_greenbox.conf замініть /path/to/your/project/GreenBox на ваш реальний шлях до папки з проєктом.

1. Запуск uWSGI:
   ```bash
   uwsgi --ini uwsgi.ini
(Зупинити: Ctrl+C)

2. Налаштування Supervisor:
   ```bash
   sudo cp deploy/supervisor_greenbox.conf /etc/supervisor/conf.d/greenbox.conf
   sudo supervisorctl reread
   sudo supervisorctl update
   sudo supervisorctl start greenbox
3. Налаштування Nginx:
   ```bash
   sudo cp deploy/nginx_greenbox.conf /etc/nginx/sites-available/greenbox
   sudo ln -s /etc/nginx/sites-available/greenbox /etc/nginx/sites-enabled/
   sudo rm /etc/nginx/sites-enabled/default
   sudo nginx -t
   sudo service nginx restart
  
Додаток буде доступний за адресою: `http://localhost:9000/`

## 📊 Лабораторна робота 1: Створення проєкту Django

### 👥 Розподіл завдань у команді Л1
*   **Анжеліка** — базовий каркас, налаштування серверної частини, загальний інтерфейс та моделі.
*   **Микола** — розробка модуля датчиків (sensors).
*   **Ірина** — розробка модуля аналітики (analytics).
*   **Роман** — розробка модуля безпеки (security).

### 🎥 Відео-демонстрація
*   **Лабораторна робота 1 (Анжеліка):** [Посилання на відео](https://youtu.be/n1K6-OzKbkU?si=Lq46PClZI6sj6f_L)
*   **Лабораторна робота 1 (Микола):** [Посилання на відео](https://youtu.be/429vZummelk?si=gDVx_Cz0h38R0Kup)
*   **Лабораторна робота 1 (Ірина):** [Посилання на відео](https://youtu.be/s9_31AZQcGI?si=dP4EtxNofKW9vmPq)
*   **Лабораторна робота 1 (Роман):** [Посилання на відео](https://youtu.be/rjY7RclCRqQ)



## 📊 Лабораторна робота 2: Зберігання IoT-даних у базах даних NoSQL (MongoDB)

У ході виконання лабораторної роботи №2 до проєкту було додано нереляційну базу даних **MongoDB** (за допомогою драйвера `PyMongo`) для зберігання різних типів даних системи.

### 👥 Розподіл завдань у команді Л2 та сторінки для перевірки:

*   **Анжеліка (БД користувачів):** 👉 [http://localhost:9000/users/](http://localhost:9000/users/)
*   **Микола (БД обладнання):** 👉 [http://localhost:9000/sensors/](http://localhost:9000/sensors/)
*   **Ірина (БД методів аналізу):** 👉 [http://localhost:9000/analytics/](http://localhost:9000/analytics/)
*   **Роман (БД кіберпогроз):** 👉 [http://localhost:9000/security/](http://localhost:9000/security/)

### ⚙️ Керівництво програміста (Як запустити на прикладі БД користувачів):

1. Переконайтеся, що MongoDB запущена
(наприклад: `sudo mongod --dbpath ~/data/db --fork --logpath ~/data/db/mongod.log`).

2. Запустіть скрипти для наповнення баз даних (у корені проєкту).
Кожен учасник розробив свій скрипт для відповідного модуля:
   ```bash
   python mongo_users.py      # Для БД користувачів (Анжеліка)
   python mongo_sensors.py    # Для БД обладнання (Микола)
   python mongo_analytics.py  # Для БД аналізу (Ірина)
   python mongo_security.py   # Для БД кіберзагроз (Роман)

3. Перейдіть за посиланнями зі списку вище (наприклад, /users/), щоб побачити дані з MongoDB у веб-інтерфейсі.

## 🎥 Відео-демонстрація
*   **Лабораторна робота 2 (Анжеліка):** [Посилання на відео]
*   **Лабораторна робота 2 (Микола):** [Посилання на відео]
*   **Лабораторна робота 2 (Ірина):** [Посилання на відео](https://youtu.be/zhcvyaFTW5Q)
*   **Лабораторна робота 2 (Роман):** [Посилання на відео]

