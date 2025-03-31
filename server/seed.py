#!/usr/bin/env python3
# server/seed.py
from random import choice as rc
from faker import Faker

from app import app
from models import db, Pet

# Initialize app context to interact with the DB
with app.app_context():

    # Create and initialize a faker generator
    fake = Faker()

    # Delete all rows in the "pets" table (optional, just in case you want to clean up before seeding)
    Pet.query.delete()

    # Create an empty list to store Pet instances
    pets = []

    # List of species to randomly choose from
    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

    # Create 10 Pet instances and add them to the pets list
    for n in range(10):
        pet = Pet(name=fake.first_name(), species=rc(species))
        pets.append(pet)

    # Insert all Pet instances into the "pets" table
    db.session.add_all(pets)

    # Commit the transaction to save data to the database
    db.session.commit()

    print(f"Successfully added {len(pets)} pets to the database.")
