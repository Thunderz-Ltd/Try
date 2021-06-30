from django.contrib import admin

from .models import House, UserProfile

# admin.site.register(Category)
admin.site.register(House)
admin.site.register(UserProfile)
