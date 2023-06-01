from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Home, name="HomePage"),
    path('about/', views.about, name="AboutPage"),
    path('AddEmp/', views.AddEmp, name="AddEmployee"),
    path("Empdelete/<int:Id>", views.Empdelete, name="EmployeeDeleted"),
    path("EmpUpdate/<int:Id>", views.EmpUpdate, name="EmployeeUpdated"),
    path("Do_update/<int:Empid>", views.Do_update, name="Do_update"),
    path("register/", views.register, name="register"),
    path("EmpLogin/", views.EmpLogin, name="EmpLogin"),
    path("Emplogout/", views.Emplogout, name="Emplogout"),
]
