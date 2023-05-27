from django.shortcuts import redirect
from django.http import HttpResponse


def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('Home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

def allowed_users(allowed_permessions= []):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            
            permession = None
            if request.user.groups.exists():
                permession = request.user.groups.all()[0].name
            
            if permession in allowed_permessions:
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse("You are not authorized to view this page")
        return wrapper_func
    return decorator