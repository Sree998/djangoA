from . import views
from django.urls import path,include


urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('user_login',views.user_login,name='user_login'),
    path('admin_welcome',views.admin_welcome,name='admin_welcome'),
    path('tutor_welcome',views.tutor_welcome,name='tutor_welcome'),
    path('load_addcourse',views.load_addcourse,name='load_addcourse'),
    path('add_course',views.add_course,name='add_course'),
    path('load_addstudent',views.load_addstudent,name='load_addstudent'),
    path('add_student',views.add_student,name='add_student'),
    path('show_student',views.show_student,name='show_student'),
    
    path('load_signup',views.load_signup,name='load_signup'),
    path('tutor_signup',views.tutor_signup,name='tutor_signup'),
    path('profile',views.profile,name='profile'),
    path('edit_page/<int:pk>',views.edit_page,name='edit_page'),
    path('edit_details/<int:pk>',views.edit_details,name='edit_details'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('show_tutor',views.show_tutor,name='show_tutor'),
    path('delete_tutor/<int:pk>',views.delete_tutor,name='delete_tutor'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('tutor_logout',views.tutor_logout,name='tutor_logout'),

    path('load_edit_profile',views.load_edit_profile,name='load_edit_profile'),
    path('profile',views.profile,name='profile'),
    path('edit',views.edit,name='edit'),

    

]