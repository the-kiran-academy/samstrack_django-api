from django.urls import path
from . import views

urlpatterns = [
    # Subject
    path('subject/get-all-subjects/', views.list_subjects),
    path('subject/get-subject-by-id/<int:id>/', views.get_subject),
    path('subject/delete-subject/<int:id>/', views.delete_subject),
    path('subject/update-subject/', views.update_subject),
    path('subject/add-subject/', views.create_subject),

    # Student
    path('student/add-student/', views.create_student),
    path('student/get-all-students/', views.list_students),
    path('student/get-student-by-id/<int:id>/', views.get_student),
    path('students/delete/<int:id>/', views.delete_student),
    path('student/update-student/', views.update_student),
    
    # User
    # user/register-user
    path('user/register-user/', views.register_user),
    path('user/get-all-user/', views.list_users),
    path('user/get-user-by-username/<str:username>/', views.get_user_by_username),
    path('user/delete-user-by-username/', views.delete_user_by_username),
    path('user/update-user/', views.update_user),
    path('user/login-user/', views.login_user),
    path('user/get-all-admin/', views.list_admins),
    path('user/get-all-faculty/', views.list_faculty),

    # Attendance
    path('attendance/take-attendance/', views.mark_attendance),
    path('attendance/get-all-attendance-records/', views.get_attendance),
    path('attendance/get-attendance-by-date-subject/<str:date>/<int:subject_id>/', views.get_attendance_by_date_subject),
    path('attendance/get-attendance-by-faculty/<str:username>/', views.get_attendance_by_faculty),
    path('attendance/get-attendance/<str:username>/<int:subject_id>/<str:date>/', views.get_attendance_by_faculty_subject_date),
]
