from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getapi/<int:pk>/', views.get_api),
    path('postapi/', views.post_api),
    path('putapi/<int:pk>', views.put_api),
    path('patchapi/<int:pk>', views.patch_api),
    path('deleteapi/<int:pk>', views.delete_api),
]
