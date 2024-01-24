from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from paciente import views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [

    path('pacientes_lista/', login_required(views.index), name='class_pacientes_lista'),
    path('search', views.SearchResultsView.as_view(), name='search'),
  
    path('upload_paciente/', login_required(views.UploadPacienteView.as_view()), name='class_upload_paciente'),
    path('paciente/<int:pk>/', login_required(views.PacienteDetailView.as_view()), name='class_detail_paciente'),    
    path('paciente_update/<int:pk>/', login_required(views.PacienteUpdateView.as_view()), name='class_update'),

    path('upload_record/', login_required(views.UploadRecordView.as_view()), name='class_upload_record'),
    path('record/<int:pk>/', login_required(views.RecordDetailView.as_view()), name='class_detail_record'),
    path('record_update/<int:pk>/', login_required(views.RecordUpdateView.as_view()), name='class_update_record'),
    path('record_delete/<int:pk>/', login_required(views.RecordDeleteView.as_view()), name='class_delete_record'),

    ]
