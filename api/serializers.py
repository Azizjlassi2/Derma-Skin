from rest_framework.serializers import ModelSerializer



from Accounts.models import  AppUser

# Site APP
from Site.models import  Description , QuestionQCM , Result,DoctorRequest , ContactMessage




class AppUserSerializers(ModelSerializer):
    class Meta:
        model = AppUser
        fields = "__all__"





class QuestionQCMSerializers(ModelSerializer):
    class Meta:
        model = QuestionQCM
        fields = "__all__"

        
class DescriptionSerializers(ModelSerializer):
    class Meta:
        model = Description
        fields = "__all__"

        

        
class DoctorRequestSerializers(ModelSerializer):
    class Meta:
        model = DoctorRequest
        fields = "__all__"

        
class ResultSerializers(ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"

       
class ContactMessageSerializers(ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = "__all__"
