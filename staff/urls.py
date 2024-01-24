from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from staff import views
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('login/', auth_views.LoginView.as_view(), name='login'),
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
     path('lista/', login_required(views.StaffListView.as_view()), name='class_staff_lista'),
     path('upload/', login_required(views.UploadStaffView.as_view()), name='class_upload_staff'),
     path('<int:pk>/', login_required(views.StaffDetailView.as_view()), name='class_detail_staff'),
     path('delete/<int:pk>/', login_required(views.StaffDeleteView.as_view()), name='class_delete_staff'),
     path('update/<int:pk>/', login_required(views.StaffUpdateView.as_view()), name='class_update_staff'),
     path('ckeditor',include('ckeditor_uploader.urls')),
     ]
