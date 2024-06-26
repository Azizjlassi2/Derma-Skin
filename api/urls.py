from django.urls import path
from . import views

urlpatterns = [

    path("",views.get_routes),
    path("login/user/",views.login_user),
    path("logout/user/",views.logout_user),
    path("register/user/",views.register_user),

    path("users/",views.AppUsersView.as_view()),
    path("users/<int:pk>/",views.AppUserView.as_view()),


    path("doctors/",views.get_doctors),
    path("doctors/<int:pk>/",views.get_doctors),

    path("descriptions/",views.DescriptionsView.as_view()),
    path("descriptions/<int:pk>/",views.DescriptionView.as_view()),

    path("questions/",views.QuestionsView.as_view()),
    path("questions/<int:pk>/",views.QuestionView.as_view()),

    path("doctor/request/",views.DoctorRequestsView.as_view()),
    path("doctor/request/<int:pk>/",views.DoctorRequestView.as_view()),
  
    path("results/",views.ResultsView.as_view()),
    path("results/<int:pk>/",views.ResultView.as_view()),
      
    path("contact/messages/",views.ContactMessagesView.as_view()),
    path("contact/messages/<int:pk>/",views.ContactMessageView.as_view()),

   
    
    
    
]