from django.urls import path
from .views import NewsList, NewDetail, PublicationsList

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewDetail.as_view()),
    path('publications', PublicationsList.as_view()),
    ]
