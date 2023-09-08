from django.db import models


# holds the record of parts
class Part(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# holds the record of sub parts and also has foreign_key of parts
class SubPart(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    count = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.part}"


# this  holds the information of introduction
class Introduction(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# can hold about us text
class AboutUs(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# model is for managing social media accounts
class ContactInfo(models.Model):
    instagram = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    youtube = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PythonCode(models.Model):
    my_code = models.TextField()
    sub_part = models.ForeignKey(SubPart, on_delete=models.CASCADE)

    def __str__(self):
        return self.my_code


# used for holding objects of contact us page
class ContactUs(models.Model):
    """This class will handle objects of contact us page"""
    # below fields used for Address column on contact us
    address_title = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100, blank=True)
    postal_code = models.IntegerField(blank=True)
    # below 2 fields used for Phone Information
    phone_title = models.CharField(max_length=100, blank=True)
    phone_no = models.CharField(max_length=100)
    # these 2 fields will be used for Email Information on contact us page
    email_title = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
