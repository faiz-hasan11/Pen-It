from django.urls import path,include
from blogs import views

urlpatterns = [
    path('create',views.create,name='create'),
    path('<int:blog_id>',views.detail,name='detail'),
    path('<int:blog_id>/delete', views.delete_view,name='delete_view' ),
    ]
