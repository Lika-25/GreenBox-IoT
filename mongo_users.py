import pymongo

# 1. Підключення до MongoDB
client = pymongo.MongoClient('localhost', 27017)
db = client['GreenBox_Users_DB'] # Наша база даних
users_collection = db['users']    # Колекція користувачів

def print_all_users():
    print("\n--- Список користувачів у БД ---")
    for user in users_collection.find():
        print(user)

# Очищаємо БД перед тестом (щоб не дублювалося при повторному запуску)
users_collection.delete_many({})

# 2. CREATE (Створення документів)
print("Додавання користувачів...")
user1 = {"name": "Анжеліка", "role": "Admin", "email": "anzhelika@greenbox.com"}
user2 = {"name": "Микола", "role": "Operator", "email": "mykola@greenbox.com"}
users_collection.insert_many([user1, user2])

# 3. READ (Отримання даних)
print_all_users()

# 4. UPDATE (Оновлення - зміна ролі Миколи)
print("\nОновлення ролі Миколи на 'Main Operator'...")
users_collection.update_one(
    {"name": "Микола"}, 
    {"$set": {"role": "Main Operator"}}
)
print_all_users()

# 5. DELETE (Видалення - видаляємо Анжеліку)
print("\nВидалення користувача Анжеліка...")
users_collection.delete_one({"name": "Анжеліка"})
print_all_users()

# 6. READ (Пошук конкретного користувача)
print("\nПошук користувача з роллю 'Main Operator':")
operator = users_collection.find_one({"role": "Main Operator"})
print(operator)