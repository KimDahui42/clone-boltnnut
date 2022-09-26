from api.permissions import IsOwnerOnly,IsPartner
from django.shortcuts import get_object_or_404
from common.models import User
from boltnnut.models import Project, ProjectFile, Partner
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.mixins import UpdateModelMixin
from api.serializers import UserSerializer, PartnerSerializer, ProjectSerializer, ProjectFileSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOnly]

    def get_queryset(self):
        if self.request.user.is_admin:
            return User.objects.all()
        else:
            return User.objects.filter(pk=self.request.user.id)

class PartnerViewSet(viewsets.ModelViewSet):
    queryset=Partner.objects.all()
    serializer_class=PartnerSerializer
    permission_classes = [IsPartner]

    def retrieve(self, request, *args, **kwargs):
        # do your customization here
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
            
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    


class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    permission_classes = [IsOwnerOnly]

    def get_queryset(self):
        return Project.objects.all().prefetch_related('projectfile_set')

    def obj_to_project(obj):
        project = dict(vars(obj))
        if obj.expired_date:
            project['expired_date'] = obj.expired_date.strftime('%Y-%m-%d %H:%M:%S')
        else:
            project['expired_date'] = '9999-12-31 00:00:00'

        del project['_prefetched_objects_cache']

        return project

class ProjectFileViewSet(viewsets.ModelViewSet):
    queryset=ProjectFile.objects.all()
    serializer_class=ProjectFileSerializer
    permission_classes = [IsOwnerOnly]
