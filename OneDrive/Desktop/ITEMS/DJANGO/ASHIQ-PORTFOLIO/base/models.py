
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    resume = models.FileField(upload_to='upload', null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images")
    current_qualification = models.CharField(max_length=100, null=True, blank=True)
    current_team = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name


class Experience(models.Model):
    post = models.CharField(max_length=100, null=True, blank=True)
    team = models.CharField(max_length=100, null=True, blank=True)
    date = models.CharField(max_length=50, null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Experience"

    def __str__(self):
        return self.post


class About(models.Model):
    about = models.TextField(null=True, blank=True)
    achievement = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images")


    class Meta:
        verbose_name_plural = "About"

    def __str__(self):
        return 'ABOUT'


class Certificate(models.Model):
    licence_name = models.CharField(max_length=100, null=True, blank=True)
    org_name = models.CharField(max_length=100, null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images")

    class Meta:
        verbose_name_plural = "License & Certification"

    def __str__(self):
        return self.licence_name


class Gallery(models.Model):

    image = models.ImageField(null=True, blank=True, upload_to="images")
    pic_name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Memorable Moment"

    def __str__(self):

        if self.pic_name == None:
            return 'IMAGE '+ str(self.id)
        else:
            return self.pic_name


class Testimonial(models.Model):
    quote = models.TextField(null=True, blank=True)
    quoter = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Testimonial"

    def __str__(self):
        return self.quoter


class WorkedClub(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="images")
    club_name = models.CharField(max_length=100, null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Worked Club"

    def __str__(self):
        return self.club_name


class ContactMe(models.Model):
    number = models.CharField(max_length=50, null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    additional = models.TextField(null=True, blank=True)
    class Meta:
        verbose_name_plural = "Contact"

    def __str__(self):
        return 'CONTACT'
