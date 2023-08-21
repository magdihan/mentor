from django.contrib import admin

# Register your models here.
from .models import Ads, Cotegory, Subcotegory


admin.site.register(Ads)
admin.site.register(Cotegory)
admin.site.register(Subcotegory)