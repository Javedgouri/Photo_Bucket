from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from user.forms import UserForm
# Create your views here.
from user.forms import PictureForm
from user.models import Picture

import os
import gridfs
#import pymongo
from django.http import HttpResponse
#from pymongo import Connection
from pymongo import MongoClient
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, RequestContext,loader
from bson import ObjectId


def uploadImage(request):
    if request.method == 'POST':
        local_dir_uploaded_file(request.FILES['file'], str(request.FILES['file']))

        client = MongoClient("mongodb://127.0.0.1:27017")
        db = client['photo_bucket']
        collection = db['images']

        # Connection Class
        # connection = Connection('mongodb://127.0.0.1:27017/photo_bucket')
        # db=connection['photo_bucket']
        # collection = db['images']

        # if 'image_scan' in request.FILES.keys():
        # image=request.FILES['file']
        # tags = request.POST['tags']
        tags = ["haris", "arman"]
        image = request.FILES["file"]
        fs = gridfs.GridFS(db)
        file_id = fs.put(image, filename="shahbaz")
        return HttpResponse(file_id)
        data = {"username": "photo_bucket", "tags": tags, "files_id": file_id}
        collection.insert(data)
    # else:
    # data={"about":about,"details":details}
    # collection.insert(data)
    return redirect("main")


# return render_to_response('home/new_narrative.html',{ }, context_instance=RequestContext(request))


def local_dir_uploaded_file(file, filename):
    if not os.path.exists('Images/'):
        os.mkdir('Images/')

    with open('Images/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


# rendering the image
def getImage(request):
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client['photo_bucket']
    collection = db['images']
    collection1 = db['chunks']
    search = request.GET['searchTag']
    fs = gridfs.GridFS(db)

    getImage_id = collection.find({"tags": search}, {"files_id": 1
        , "_id": 0})

    # return HttpResponse(getImage_id)

    str1 = ""
    str2 = ""
    i = 0;
    dict1 = {}
    for look in getImage_id:
        i = i + 1
        return HttpResponse(db.fs.chunks.find({'files_id': ObjectId('5adcbd48086ecb0424e0aed4')}))

        dict1["id" + str(i)] = str1;
    return HttpResponse(look)


# return render(request,"display.html",{"dict1":dict1})


# fs=gridfs.GridFS(db)

# image_data = fs.get("5ad603187edbec1d0e336118")
# return HttpResponse(image_data, mimetype="image/png,image/jpeg,image/jpg")


def register(request):

    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
        else:
            print(user_form.errors)

        return redirect('goto')

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
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
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
    return redirect('goto')


def main(request):
    return render(request,'home1.html',{})


def home(request):
    return render(request,'home1.html',{})


def savePicture(request):
    saved = False

    if request.method == "POST":
        # Get the posted form
        MyPictureForm = PictureForm(request.POST, request.FILES)

        if MyPictureForm.is_valid():
            picture1 = Picture()
            picture1.picture = request.FILES['picture']
            picture1.save()
            saved = True
    else:
        MyPictureForm = PictureForm()

    return redirect("home")


