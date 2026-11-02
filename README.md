# Розумна тепличка (Фітобокс) - Проєкт IoT

Цей проєкт є веб-додатком для моніторингу та управління параметрами розумної теплиці. Розроблено в рамках лабораторних робіт з дисципліни «Проєктування та моделювання IoT-систем».

## 🏗️ Архітектура рішення
Система побудована за архітектурою MTV (Model-Template-View) на базі Django. 
Серверна частина розгорнута за допомогою стеку: Django, uWSGI, Supervisor, Nginx.

## 👥 Розподіл ролей у команді
*   **Анжеліка** — базовий каркас, налаштування серверної частини, загальний інтерфейс та моделі.
*   **Микола** — розробка модуля датчиків (sensors).
*   **Ірина** — розробка модуля аналітики (analytics).
*   **Роман** — розробка модуля безпеки (security).

---

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

## 🎥 Відео-демонстрація
*   **Лабораторна робота 1 (Анжеліка):** [Посилання на відео]
*   **Лабораторна робота 1 (Микола):** [Посилання на відео]
*   **Лабораторна робота 1 (Ірина):** [Посилання на відео]
*   **Лабораторна робота 1 (Роман):** [Посилання на відео]
