from django.db import models
from django.urls import reverse

class Portfolio(models.Model):
    title = models.CharField("Title", max_length=200)
    contact_email = models.CharField("Contact Email", max_length=200)
    is_active = models.BooleanField(default=False)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("portfolio-detail", args=[str(self.id)])
    
class Project(models.Model):
    title = models.CharField("Title", max_length=200)
    description = models.TextField("Description")
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="projects")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project-detail", args=[str(self.id)])
    
class Student(models.Model):
    MAJOR = (
        ('CSCI-BS', 'BS in Computer Science'),
        ('CPEN-BS', 'BS in Computer Engineering'),
        ('BIGD-BI', 'BI in Game Design and Development'),
        ('BICS-BI', 'BI in Computer Science'),
        ('BISC-BI', 'BI in Computer Security'),
        ('CSCI-BA', 'BA in Computer Science'),
        ('DASE-BS', 'BS in Data Analytics and Systems Engineering')
    )

    name = models.CharField(max_length=200)
    email = models.CharField("UCCS Email", max_length=200)
    major = models.CharField(max_length=200, choices=MAJOR)
    portfolio = models.OneToOneField(Portfolio, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("student-detail", args=[str(self.id)])
