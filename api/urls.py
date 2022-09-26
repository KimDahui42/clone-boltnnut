from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'users',views.UserViewSet, basename='User')
router.register(r'projects',views.ProjectViewSet, basename='Project')
router.register(r'partners',views.PartnerViewSet,basename='Partner')
router.register(r'project-files',views.ProjectFileViewSet,basename='Project File')

urlpatterns = [
   path('user/',views.UserViewSet.as_view(actions={
        'get':'list',
   }),name='user-list'),
    path('user/<int:pk>/',views.UserViewSet.as_view(actions={
        'get':'retrieve',
    }),name='user-detail'),
    path('project/',views.ProjectViewSet.as_view(actions={
        'get':'list',
        'post':'create',
    }),name='project-list'),
    path('project/<int:pk>/',views.ProjectViewSet.as_view(actions={
        'get':'retrieve',
    }),name='project-detail'),
    path('partner/',views.PartnerViewSet.as_view(actions={
        'get':'list',
        'post':'create',
    }),name='partner-list'),
    path('partner/<int:pk>/',views.PartnerViewSet.as_view(actions={
        'get':'retrieve',
        'patch':'update',
    }),name='partner-detail'),
    path('project-file/', views.ProjectFileViewSet.as_view(actions={
        'get':'list',
        'post':'create'
    }), name='projectfile-detail'),
]