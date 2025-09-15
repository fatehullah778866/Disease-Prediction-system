from django.urls import path
from heart.views import heart_home, predict_heart, heart_detail
app_name = 'heart'
urlpatterns = [
    path('', heart_home, name='heart_home'),
    path('predict/', predict_heart, name='predict_heart'),
    path('details/', heart_detail, name='details'),
]