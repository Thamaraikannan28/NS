import os
import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.core.validators import FileExtensionValidator

def file_path1(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/Home",filename)

def file_path2(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/Services",filename)

def file_path3(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/POs",filename)

def file_path4(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/PMY",filename)

def file_path5(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/DL",filename)

def file_path6(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/NLM",filename)

def file_path7(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/SBM",filename)

def file_path8(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/UBA",filename)

def file_path9(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/Awards",filename)

def file_path10(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/VolunteerTalent",filename)

def file_path11(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/Sapling",filename)

def file_path12(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/BDC",filename)

def file_path13(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/Seminars",filename)

def file_path14(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("pdfs/Reports",filename)

def file_path15(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("pdfs/ActivityCalendar",filename)

def file_path16(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("pdfs/Assets",filename)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError("Users must have an email address")
        email = email.lower()
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

class Home(models.Model):
    """Model for creating image slider in homepage"""
    class Meta:
        verbose_name_plural = "Home"

    image = models.ImageField(null=True, upload_to=file_path1,
                                verbose_name="Home Slider")

    def __str__(self):
        return "Homepage Images"

class Services(models.Model):
    """Model for creating slider of services in homepage"""
    class Meta:
        verbose_name_plural = "Services"

    image = models.ImageField(null=True, upload_to=file_path2, 
                                verbose_name= "Services Slider")

    def __str__(self):
        return "Services Captured"

class UpcomingEvent(models.Model):
    """Model for updating upcoming events"""

    class Meta:
        verbose_name_plural = "Upcoming Events"

    event = models.CharField(max_length=255, default=None, verbose_name="Event Name")
    date = models.CharField(max_length=255, default=None, verbose_name="Event Data & Time")

    def __str__(self):
        return self.event

class POs(models.Model):
    """Model for updating Programme Officers"""

    class Meta:
        verbose_name_plural = "Programme Officers"

    name = models.CharField(max_length=255, default=None, verbose_name="Event Name")
    position = models.CharField(max_length=255, default=None, verbose_name="Event Data & Time")
    photo = models.ImageField(null=True, upload_to=file_path3, 
                                validators=[FileExtensionValidator(allowed_extensions=['jpeg','jpg'])],
                                verbose_name="Photo")

    def __str__(self):
        return self.name

class AC(models.Model):
    """Model for updating Advisory Committee Members"""
    class Meta:
        verbose_name_plural = "Advisory Committee"

    S_No = models.IntegerField(unique=True, verbose_name="S.No.")
    name = models.CharField(max_length=255, default=None, verbose_name="Event Name")
    position = models.CharField(max_length=255, default=None, verbose_name="Event Data & Time")

    def __str__(self):
        return self.name

class PMY(models.Model):
    """Model for updating pradhan mantri yojana"""
    class Meta:
        verbose_name_plural = "Pradhan Mantri Yojana (PMY)"

    title = models.CharField(max_length=255, default=None, verbose_name="Scheme Title ")
    Objective = models.TextField(max_length=500, null=True, default=None, verbose_name="Objective")
    link = models.URLField(max_length=500, default=None,null=True, verbose_name="Read More Link") 
    image = models.ImageField(null=True, upload_to=file_path4, 
                                verbose_name= "Scheme Image")

    def __str__(self):
        return self.title


class DL(models.Model):
    """Model for updating Digital Literacy"""
    class Meta:
        verbose_name_plural = "Digital Literacy"

    title = models.CharField(max_length=255, default=None, verbose_name="Scheme Title ")
    image1 = models.ImageField(null=True, upload_to=file_path5,
                                verbose_name= "Image 1")
    date1 = models.CharField(max_length=255, default=None, verbose_name="Date")
    image2 = models.ImageField(null=True, upload_to=file_path5,
                                verbose_name= "Image 2")
    date2 = models.CharField(max_length=255, default=None, verbose_name="Date")
    image3 = models.ImageField(null=True, upload_to=file_path5,
                                verbose_name= "Image 3")
    date3 = models.CharField(max_length=255, default=None, verbose_name="Date")
    image4 = models.ImageField(null=True, upload_to=file_path5,
                                verbose_name= "Image 4")
    date4 = models.CharField(max_length=255, default=None, verbose_name="Date")
    video = models.URLField(max_length=500, default=None,null=True, verbose_name="Video URL") 
    place = models.CharField(max_length=255, default=None, verbose_name="Place")

    def __str__(self):
        return self.title


class NLM(models.Model):
    """Model for updating National Literacy Mission"""
    class Meta:
        verbose_name_plural = "National Literacy Mission"

    date = models.CharField(max_length=255, default=None, verbose_name=" Year ")
    image1 = models.ImageField(null=True, upload_to=file_path6,
                                verbose_name= "Image 1")
    image2 = models.ImageField(null=True, upload_to=file_path6,
                                verbose_name= "Image 2")
    image3 = models.ImageField(null=True, upload_to=file_path6,
                                verbose_name= "Image 3")
    image4 = models.ImageField(null=True, upload_to=file_path6,
                                verbose_name= "Image 4")
    place = models.CharField(max_length=255, default=None, verbose_name="Place")

    def __str__(self):
        return self.date

class SBM(models.Model):
    """Model for updating Swachh Bharath Mission"""
    class Meta:
        verbose_name_plural = "Swachh Bharath Mission"

    date = models.CharField(max_length=255, default=None, verbose_name=" Year ")
    image1 = models.ImageField(null=True, upload_to=file_path7,
                                verbose_name= "Image 1")
    image2 = models.ImageField(null=True, upload_to=file_path7,
                                verbose_name= "Image 2")
    image3 = models.ImageField(null=True, upload_to=file_path7,
                                verbose_name= "Image 3")
    image4 = models.ImageField(null=True, upload_to=file_path7,
                                verbose_name= "Image 4")
    place = models.CharField(max_length=255, default=None, verbose_name="Place")
    video = models.URLField(max_length=500, default=None,null=True, verbose_name="Video URL")

    def __str__(self):
        return self.date

class UBA(models.Model):
    """Model for updating Unnat Bharat Abhiyan(UBA)"""
    class Meta:
        verbose_name_plural = "Unnat Bharat Abhiyan(UBA)"

    event = models.CharField(max_length=255, default=None, verbose_name="Event Name ")
    date = models.CharField(max_length=255, default=None, verbose_name=" Year ")
    description = models.TextField(max_length=500, null=True, default=None, verbose_name="Description")
    image1 = models.ImageField(null=True, upload_to=file_path8,
                                verbose_name= "Image 1")
    image2 = models.ImageField(null=True, upload_to=file_path8,
                                verbose_name= "Image 2")
 
    def __str__(self):
        return self.event

class Awards(models.Model):
    """Model for updating Awards & Achievements"""
    class Meta:
        verbose_name_plural = "Awards & Achievements"

    date = models.CharField(max_length=255, default=None, verbose_name=" Year ")
    description = models.TextField(max_length=500, null=True, default=None, verbose_name="Description")
    image = models.ImageField(null=True, upload_to=file_path9,
                                verbose_name= "Image")
    def __str__(self):
        return self.description

class Reports(models.Model):
    """Model for updating Reports and Magazines"""
    class Meta:
        verbose_name_plural = "Reports & Magazines"

    type = models.CharField(max_length=255, default=None, verbose_name=" type ")
    year = models.CharField(max_length=255, default=None, verbose_name=" Year ")
    file = models.FileField(null=True,upload_to=file_path14,
                    validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
                    verbose_name="PDF File")
    
    def __str__(self):
        return self.year

class ActivityCalendar(models.Model):
    """Model for uploading Activity Calendar"""
    class Meta:
        verbose_name_plural = "Activity Calendar"

    year = models.CharField(max_length=255, default=None, verbose_name=" Year ")
    pdf1 = models.FileField(null=True,upload_to=file_path15,
                    validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
                    verbose_name="PDF File")
    
    def __str__(self):
        return self.year

class Assets(models.Model):
    """Model for uploading Assets document"""
    class Meta:
        verbose_name_plural = "Assets Created"

    file = models.FileField(null=True,upload_to=file_path16,
                    validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
                    verbose_name="PDF File")
    
    def __str__(self):
        return "Assets"

class VT(models.Model):
    """Model for uploading Volunteer's Talent"""
    class Meta:
        verbose_name_plural = "Volunteers Talent"

    name = models.CharField(max_length=255, default=None, verbose_name="Name ")
    skill = models.CharField(max_length=255, default=None, verbose_name="Skill ")
    file = models.FileField(null=True,upload_to=file_path10,
                    validators=[FileExtensionValidator(allowed_extensions=['mp4', 'jpg'])],
                    verbose_name="Video or Image")
    image1 = models.ImageField(null=True, upload_to=file_path10,
                                verbose_name= "Image 1")
    image2 = models.ImageField(null=True, upload_to=file_path10,
                                verbose_name= "Image 2")
 
    def __str__(self):
        return self.name

class Sapling(models.Model):
    """Model for updating Sapling Plantation events"""
    class Meta:
        verbose_name_plural = "Sapling Plantation"

    event = models.CharField(max_length=255, default=None, verbose_name="Event Name ")
    count = models.CharField(max_length=255, default=None, verbose_name=" Sampling Count ")
    About = models.TextField(max_length=500, null=True, default=None, verbose_name="Event Description")
    count = models.CharField(max_length=255, default=None, verbose_name=" Year ")
    image1 = models.ImageField(null=True, upload_to=file_path11,
                                verbose_name= "Image 1")

 
    def __str__(self):
        return self.event


class BDC(models.Model):
    """Model for uploading Blood Donation Camps"""
    class Meta:
        verbose_name_plural = "Blood Donation Camp (BDC)"

    date = models.CharField(max_length=255, default=None, verbose_name="Event Date ")
    donated_to = models.CharField(max_length=255, default=None, verbose_name=" Donated to ")
    count = models.IntegerField(unique=True, verbose_name="Units")
    photo = models.ImageField(null=True, upload_to=file_path12,
                                verbose_name= "Image")

 
    def __str__(self):
        return self.date

class Camp(models.Model):
    """Model for uploading camps"""
    class Meta:
        verbose_name_plural = "Camp Organised"

    date = models.CharField(max_length=255, default=None, verbose_name="Event Date ")
    description = models.TextField(max_length=500, null=True, default=None, verbose_name="Description")
    video = models.URLField(max_length=500, default=None,null=True, verbose_name="Video URL")
 
    def __str__(self):
        return self.date

class Seminar(models.Model):
    """Model for uploading seminars and conferences"""
    class Meta:
        verbose_name_plural = "Seminars & Conferences"

    date = models.CharField(max_length=255, default=None, verbose_name="Event Date ")
    description = models.TextField(max_length=500, null=True, default=None, verbose_name="Description")
    photo = models.ImageField(null=True, upload_to=file_path13,
                                verbose_name= "Image")

 
    def __str__(self):
        return self.date