from django.contrib import admin

from .models import BookInfo

# Register your models here.

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_data']

admin.site.register(BookInfo, BookInfoAdmin)


