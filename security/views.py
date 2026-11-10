from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from pymongo import MongoClient
from bson.objectid import ObjectId
from .forms import MongoSecurityForm
from datetime import datetime

def get_threats_collection():
    client = MongoClient("mongodb://localhost:27017/")
    return client["GreenBox_Users_DB"]["cyber_threats"]

def security_list(request):
    col = get_threats_collection()
    raw_threats = list(col.find().sort("_id", -1))
    
    threats = []
    for item in raw_threats:
        item['id_str'] = str(item['_id'])
        threats.append(item)
        
    return render(request, 'security/security_list.html', {'threats': threats})

def add_security(request):
    if request.method == 'POST':
        form = MongoSecurityForm(request.POST)
        if form.is_valid():
            col = get_threats_collection()
            
            count = col.count_documents({})
            new_id = f"THR-{count + 1:03d}"
            
            new_threat = form.cleaned_data
            new_threat['threat_id'] = new_id
            new_threat['created_at'] = datetime.now()
            
            col.insert_one(new_threat)
            return redirect('security_list')
    else:
        form = MongoSecurityForm()
    return render(request, 'security/add_security.html', {'form': form})

@require_POST
def toggle_threat_status(request, threat_id):
    col = get_threats_collection()
    threat = col.find_one({"_id": ObjectId(threat_id)})
    if threat:
        new_status = "neutralized" if threat.get("status") == "active" else "active"
        col.update_one({"_id": ObjectId(threat_id)}, {"$set": {"status": new_status}})
    return redirect('security_list')

@require_POST
def delete_threat(request, threat_id):
    col = get_threats_collection()
    col.delete_one({"_id": ObjectId(threat_id)})
    return redirect('security_list')