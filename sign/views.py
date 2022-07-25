from django.db import connection
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Users
from django.contrib import messages


# Create your views here.
def signup_login(request):
    return render(request, 'login_signup.html')


def signup(request):
    name = request.POST.get("name")
    psw = request.POST.get("psw")
    email = request.POST.get("email")
    mobile = request.POST.get("mob")
    address = request.POST.get("line1")
    city=request.POST.get("city")
    state=request.POST.get("state")
    country=request.POST.get("country")
    pincode=request.POST.get("pincode")
    user_type=request.POST.get("user")
    username=request.POST.get("username")
    if Users.objects.filter(Email=email).exists():
        return render(request, 'login_signup.html')                  ####### Need to improve
    else:
        users = Users(name=name, mob=mobile, line1=address, Email=email, password=psw,city=city,country=country,state=state,pincode=pincode,user_type=user_type,username=username)
        users.save()
        Id = Users.objects.filter(Email=email)[0].id
        messages.success(request, 'Signup Success')         ############
        return render(request, 'index.html',{'user_id':Id})


def signin(request):
    psw = request.POST.get("psw")
    email = request.POST.get("email")
    cursor = connection.cursor()
    query1 = "select * from sign_users where Email='" + email + "'"
    cursor.execute(query1)
    data = cursor.fetchone()
    query2 = "select * from sign_appointment where user_id='" + str(data[0]) + "'"
    cursor.execute(query2)
    data1 = cursor.fetchone()
    if data[4]==psw:
        data= {'user_id':data[0],'Name':data[1],'Contact_number':data[2],'Address':data[8],'Email':data[3],'Password':data[4],'Pincode':data[9],'State':data[10],'user_type':data[11],'username':data[12]}
               # 'appointment_id':data1[0],'timedate':data1[1],'worker_id':data[4]}
        return render(request,'profile.html',data)
    else:
        return redirect('signup_login')
