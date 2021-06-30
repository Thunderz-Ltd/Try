from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models

from datetime import date

class House(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    room = models.CharField(max_length=255, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    accommodationtype = models.CharField(max_length=255,null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name
     
    def get_absolute_url(self):
        return f'/findhouse/{self.id}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

class UserProfile(models.Model):
    
    fullname = models.CharField(max_length=255)
    username = models.CharField(max_length=255, null=True)
    phonenumber = models.CharField(max_length=255)
    dateofbirth = models.DateField(max_length=255)
    gender = models.CharField(max_length=10,null=True)
    orientation = models.CharField(max_length=10,null=True)
    religion = models.CharField(max_length=20,null=True)
    occupation = models.CharField(max_length=255,null=True)
    bio = models.CharField(max_length=255,null=True)
    HasRoom = models.CharField(max_length=255,null=True, default='Needs A Room') #By default everyone will be registered as 'Needs A Room' until they posted a property, then this value will be changed
    pet = models.CharField(max_length=10,null=True)

    preferredgender = models.CharField(max_length=255,null=True)
    preferredorientation = models.CharField(max_length=255,null=True)
    preferredage = models.CharField(max_length=20,null=True)
    preferredreligion = models.CharField(max_length=20,null=True)
    preferredoccupation = models.CharField(max_length=255,null=True)

    preferredlocation = models.CharField(max_length=255,null=True)
    preferredmaxrent = models.IntegerField(null=True)
    preferredaccommodationtype = models.CharField(max_length=255,null=True)

    profilephoto = models.ImageField(upload_to='profilephoto/', blank=True, null=True)
    profilethumbnail = models.ImageField(upload_to='profilephoto/', blank=True, null=True)

    def __str__(self):
        return self.fullname

    def get_absolute_url(self):
        return f'/findhousemate/{self.username}/'

    def age(self):
        current_year = int((date.today()).year)
        return current_year - int(self.dateofbirth.year)
    
    def get_username(self): #temporary solution because supposedly username should be retrieved/registered from Sign Up page
        if self.username:
            return self.username
        else:
            self.username = ((self.fullname).replace(" ","")).lower()
            self.save()
            return self.username

    def get_profilephoto(self):
        if self.profilephoto:
            return 'http://127.0.0.1:8000' + self.profilephoto.url
        return ''
    
    def get_profilethumbnail(self):
        if self.profilethumbnail:
            return 'http://127.0.0.1:8000' + self.profilethumbnail.url
        else:
            if self.profilephoto:
                self.profilethumbnail = self.make_profilethumbnail(self.profilephoto)
                self.save()

                return 'http://127.0.0.1:8000' + self.profilethumbnail.url
            else:
                return ''
    
    def make_profilethumbnail(self, profilephoto, size=(300, 200)):
        img = Image.open(profilephoto)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        profilethumbnail = File(thumb_io, name=profilephoto.name)

        return profilethumbnail
    