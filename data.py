import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diaryapi.settings')
from django.contrib.auth.hashers import make_password
import pickle
import django
import pandas as pd
django.setup()

from faker import Faker
from django.contrib.auth.models import User
from base.models import Text

# Import Faker librairy to generate fake data
df = pd.read_csv('data/clean_data.csv')
# Using english/US locale
fk = Faker('en_US')

def populate(nb_users=10, nb_texts=30):
    """
    Function used to populate database with fake data.
    We use python faker here to generate fake data and feed them in the database
    
    **Parameters**
    nb_users => Number of of users we want to create
    nb_texts => Number of texts associated to the user
    """
    text_loc = 1
    # For loop that creates the user / 10 users 
    for i in range(nb_users):
        # Hydrating the user entity 
        fake_username = fk.unique.first_name().lower()
        fake_email = fk.unique.email()
        password = 'simplon59'

        # Saving the user to the database
        user = User.objects.get_or_create(
            username = fake_username, 
            email = fake_email, 
            password = make_password(password)
        )
        text_loc += 30

        # For loop that creates texts associated to the user / 30 texts
        for j in range(nb_texts):
            fake_date = fk.date_time_between(start_date='-5y', end_date='now')
            fake_text = df['Text'][(j + text_loc)]
            # Machine learning model that predicts the emotion of the text generated
            tfidf, model = pickle.load(open('dl-model/lr_combined_tfidf.bin', 'rb'))
            y_pred = model.predict(tfidf.transform([fake_text]))

            # Saving the text to the database
            text = Text.objects.get_or_create(
                text = fake_text,
                created_at = fake_date,
                emotion = y_pred[0],
                client = User.objects.get(id=user[0].id)
            )



if __name__ == '__main__':
    # Function call
    populate()






