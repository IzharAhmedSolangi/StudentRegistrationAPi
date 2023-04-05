
from django.urls import path
from . import views

urlpatterns = [
   path('register/',views.register),
   path('login/',views.login),
   path('getStudent/',views.getStudent ),
   path('varifystudent/',views.varifyStudent),
   path('forgetPasswordrequest/',views.restPasswordRequest),
   path('resetPassword/',views.resetPassword),
   path('getstudentByid/<str:rollnum>',views.getStudentById),
   path('createCourse/',views.createCourse),
   path('getCourses/',views.getCourses),
   path('assignCourse/',views.assignCourse)
   
]