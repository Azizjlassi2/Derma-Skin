
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# rest framework
from rest_framework.response import Response as R
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view




from django.contrib.auth import authenticate,logout,login







from Accounts.models import AppUser,DoctorRequest
from Site.models import *
from .serializers import *

@api_view(["GET"])
def get_routes(request):
    routes = [
        {
            "Endpoint":'/doctors/',
            "method": 'GET',
            'body':None,
            'Description': "Returns all the doctors"
        },
         {
            "Endpoint":'/doctors/<pk>/',
            "method": 'GET',
            'body':None,
            'Description': "Returns a doctor with the specific pk"
        },
         {
            "Endpoint":'/login/user/',
            "method": 'POST',
            'body':{
                "username":"the name of the user ",
                "password":"the password of the user "
            },
            'Description': "Invoke the Login System "
        },
         {
            "Endpoint":'/logout/user/',
            "method": 'POST',
            'body':None,
            'Description': "Invoke the Logout System"
        },
          {
            "Endpoint":'/register/user/',
            "method": 'POST',
            'body':{
             "username"      :"the name of the user ",
             "password"      :"the password of the user ",
             "email"         :"the email of the user ",
             "gouvernorat"   :"the gouvernorat of the user ",
             "city"          :"the city of the user ",
             "age"           :"the age of the user ",
             "profil_image"  :"the profil image of the user ",
             "genre"         :"the gender of the user ",
             
            },
            'Description': "Invoke the Registration System"
        },


    ]
    return R(routes)

@api_view(["GET"])
def get_doctors(request,pk=None):
    if request.method == 'GET' and pk == None:
        doctors = AppUser.objects.filter(user_type="Doctor").order_by("-created")
        doctors_serializer = AppUserSerializers(doctors,many=True)
        return R(doctors_serializer.data)
    
    elif request.method == 'GET' and pk != None:
        try:
            doctor = AppUser.objects.get(id=pk)
        except AppUser.DoesNotExist:
            return R('Doctor Does Not Exist')
        doctor_serializer = AppUserSerializers(doctor)
        return R(doctor_serializer.data)

@api_view(["POST"])
def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password') 

    # Authenticate for users
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
        return R("User Is Authenticated",status=status.HTTP_200_OK)
    else:
        return R("User Is Not Authenticated",status=status.HTTP_400_BAD_REQUEST)
        
@api_view(["POST"])
def logout_user(request):
    logout(request)
    return R("User Is Log Out",status=status.HTTP_200_OK)

@api_view(["POST"])
def register_user(request):
        data = request.POST
        username = data.get('username')

        if data.get('age'):
            age = data.get('age')

        user_type = "Patient"
        genre = data.get('genre')
        gouvernorat = data.get('gouvernorat')
        city = data.get('city')
        email = data.get('email')
        password = data.get('password')
    
        profil_image = request.FILES.get('profil_image')
        
        try:
            user = AppUser.objects.create_user(email=email, username=username, age=age, user_type=user_type, genre=genre, gouvernorat=gouvernorat, city=city, password=password,profil_image=profil_image)
            user.save()
            return R("User Is Created",status=status.HTTP_200_OK)       
        except Exception as e:
            return R("There Was A Problem In Creating User ",status=status.HTTP_400_BAD_REQUEST)

       



class AppUsersView(APIView):

    def get(self,request,format=None):

        appusers = AppUser.objects.all().order_by("-created")
        appuser_serializer = AppUserSerializers(appusers,many=True)
        return R(appuser_serializer.data)
        
           
    
    def  post(self,request,format=None):
        appuser_serializer = AppUserSerializers(data=request.data)
        if appuser_serializer.is_valid():
            appuser_serializer.save()
            return R(appuser_serializer.data, status=status.HTTP_201_CREATED)
        return R(appuser_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class AppUserView(APIView):

    def get(self,request,pk,format=None):
        try:
            appuser= AppUser.objects.get(id=pk)
        except AppUser.DoesNotExist:
            return R('User Does Not Exist')
            
        appuser_serializer = AppUserSerializers(appuser)
        return R(appuser_serializer.data)

    def put(self, request, pk, format=None):
        try:
            appuser = AppUser.objects.get(id=pk)
        except AppUser.DoesNotExist:
            return R('User Does Not Exist')
            
        appuser_serializer = AppUserSerializers(appuser, data=request.data)
        if appuser.is_valid():
            appuser_serializer.save()
            return R(appuser_serializer.data)
        return R(appuser_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        try:
            appuser = AppUser.objects.get(id=pk)
        except AppUser.DoesNotExist:
            return R('User Does Not Exist')
        appuser.delete()
        return R(status=status.HTTP_204_NO_CONTENT)




class QuestionsView(APIView):

    def get(self,request,format=None):

        questions = QuestionQCM.objects.all()
        questions_serializer = QuestionQCMSerializers(questions,many=True)
        return R(questions_serializer.data)
        
           
    
    def  post(self,request,format=None):
        questions_serializer = QuestionQCMSerializers(data=request.data)
        if questions_serializer.is_valid():
            questions_serializer.save()
            return R(questions_serializer.data, status=status.HTTP_201_CREATED)
        return R(questions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class QuestionView(APIView):

    def get(self,request,pk,format=None):
        try:
            questions= QuestionQCM.objects.get(id=pk)
        except QuestionQCM.DoesNotExist:
            return R('QuestionQCM Does Not Exist')
            
        questions_serializer = QuestionQCMSerializers(questions)
        return R(questions_serializer.data)

    def put(self, request, pk, format=None):
        try:
            questions = QuestionQCM.objects.get(id=pk)
        except QuestionQCM.DoesNotExist:
            return R('QuestionQCM Does Not Exist')
            
        questions_serializer = QuestionQCMSerializers(questions, data=request.data)
        if questions.is_valid():
            questions_serializer.save()
            return R(questions_serializer.data)
        return R(questions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        try:
            questions = QuestionQCM.objects.get(id=pk)
        except QuestionQCM.DoesNotExist:
            return R('QuestionQCM Does Not Exist')
        questions.delete()
        return R(status=status.HTTP_204_NO_CONTENT)



class  DescriptionsView(APIView):

    def get(self,request,format=None):

        descriptions = Description.objects.all()
        descriptions_serializer = DescriptionSerializers(descriptions,many=True)
        return R(descriptions_serializer.data)
        
           
    
    def  post(self,request,format=None):
        descriptions_serializer = DescriptionSerializers(data=request.data)
        if descriptions_serializer.is_valid():
            descriptions_serializer.save()
            return R(descriptions_serializer.data, status=status.HTTP_201_CREATED)
        return R(descriptions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class DescriptionView(APIView):

    def get(self,request,pk,format=None):
        try:
            descriptions= Description.objects.get(id=pk)
        except Description.DoesNotExist:
            return R('description Does Not Exist')
            
        descriptions_serializer = DescriptionSerializers(descriptions)
        return R(descriptions_serializer.data)

    def put(self, request, pk, format=None):
        try:
            descriptions = Description.objects.get(id=pk)
        except Description.DoesNotExist:
            return R('description Does Not Exist')
            
        descriptions_serializer = DescriptionSerializers(descriptions, data=request.data)
        if descriptions.is_valid():
            descriptions_serializer.save()
            return R(descriptions_serializer.data)
        return R(descriptions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        try:
            descriptions = Description.objects.get(id=pk)
        except Description.DoesNotExist:
            return R('description Does Not Exist')
        descriptions.delete()
        return R(status=status.HTTP_204_NO_CONTENT)



class  ResultsView(APIView):

    def get(self,request,format=None):

        results = Result.objects.all()
        results_serializer = ResultSerializers(results,many=True)
        return R(results_serializer.data)
        
           
    
    def  post(self,request,format=None):
        results_serializer = ResultSerializers(data=request.data)
        if results_serializer.is_valid():
            results_serializer.save()
            return R(results_serializer.data, status=status.HTTP_201_CREATED)
        return R(results_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class ResultView(APIView):

    def get(self,request,pk,format=None):
        try:
            results= Result.objects.get(id=pk)
        except Result.DoesNotExist:
            return R('Result Does Not Exist')
            
        results_serializer = ResultSerializers(results)
        return R(results_serializer.data)

    def put(self, request, pk, format=None):
        try:
            results = Result.objects.get(id=pk)
        except Result.DoesNotExist:
            return R('Result Does Not Exist')
            
        results_serializer = ResultSerializers(results, data=request.data)
        if results_serializer.is_valid():
            results_serializer.save()
            return R(results_serializer.data)
        return R(results_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        try:
            results = Result.objects.get(id=pk)
        except Result.DoesNotExist:
            return R('Result Does Not Exist')
        results.delete()
        return R(status=status.HTTP_204_NO_CONTENT)



class  DoctorRequestsView(APIView):

    def get(self,request,format=None):

        doctor_requests = DoctorRequest.objects.all()
        doctor_requests_serializer = DoctorRequestSerializers(doctor_requests,many=True)
        return R(doctor_requests_serializer.data)
        
           
    
    def  post(self,request,format=None):
        doctor_requests_serializer = DoctorRequestSerializers(data=request.data)
        if doctor_requests_serializer.is_valid():
            doctor_requests_serializer.save()
            return R(doctor_requests_serializer.data, status=status.HTTP_201_CREATED)
        return R(doctor_requests_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class DoctorRequestView(APIView):

    def get(self,request,pk,format=None):
        try:
            doctor_requests= DoctorRequest.objects.get(id=pk)
        except DoctorRequest.DoesNotExist:
            return R('Doctor Request Does Not Exist')
            
        results_serializer = DoctorRequestSerializers(doctor_requests)
        return R(results_serializer.data)

    def put(self, request, pk, format=None):
        try:
            doctor_requests = DoctorRequest.objects.get(id=pk)
        except DoctorRequest.DoesNotExist:
            return R('Doctor Request Does Not Exist')
            
        doctor_requests_serializer = DoctorRequestSerializers(doctor_requests, data=request.data)
        if doctor_requests_serializer.is_valid():
            doctor_requests_serializer.save()
            return R(doctor_requests_serializer.data)
        return R(doctor_requests_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        try:
            doctor_requests = DoctorRequest.objects.get(id=pk)
        except DoctorRequest.DoesNotExist:
            return R('Doctor Request Does Not Exist')
        doctor_requests.delete()
        return R(status=status.HTTP_204_NO_CONTENT)





class  ContactMessagesView(APIView):

    def get(self,request,format=None):

        contact_messages = ContactMessage.objects.all()
        contact_messages_serializer = ContactMessageSerializers(contact_messages,many=True)
        return R(contact_messages_serializer.data)
        
           
    
    def  post(self,request,format=None):
        contact_messages_serializer = ContactMessageSerializers(data=request.data)
        if contact_messages_serializer.is_valid():
            contact_messages_serializer.save()
            return R(contact_messages_serializer.data, status=status.HTTP_201_CREATED)
        return R(contact_messages_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class ContactMessageView(APIView):

    def get(self,request,pk,format=None):
        try:
            contact_messages= ContactMessage.objects.get(id=pk)
        except ContactMessage.DoesNotExist:
            return R('ContactMessage Does Not Exist')
            
        contact_messages_serializer = ContactMessageSerializers(contact_messages)
        return R(contact_messages_serializer.data)

    def put(self, request, pk, format=None):
        try:
            contact_messages = ContactMessage.objects.get(id=pk)
        except ContactMessage.DoesNotExist:
            return R('ContactMessage Does Not Exist')
            
        contact_messages_serializer = ContactMessageSerializers(contact_messages, data=request.data)
        if contact_messages_serializer.is_valid():
            contact_messages_serializer.save()
            return R(contact_messages_serializer.data)
        return R(contact_messages_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        try:
            results = ContactMessage.objects.get(id=pk)
        except ContactMessage.DoesNotExist:
            return R('ContactMessage Does Not Exist')
        results.delete()
        return R(status=status.HTTP_204_NO_CONTENT)


