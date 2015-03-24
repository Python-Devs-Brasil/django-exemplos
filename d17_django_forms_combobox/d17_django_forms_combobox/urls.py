from django.conf.urls import patterns, include, url
from django.contrib import admin
from d17_django_forms_combobox import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'd17_django_forms_combobox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^enviar/$', views.enviar, name='enviar'),
)