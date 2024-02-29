import factory 
from .models import User 

class UserFactory(factory.django.DjangoModelFactory): 
    class Meta: 
        model = User 
    name = factory.Faker('name') 
    address = factory.Faker('address') 
    email_address = factory.Faker('email') 
    country = factory.Faker('country') 