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
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
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
