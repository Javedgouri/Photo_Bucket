# Create your views here.
from django.contrib.auth import logout
from ImageTagging.Tagger.tagger import predict

import os
#import pymongo
#from pymongo import Connection
from pymongo import MongoClient
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect


def uploadImage(request):
    if request.method == 'POST':
        local_dir_uploaded_file(request.FILES['image_file'], str(request.FILES['image_file']))

        client = MongoClient("mongodb://127.0.0.1:27017")
        db = client['photo_bucket']
        collection = db['images']
        filename=str(request.FILES['image_file'])
        img_path = "/Users/javed/PycharmProjects/Photo_Bucket/static/user_images/" + filename
        print(img_path)
        pred = predict(img_path)
        #print(pred)

        # Connection Class
        # connection = Connection('mongodb://127.0.0.1:27017/photo_bucket')
        # db=connection['photo_bucket']
        # collection = db['images']

        # if 'image_scan' in request.FILES.keys():
        # image=request.FILES['file']
        # tags = request.POST['tags']
        username=request.user.username

        tags = []

        for i in pred:
            for a in i:
                tags.append(a[1])

        image = request.FILES['image_file']
        filename=str(request.FILES['image_file'])
        data = {"username": username,"tags":tags, "image_id": filename}
        collection.insert(data)


    # else:
    # data={"about":about,"details":details}
    # collection.insert(data)
    return redirect("main")


# return render_to_response('home/new_narrative.html',{ }, context_instance=RequestContext(request))



def local_dir_uploaded_file(file, filename):
    if not os.path.exists('static/user_images/'):
        os.mkdir('static/user_images/')

    with open('static/user_images/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)



def getImage(request):
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client['photo_bucket']
    collection = db['images']

    username=request.user.username
    search=request.GET["searchTag"]
    getImage_id=collection.find({ "$and": [ { "tags": search }, { "username": username } ] },{"image_id":1,"_id":0})

    return render(request,"home1.html",{"getImage_id_List":getImage_id})


# rendering the image
# def getImage(request):
#     client = MongoClient("mongodb://127.0.0.1:27017")
#     db = client['photo_bucket']
#     collection = db['images']
#     collection1 = db['chunks']
#     search = request.GET['searchTag']
#     fs = gridfs.GridFS(db)
#
#     getImage_id = collection.find({"tags": search}, {"files_id": 1
#         , "_id": 0})
#
#     # return HttpResponse(getImage_id)
#
#     str1 = ""
#     str2 = ""
#     i = 0;
#     dict1 = {}
#     for look in getImage_id:
#         i = i + 1
#         return HttpResponse(db.fs.chunks.find({'files_id': ObjectId('5adcbd48086ecb0424e0aed4')}))
#
#         dict1["id" + str(i)] = str1;
#     return HttpResponse(look)


# return render(request,"display.html",{"dict1":dict1})


# fs=gridfs.GridFS(db)

# image_data = fs.get("5ad603187edbec1d0e336118")
# return HttpResponse(image_data, mimetype="image/png,image/jpeg,image/jpg")


def user_logout(request):
    logout(request)
    return redirect('goto')

def index(request):
    return render(request, 'model.html',{})


def main(request):
    if request.user.is_authenticated:
        client = MongoClient("mongodb://127.0.0.1:27017")
        db = client['photo_bucket']
        collection = db['images']
        username=request.user.username
        # username="javed567@gmail.com"
        image_id=collection.find({"username":username},{"_id":0,"image_id":1})
        return render(request, 'home1.html',{"getImage_id_List":image_id})
    else:
        return redirect("goto")

def index_main(request):
    return render(request,'index.html',{})


def goto(request):
    return render(request,'model.html',{})


def initialRequest(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('http://yahoo.com')
    else:
        return HttpResponseRedirect('http://google.com')