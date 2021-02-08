from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Schedule
from .forms import ScheduleForm


def index(request):
    schedule_list = Schedule.objects.order_by('-create_date')
    context = {'schedule_list': schedule_list}
    return render(request, 'schedule_list.html', context)


def schedule_create(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.create_date = timezone.now()
            schedule.save()
            return redirect('list:index')
            # urls.py의 name으로 이동. (그냥 주소도 가능)
    else:
        form = ScheduleForm()
    context = {'form': form}
    return render(request, 'schedule_form.html', context)


def schedule_delete(request, schedule_id):
    schedule = Schedule.objects.get(pk=schedule_id)
    schedule.delete()
    return redirect('list:index')