from django.contrib import admin
from .models import Produto
@admin.register(Produto)
class ProdutoADM(admin.ModelAdmin):
    list_display = ['nome','preco','estoque']