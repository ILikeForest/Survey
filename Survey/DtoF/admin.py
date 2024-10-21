from django.contrib import admin
from .models import selectionCount


class selectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    search_fields = ('name',)    # 검색 기능


admin.site.register(selectionCount, selectionAdmin)