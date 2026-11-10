from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["GreenBox_Users_DB"]          # база даних проєкту
threats_col = db["cyber_threats"]   # база кіберпогроз

print("=== Очищення старих даних ===")
threats_col.delete_many({})

print("\n=== Додавання загроз ===")
initial_threats = [
    {
        "threat_id": "THR-001",
        "name": "MQTT MitM Traffic Sniffing",
        "category": "network_attack",
        "severity": "high",
        "vector": "Перехоплення телеметричного трафіку брокера без TLS",
        "target_node": "Edge Gateway",
        "status": "active",
        "created_at": datetime.now()
    },
    {
        "threat_id": "THR-002",
        "name": "Sensor Data Spoofing",
        "category": "data_integrity",
        "severity": "critical",
        "vector": "Ін'єкція фейкових значень вологості та температури",
        "target_node": "ESP32 Sensor Bus",
        "status": "active",
        "created_at": datetime.now()
    },
    {
        "threat_id": "THR-003",
        "name": "API Token Brute-force",
        "category": "unauthorized_access",
        "severity": "medium",
        "vector": "Підбір авторизаційного токена локального Edge-сервера",
        "target_node": "REST API Controller",
        "status": "active",
        "created_at": datetime.now()
    },
    {
        "threat_id": "THR-004",
        "name": "UART Debug Tampering",
        "category": "physical_tampering",
        "severity": "low",
        "vector": "Підключення до відлагоджувального порту мікроконтролера",
        "target_node": "Hardware Board",
        "status": "neutralized",
        "created_at": datetime.now()
    }
]

result = threats_col.insert_many(initial_threats)
print(f"Успішно додано загроз: {len(result.inserted_ids)}")

print("\n=== Виведення всіх загроз ===")
for threat in threats_col.find():
    print(f"[{threat.get('threat_id')}] {threat.get('name')} | Рівень: {threat.get('severity')} | Статус: {threat.get('status')}")

print("\n=== Оновлення статусу ===")

threats_col.update_one(
    {"threat_id": "THR-001"},
    {"$set": {"status": "neutralized", "mitigation": "Увімкнено шифрування TLS v1.3"}}
)
updated = threats_col.find_one({"threat_id": "THR-001"})
print(f"Оновлено: {updated.get('name')} -> Новий статус: {updated.get('status')}")

print("\n=== Видалення ===")
threats_col.delete_one({"threat_id": "THR-004"})
print("Загрозу THR-004 видалено з бази.")

print("\n=== Загрози в БД ===")
for threat in threats_col.find():
    print(f"[{threat.get('threat_id')}] {threat.get('name')} | Рівень: {threat.get('severity')} | Статус: {threat.get('status')}")