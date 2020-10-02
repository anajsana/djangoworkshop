from django.contrib import admin
from .models import Post


# registramos el modelo con esta línea
admin.site.register(Post)