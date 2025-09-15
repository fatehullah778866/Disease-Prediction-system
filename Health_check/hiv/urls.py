from django.urls import path
from .import views

app_name = "hiv"
urlpatterns = [
    path('', views.aids_hiv, name='aids_hiv'),
    path('hiv/', views.predict_hiv, name="predict_hiv"),
    path('details/', views.detail, name='detail'),
]
