from django.urls import path
from .views import index , post_edit , post_detail, post_delete



urlpatterns=[
    path('blog/' ,index ,name="index"),
    path('post_detail/<int:pk>/' ,post_detail ,name="post_detail"),
    path('post_edit/<int:pk>/' ,post_edit ,name="post_edit"),
    path('post_delet/<int:pk>/' ,post_delete ,name="post_delete"),
]

