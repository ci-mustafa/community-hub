from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from phonenumber_field.modelfields import PhoneNumberField
from . import validators

# creating models (tables)

################
## User Model ##
################
class User(AbstractUser):
    # Define marital status choices
    SINGLE = 'S'
    MARRIED = 'M'
    DIVORCED = 'D'
    WIDOWED = 'W'
    ENGAGED = 'E'

    MARITAL_STATUS_CHOICES = [
        (SINGLE, 'Single'),
        (MARRIED, 'Married'),
        (DIVORCED, 'Divorced'),
        (WIDOWED, 'Widowed'),
        (ENGAGED, 'Engaged'),
    ]

    # Define has children choices
    YES = "Y"
    NO = "N"

    HAS_CHILDREN_CHOICES = [
        (YES, "Yes"),
        (NO, "No"),
    ]

    # Define gender choices
    MALE = 'M'
    FEMALE = 'F'
    PREFER_NOT_TO_SAY = 'N'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (PREFER_NOT_TO_SAY, 'Prefer not to say'),
    ]

    # Define table fields
    profile_image = models.ImageField(upload_to="images/profile", null=True, blank=True, validators=[validators.validate_file_size])
    father_full_name = models.CharField(max_length=255, null=True, blank=True)
    grand_father_full_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True, validators=[EmailValidator], null=False, blank=False)
    birth_date = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    province = models.CharField(max_length=255, null=True, blank=True)
    district = models.CharField(max_length=255, null=True, blank=True)
    village = models.CharField(max_length=255, null=True, blank=True)
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES, default=SINGLE)
    has_children = models.CharField(max_length=1, choices=HAS_CHILDREN_CHOICES, default=YES)
    underage_children_count = models.IntegerField(null=True, blank=True)
    total_children = models.IntegerField(null=True, blank=True)
    country_of_residence = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=PREFER_NOT_TO_SAY)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = PhoneNumberField(region='NZ', blank=True, null=True, help_text='Enter phone number in New Zealand format.')


