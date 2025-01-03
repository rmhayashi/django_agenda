from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    #  as informações abaixo podem ser sets ou listas
    list_display = ('id','first_name', 'last_name', 'phone', 'email',)
    ordering = ('-first_name',) # o menos indica ordenar decrescente
    list_filter = ('gender',)
    search_fields = ('id', 'first_name', 'email')
    list_per_page = 10
    list_max_show_all = 200
    list_editable = ('last_name', 'phone',)
    list_display_links = ('id', 'first_name')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']