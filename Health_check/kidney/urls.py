from django.urls import path
from kidney import views
app_name = 'kidney'
urlpatterns = [
    path('', views.predict, name='predict_kidney'),
    path('details/', views.detail, name='details'),
    path('kidney_back/', views.kidney_back, name = 'kidney_back'),
]