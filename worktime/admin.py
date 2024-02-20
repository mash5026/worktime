from typing import Any
from django.contrib import admin
from django.db.models.fields.related import ForeignKey
from django.forms.models import ModelChoiceField
from django.http.request import HttpRequest
from .models import WorkRecord, WorkRecordFinally, Holiday
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html


@admin.register(WorkRecord)
class WorkRecordAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('arrived_time', 'departure_time', 'person', 'date' , 'night_work', 'overtime_morning', 
'normal_working_hours', 'overtime_evening', 'work_nights', 'work_deduction_morning', 'work_deduction_evening',
'status')
    list_filter = ('person',)
    search_fields = ('person',)


@admin.register(WorkRecordFinally)
class WorkRecordFinallyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display  = ('person', 'date', 'date_persian', 
                     'normal_working_hours', 'normal_working_hours_formatted',
                      'over_time', 'over_time_formatted', 
                      'work_night', 'work_night_formatted',
                     'work_deduction', 'work_deduction_formatted',
                    'absent_overtime', 'absent_overtime_formatted',
                    'status', 'status_holiday')
    list_filter = ('person',)
    search_fields = ('person',)

    def colored_status(self, obj):
        color = 'green'
        if obj.status == 1:
                    color = 'red'
                    return format_html(

            '<b style="background:{};">{}</b>',
            color,
            obj.status
                       )
        else:
            return obj.status
    colored_status.allow_tags = True
    colored_status.short_description = 'Status'

    # Add the method to the list_display
    list_display = list(list_display)
    list_display.remove('status')
    list_display.append('colored_status')

    def colored_status_holiday(self, obj):
        color = 'green'
        if obj.status_holiday == 1:
                    color = 'yellow'
                    return format_html(

            '<b style="background:{};">{}</b>',
            color,
            obj.status_holiday
                       )
        else:
            return obj.status_holiday
    colored_status_holiday.allow_tags = True
    colored_status_holiday.short_description = 'Status Holiday'

    # Add the method to the list_display
    list_display = list(list_display)
    list_display.remove('status_holiday')
    list_display.append('colored_status_holiday')


@admin.register(Holiday)
class AdminHoliday(admin.ModelAdmin):
    list_display = ('date_holiday', 'event')

 