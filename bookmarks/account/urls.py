from django.conf.urls import url
from django.contrib.auth import views
from .views import dashboard


urlpatterns = [
    # url(r'^login/$', views.user_login, name='login'),
    url(r'^$', dashboard, name='dashboard'),

    # login / logout urls
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^logout-then-login/$', views.logout_then_login, name='logout_then_login'),

    # change password urls
    url(r'^password-change/$', views.password_change, name='password_change'),
    url(r'^password-change/done/$', views.password_change_done, name='password_change_done'),
]
