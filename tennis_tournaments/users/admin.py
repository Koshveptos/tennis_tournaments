from django.contrib import admin

# Register your models here.
from users.models import*

admin.site.register(user)
admin.site.register(sessions)
admin.site.register(basket)