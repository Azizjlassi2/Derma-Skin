from django.shortcuts import render, redirect
from django.http import JsonResponse

#authentification
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required

from Accounts.models import AppUser













@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        # Extract credentials from request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate for super users
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login user and redirect to homepage
            if user.is_superuser:
                login(request, user)
                return redirect("/admin/")
            else:
                return  redirect('Home')
        else:
            # Return error message
            messages.error(request,('There was a Error in Login ! '))
            return redirect('login_page')
   
    return render(request,'Auth/login.html',{})


def logout_user(request):
    logout(request)
    return redirect('login_page')

@unauthenticated_user
def register(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')

        if data.get('age'):
            age = data.get('age')

        user_type = "Patient"
        genre = data.get('genre')
        gouvernorat = data.get('gouvernorat')
        city = data.get('city')
        email = data.get('email')
        password = data.get('password')
    
        profil_image = request.FILES.get('profil_image')
        
        try:
            user = AppUser.objects.create_user(email=email, username=username, age=age, user_type=user_type, genre=genre, gouvernorat=gouvernorat, city=city, password=password,profil_image=profil_image)
            user.save()
            

            return redirect('login_page')
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})


    
    
    return render(request,'Auth/index.html',{})





def register_doctor(request):
    
    if request.method == 'GET':
        return render(request,'Auth/DoctorAuth/index.html',{})
    

    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        age = data.get('age')
        genre = data.get('genre')
        gouvernorat = data.get('gouvernorat')
        city = data.get('city')
        email = data.get('email')
        number = data.get('degree_image')
        password = data.get('password')

        from .models import DoctorRequest

        doctor_request = DoctorRequest()
        
        doctor_request.doctor_age = age
        doctor_request.doctor_city = city
        doctor_request.doctor_email = email
        doctor_request.doctor_gouvernerat = gouvernorat
        doctor_request.doctor_name = username
        doctor_request.doctor_genre = genre
        doctor_request.doctor_phone = number
        doctor_request.doctor_password = password
        doctor_request.save()
        
        return render(request,'Auth/DoctorAuth/succes.html',{})


@login_required
def my_account(request):
    
    if request.method == 'GET':
        return render(request,"Pages/account.html",{})
    
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        age = data.get('age')
        genre = data.get('genre')
        gouvernorat = data.get('gouvernorat')
        city = data.get('city')
        email = data.get('email')
        number = data.get('number')
        password = data.get('password')

        user = AppUser.objects.get(pk= request.user.id)

        user.change_username(username)
        user.change_email(email)
        user.change_age(age)
        user.change_genre(genre)
        user.change_gouvernorat(gouvernorat)
        user.change_city(city)
        user.set_password(password)
        if user.user_type=='Doctor':
            user.change_number(number)
        user.save()
        login(request,user)
        messages.success(request,("We've saved your profile changes."))
        return render(request,"Pages/account.html",{})


        


