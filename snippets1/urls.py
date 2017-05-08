from django.conf.urls import url
from snippets1 import views

urlpatterns = [
    url(r'^snippets[\d]+/$', views.snippet_list),
    url(r'^snippets2/$', views.snippet_list),
    url(r'^admin/', views.admin, name='admin'),
    url(r'^notify/loadtest/$', views.notification_input),
    url(r'^snippets1/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^snippets2/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^snippets1/[2-4][0][0-6]|[3][0][7]|[4][0][7-9]|[4][1][0-7]|[5][0][0-5]', views.snippet_200,name='snippet_code'),
    url(r'^snippets1/oauth*',views.snippet_oauth,name='snippets_oauth'),
]
