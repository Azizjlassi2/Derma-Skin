
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# rest framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status






from Accounts.models import AppUser
from Site.models import *
from .serializers import *


class AppUsersView(APIView):

    def get(self,request,format=None):

        appusers = AppUser.objects.all().order_by("-created")
        appuser_serializer = AppUserSerializers(appusers,many=True)
        return Response(appuser_serializer.data)
        
           
    
    def  post(self,request,format=None):
        appuser_serializer = AppUserSerializers(data=request.data)
        if appuser_serializer.is_valid():
            appuser_serializer.save()
            return Response(appuser_serializer.data, status=status.HTTP_201_CREATED)
        return Response(appuser_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class AppUserView(APIView):

    def get(self,request,pk,format=None):
        try:
            appuser= AppUser.objects.get(id=pk)
        except AppUser.DoesNotExist:
            return HttpResponse('User Does Not Exist')
            
        appuser_serializer = AppUserSerializers(appuser)
        return Response(appuser_serializer.data)

    def put(self, request, pk, format=None):
        try:
            appuser = AppUser.objects.get(id=pk)
        except AppUser.DoesNotExist:
            return HttpResponse('User Does Not Exist')
            
        appuser_serializer = AppUserSerializers(appuser, data=request.data)
        if appuser.is_valid():
            appuser_serializer.save()
            return Response(appuser_serializer.data)
        return Response(appuser_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        try:
            appuser = AppUser.objects.get(id=pk)
        except AppUser.DoesNotExist:
            return HttpResponse('User Does Not Exist')
        appuser.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#QuestionQCMSerializers
class QuestionsView(APIView):

    def get(self,request,format=None):

        questions = QuestionQCM.objects.all()
        questions_serializer = QuestionQCMSerializers(questions,many=True)
        return Response(questions_serializer.data)
        
           
    
    def  post(self,request,format=None):
        questions_serializer = QuestionQCMSerializers(data=request.data)
        if questions_serializer.is_valid():
            questions_serializer.save()
            return Response(questions_serializer.data, status=status.HTTP_201_CREATED)
        return Response(questions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class QuestionView(APIView):

    def get(self,request,pk,format=None):
        try:
            questions= QuestionQCM.objects.get(id=pk)
        except QuestionQCM.DoesNotExist:
            return HttpResponse('QuestionQCM Does Not Exist')
            
        questions_serializer = QuestionQCMSerializers(questions)
        return Response(questions_serializer.data)

    def put(self, request, pk, format=None):
        try:
            questions = QuestionQCM.objects.get(id=pk)
        except QuestionQCM.DoesNotExist:
            return HttpResponse('QuestionQCM Does Not Exist')
            
        questions_serializer = QuestionQCMSerializers(questions, data=request.data)
        if questions.is_valid():
            questions_serializer.save()
            return Response(questions_serializer.data)
        return Response(questions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        try:
            questions = QuestionQCM.objects.get(id=pk)
        except QuestionQCM.DoesNotExist:
            return HttpResponse('QuestionQCM Does Not Exist')
        questions.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class  DescriptionsView(APIView):

    def get(self,request,format=None):

        descriptions = Description.objects.all()
        descriptions_serializer = DescriptionSerializers(descriptions,many=True)
        return Response(descriptions_serializer.data)
        
           
    
    def  post(self,request,format=None):
        descriptions_serializer = DescriptionSerializers(data=request.data)
        if descriptions_serializer.is_valid():
            descriptions_serializer.save()
            return Response(descriptions_serializer.data, status=status.HTTP_201_CREATED)
        return Response(descriptions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class DescriptionView(APIView):

    def get(self,request,pk,format=None):
        try:
            descriptions= Description.objects.get(id=pk)
        except Description.DoesNotExist:
            return HttpResponse('description Does Not Exist')
            
        descriptions_serializer = DescriptionSerializers(descriptions)
        return Response(descriptions_serializer.data)

    def put(self, request, pk, format=None):
        try:
            descriptions = Description.objects.get(id=pk)
        except Description.DoesNotExist:
            return HttpResponse('description Does Not Exist')
            
        descriptions_serializer = DescriptionSerializers(descriptions, data=request.data)
        if descriptions.is_valid():
            descriptions_serializer.save()
            return Response(descriptions_serializer.data)
        return Response(descriptions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        try:
            descriptions = Description.objects.get(id=pk)
        except Description.DoesNotExist:
            return HttpResponse('description Does Not Exist')
        descriptions.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






class  ResultsView(APIView):

    def get(self,request,format=None):

        results = Result.objects.all()
        results_serializer = ResultSerializers(results,many=True)
        return Response(results_serializer.data)
        
           
    
    def  post(self,request,format=None):
        results_serializer = ResultSerializers(data=request.data)
        if results_serializer.is_valid():
            results_serializer.save()
            return Response(results_serializer.data, status=status.HTTP_201_CREATED)
        return Response(results_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class ResultView(APIView):

    def get(self,request,pk,format=None):
        try:
            results= Result.objects.get(id=pk)
        except Result.DoesNotExist:
            return HttpResponse('Result Does Not Exist')
            
        results_serializer = ResultSerializers(results)
        return Response(results_serializer.data)

    def put(self, request, pk, format=None):
        try:
            results = Result.objects.get(id=pk)
        except Result.DoesNotExist:
            return HttpResponse('Result Does Not Exist')
            
        results_serializer = ResultSerializers(results, data=request.data)
        if results_serializer.is_valid():
            results_serializer.save()
            return Response(results_serializer.data)
        return Response(results_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        try:
            results = Result.objects.get(id=pk)
        except Result.DoesNotExist:
            return HttpResponse('Result Does Not Exist')
        results.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class  DoctorRequestsView(APIView):

    def get(self,request,format=None):

        doctor_requests = DoctorRequest.objects.all()
        doctor_requests_serializer = DoctorRequestSerializers(doctor_requests,many=True)
        return Response(doctor_requests_serializer.data)
        
           
    
    def  post(self,request,format=None):
        doctor_requests_serializer = DoctorRequestSerializers(data=request.data)
        if doctor_requests_serializer.is_valid():
            doctor_requests_serializer.save()
            return Response(doctor_requests_serializer.data, status=status.HTTP_201_CREATED)
        return Response(doctor_requests_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class DoctorRequestView(APIView):

    def get(self,request,pk,format=None):
        try:
            doctor_requests= DoctorRequest.objects.get(id=pk)
        except DoctorRequest.DoesNotExist:
            return HttpResponse('Doctor Request Does Not Exist')
            
        results_serializer = DoctorRequestSerializers(doctor_requests)
        return Response(results_serializer.data)

    def put(self, request, pk, format=None):
        try:
            doctor_requests = DoctorRequest.objects.get(id=pk)
        except DoctorRequest.DoesNotExist:
            return HttpResponse('Doctor Request Does Not Exist')
            
        doctor_requests_serializer = DoctorRequestSerializers(doctor_requests, data=request.data)
        if doctor_requests_serializer.is_valid():
            doctor_requests_serializer.save()
            return Response(doctor_requests_serializer.data)
        return Response(doctor_requests_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        try:
            doctor_requests = DoctorRequest.objects.get(id=pk)
        except DoctorRequest.DoesNotExist:
            return HttpResponse('Doctor Request Does Not Exist')
        doctor_requests.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class  ContactMessagesView(APIView):

    def get(self,request,format=None):

        contact_messages = ContactMessage.objects.all()
        contact_messages_serializer = ContactMessageSerializers(contact_messages,many=True)
        return Response(contact_messages_serializer.data)
        
           
    
    def  post(self,request,format=None):
        contact_messages_serializer = ContactMessageSerializers(data=request.data)
        if contact_messages_serializer.is_valid():
            contact_messages_serializer.save()
            return Response(contact_messages_serializer.data, status=status.HTTP_201_CREATED)
        return Response(contact_messages_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class ContactMessageView(APIView):

    def get(self,request,pk,format=None):
        try:
            contact_messages= ContactMessage.objects.get(id=pk)
        except ContactMessage.DoesNotExist:
            return HttpResponse('ContactMessage Does Not Exist')
            
        contact_messages_serializer = ContactMessageSerializers(contact_messages)
        return Response(contact_messages_serializer.data)

    def put(self, request, pk, format=None):
        try:
            contact_messages = ContactMessage.objects.get(id=pk)
        except ContactMessage.DoesNotExist:
            return HttpResponse('ContactMessage Does Not Exist')
            
        contact_messages_serializer = ContactMessageSerializers(contact_messages, data=request.data)
        if contact_messages_serializer.is_valid():
            contact_messages_serializer.save()
            return Response(contact_messages_serializer.data)
        return Response(contact_messages_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        try:
            results = ContactMessage.objects.get(id=pk)
        except ContactMessage.DoesNotExist:
            return HttpResponse('ContactMessage Does Not Exist')
        results.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


