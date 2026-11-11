from django.shortcuts import render, redirect
from datetime import datetime
import pymongo
from .forms import AnalyticsFilterForm, AnalyticsReportForm

client = pymongo.MongoClient('localhost', 27017)
db = client['GreenBox_Analytics_DB'] 
reports_collection = db['analytics_reports'] 

def analytics_dashboard(request):
    filter_form = AnalyticsFilterForm(request.GET or None)
    report_form = AnalyticsReportForm(request.POST or None)

    if request.method == 'POST' and report_form.is_valid():
        cleaned_data = report_form.cleaned_data
        
        average_temperature = cleaned_data['average_temperature']
        avg_soil_moisture = cleaned_data['avg_soil_moisture']
        
        if average_temperature > 30.0 or avg_soil_moisture < 20.0:
            plant_health_status = 'danger'
        elif (25.0 < average_temperature <= 30.0) or (20.0 <= avg_soil_moisture < 35.0):
            plant_health_status = 'warning'
        else:
            plant_health_status = 'good'

        new_report = {
            "title": cleaned_data['title'],
            "created_at": datetime.now(),
            "average_temperature": average_temperature,
            "average_humidity": cleaned_data['average_humidity'],
            "avg_soil_moisture": avg_soil_moisture,
            "avg_light_level": cleaned_data['avg_light_level'],
            "plant_health_status": plant_health_status, 
            "notes": cleaned_data.get('notes', '')
        }
        reports_collection.insert_one(new_report)
        return redirect('analytics:dashboard')

    query = {}
    if filter_form.is_valid():
        date_from = filter_form.cleaned_data.get('date_from')
        date_to = filter_form.cleaned_data.get('date_to')
        if date_from and date_to:
            query['created_at'] = {
                '$gte': datetime.combine(date_from, datetime.min.time()),
                '$lte': datetime.combine(date_to, datetime.max.time())
            }

    reports = list(reports_collection.find(query).sort('_id', -1))

    context = {
        'reports': reports,
        'filter_form': filter_form,
        'report_form': report_form,
    }
    return render(request, 'analytics/analytics_dashboard.html', context)