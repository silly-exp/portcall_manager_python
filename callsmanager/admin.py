from django.contrib import admin

# Register your models here.
from .models import Call, Ship, Port

admin.site.register(Call)
admin.site.register(Ship)
admin.site.register(Port)