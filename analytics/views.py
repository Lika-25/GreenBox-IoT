from django.shortcuts import render, redirect
from datetime import datetime
import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client['GreenBox_Analytics_DB'] 
reports_collection = db['analytics_reports'] 

def analytics_dashboard(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        average_temperature = float(request.POST.get('average_temperature', 0))
        average_humidity = float(request.POST.get('average_humidity', 0))
        avg_soil_moisture = float(request.POST.get('avg_soil_moisture', 0))
        avg_light_level = float(request.POST.get('avg_light_level', 0))
        notes = request.POST.get('notes', '')
        
        if average_temperature > 30.0 or avg_soil_moisture < 20.0:
            plant_health_status = 'danger'
        elif (25.0 < average_temperature <= 30.0) or (20.0 <= avg_soil_moisture < 35.0):
            plant_health_status = 'warning'
        else:
            plant_health_status = 'good'

        new_report = {
            "title": title,
            "created_at": datetime.now(),
            "average_temperature": average_temperature,
            "average_humidity": average_humidity,
            "avg_soil_moisture": avg_soil_moisture,
            "avg_light_level": avg_light_level,
            "plant_health_status": plant_health_status, 
            "notes": notes
        }
        reports_collection.insert_one(new_report)
        return redirect('analytics:dashboard')

    query = {}
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    
    if date_from and date_to:
        query['created_at'] = {'$gte': date_from, '$lte': date_to + ' 23:59:59'}

    reports = list(reports_collection.find(query).sort('_id', -1))

    context = {
        'reports': reports,
    }
    return render(request, 'analytics/analytics_dashboard.html', context)
