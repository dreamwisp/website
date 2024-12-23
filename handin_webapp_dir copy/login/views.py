from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from templates.login import *
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from login.models import Users,NotConfirmedUsers
# Create your views here.
from handin_webapp import settings
# import settings
import jwt


secret_key = settings.SECRET_KEY

def deleteall(request):
  

    #number_of_users = UsersnoPassword.objects.count()

    #print(f"There are {number_of_users} users in the Users model.")
    Users.objects.get(pk=1).delete()
    return HttpResponse("delete")

def home_usuario(request, context= None):
    user = context.get("user", None)
    
    if user:

        return render(request, 'usuario_home.html', context=context)

 
  


def crear_usuario(request):
    if request.method == "POST":
        print('here')
        print("Request post: ", request.POST)
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = NotConfirmedUsers(
            first_name=first_name, last_name=last_name, email=email,
                     username=username, password=password)
        user.save()
        token = default_token_generator.make_token(user)
        
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        print("uid: ", user.pk)
        confirmation_link = request.build_absolute_uri(
            reverse('setup', kwargs={'uidb64': uid, 'token': token}) # 
        )

        sender_email='virtual.web.operation@gmail.com'

        html_email = render_to_string(
            'login/email.html', {
                'confirmation_link': confirmation_link  
            }
        )
        try:
            send_mail(
                'Message',
                html_email,
                sender_email,
                [email],
                html_message = html_email,  #uno de los repartidos es en caso de que el browser no soporte el html para el correp
                fail_silently= False
            )
            return HttpResponse(f'Un correo ha sido enviado a {email}')
        except Exception as e:
            return HttpResponse("Something went wrong")

    else:
        return render(request, 'login/crear_usuario.html')

def confirm_url(request, uidb64, token):
    uid = urlsafe_base64_decode(uidb64).decode()
    user = NotConfirmedUsers.objects.get(pk=uid)
    
    if user and default_token_generator.check_token(user, token):
        new_user = Users(
            first_name=user.first_name, 
            last_nam =user.last_name, 
            email = user.email, 
            username =user.username, 
            password = user.password)
        new_user.save()
        user.delete()
        context = {'user': new_user}
        HttpResponseRedirect(reversed('user-home',context=context))
    else: 
        HttpResponse("Error with user and token")

def login(request):
    if request.method == 'POST':
        username = request.POST('username')
        password = request.POST('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            return redirect('user-home')
    # form = AuthenticationForm()
    return render(request, 'login/login.html')
"""
def crear_usuario(request):
    user = User.objects.create_user( username, email, password)

    user.primer_nombre = 
    user.apellido ="""