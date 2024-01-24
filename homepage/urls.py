from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from staff import views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [

    path('dashboard/', login_required(views.dashboard), name='dashboard'),

    ]
