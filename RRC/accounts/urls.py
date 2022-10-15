from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserProfileListCreateView, UserProfileDetailView

# router=DefaultRouter()

# router.register("all-profiles",UserProfileListCreateView)
# router.register("profile/<int:pk>",userProfileDetailView,basename='profile')

urlpatterns = [
    path("all-profiles",UserProfileListCreateView.as_view(),name="all-profiles"),
    path("profile/<int:pk>",UserProfileDetailView.as_view(),name="profile")
    # path("",include(router.urls))
]