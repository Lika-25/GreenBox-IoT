import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client['GreenBox_Analytics_DB'] 
reports_collection = db['analytics_reports'] 

def print_all_reports():
    print("\n--- Список аналітичних звітів у БД ---")
    for report in reports_collection.find():
        print(report)

reports_collection.delete_many({})

print("Додавання аналітичних звітів...")
report1 = {
    "title": "Ранковий звіт фітобокса", 
    "average_temperature": 23.5, 
    "average_humidity": 65.0, 
    "avg_soil_moisture": 45.2,
    "avg_light_level": 1200.0,
    "plant_health_status": "good",
    "notes": "Стабільні показники, ріст активний."
}
report2 = {
    "title": "Вечірній звіт фітобокса", 
    "average_temperature": 28.1, 
    "average_humidity": 50.0, 
    "avg_soil_moisture": 28.5,
    "avg_light_level": 800.0,
    "plant_health_status": "warning",
    "notes": "Зафіксовано підвищення температури та зниження вологості ґрунту."
}
reports_collection.insert_many([report1, report2])

print_all_reports()

print("\nОновлення вечірнього звіту (зміна статусу на 'Критично' після поливу)...")
reports_collection.update_one(
    {"title": "Вечірній звіт фітобокса"}, 
    {"$set": {
        "plant_health_status": "danger", 
        "notes": "Ґрунт пересушено, терміново активовано систему поливу."
    }}
)
print_all_reports()

print("\nВидалення ранкового звіту...")
reports_collection.delete_one({"title": "Ранковий звіт фітобокса"})
print_all_reports()

print("\nПошук звітів із критичним статусом ('danger'):")
critical_report = reports_collection.find_one({"plant_health_status": "danger"})
print(critical_report)
