from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from courses.views import index, base_test

urlpatterns = [
    url(r'^accounts/login/', auth_views.login, name='login'),
    url(r'^accounts/logout/', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'course/', include('courses.url'), name='course'),
    url(r'^index/', index, name='in'),
    url(r'^base/', base_test, name='base'),
]
