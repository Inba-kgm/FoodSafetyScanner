from django.shortcuts import render,redirect
from . models import *
import random,smtplib
from email.message import EmailMessage
from django.contrib.auth import authenticate

# Create your views here.
def login(request):
  error={
        'err':"",
    }
  if request.method == "POST":
    email=request.POST.get('email')
    password=request.POST.get('password')
    user= register.objects.filter(Email=email,Password=password).exists()
    if user:
      user=register.objects.get(Email=email,Password=password)
      request.session['myname']=user.Username
      request.session['mymail']=email
      request.session['mypass']=password
      data={
          'username':user.Username,
          'password':password,
          'email':email,
      }
      return render(request,"index.html",data)
    else:
        error={
            "err":"User doesn't exist"
        }
  return render(request,'login/login.html',error)
  
def otpgen(request):
    error={'err':''}
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')

        usr=register.objects.filter(Username=username,Password=password).exists()
        if usr:
             error={"err":'*user already exists'}
             return render(request,'login/login.html',error)
        
        usr=register.objects.filter(Email=email).exists()
        if usr:
            error={"err":'*Email already exists'}
            return render(request,'login/login.html',error)
        
        otp=''

        for i in range(6):
            otp+=str(random.randint(0,6))
        
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        from_mail='phantom.dragon.43@gmail.com'
        to_mail=email

        server.login(from_mail,'asst skdu igij nluc')
        

        msg=EmailMessage()
        msg['Subject']="OTP Verification"
        msg['From']=from_mail
        msg['To']=to_mail

        msg.set_content('Your OTP is : '+ otp)
        server.send_message(msg)
        sent='OTP sent'
        data={
            'username':username,
            "password":password,
            "email":email,
            "otp":otp,
        }
        return render(request,'login/otpverify.html',data)
    return render(request,'login/login.html',{"err":"*OTP Mismatch"})
def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get("email")
        otpgen=request.POST.get('otpgen')
        otpinp=request.POST.get('otpinp')
        if otpgen==otpinp:
            request.session['myname']=username
            request.session['mypass']=password
            request.session['mymail']=email
            register.objects.create(Username=username,Password=password,Email=email)
            data={
                'username':username,
                "password":password,
                "email":email
            }
            return render(request,'index.html',data)
        return render(request,'login/login.html',{'err':"*OTP Mismatch"})
    return render(request,'login/login.html',{'err':"*OTP Mismatch"})
    
def logout(request):
    request.session['myname']=""
    request.session["mypass"]=""
    request.session['mymail']=""
    return render(request,'login/login.html',{"err":"Logged out Successfully"})

def forgotpass(request):
    error={
        "err":""
    }
    if request.method=="POST":
        email=request.POST.get("email")
        usr=register.objects.filter(Email=email).exists()
        if usr:
            otp=''
            usr=register.objects.get(Email=email)
            username=usr.Username
            password=usr.Password

            for i in range(6):
                otp+=str(random.randint(0,6))
            
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            from_mail='phantom.dragon.43@gmail.com'
            to_mail=email

            server.login(from_mail,'asst skdu igij nluc')
            

            msg=EmailMessage()
            msg['Subject']="OTP Verification"
            msg['From']=from_mail
            msg['To']=to_mail

            msg.set_content('Your OTP is : '+ otp)
            server.send_message(msg)
            data={
                "email":to_mail,
                "otp":otp,
                "username":username,
                "password":password,
            }
            return render(request,"login/logotpverify.html",data)
        else:
            error={
                "err":"User doesn't exist"
            }
    return render(request,'login/forgotpass.html',error)

def createpass(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    email=request.POST.get("email")
    otpgen=request.POST.get('otpgen')
    otpinp=request.POST.get('otpinp')
    if otpgen==otpinp:
        data={
                "email":email,
                "username":username,
                "password":password,
            }
        return render(request,'login/createpass.html',data)
    else:
        return render(request,'login/forgotpass.html',{"err":"OTP Mismatch"})
    return render(request,'login/forgotpass.html')

def newpass(request):
    username=request.POST.get('username')
    password=request.POST.get('pass')
    cpassword=request.POST.get('cpass')
    email=request.POST.get("email")
    if password==cpassword:
        request.session['myname']=username
        request.session['mypass']=password
        request.session['mymail']=email
        usr=register.objects.get(Email=email)
        usr.Password=password
        usr.save()
        
        return redirect("/logic/")
    return render(request,"login/createpass.html",{"err":"Password Mismatch"})