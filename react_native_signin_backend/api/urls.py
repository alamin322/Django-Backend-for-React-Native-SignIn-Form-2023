from django.urls import path
from api import views


urlpatterns = [
    path(route="", view=views.home_view, name="home"),
    path(route="create/", view=views.create_view, name="create_view"),
    path(route="show/", view=views.show_view, name="show_view"),
]
