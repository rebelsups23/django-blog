from django.urls import path
from .views import blogCreate, blogDetail, blogList, index, blogForm

urlpatterns = [
    path('', index, name="blogs.index"),
    path('all/', blogList, name="blogs.all"),
    path('create/', blogCreate, name="blogs.create"),
    path('<int:id>/', blogDetail, name="blogs.detail"),
]
