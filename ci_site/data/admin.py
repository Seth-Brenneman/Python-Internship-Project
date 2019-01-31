from django.contrib import admin
from django.contrib.admin import site
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Permission
from .models import Defect, ChartDefect, Profile
from django import forms
from requests import request
from import_export.admin import ImportExportActionModelAdmin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter
from rangefilter.filter import DateRangeFilter

class ChartAdmin(admin.ModelAdmin):
    list_filter = (
        ('plant', DropdownFilter),
        ('value_stream', DropdownFilter),
        ('process_step', DropdownFilter),
        ('event', DropdownFilter),
        ('day_of_week', DropdownFilter),
        ('date_created', DateRangeFilter)
    )
    change_list_template = 'admin/change_list_graph.html'
    list_display = (
        'date_created',
        'time_created',
        'day_of_week',
        'plant',
        'value_stream',
        'process_step',
        'event'
    )
    readonly_fields = [
        'date_created',
        'day_of_week'
    ]


class MyModelAdmin(ImportExportActionModelAdmin):
    list_display = (
        'date_created',
        'time_created',
        'day_of_week',
        'plant',
        'value_stream',
        'process_step',
        'event'
    )

    list_filter = (
        ('plant', DropdownFilter),
        ('value_stream', DropdownFilter),
        ('process_step', DropdownFilter),
        ('event', DropdownFilter),
        ('day_of_week', DropdownFilter),
        ('date_created', DateRangeFilter)
    )

    ordering = ('plant',)
    date_hierarchy = 'date_created'
    readonly_fields = [
        'date_created',
        'day_of_week'
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super(MyModelAdmin, self).get_form(request, obj, **kwargs)
        if request.user.is_authenticated:
            form.base_fields['plant'].initial = request.user.profile.plant
            form.base_fields['value_stream'].initial = request.user.profile.value_stream
            form.base_fields['process_step'].initial = request.user.profile.process_step
            return form


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'get_plant',
        'get_value_stream',
        'get_process_step',
        'is_staff'
    )

    list_select_related = ('profile', )

    def get_plant(self, instance):
        return instance.profile.plant
    get_plant.short_description = 'Plant'

    def get_value_stream(self, instance):
        return instance.profile.value_stream
    get_value_stream.short_description = 'Value Stream'

    def get_process_step(self, instance):
        return instance.profile.process_step
    get_process_step.short_description = 'Process Step'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(Defect, MyModelAdmin)
admin.site.register(ChartDefect, ChartAdmin)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Permission)
