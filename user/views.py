from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from user.forms import UserForm
# Create your views here.


def register(request):

    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
        else:
            print(user_form.errors)

        return redirect('register')

    else:
        user_form = UserForm()

    return render(request, 'model.html',
                  {
                      'user_form':user_form
                  })


def user_login(request):
    if request.method  == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username , password = password)
        if user:
            if user.is_active:
                login(request , user)
                return redirect('main')
            else:
                return HttpResponse('You dont have an account with us')
        else:
            print("Invalid Login Details: {0} , {1}".format(username , password))
            return HttpResponse('Invalid Login Details ')

    else:
        return render(request, 'model.html', {})


def user_logout(request):
    logout(request)
    return redirect('login')

def main(request):
    return render(request,'home.html',{})