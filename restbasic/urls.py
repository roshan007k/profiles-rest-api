from django.urls import path,include
from restbasic import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,basename='hello-viewset')
router.register('profile-viewset',views.UserProfileViewSet)
router.register('feed',views.UserProfileFeedViewSet)
urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls))
]
