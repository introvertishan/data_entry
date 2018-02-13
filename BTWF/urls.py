from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.all_data.as_view(),name='home'),
    url(r'^form/$',views.form_page,name='form'),
    url(r'^edit/(\d+)/$',views.edit,name='edit'),
    url(r'^edit/[0-9]+/delete/(?P<data_id>\d+)/$',views.delete),
]