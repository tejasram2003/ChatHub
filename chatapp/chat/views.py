from django.shortcuts import render,redirect
from chat.models import *
from django.http import HttpResponse,JsonResponse,Http404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User,auth

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('login')

def room(request,room):
    username = request.user.username
    try:
        room_details = Room.objects.get(name=room)
    except Room.DoesNotExist:
        raise Http404()
    return render(request, 'room.html',{'username': username, 'room': room, 'room_details': room_details})

def checkview(request):
    room = request.POST['room_name']
    if Room.objects.filter(name=room).exists():
        return redirect('verify/'+room)
        
    else:
        return redirect('/createroom/'+room)
    
def send(request):
    message = request.POST['message']
    username = request.user.username
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    return HttpResponse('Message sent successfully')

def getMessages(request,room):
    room_details = Room.objects.get(name=room)
    
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})

def createroom(request,room):
    if request.method == 'POST':
        room_name = room
        code = request.POST['code']
        username=request.user.username
        room_details = Room.objects.create(name=room_name,code=code)
        message0 = Message.objects.create(value="Heyyyy welcome to the room!!! Hope y'all have a good time here!",user='WelcomeBot',room = room_details.id)
        url = '/'+room_details.name+'/'
        if username:
            url+='?username='+username
        return redirect(url)
    else:
        return render(request,'create.html',{'room_name':room})
    

def verify(request,room):
    if request.method == 'POST':
        user_code = request.POST['code']
        username = request.user.username
        room = Room.objects.get(name=room)
        real_code = room.code
        if user_code == real_code:
            url = '/'+room.name+'/'
            if username:
                url+='?username='+username
            return redirect(url)
        else:
            messages.info(request,'Incorrect code')
            return redirect('verify/'+room)
    return render(request,'verify.html',{'room':room})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['cpassword']
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,password=password)
                auth.login(request,user)
                return redirect('/')
        else:
            messages.info(request,'Passwords do not match')
            return redirect('signup')

    return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if User is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Username not registered')
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')


    
