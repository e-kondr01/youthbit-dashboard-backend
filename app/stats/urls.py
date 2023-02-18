from django.urls import path

from stats import views

urlpatterns = [
    path("features", views.ParentFeatureListView.as_view()),
    path("features/child-features", views.ChildFeatureListView.as_view()),
    path("feature-values/map", views.MapFeatureValueListView.as_view()),
    path("feature-values/children", views.ChildFeatureValueListView.as_view()),
    path("feature-values", views.FeatureValueListView.as_view()),
]
