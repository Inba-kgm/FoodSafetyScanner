from django.shortcuts import render,redirect
import random
from login.models import register
# Create your views here.
def home(request):
    return render(request,"index.html")

def generate(request):
    data = ['Healthy','Avoid it','Avoid it','Healthy','Avoid it','Avoid it','Healthy','Avoid it']
    value = random.randint(0,7)
    output = data[value]
    username=request.POST.get('username')
    password=request.POST.get('password')
    email=request.POST.get("email")
    usr=register.objects.filter(Email=email).exists()
    if usr:
        usr=register.objects.get(Email=email)
        if output == "Healthy":
            usr.Healthy=usr.Healthy+1
        usr.Total=usr.Total+1
        usr.save()
        Heal=usr.Healthy
        tot=usr.Total
        unheal=tot-Heal
    outp={
            'username':username,
            "password":password,
            "email":email,
            "out":output,
            "heal":Heal,
            "unheal":unheal,
        }

    return render(request,"index.html",outp)