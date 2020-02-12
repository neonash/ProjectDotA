from django.conf.urls import url
from dota_analytics.services import fetchdata_service

urlpatterns = [
    url(r'^getData/$', fetchdata_service.FetchParseData.deparseTrainData),
    url(r'^pushData/$', fetchdata_service.parseData),

]

