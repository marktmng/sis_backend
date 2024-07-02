from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.viewsets import StudentViewSet, studentMarkViewSet, ProgramViewSet, LecturerViewSet, ParentViewSet, TuitionFeeViewSet

router = DefaultRouter()

# router.register(r'student', StudentViewSet, 'student')
# router.register(r'studentmark', studentMarkViewSet, 'studentmark')
# router.register(r'program', ProgramViewSet, 'program')
# router.register(r'lecturer', LecturerViewSet, 'lecturer')
# router.register(r'parent', ParentViewSet, 'parent')
# router.register(r'tuitionfee', TuitionFeeViewSet, 'tuitionfee')

router = DefaultRouter()
router.register('student', StudentViewSet, basename='student')
router.register('studentmark', studentMarkViewSet, basename='studentmark')
router.register('program', ProgramViewSet, basename='program')
router.register('lecturer', LecturerViewSet, basename='lecturer')
router.register('parent', ParentViewSet, basename='parent')
router.register('tuitionfee', TuitionFeeViewSet, basename='tuitionfee')

urlpatterns = router.urls

# urlpatterns = [
#     path('progrgram/', views.program, name='program'),
# ]