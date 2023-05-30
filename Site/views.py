from django import utils
from django.shortcuts import redirect, render
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
from .decorators import unauthenticated_user
from django.contrib import messages



from Accounts.models import AppUser
from .models import QuestionQCM 
from Accounts.models import DoctorRequest


import tensorflow as tf

from PIL import Image




def get_image(request):


    try :
        uploaded_image = request.FILES['image']
        return uploaded_image
    except   utils.datastructures.MultiValueDictKeyError:
        return " NO IMAGE UPLOADED "
    


def image_processing(image):

    image = Image.open(image)

    # Convert the PIL Image object to a NumPy array
    image_array = np.array(image)

    # Convert the image data to a NumPy array using PIL
    image = tf.image.resize(image_array, [28, 28])
    image = tf.cast(image, tf.float32) / 255.0   # cast to float32 and normalize
    image=image[...,:3]
    return image

def prediction(image):

    classes = {4: ('nv', ' melanocytic nevi'), 6: ('mel', 'melanoma'), 2 :('bkl', 'benign keratosis-like lesions'), 1:('bcc' , ' basal cell carcinoma'), 5: ('vasc', ' pyogenic granulomas and hemorrhage'), 0: ('akiec', 'Actinic keratoses and intraepithelial carcinomae'),  3: ('df', 'dermatofibroma')}
    
    model = tf.keras.models.load_model('./Model/my_model3.h5')

    import matplotlib.pyplot as plt 
    plt.figure()
    plt.imshow(image)

    pred = model.predict(np.array([image]))
    class_index = np.argmax(pred,axis=1)

    # Return the predicted class as a response
    result = classes[class_index[0]][1]

    return result

def save_test_image(request,image,result):
    from Site.models import Test

    user = request.user
    
   
    test = Test()
    test.user_name =user.username
    test.user_id = int(user.id)
    test.image = image
    test.result = result
    test.save()


def home(request,pk=None):
    points = 0
    question_number = 0
    if request.method == 'GET':
        doctors = AppUser.objects.filter(user_type="Doctor")
        qcm_questions = QuestionQCM.objects.all()


        return render(request,'Pages/index.html',{"doctors":doctors,"questions":qcm_questions})
    elif request.method == 'POST':

        question_id = QuestionQCM.objects.get(id=pk)


        answer = request.POST['answer']
        question_number +=1
        
        if answer == 'OUI':
            points +=5
        elif answer == 'NON':
            points -=5

        if question_number == QuestionQCM.objects.count:
            return render(request,'Pages/index.html',{"doctors":doctors,"result":points})
       

def contactUs(request):
    return render(request,'Pages/contact.html',{})


def doctorsPage(request):
    doctors = AppUser.objects.filter(user_type="Doctor")
    return render(request,"Pages/team.html",{"doctors":doctors})

@unauthenticated_user
def testPage(request):
    if request.method == 'GET':
        return render(request,'Pages/test.html',{})
    if request.method == 'POST':
        print(request.POST)
    
        message = ""
        result = ""
        try:
            image = get_image(request)
            processed_image = image_processing(image)
            
            result = prediction(processed_image)
            save_test_image(request,image ,result)
        
        except FileNotFoundError:
            messages.warning(request,"No Image Uploaded, Please pick a Image")
        return render(request,'Pages/test.html',{'result':result})

    
@unauthenticated_user
def patientsPage(request):
    patients = AppUser.objects.filter(user_type="Patient")
    return render(request,"Pages/patients.html",{"patients":patients})



def FAQ_Page(request):

    from .models import Description 
    descriptions = Description.objects.all()

    return render(request,'Pages/FAQ.html',{'descriptions':descriptions})



def QUIZ_Page(request):
    if request.method == "GET":
        from .models import QuestionQCM
        questions = QuestionQCM.objects.all()
        return render(request,'Pages/QUIZ.html',{'questions':questions})
    elif request.method == 'POST':
        data = request.POST
        print(request.POST)
        message = ""
        Num_YES = 0
        for value in data:
            print(value)
            if value.lower().startswith("yes"):
                Num_YES +=1

        
        if Num_YES <3:
            message = " You Have a Low risk. However, it is still important to regularly monitor your skin and practice sun safety measures."
        elif Num_YES > 3 and Num_YES <6:
            message = "You Have a Moderate risk. Consider scheduling a professional skin examination with a dermatologist."
        else:
            message = " You Have a  High risk. It is recommended to seek medical attention promptly for a thorough evaluation and possible skin biopsy."


    
    return HttpResponse(f"<h1>{message}</h1>")



@unauthenticated_user
def contact_doctor(request):
    if request.method == 'POST':
        data = json.loads(request.body)    
        doctor_id = data['doctor_id']

        return redirect("contactSelectedDoctor",pk=doctor_id)

    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)



def search_doctor(request):
    if request.method == 'POST':
        data = json.loads(request.body)
      
        gouvernerat = data['gouvernerat']
        city = data['city']
        print(gouvernerat," : ",city)
        return JsonResponse({'message': 'Data submitted successfully.'})
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)
    


def messagesPage(request):
    return render(request,"Pages/messages.html",{})


# tache :
"""
1. QUIZ APP 
2. CHAT APP 
3. CNN MODEL 

"""