from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages

from django.contrib.auth.models import Group, Permission
from django.contrib.auth.decorators import user_passes_test
from .models import CustomUser

from .forms import CustomUserCreationForm


# Verifica si el usuario es admin
def is_admin(user):
    return user.is_superuser

# Decora la funcion y si es super usuario, esta se ejecuta
@user_passes_test(is_admin)
def manage_groups(request):
    groups = Group.objects.all()

    context = {
        'groups': groups
    }

    return render(request, 'manage-admin/manage_groups.html', context)

@user_passes_test(is_admin)
def add_group(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        permissions = request.POST.getlist('permissions')
        users = request.POST.getlist('users')

        group, created = Group.objects.get_or_create(name=group_name)

        if permissions:
            group.permissions.set(Permission.objects.filter(id__in=permissions))

        if users:
            for user_id in users:
                user = CustomUser.objects.get(id=user_id)
                user.groups.add(group)

        return redirect('manage_groups')
    all_permissions = Permission.objects.all()
    all_users = CustomUser.objects.all()
    all_groups = Group.objects.all()

    context = {
        'permissions': all_permissions,
        'users': all_users,
    }
    return render(request, 'manage-admin/add_group.html', context)
 
# Editar Grupos
@user_passes_test(is_admin)
def edit_group(request, pk):
    group = get_object_or_404(Group, pk=pk)

    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        permissions = request.POST.getlist('permissions')
        users = request.POST.getlist('users')

        if group_name:
            group.name = group_name
            group.save()

        if permissions:
            valid_permissions = Permission.objects.filter(id__in=permissions)
            group.permissions.set(valid_permissions)
        else:
            group.permissions.clear()

        if users:
            valid_users = CustomUser.objects.filter(id__in=users)
            group.user_set.set(valid_users)
        else:
            group.user_set.clear()

        return redirect('manage_groups')

    all_permissions = Permission.objects.all()
    all_users = CustomUser.objects.all()
    context = {
        'group': group,
        'permissions': all_permissions,
        'group_permissions': group.permissions.all(),
        'users': all_users,
        'group_users': group.user_set.all()
    }
    return render(request, 'manage-admin/update_group.html', context)

# Eliminar grupos
@user_passes_test(is_admin)
def delete_group(request, pk):
    group = get_object_or_404(Group, pk=pk)

    if request.method == 'POST':
        group.delete()
        return redirect('manage_groups')
    return render(request, 'manage-admin/confirm_detele_group.html', {'group':group})


# Formulario de registro para usuario
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
