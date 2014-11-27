from django.conf.urls import patterns,url
from measurements import views

urlpatterns = patterns(
           'measurements.views',
           url(r'^$', views.patients, name='patients'),
           url(r'^all', views.patients, name='patients'),
           url(r'^add_patient', views.add_patient, name="add_patient"),
           url(r'^(?P<slug>\w+)/$', views.patient, name="patient"),

)
