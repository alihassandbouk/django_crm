from django.urls import path
from . import views
app_name = "website"

urlpatterns = [
    path("",views.home,name="home"),
    path("logout/",views.logout_user,name="logout"),
    path("register/",views.register,name="register")
]