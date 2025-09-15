from django.urls import path
from liver import views
app_name = 'liver'

urlpatterns = [
    path('', views.home_liver, name='home_liver'),
    path('predict_liver/', views.predict_liver, name='predict_liver'),
    path('detail/', views.detail, name='details')
]
