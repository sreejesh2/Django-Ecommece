from django.urls import path
from . import views

urlpatterns = [

   path('register/',views.RegistrationView.as_view(),name='register'),
   path('login/',views.SignInView.as_view(),name='login'),
   path("token/",views.token_send,name="token"),
   path('',views.IndexView.as_view(),name='home'),
   path('verify/<auth_token>/',views.verify,name='verify')
]
