from django.urls import path
from .views import blogList, index, blogDetail

urlpatterns = [
    path('', index, name="blogs.index"),
    path('all/', blogList, name="blogs.all"),
    path('<int:id>/', blogDetail, name="blogs.detail"),
]
