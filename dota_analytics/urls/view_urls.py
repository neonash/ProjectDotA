from django.conf.urls import url
from dota_analytics import views
from django.contrib.auth import views as vi

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'prediction/$', views.prediction, name ='prediction'),

    url(r'^login/$', vi.LoginView.as_view(), name='login'),
    url(r'^password_reset_form/$', views.password_reset, name='password_reset_form'),
    url(r'^password_reset_done/$', views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        vi.PasswordResetConfirmView, name='password_reset_confirm'),
    url(r'^reset/done/$', vi.PasswordResetCompleteView, name='password_reset_complete'),
    url(r'^signup/$', views.signup, name='signup'),

]
