from django.db import models
from apps.users.models import NGO

class Child(models.Model):
    GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'))
    child_id = models.AutoField(primary_key=True)
    ngo = models.ForeignKey(NGO, on_delete=models.CASCADE, related_name='children')
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    health_status = models.TextField(blank=True, null=True)
    education_level = models.CharField(max_length=100, blank=True, null=True)
    is_sponsored = models.BooleanField(default=False)
    is_available_for_adoption = models.BooleanField(default=False)
    profile_photo = models.ImageField(upload_to='children/', null=True, blank=True)
    story = models.TextField(blank=True, null=True)
    needs = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
