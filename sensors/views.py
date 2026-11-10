from django.shortcuts import render, redirect
from .models import Sensor
from .forms import SensorForm

def sensor_list(request):
    # Отримуємо всі датчики з бази даних
    sensors = Sensor.objects.all()
    return render(request, 'sensors/sensor_list.html', {'sensors': sensors})

def add_sensor(request):
    # Обробка форми додавання нового датчика
    if request.method == 'POST':
        form = SensorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sensor_list')
    else:
        form = SensorForm()
    return render(request, 'sensors/add_sensor.html', {'form': form})