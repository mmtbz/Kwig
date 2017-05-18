from django.contrib import admin
from .models import Course, Subject, Module


# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class ModuleInLine(admin.StackedInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created_date']
    list_filter = ['created_date', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('slug',)}
    inlines = [ModuleInLine]
