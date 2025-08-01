from django.contrib import admin
from .models import Author, Post

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'author', 'fecha_publicacion')
    list_filter = ('titulo', 'fecha_publicacion')
    search_fields = ('titulo', 'contenido')