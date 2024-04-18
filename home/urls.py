from django.urls import path
from home.views import Home


app_name = "home"


urlpatterns = [
    path("", Home.as_view(), name="home"),
] 