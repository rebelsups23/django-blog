from django.urls import path
from .views import blogList, index

urlpatterns = [
    path('', index, name="blogs.index"),
    path('all/', blogList, name="blogs.all")
]
