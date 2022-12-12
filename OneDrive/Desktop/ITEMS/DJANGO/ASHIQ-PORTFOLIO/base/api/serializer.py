from rest_framework import serializers
from base.models import *
from django.contrib.auth.models import User


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = Profile        
        # fields = '__all__'
        exclude = ('user',)



class ExperienceSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = Experience
        # exclude = ('id',)
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = About
        # exclude = ('id',)
        fields = '__all__'

class LCSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = Certificate
        # exclude = ('id',)
        fields = '__all__'

class MemorableMomentSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = Gallery
        # exclude = ('id',)
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = Testimonial
        # exclude = ('id',)
        fields = '__all__'

class WorkedClubSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = WorkedClub
        # exclude = ('id',)
        fields = '__all__'

class ContactMeSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = ContactMe
        # exclude = ('id',)
        fields = '__all__'
        
