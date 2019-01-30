from functools import wraps
from django.shortcuts import redirect


# No use right now
def check_permission(profiletype):
    def main_decorator(viewfunc):
        @wraps(viewfunc)
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                if request.user.profileType == profiletype:
                    return viewfunc(request, *args, **kwargs)
                return redirect('home')
            return redirect('login')
        return wrapper
    return main_decorator
