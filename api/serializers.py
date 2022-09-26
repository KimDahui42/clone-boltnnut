from urllib import request
from rest_framework import serializers
from common.models import User
from boltnnut.models import Project, ProjectFile, Partner

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','company','name','userType','phone','jobPosition']

class ProjectSerializer(serializers.ModelSerializer):
    owner=serializers.CharField(source='owner.email')
    files = serializers.SerializerMethodField(source='projectfile_set')
    class Meta:
        model = Project
        fields =['id','owner','title','budget','budget_show','expired_date','expired_negotiate','goal','goal_negotiate','descript','ongoing','files']
    def get_files(self, obj):
        return obj.projectfile_set.values('id','file')

class ProjectFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectFile
        fields = ['id','project','file']
    
    def create(self,validated_data):
        return ProjectFile.objects.create(**validated_data)

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields= '__all__'
