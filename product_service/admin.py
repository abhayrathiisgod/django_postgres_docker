from django.contrib import admin
from .models import Product, SERVICE
from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)
admin.site.site_url = None


class PRODUCTAdmin(admin.ModelAdmin):
    list_display = ('ID', 'NAME', 'SLUG', 'CREATED_AT', 'UPDATED_AT')
    # list_filter = ('ID', 'NAME', 'SLUG', 'CREATED_AT', 'UPDATED_AT')
    list_display_links = ('ID', 'NAME', 'SLUG', 'CREATED_AT', 'UPDATED_AT')
    search_fields = ('NAME', 'SLUG')
    readonly_fields = ('CREATED_AT', 'UPDATED_AT')


class SERVICEAdmin(admin.ModelAdmin):
    list_display = ('ID', 'NAME', 'SLUG', 'CREATED_AT', 'UPDATED_AT')
    # list_filter = ('ID', 'NAME', 'SLUG', 'CREATED_AT', 'UPDATED_AT')
    search_fields = ('NAME', 'SLUG')
    list_display_links = ('ID', 'NAME', 'SLUG', 'CREATED_AT', 'UPDATED_AT')
    readonly_fields = ('CREATED_AT', 'UPDATED_AT')


# Register your models here.
admin.site.register(Product, PRODUCTAdmin)
admin.site.register(SERVICE, SERVICEAdmin)
