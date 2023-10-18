from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('add_student/', views.add_student, name='add_student'),
    path('saveStudent/', views.saveStudent, name='saveStudent'),
    path('save_followup/<int:id>', views.save_followup, name='save_followup'),
    path('save_assignee/<int:id>', views.save_assignee, name='save_assignee'),
    path('savefollowup/<int:id>', views.savefollowup, name='savefollowup'),
    path('editStudent/<int:id>', views.editStudent, name='editStudent'),
    path('updateStudent/<int:id>', views.updateStudent, name='updateStudent'),
    path('edit_student/<int:id>', views.edit_student, name='edit_student'),
    ]
