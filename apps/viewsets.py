from rest_framework import viewsets 
from .models import Student, StudentMark, Program, Lecturer, Parent, TuitionFee 
from .serializers import StudentSerializer, StudentMarkSerializer, ProgramSerializer, LecturerSerializer, ParentSerializer, TuitionFeeSerializer # added

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    
class LecturerViewSet(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class studentMarkViewSet(viewsets.ModelViewSet):
    queryset = StudentMark.objects.all()
    serializer_class = StudentMarkSerializer
    
class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    
class TuitionFeeViewSet(viewsets.ModelViewSet):
    queryset = TuitionFee.objects.all()
    serializer_class = TuitionFeeSerializer