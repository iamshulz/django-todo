from django.contrib import admin
from .models import Task


# Override Task on admin side
# This will show the columns on the admin side
# See More here: https://docs.djangoproject.com/en/6.0/ref/contrib/admin/
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'updated_at')
    search_fields = ('task')

# Register your models here.
admin.site.register(Task, TaskAdmin)