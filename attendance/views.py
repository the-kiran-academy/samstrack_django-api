from turtle import update
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student, Subject, AttendanceRecord, User
from .serializers import AttendanceRequestSerializer, StudentSerializer, SubjectSerializer, AttendanceSerializer, UserSerializer

# ---------- SUBJECT ----------
@api_view(['POST'])
def create_subject(request):
    serializer = SubjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(True)  # same as Spring Boot returning boolean
    return Response(False)

@api_view(['GET'])
def get_subject(request, id):
    try:
        subject = Subject.objects.get(id=id)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)
    except Subject.DoesNotExist:
        return Response(False)

@api_view(['DELETE'])
def delete_subject(request, id):
    try:
        subject = Subject.objects.get(id=id)
        subject.delete()
        return Response(True)
    except Subject.DoesNotExist:
        return Response(False)

@api_view(['PUT'])
def update_subject(request):
    try:
        subject = Subject.objects.get(id=request.data.get("id"))
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(True)
        return Response(False)
    except Subject.DoesNotExist:
        return Response(False)

@api_view(['GET'])
def list_subjects(request):
    subjects = Subject.objects.all()
    serializer = SubjectSerializer(subjects, many=True)
    return Response(serializer.data)


# ---------- STUDENT ----------
@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(True)
    return Response(False)


@api_view(['GET'])
def list_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_student(request, id):
    try:
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response(False)


@api_view(['PUT'])
def update_student(request):
    try:
        student = Student.objects.get(id=request.data.get("id"))
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(True)
        return Response(False)
    except Student.DoesNotExist:
        return Response(False)

@api_view(['DELETE'])
def delete_student(request, id):
    try:
        student = Student.objects.get(id=id)
        student.delete()
        return Response(True)
    except Student.DoesNotExist:
        return Response(False)


# ---------- USER ----------

#user/register-user
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"success": True}, status=status.HTTP_201_CREATED)
    return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_user_by_username(request,username):
    try:
        user = User.objects.get(username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response(False)

@api_view(['PUT'])
def update_user(request):
    try:
        user = User.objects.get(username=request.data.get("username"))
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(True)
        return Response(False)
    except User.DoesNotExist:
        return Response(False)

#login_user
@api_view(['POST'])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")
    try:
        user = User.objects.get(username=username, password=password)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response(False)

#list_admins
@api_view(['GET'])
def list_admins(request):
    admins = User.objects.filter(role='admin').values('username', 'email', 'firstName', 'lastName')
    return JsonResponse(list(admins), safe=False)


#list_faculty
@api_view(['GET'])
def list_faculty(request):
    faculty = User.objects.filter(role='faculty').values('username', 'email', 'firstName', 'lastName')
    return JsonResponse(list(faculty), safe=False)



@api_view(['PUT'])
def update_user(request):
    try:
        user = User.objects.get(id=request.data.get("id"))
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(True)
        return Response(False)
    except User.DoesNotExist:
        return Response(False)

@api_view(['DELETE'])
def delete_user_by_username(id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return Response(True)
    except User.DoesNotExist:
        return Response(False)

# ---------- ATTENDANCE ----------
@api_view(['POST'])
def mark_attendance(request):
    serializer = AttendanceRequestSerializer(data=request.data)
    if serializer.is_valid():
        record = serializer.save()
        return Response({"success": True, "attendance_id": record.id})
    return Response(serializer.errors, status=400)




@api_view(['GET'])
def get_attendance(request):
    attendance = AttendanceRecord.objects.all()
    serializer = AttendanceSerializer(attendance, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_attendance_by_date_subject(request,date, subject_id):
    attendance = AttendanceRecord.objects.filter(date=date, subject_id=subject_id)
    serializer = AttendanceSerializer(attendance, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_attendance_by_faculty(request, username):
    attendance = AttendanceRecord.objects.filter(faculty__username=username)
    serializer = AttendanceSerializer(attendance, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def get_attendance_by_faculty_subject_date(request, username, subject_id, date):
    attendance = AttendanceRecord.objects.filter(faculty__username=username, subject_id=subject_id, date=date)
    serializer = AttendanceSerializer(attendance, many=True)
    return Response(serializer.data)

