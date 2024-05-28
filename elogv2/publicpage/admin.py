from django.contrib import admin
from .models import ChaiVarity


# Register your models here.
class ChaiVarityAdmin(admin.ModelAdmin):
    list_display = ("name", "image_display", "data_added", "type_of_chai")

    def image_display(self, obj):
        return obj.image.url if obj.image else ""  # display image Url

    image_display.short_description = "Image"


admin.site.register(ChaiVarity, ChaiVarityAdmin)
