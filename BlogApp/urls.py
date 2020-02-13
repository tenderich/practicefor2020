from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:writing_id>',views.detail, name="detail"),
    path('new/', views.writingpost, name='new'),
    path('create/', views.create, name='create'),
    path('newwriting/',views.writingpost, name='writingpost')
]