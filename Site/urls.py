from django.urls import path
from . import views


urlpatterns = [
  path('',views.home,name='Home'),
  path('contact/us/',views.contactUs,name="contact"),
  path('contact/doctor/',views.contact_doctor,name="contactDoctors"),
  path('search/doctor/',views.search_doctor,name="searchDoctor"),
  path('team/',views.doctorsPage,name='team'),
  path('patients/',views.patientsPage,name='patients'),
  path('test/',views.testPage, name="test"),
  path('drag/',views.testPage,name="drag"),
  path('FAQ/',views.FAQ_Page,name="faq"),
  path('QUIZ/',views.QUIZ_Page,name="QUIZ"),
  path('messages/',views.messagesPage,name="messages"),
  

] 