from django.shortcuts import render, HttpResponse, redirect
from .models import Registration
from django.conf import settings
from .serializers import UserSerializer, RegistrationSerializer
# This Function is home page function
def home(request):
    return render(request, 'registration.html')


# This Function is Registration page stored data in database
def registration(request):
    if request.method == 'POST':
        password = request.POST['password']
        repassword = request.POST['confirm_password']
        if password == repassword:
            full_name = request.POST['full_name']
            dob = request.POST['dob']
            phone = request.POST['phone']
            email = request.POST['email']
            passport_no = request.POST['passport']
            image = request.FILES.get('image')
            reg = Registration(full_name=full_name, dob=dob, phone=phone, email=email, passport_no=passport_no, image=image,
                           password=password, repassword=repassword)
            reg.save()
            success = "Successfully Registered"
    else:
        return HttpResponse("This is Get Request")
    return render(request, 'registration.html', {'success': success})


# This Function is used for login using header
def Login(request):
    if request.method == 'POST':
        number = request.POST['uname']
        password = request.POST['psw']
        data = Registration.objects.filter(phone=number, password=password)
        if not data:
            error = "Please Check our Username and Password"
            return render(request, 'login.html', {'error': error})
        else:
            request.session['session'] = 'Shivam'
            da = Registration.objects.get(phone=number)
            success = "Successfully you are logged In."
            return render(request, 'logout.html', {'success': success, 'data': da, 'media_url': settings.MEDIA_URL})
    return render(request, 'login.html')


# This Function is used for logout
def Logout(request):
    if request.method == 'POST':
        del request.session
    return redirect('/login')



# This is RestFul API
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        number = request.data.get('uname')
        password = request.data.get('psw')
        data = Registration.objects.filter(phone=number, password=password)
        if not data:
            Response({'error': "your username or password is incorrect "})
        else:
            return Response({'success': 'you are successfull logged in.'})

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class RegisterView(APIView):
    def post(self, request):
        serialized = RegistrationSerializer(data=request.DATA)
        if serialized.is_valid():
            User.objects.create_user(
                serialized.init_data['full_name'],
                serialized.init_data['dob'],
                serialized.init_data['phone'],
                serialized.init_data['email'],
                serialized.init_data['passport_no'],
                serialized.init_data['image'],
                serialized.init_data['password'],
                serialized.init_data['repassword']
            )
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
