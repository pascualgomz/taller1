from django.core.management.base import BaseCommand 
from pages.factories import UserFactory 

 

class Command(BaseCommand): 
    help = 'Seed the database with users' 

    def handle(self, *args, **kwargs): 

        UserFactory.create_batch(8) 
        self.stdout.write(self.style.SUCCESS('Successfully seeded users')) 