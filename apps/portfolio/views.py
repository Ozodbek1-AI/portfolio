from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions
from .models import UserProfile, Skill, Experience, Education, Project, ContactMessage
from .serializers import (
    UserProfileSerializer,
    SkillSerializer,
    ExperienceSerializer,
    EducationSerializer,
    ProjectSerializer,
    ContactMessageSerializer
)


# Profil asosiy ma'lumotlari
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]


# Ko‘nikmalar (skills)
class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.AllowAny]


# Tajriba (work experience)
class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.AllowAny]


# Ta’lim (education)
class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [permissions.AllowAny]


# Loyihalar (projects)
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]


# Aloqa (contact form)
class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.AllowAny]
