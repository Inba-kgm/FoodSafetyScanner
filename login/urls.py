from django.urls import path,include
from . views import*

urlpatterns = [
    path('',login,name="login"),
    path('otpgen/',otpgen,name="otpgen"),
    path('createpass/',createpass,name="createpass"),
    path('newpass/',newpass,name="newpass"),
    path('signup/',signup,name="signup"),
    path('logout/',logout,name="logout"),
    path('forgotpass/',forgotpass,name="forgotpass"),
]
