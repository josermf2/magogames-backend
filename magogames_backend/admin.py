from django.contrib import admin
from .models import Favorite, User

# Register your models here.
admin.site.register(Favorite)
admin.site.register(User)