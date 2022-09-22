from common.models import User
from boltnnut.models import Project, ProjectFile, Partner
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from api.serializers import UserSerializer, PartnerSerializer, ProjectSerializer, ProjectFileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PartnerViewSet(viewsets.ModelViewSet):
    queryset=Partner.objects.all()
    serializer_class=PartnerSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    def get_queryset(self):
        return Project.objects.all().prefetch_related('projectfile_set')

    '''def retrieve(self, request, *args, **kwargs):
        instance=self.get_object()
        fileList=instance.projectfile_set.all()
        projectDict=self.obj_to_project(instance)
        fileDict=[self.obj_to_projectfile(file) for file in fileList]

        dataDict={
            'project': projectDict,
            'fileList': fileDict,
        }
        return Response(dataDict)

    def obj_to_project(obj):
        project = dict(vars(obj))
        if obj.expired_date:
            project['expired_date'] = obj.expired_date.strftime('%Y-%m-%d %H:%M:%S')
        else:
            project['expired_date'] = '9999-12-31 00:00:00'

        del project['_prefetched_objects_cache']

        return project

    def obj_to_projectfile(obj):
        file = dict(vars(obj))
        return file'''

class ProjectFileViewSet(viewsets.ModelViewSet):
    queryset=ProjectFile.objects.all()
    serializer_class=ProjectFileSerializer
