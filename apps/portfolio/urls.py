from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserProfileViewSet,
    SkillViewSet,
    ExperienceViewSet,
    EducationViewSet,
    ProjectViewSet,
    ContactMessageViewSet
)

router = DefaultRouter()
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'experiences', ExperienceViewSet)
router.register(r'educations', EducationViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'contacts', ContactMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
