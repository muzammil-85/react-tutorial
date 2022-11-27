from django.shortcuts import render
from .models import *
from ashiq_portfolio import settings



# Create your views here.
def home(request):
    contact = ContactMe.objects.all()
    workedclub = WorkedClub.objects.all()
    testimonial = Testimonial.objects.all()
    memorable_moments = MemorableMoment.objects.all()
    license = LC.objects.all()
    about = About.objects.all()
    experience = Experience.objects.all()
    profile = Profile.objects.all()
    bucket_name = 'media/'
    context = {
        'contact':contact,
        'workedclub':workedclub,
        'testimonial':testimonial,
        'memorable_moments':memorable_moments,
        'license':license,
        'about':about,
        'experience':experience,
        'profile':profile,
        'b_name':bucket_name,
    }
    
    return render(request,'index.html',context)

def LoginPage(request):
    return render(request,'login.html')

def registerPage(request):
    return render(request,'login.html')


def logoutUser(request):
#    logout(request)
# 	return redirect('home')
    pass

