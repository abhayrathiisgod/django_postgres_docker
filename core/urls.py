from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.site.site_header = 'Techcolab SuperAdmin'
admin.site.index_title = 'Techcolab'
admin.site.site_title = 'Techcolab Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products-services/', include('product_service.urls')),
    path('api/v1/vacancies/', include('vacancies.urls')),
    path('api/v1/website/', include('website.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
