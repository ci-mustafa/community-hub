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

################
# Family Model #
################
class Family(models.Model):
    # Define family relationship choices
    DEFAULT_FAMILY_RELATIONSHIP_CHOICE = "Father"
    RELATIONSHIP_CHOICES = [
    (DEFAULT_FAMILY_RELATIONSHIP_CHOICE, 'Father'),
    ('Mother', 'Mother'),
    ('Son', 'Son'),
    ('Daughter', 'Daughter'),
    ('Brother', 'Brother'),
    ('Sister', 'Sister'),
    ('Cousin', 'Cousin'),
    ('Brother-in-law', 'Brother-in-law'),
    ('Sister-in-law', 'Sister-in-law'),
    ('Paternal Grandfather', 'Paternal Grandfather'),
    ('Paternal Grandmother', 'Paternal Grandmother'),
    ('Maternal Grandfather', 'Maternal Grandfather'),
    ('Maternal Grandmother', 'Maternal Grandmother'),
    ('Paternal Uncle', 'Paternal Uncle'),
    ('Maternal Uncle', 'Maternal Uncle'),
    ('Paternal Aunt', 'Paternal Aunt'),
    ('Maternal Aunt', 'Maternal Aunt'),
    ('Nephew', 'Nephew'),
    ('Niece', 'Niece'),
    ('Grandson', 'Grandson'),
    ('Granddaughter', 'Granddaughter'),
    ('Father-in-law', 'Father-in-law'),
    ('Mother-in-law', 'Mother-in-law'),
    ('Son-in-law', 'Son-in-law'),
    ('Daughter-in-law', 'Daughter-in-law'),
]
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    father_name = models.CharField(max_length=255, null=False, blank=False)
    family_relationship = models.CharField(max_length=20, choices=RELATIONSHIP_CHOICES, default=DEFAULT_FAMILY_RELATIONSHIP_CHOICE)

    # One-to-many relationship with User
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="family")

###############
# Group Model #
###############
class Group(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    # string representation
    def __str__(self) -> str:
        return self.title

###############
# Event Model #
###############
class Event(models.Model):
    # Define type choices
    PRIVATE = 'Private'
    PUBLIC = 'Public'

    EVENT_TYPE_CHOICES = [
        (PRIVATE, 'Private'),
        (PUBLIC, 'Public'),
    ]
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to="images/evnet", null=True, blank=True, validators=[validators.validate_file_size])
    event_type = models.CharField(max_length=7, choices=EVENT_TYPE_CHOICES, default=PUBLIC)

    # One-to-one relationship with Group
    group = models.OneToOneField(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name="event")

    # string representation
    def __str__(self):
        return self.title



