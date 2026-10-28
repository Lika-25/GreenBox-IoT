from django.shortcuts import render, redirect
from .models import AnalyticsReport
from .forms import AnalyticsFilterForm, AnalyticsReportForm

def analytics_dashboard(request):
    filter_form = AnalyticsFilterForm(request.GET or None)
    report_form = AnalyticsReportForm(request.POST or None)
    
    reports = AnalyticsReport.objects.all().order_by('-created_at')

    if filter_form.is_valid():
        date_from = filter_form.cleaned_data.get('date_from')
        date_to = filter_form.cleaned_data.get('date_to')
        if date_from:
            reports = reports.filter(created_at__date__gte=date_from)
        if date_to:
            reports = reports.filter(created_at__date__lte=date_to)

    if request.method == 'POST' and report_form.is_valid():
        report_form.save()
        return redirect('analytics:dashboard')

    context = {
        'reports': reports,
        'filter_form': filter_form,
        'report_form': report_form,
    }
    return render(request, 'analytics/analytics_dashboard.html', context)
