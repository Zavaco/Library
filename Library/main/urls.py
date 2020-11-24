from django.urls import path, include
from. import views
urlpatterns = [
    path('', views.main, name='home'),
    path('userform/', views.UserFormView.as_view(), name='userform'),
    path('success/', views.success, name='success'),
    path('libuser/', views.lib_user, name='libuser'),
]