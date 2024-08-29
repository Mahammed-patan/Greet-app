from django.shortcuts import render, redirect, reverse
from .models import *
from django.contrib.auth.hashers import make_password, check_password


def index(request):
    return render(request,'app/base.html')

def loginpage(request):
    return render(request,'app/login.html')

def signuppage(request):
    return render(request,'app/signup.html')

def Userlogout(request):
    
    request.session.flush()
    message = 'logged out successfully'
    return redirect(reverse('index'), {'message': message})

def UserRegister(request):
  if request.method == 'POST':
    first_name = request.POST['firstName']
    last_name = request.POST['lastName']
    gender = request.POST.get('selection', '')

    if len(first_name) > 100 or len(last_name) > 100:
      message = 'First name or Last name exceeds character limit (100 characters)'
      return render(request, 'app/signup.html', {'msg': message})

    username = f"{first_name.capitalize()}.{last_name.lower()}"

    if not gender:
      message = 'Please select your gender'
      return render(request, 'app/signup.html', {'msg': message})

    email = request.POST['email']
    raw_password = request.POST['password']
    confirm_password = request.POST['confirmPassword']

    # Check for existing user (same logic applies)
    exist_user = Userinfo.objects.filter(Email=email).exists()

    if exist_user:
      message = 'User already exists'
      return render(request, 'app/signup.html', {'msg': message})

    else:
      if raw_password != confirm_password:
        message = 'Password does not match with Confirm Password'
        return render(request, 'app/signup.html', {'msg': message})

      hashed_password = make_password(raw_password)

      # Create new user with generated username
      new_user = Userinfo.objects.create(
          First_Name=first_name,
          Last_Name=last_name,
          Gender=gender,
          Email=email,
          Username=username,  # Added username field
          Password=hashed_password
      )
      new_user.save()
      message = 'User registered successfully'
      return render(request, 'app/login.html', {'msg': message})

  return render(request, 'app/signup.html')

def UserLogin(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            password = request.POST['password']

            user = Userinfo.objects.get(Email=email)  # Might raise DoesNotExist

            if check_password(password, user.Password):
                request.session['Username'] = user.Username
                request.session['Email'] = user.Email
                if user.Gender:
                    request.session['Gender'] = user.Gender

                return render(request, 'app/home.html')
            else:
                message = 'Password does not match'
                return redirect(reverse('login'), {'msg': message})

        except Userinfo.DoesNotExist:
            message = 'User does not Exist'
            return redirect(reverse('login'), {'msg': message})

    # Handle GET requests or any other cases where there's no POST data
    else:
        # Here you can prepare an empty form or handle other logic for GET requests
        return render(request, 'app/login.html')  # Replace with your login template name
