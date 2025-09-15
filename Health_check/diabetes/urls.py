from django.urls import path
from diabetes import views
app_name = 'diabetes'
urlpatterns = [
    path('', views.diabetic, name='diabetes_prediction'),
    path('predicts/', views.predicts, name='predicts'),
    path('details', views.details, name = 'diabetes_details'),
]