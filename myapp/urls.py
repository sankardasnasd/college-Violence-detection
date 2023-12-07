"""
URL configuration for college_violence project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('adminhome/',views.adminhome),

    path('login/',views.login),
    path('login_post/',views.login_post),
    path('logout/',views.logout),


    path('adminchangepassword/',views.adminchangepassword),
    path('adminchangepassword_post/',views.adminchangepassword_post),


    path('adminadddepartment/',views.adminadddepartment),
    path('adminadddepartment_post/',views.adminadddepartment_post),


    path('adminviewdepartment/',views.adminviewdepartment),
    path('adminviewdepartment_post/',views.adminviewdepartment_post),

    path('admineditdepartment/<id>',views.admineditdepartment),
    path('admineeditdepartment_post/',views.admineeditdepartment_post),
    path('admindeletedepartment/<id>',views.admindeletedepartment),


    path('adminaddcourse/',views.adminaddcourse),
    path('adminaddcourse_post/',views.adminaddcourse_post),

    path('adminviewcourse/',views.adminviewcourse),
    path('admineditcourse/<id>',views.admineditcourse),
    path('admineditcourse_POST/',views.admineditcourse_POST),

    path('admindeletecourse/<id>',views.admindeletecourse),

    path('adminviewcourse_POST/',views.adminviewcourse_POST),

    path('adminaddstudent/',views.adminaddstudent),
    path('adminaddstudent_post/',views.adminaddstudent_post),


    path('admineditstudent/<id>',views.admineditstudent),
    path('admineditstudent_POST/',views.admineditstudent_POST),

    path('admindeletestudent/<id>',views.admindeletestudent),

    path('adminviewstudent/',views.adminviewstudent),
    path('adminviewstudent_post/',views.adminviewstudent_post),



    path('adminaddstaff/',views.adminaddstaff),
    path('adminaddstaff_post/',views.adminaddstaff_post),

    path('admineditstaff/<id>',views.admineditstaff),
    path('admineditstaff_post/',views.admineditstaff_POST),
    path('adminviewstaff/',views.adminviewstaff),
    path('adminviewstaff_post/',views.adminviewstaff_post),
    path('admindeletestaff/<id>',views.admindeletestaff),

    path('adminaddauthority/',views.adminaddauthority),
    path('adminaddauthority_post/',views.adminaddauthority_post),

    path('admineditauthority/<id>',views.admineditauthority),
    path('admineditauthority_post/',views.admineditauthority_POST),
    path('admindeleteauthority/<id>',views.admindeleteauthority),

    path('adminviewauthority/',views.adminviewauthority),
    path('adminviewauthority_post/',views.adminviewauthority_post),

    path('adminaddincident/',views.adminaddincident),
    path('adminaddincident_post/',views.adminaddincident_post),

    path('admineditincident/<id>',views.admineditincident),
    path('admineditincident_post/',views.admineditincident_POST),
    path('admindeleteincident/<id>',views.admindeleteincident),

    path('adminviewincident/',views.adminviewincident),
    path('adminviewincident_post/',views.adminviewincident_post),

    path('adminaddfeedback/',views.adminaddfeedback),
    path('adminaddfeedback_post/',views.adminaddfeedback_post),

    path('admineditfeedback/',views.admineditfeedback),
    path('adminviewfeedback/',views.adminviewfeedback),
    path('adminviewfeedback_post/',views.adminviewfeedback_post),

    path('adminviewcomplient/',views.adminviewcomplient),
    path('adminviewcomplient_post/',views.adminviewcomplient_post),
    path('adminSendrply/<id>',views.adminSendrply),
    #path('adminreplay/',views.adminreplay),
    path('adminsendrply_post/', views.adminsendrply_post),

    path('adminViewViolence/', views.adminViewViolence),
    path('adminViewViolence_post/', views.adminViewViolence_post),

    path('adminViewIncludedFace/<id>', views.adminViewIncludedFace),
    path('adminViewIncludedFace_post/', views.adminViewIncludedFace_post),

    path('delface/<id>', views.delface),





    # ------------------------------------------
    path('authorityhome/', views.authorityhome),

    path('authoritychangepassword/', views.authoritychangepassword),
    path('authoritychangepassword_post/', views.authoritychangepassword),
    path('viewprofile/',views.viewprofile),
    path('authorityviewstudent/',views.authorityviewstudent),
    path('authorityviewstudent_post/',views.authorityviewstudent_post),
    path('viewcheckin_post/',views.viewcheckin_post),
    path('viewcheckin/',views.viewcheckin),
    path('viewattendance/',views.viewattendance),
    path('viewalert/',views.viewalert),
    path('viewalert_post/',views.viewalert_post),
    path('authoritytakeaction/',views.authoritytakeaction),
    path('post_authoritytakeaction/',views.post_authoritytakeaction),
    path('authorityviewfeedback_post/',views.authorityviewfeedback_post),
    path('authorityviewfeedback/',views.authorityviewfeedback),
    path('authoritysendnotification/',views.authoritysendnotification),
    path('authoritysendnotification_post/',views.authoritysendnotification_post),
    path('authoritysendmessage/',views.authoritysendmessage),
    path('authoritysendmessage_post/',views.authoritysendmessage_post),
    path('auth_view_parent/',views.auth_view_parent),
    path('parent_view_notification/',views.parent_view_notification),
    path('authorityViewViolence/', views.authorityViewViolence),
    path('authorityViewViolence_post/', views.authorityViewViolence_post),
    path('authorityViewIncludedFace/<id>', views.authorityViewIncludedFace),
    path('authorityViewIncludedFace_post/', views.authorityViewIncludedFace_post),
    path('searchStudent/', views.searchStudent),
    path('addStudentTOIncludedFace_post/<id>/<stdid>', views.addStudentTOIncludedFace_post),
    path('authoritytest/<id>', views.authoritytest),

    ################33


    path('and_login/',views.and_login),
    path('and_viewprofile/',views.and_viewprofile),
    path('and_changepassword/',views.and_changepassword),
    path('and_sendfeedback/',views.and_sendfeedback),
    path('parent_and_changepassword/',views.parent_and_changepassword),
    path('view_attendance/',views.view_attendance),

    path('parent_view_authority/',views.parent_view_authority),
    path('parent_view_attendance/',views.parent_view_attendance),
    path('parent_view_student/',views.parent_view_student),
    path('and_sendcomplaint/',views.and_sendcomplaint),
    path('parent_view_replay/',views.parent_view_replay),
    path('and_par_sendfeedback/',views.and_par_sendfeedback),



    path('chat/<id>',views.chat1),
    path('chat_view/',views.chat_view),
    path('chat_send/<msg>',views.chat_send),
    path('user_sendchat/',views.user_sendchat),
    path('user_viewchat/',views.user_viewchat),
    path('viewattendance_post/',views.viewattendance_post),


    path('test/',views.test),
    path('lkindex/',views.lkindex),
    path('auth_viewnotification/',views.auth_viewnotification),
    path('auth_viewnotification_post/',views.auth_viewnotification_post),
    path('auth_assign_violence_to_studentpost/',views.auth_assign_violence_to_studentpost),
    path('auth_deletenotification/<id>',views.auth_deletenotification),
    path('auth_violence_subimages/<vid>',views.auth_violence_subimages),
    path('auth_assign_violence_to_student/<vid>',views.auth_assign_violence_to_student),
    path('assgn/<id>',views.assgn),


]