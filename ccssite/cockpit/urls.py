from django.urls import path
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns = [
    # ex: /polls/
    path('load/', views.load, name='load'),
    path('production_table', views.p_table, name='index'),
    path('production_chart/', views.p_chart, name='chart'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
]+ static(settings.MEDIA_URL, serve, document_root=settings.MEDIA_ROOT)
