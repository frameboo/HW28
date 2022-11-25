from ads.views.category import *
from django.urls import path

urlpatterns = [
        path('create/', CategoryCreateView.as_view()),
        path('', CategoryListCreateView.as_view()),
        path('<int:pk>/', CategoryDetailView.as_view()),
    ]