from django.urls import path
from .views import AssignmentListView, SubmissionFormView, SubmissionListView ,homeview,student_loginview,student_regview

urlpatterns = [
    path('', homeview.as_view(), name='home'),
    path('assignment_list/', AssignmentListView.as_view(), name='assignment_list'),
    path('assignments/<int:assignment_id>/submissions/new/', SubmissionFormView.as_view(), name='submission_create'),
    path('assignments/<int:pk>/submissions/', SubmissionListView.as_view(), name='submission_list'),
    path("studentreg/",student_regview.as_view(),name="s_reg"),
    path("studentlogin/",student_loginview.as_view(),name="s_login")
]
