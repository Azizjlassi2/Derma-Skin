from django.contrib import admin
from .models import *
from Accounts.models import DoctorRequest
# Register your models here.



def send_email(doctor:AppUser):
    pass


@admin.action(description="Refuse Request")
def refuse(modelAdmin,request,queryset):
    queryset.delete()



class DoctorRequestAdmin(admin.ModelAdmin):
    list_display = ("doctor_name","doctor_email","doctor_age","doctor_gouvernerat","request_date")
    actions= ["accept","refuse",]


    def accept(modelAdmin,request,queryset):
        
        queryset = queryset.get()
        

        new_doctor =  AppUser(user_type="Doctor")
        new_doctor.username = queryset.doctor_name
        new_doctor.age = queryset.doctor_age
        new_doctor.city = queryset.doctor_city
        new_doctor.genre = queryset.doctor_genre
        new_doctor.gouvernorat = queryset.doctor_gouvernerat
        new_doctor.email = queryset.doctor_email
        new_doctor.password = queryset.doctor_password
        new_doctor.profil_image = queryset.profil_image
        
        new_doctor.save()

        send_email(new_doctor)
        queryset.delete()
       
    accept.short_description = "Accept Request"

    

    @admin.action(description="Refuse Request")
    def refuse(modelAdmin,request,queryset):
        queryset.delete()






admin.site.register(Description)
admin.site.register(QuestionQCM)
admin.site.register(Response)
admin.site.register(Result)
admin.site.register(DoctorRequest,DoctorRequestAdmin)
admin.site.register(ContactMessage)
admin.site.register(Test)

