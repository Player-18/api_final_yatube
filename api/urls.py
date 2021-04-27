from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, 
                                            TokenRefreshView) 

from . import views

router = DefaultRouter()
router.register('posts', views.PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', views.CommentViewSet)
router.register('follow', views.FollowViewSet)
router.register('group', views.GroupViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('api/v1/token/', TokenObtainPairView.as_view(), 
         name='token_obtain_pair'), 
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), 
         name='token_refresh')
]
