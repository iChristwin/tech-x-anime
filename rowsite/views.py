from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *
from .decorators import unauthenticated_user, allowed_users, admin_only


@login_required(login_url='login')

def home(request):
    customers = Customer.objects.all()
    groups = Groups.objects.all()
    specialization = Specialization.objects.all()

    total_customers = customers.count()
    total_anime = specialization.filter(level='Anime').count()
    total_tech = specialization.filter(level='Tech').count()
    total_crypto = specialization.filter(level='Crypto').count()
    total_design = specialization.filter(level='Graphics').count()

    context = {'groups': groups, 'customers': customers, 'specialization':specialization, 'total_customers': total_customers,
               'total_anime': total_anime, 'total_tech':total_tech, 'total_crypto': total_crypto, 'total_design':total_design}
    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
def techxanime(request):
    return render(request, 'accounts/techxanime.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def groups(request):
    groups = Groups.objects.all()
    context = {'groups': groups}
    return render(request, 'accounts/groups.html', context)

@login_required(login_url='login')
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    group = Groups.objects.filter(id=pk)
    customergp = customer.specialization_set.all()
    context = {'customer':customer,'group':group, 'customergp':customergp}
    return render(request, 'accounts/customer.html', context)





def anime(request):
    return render(request, 'accounts/anime.html')


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')


            messages.success(request, 'TechClan account was created for ' + username )
            return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('/')
            return redirect('customer', user.customer.id)
        else:
            messages.info(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def createSpecialization(request, pk):
    customer = Customer.objects.get(id=pk)
    form = SpecializationForm(initial={'customer':customer})
    if request.method == 'POST':
    # print('printing Post:', request.POST)
        form = SpecializationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer', pk)


    context = {'form':form, 'customer':customer }
    return render(request, 'accounts/specialization_form.html', context)


@login_required(login_url='login')
def updateSpecialization(request,pk):

    same = Specialization.objects.get(id=pk)
    form = SpecializationForm(instance=same)
    if request.method == 'POST':
        form = SpecializationForm(request.POST, instance=same)
        if form.is_valid():
            form.save()
            return redirect('customer', request.user.customer.id)

    context = {'form':form}

    return render(request, 'accounts/specialization_form.html', context)


@login_required(login_url='login')
def deleteSpecialization(request, pk):
    same = Specialization.objects.get(id=pk)
    if request.method == 'POST':
        same.delete()
        return redirect('customer', request.user.customer.id)
    context = {'item':same}
    return render(request, 'accounts/delete.html', context)

@login_required(login_url='login')
def userPage(request):

    special = request.user.customer.specialization_set.all()
    context = {'special':special}
    return render(request, 'accounts/user.html', context)