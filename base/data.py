from faker import Faker
from django.contrib.auth.models import User

# Import Faker librairy to generate fake data
fk = Faker('fr_FR')

for i in range(0,50):
    user = User()
    




