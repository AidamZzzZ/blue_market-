from django.urls import path
from .views import (
    SignUpView, 
    manage_groups, 
    delete_group,
    edit_group,
    add_group,
)

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("manage-groups/", manage_groups, name="manage_groups"),
    path("add-group/", add_group, name="add_group"),
    path("edit-group/<pk>", edit_group, name="edit_group"),
    path("delete-group/<pk>", delete_group, name="delete_group"),
]


