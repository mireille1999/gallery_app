from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name='index'),
    path('search/', views.search_results, name='search_results'),
    path('image/<image_id>', views.single, name='single'),
    path('location/<image_location>', views.location_filter, name='location_filter')
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)