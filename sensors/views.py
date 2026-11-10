from django.shortcuts import render, redirect
from .models import Sensor
from .forms import SensorForm
import pymongo

def sensor_list(request):
    client = pymongo.MongoClient('localhost', 27017)
    db = client['GreenBox_Sensors_DB']
    sensors_collection = db['sensors']
    
    sensors = list(sensors_collection.find())
    
    return render(request, 'sensors/sensor_list.html', {'sensors': sensors})

def add_sensor(request):
    if request.method == 'POST':
        form = SensorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sensor_list')
    else:
        form = SensorForm()
    
    return render(request, 'sensors/add_sensor.html', {'form': form})