from django.contrib import admin
from .models import Winner,Contact
from django.utils.html import format_html
# Register your models here.

class WinnerAdmin(admin.ModelAdmin):
    class Meta:
        model = Winner
    fields = ('image_tag','picture','winner_name','mobile_number','lottery_number','amount','pub_date')
    readonly_fields = ('image_tag',)
    exclude = ('image_tag',)
admin.site.register(Winner,WinnerAdmin)
admin.site.register(Contact)
