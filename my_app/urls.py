from django.urls import path

from my_app import views 

app_name = "my_app"
urlpatterns = [
    path("cellphones", view=views.cellphones, name="cellphone-list"),
    path("cellphone/add", view=views.create_cellphones, name="cellphone-add"),
    path("computers", view=views.computers, name="computer-list"),
    path("computer/add", view=views.create_computers, name="computer-add"),
    path("accessories", view=views.accessories, name="accessorie-list"),
    path("accessorie/add", view=views.create_accessories, name="accessorie-add"),  
]
