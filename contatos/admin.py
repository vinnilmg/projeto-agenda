from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria')
    list_display_links = ('id', 'nome', 'sobrenome')
    list_filter = ('nome', 'sobrenome')
    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'telefone')


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    list_filter = ('nome',)
    list_per_page = 10
    search_fields = ('nome',)


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Contato, ContatoAdmin)
