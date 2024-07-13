from django.urls import path
from.views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',index,name='index'),
    path('add_task/',add_task,name='add_task'),
    path('viewtask/',viewtask,name='viewtask'),
    path('contact/', contact,name='contact'),
    path('about/',about,name='about'),
    path('register/',register,name='register'),
    path('log_in/',log_in,name='log_in'),
    path('logout/',log_out,name='log_out'),
    path('searsh/',search_form,name='search_form'),
    path('delete/<int:id>',delete_data,name='delete_data'),
    path('update/<int:id>',update,name='update'),
    
    # forget password set up
    path("password_reset/",auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="password_reset"),
    path("password_reset_done/",auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>",auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),name="password_reset_confirm"),
    path("password_reset_complete/",auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),name="password_reset_complete")
]