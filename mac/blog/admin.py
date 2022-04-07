from django.contrib import admin
from .models import Blogpost, Contact

# Register your models here.
admin.site.register(Blogpost)
admin.site.register(Contact)