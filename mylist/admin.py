from django.contrib import admin
from .models import Schedule


# /admin에서 todolist 관리
# admin.site.register(Schedule)

# /admin에서 데이터 검색
class ScheduleAdmin(admin.ModelAdmin):
    search_fields = ['content']


admin.site.register(Schedule, ScheduleAdmin)