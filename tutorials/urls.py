from django.urls import path
from django.urls import include
from tutorials import views 
 
urlpatterns = [ 
    path('api/tutorials', views.tutorial_list),
    path('api/tutorials/<int:pk>', views.tutorial_detail),
    path('api/tutorials/published', views.tutorial_list_published)
]