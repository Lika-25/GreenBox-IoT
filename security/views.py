from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import SecurityMeasure
from .forms import SecurityMeasureForm

def security_list(request):
    measures = SecurityMeasure.objects.all().order_by('-id')
    return render(request, 'security/security_list.html', {'measures': measures})

def add_security_measure(request):
    if request.method == 'POST':
        form = SecurityMeasureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('security_list')
    else:
        form = SecurityMeasureForm()
    return render(request, 'security/add_security.html', {'form': form})

@require_POST
def toggle_security_status(request, pk):
    measure = get_object_or_404(SecurityMeasure, pk=pk)
    measure.is_active = not measure.is_active
    measure.save()
    return redirect('security_list')

@require_POST
def delete_security_measure(request, pk):
    measure = get_object_or_404(SecurityMeasure, pk=pk)
    measure.delete()
    return redirect('security_list')