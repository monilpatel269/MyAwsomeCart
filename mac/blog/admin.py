from django.contrib import admin
from .models import BlogComment, Blogpost, Contact

# Register your models here.
admin.site.register(Blogpost)
admin.site.register(Contact)
admin.site.register(BlogComment)