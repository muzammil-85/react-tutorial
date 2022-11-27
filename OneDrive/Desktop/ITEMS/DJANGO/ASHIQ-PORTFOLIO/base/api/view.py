from rest_framework import viewsets
from base.models import Profile, Experience, About, Certificate, Gallery, Testimonial, WorkedClub, ContactMe
from . import serializer
from . import serializer as srz
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class ProfileView(viewsets.ModelViewSet):
    queryset =  Profile.objects.all()
    serializer_class = serializer.ProfileSerializer

class ExperienceView(viewsets.ModelViewSet):
    queryset =  Experience.objects.all()
    serializer_class = serializer.ExperienceSerializer

class AboutView(viewsets.ModelViewSet):
    queryset =  About.objects.all()
    serializer_class = serializer.AboutSerializer

class LCView(viewsets.ModelViewSet):
    queryset =  Certificate.objects.all()
    serializer_class = serializer.LCSerializer

class MemorableMomentView(viewsets.ModelViewSet):
    queryset =  Gallery.objects.all()
    serializer_class = serializer.MemorableMomentSerializer

class TestimonialView(viewsets.ModelViewSet):
    queryset =  Testimonial.objects.all()
    serializer_class = serializer.TestimonialSerializer

class WorkedClubView(viewsets.ModelViewSet):
    queryset =  WorkedClub.objects.all()
    serializer_class = serializer.WorkedClubSerializer

class ContactMeView(viewsets.ModelViewSet):
    queryset =  ContactMe.objects.all()
    serializer_class = serializer.ContactMeSerializer


# Login API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = srz.RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": srz.UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })