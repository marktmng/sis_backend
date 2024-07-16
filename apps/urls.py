from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.viewsets import StudentViewSet, studentMarkViewSet, ProgramViewSet, LecturerViewSet, ParentViewSet, TuitionFeeViewSet
from apps.views import RegistrationView

router = DefaultRouter()

router = DefaultRouter()
router.register('program', ProgramViewSet, basename='program')
router.register('lecturer', LecturerViewSet, basename='lecturer')
router.register('student', StudentViewSet, basename='student')
router.register('studentmark', studentMarkViewSet, basename='studentmark')
router.register('parent', ParentViewSet, basename='parent')
router.register('tuitionfee', TuitionFeeViewSet, basename='tuitionfee')
router.register('registration', RegistrationView, basename='registration')

urlpatterns = router.urls

# urlpatterns = [
#     path('progrgram/', views.program, name='program'),
# ]