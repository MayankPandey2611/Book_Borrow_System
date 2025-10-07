from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('student-register/', views.student_register, name='student_register'),
    path('student-login/', views.student_login, name='student_login'),

    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add-book/', views.add_book, name='add_book'),

    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('update-book/<int:book_id>/', views.update_book, name='update_book'),
    path('delete-book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('return_book/<int:book_id>/', views.return_book, name='return_book'),
    path('logout/',views.logout,name='logout'),
    path('mail/',views.mail,name='mail'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
