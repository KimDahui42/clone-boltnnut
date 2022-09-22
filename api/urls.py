from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'projects',views.ProjectViewSet)
router.register(r'partners',views.PartnerViewSet)
router.register(r'project-files',views.ProjectFileViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
