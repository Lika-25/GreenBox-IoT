import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client['GreenBox_Sensors_DB'] 
sensors_collection = db['sensors'] 

def print_all_sensors():
    print("\n--- Список датчиків у БД ---")
    for sensor in sensors_collection.find():
        print(sensor)

sensors_collection.delete_many({})

print("Додавання датчиків...")
sensor1 = {"name": "DHT22", "sensor_type": "Температура", "pin": "GPIO 4", "is_active": True}
sensor2 = {"name": "YL-69", "sensor_type": "Вологість ґрунту", "pin": "A0", "is_active": True}
sensor3 = {"name": "BH1750", "sensor_type": "Освітленість", "pin": "I2C", "is_active": False}
sensors_collection.insert_many([sensor1, sensor2, sensor3])

print_all_sensors()

print("\nОновлення: активація датчика BH1750...")
sensors_collection.update_one(
    {"name": "BH1750"}, 
    {"$set": {"is_active": True}}
)
print_all_sensors()

print("\nВидалення датчика YL-69...")
sensors_collection.delete_one({"name": "YL-69"})
print_all_sensors()

print("\nПошук датчика підключеного до GPIO 4:")
specific_sensor = sensors_collection.find_one({"pin": "GPIO 4"})
print(specific_sensor)