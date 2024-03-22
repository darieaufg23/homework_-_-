from django.contrib import admin
from django.urls import path
from . views import ProductList, ProductDetail, ProductEdit
# from . views import index, detail, create, create_comment

urlpatterns = [
    path("", ProductList.as_view(), name="list"),
    path("<int:pk>/detail", ProductDetail.as_view(), name="detail"),
    path("<int:pk>/edit", ProductEdit.as_view(), name="edit"),
    # path('', index, name="index"),
    # path('<int:post_id>', detail, name="detail"),
    # path('create/', create, name="create"),
    # path('create_comment/<int:post_id>', create_comment, name="create_comment"),
]
