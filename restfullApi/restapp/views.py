from django.shortcuts import render

from rest_framework.response import Response
from .models import student , course , enrolled
from .serializer import studentSeriaizer , courseSerializer , enrolledSerializer
from rest_framework.decorators import api_view
import json

from django.conf import settings
from django.core.mail import send_mail
import random


# ---------------------------------     STUDENT SECTION  ---------------------------------------------

# ============================= EMAIL SENDING TO USER FOR VERIFICATION ==================
def send_account_activation_email(email , email_token): 
    subject = 'Your account needs to be verified'
    email_from = settings.EMAIL_HOST_USER
    message = str(email_token)
    send_mail(subject , message , email_from , [email])


def  send_email_token( reciever_email  ):
    try:        
        email_token =  random.randint(0000,9999)
        std_obj = student.objects.get(email=reciever_email)
        std_obj.email_token = email_token
        std_obj.save()
        email = reciever_email
        send_account_activation_email(email , email_token)
    except Exception as e:
        print(e)
# ==================================   ENDS  ====================================


# ======================== REGISTER STUDENTS =====================================

@api_view(['POST'])
def register(request):
    request_data = json.loads(request.body)
    seriaizer = studentSeriaizer(data=request.data)
    if seriaizer.is_valid():
        seriaizer.save()
        send_email_token(request_data['email'])
        return Response({'status :' : '200' ,'Message':'An Email has been sent to your email !', 'Data': seriaizer.data})
    return Response({'status':'400','data':'something went wrong'})   



# ====================================  VARIFYING STUDENT EMAILS ====================

@api_view(['POST'])
def varifyStudent(request):
    request_data = json.loads(request.body)
    std = student.objects.get(email=request_data['email'])
    if std:
        if std.email_token == request_data['email_token']:
            std.is_email_varified = True
            std.save()
            return Response({'status':'200','Message':'User has been varified.'})
        return Response({'status':'401','Message':'Invalid Varification Code'})

# ===============================  GETTING STUDENT RECORD FROM DB ======================

@api_view(['GET'])
def getStudent(request):
    data = student.objects.all()
    serliazer = studentSeriaizer(data , many=True)
    return Response(serliazer.data)

# ===============================  LOGIN METHOD ==========================================

@api_view(['POST'])
def login(request):
    request_data = json.loads(request.body)
    student_obj = student.objects.filter(email = request_data['email'] , password = request_data['password'])
    if student_obj.exists():
        return Response({'status':'200','Message': 'Login Successfully '})
    return Response({'status':'404' , 'Message':'Username or password is invalid ..'})


# ==============================   RESET PASSWORD REQUEST ===============================

@api_view(['POST'])
def restPasswordRequest(request):
    request_data = json.loads(request.body)
    std_obj = student.objects.filter(email = request_data['email'])
    if std_obj.exists():
        send_email_token(request_data['email'])
        return Response({'status :' : '200' ,'Message':'An Email has been sent to your email !'})
    return Response({'status':'404','Message':'Account with this email not found !'})

# =============================  RESET PASSWORD  =============================

@api_view(['POST'])
def resetPassword(request):
    request_data = json.loads(request.body)
    studentobj = student.objects.get(email=request_data['email'])
    if studentobj.email_token == request_data['email_token']:
        studentobj.password = request_data['password']
        studentobj.save()
        return Response({'status':'200' , 'Message':'Password updated successfuly !'})
    return Response({'status':'404' , 'Message':'Invalid varification code!'})


@api_view(['GET'])
def getStudentById(request , rollnum):
    print(rollnum)
    student_Data = student.objects.get(rollnum = rollnum)
    if student_Data:
        serializer = studentSeriaizer(student_Data)
        return Response({'status':'200','Data':serializer.data})
    return Response({'status':'404', 'Message':'Not found'})



# ---------------------------------   STUDENT SECTION ENDS  ---------------------------------------













# =============================  CREATING NEW COURSE  ======================================

@api_view(['POST'])
def createCourse(request):
    seriaizer = courseSerializer(data=request.data)
    if seriaizer.is_valid():
        seriaizer.save()
        return Response({'status':'200' , 'Message':'Course Created Successfully .' , 'Data':seriaizer.data})
    return Response({'status':'404','Message':'Something went wrons'})



# ================================   GETTING ALL COURSES  ====================================

@api_view(['GET'])
def getCourses(request):
    data = course.objects.all()
    seriliazer = courseSerializer(data , many=True)
    return Response(seriliazer.data)


# ================================== ENROLL STUDENT IN COURSES =========================

@api_view(['POST'])
def assignCourse(request):
    data = enrolledSerializer(data=request.data)
    if data.is_valid():
        data.save()
        return Response({'status': '200' , 'Message':'Course has been Assigned to student' , 'data':data.data})
    return Response({'status':'401' , 'Message':'Course did not assign to student'})