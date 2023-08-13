from django.urls import path
from . import views

urlpatterns = [
    path('submit_review/', views.submit_review, name='submit_review'),
    path('review_success/',views.review_success, name='review_success'),
]
