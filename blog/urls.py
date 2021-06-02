from django.urls import path
from .views import blogCreate, blogDelete, blogDetail, blogEdit, blogList, index, blogForm

urlpatterns = [
    path('', index, name="blogs.index"),
    path('all/', blogList, name="blogs.all"),
    path('create/', blogCreate, name="blogs.create"),
    path('<int:id>/', blogDetail, name="blogs.detail"),
    path('delete/<int:id>/', blogDelete, name="blogs.delete"),
    path('edit/<int:id>/', blogEdit, name="blogs.edit"),
]
