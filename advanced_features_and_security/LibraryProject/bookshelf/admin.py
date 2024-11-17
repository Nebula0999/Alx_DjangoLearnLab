from django.contrib import admin
from .models import Book, CustomUser, CustomUserAdmin


admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year') 
    list_filter = ('publication_year',)  
    search_fields = ('title', 'author')
# Register your models here.
