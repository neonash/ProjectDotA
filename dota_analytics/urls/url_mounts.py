from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('dota_analytics.urls.view_urls')),
    url(r'^service/', include('dota_analytics.urls.service_urls'))
]