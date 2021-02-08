from django.contrib import admin
from .models import Market
from leaflet.admin import LeafletGeoAdmin


class MarketAdmin(LeafletGeoAdmin):
    list_display = ('store', 'geos')


admin.site.register(Market, MarketAdmin)