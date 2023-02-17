from django.urls import path
from stats import views

urlpatterns = [
    path("features", views.FeatureListView.as_view()),
    path("feature-values", views.FeatureValueListView.as_view()),
]
