from django.conf.urls import include, url
import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^pro/$', views.pro),
    url(r'^city(\d+)/$', views.city),
    url(r'^htmlEditor/$', views.htmlEditor),
    url(r'^htmlEditorHandle/$', views.htmlEditorHandle),

]
