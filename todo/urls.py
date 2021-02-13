from django.urls import path
from .views import TodoList
from .views import TodoDetail

urlpatterns = [
    path("list/", TodoList.as_view()),
    path("detail/<int:pk>/", TodoDetail.as_view()),
]
