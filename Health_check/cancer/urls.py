from django.urls import path
from cancer import views
app_name = 'cancer'
urlpatterns = [
    path('predict/', views.predict, name='predict_cancer'),
    path('details/', views.cancer_details, name = 'cancer_details'),
]