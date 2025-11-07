from rest_framework import serializers
from .models import Student, Subject, AttendanceRecord, User

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    faculty = UserSerializer(read_only=True)   # show faculty object instead of id
    subject = SubjectSerializer(read_only=True)  # show subject object instead of id
    students = StudentSerializer(many=True, read_only=True)  # show student objects instead of ids

    class Meta:
        model = AttendanceRecord
        fields = '__all__'

        
class AttendanceRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    subjectId = serializers.IntegerField()
    date = serializers.CharField()
    time = serializers.CharField()
    students = serializers.ListField(
        child=serializers.DictField()
    )

    def create(self, validated_data):
        # get faculty (User)
        faculty = User.objects.get(username=validated_data["username"])

        # get subject
        subject = Subject.objects.get(id=validated_data["subjectId"])

        # create attendance record (without student!)
        record = AttendanceRecord.objects.create(
            faculty=faculty,
            subject=subject,
            date=validated_data["date"],
            time=validated_data["time"],
            number_of_students=len(validated_data["students"])
        )

        # add students to ManyToMany
        for stu in validated_data["students"]:
            student = Student.objects.get(id=stu["id"])
            record.students.add(student)

        return record        
