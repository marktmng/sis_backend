from rest_framework import serializers
from .models import Student, StudentMark, Program, Lecturer, Parent, TuitionFee
from .models import Registration

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['id', 'name', 'duration_months']
        
class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ['id', 'name', 'email', 'program']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'program']
        
class StudentMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentMark
        fields = ['id', 'student', 'course', 'mark']
        
class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ['id', 'student', 'name', 'contact']
        
class TuitionFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TuitionFee
        fields = ['id', 'student', 'paid_date', 'amount']
        
class RegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Registration
        fields = ['id', 'name','program', 'email', 'username']