from django.db import models
from apps.users.models import NGO
from apps.donations.models import Child

class Visit(models.Model):
    PURPOSE_CHOICES = (
        ('volunteer', 'Volunteer'),
        ('adoption_inquiry', 'Adoption Inquiry'),
        ('donation_visit', 'Donation Visit'),
        ('other', 'Other'),
    )
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('completed', 'Completed'),
    )
    visit_id = models.AutoField(primary_key=True)
    visitor_name = models.CharField(max_length=100)
    visitor_email = models.EmailField()
    visitor_phone = models.CharField(max_length=15)
    ngo = models.ForeignKey(NGO, on_delete=models.CASCADE)
    child = models.ForeignKey(Child, on_delete=models.SET_NULL, null=True, blank=True)
    visit_date = models.DateField()
    visit_time = models.TimeField()
    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES)
    message = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.visitor_name} - {self.ngo.name}"
