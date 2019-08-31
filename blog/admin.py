from django.contrib import admin
from .models import Post

# Hacer el modelo visible en la consola de Django
admin.site.register(Post)