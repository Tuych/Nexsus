from django.urls import path
from . import views

urlpatterns=[
    path('list/', views.blog_list, name='blog_list'),
    path('<int:pk>/detail/',views.blog_detail,name='blog_detail')
]