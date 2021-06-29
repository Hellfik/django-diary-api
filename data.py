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
fk = Faker('en_US')

def populate(nb_users=10, nb_texts=30):
    text_loc = 1
    for i in range(nb_users):
        fake_username = fk.unique.first_name().lower()
        fake_email = fk.unique.email()
        password = 'simplon59'

        user = User.objects.get_or_create(
            username = fake_username, 
            email = fake_email, 
            password = make_password(password)
        )
        text_loc += 30


        for j in range(nb_texts):
            fake_date = fk.date_time_between(start_date='-5y', end_date='now')
            fake_text = df['Text'][(j + text_loc)]
            tfidf, model = pickle.load(open('dl-model/lr_combined_tfidf.bin', 'rb'))
            y_pred = model.predict(tfidf.transform([fake_text]))

            text = Text.objects.get_or_create(
                text = fake_text,
                created_at = fake_date,
                emotion = y_pred[0],
                client = User.objects.get(id=user[0].id)
            )

populate()






