from app import app, db
from models import Hero, Power, HeroPower
import random

def seed_database():
    with app.app_context():
        # Clear existing data
        HeroPower.query.delete()
        Hero.query.delete()
        Power.query.delete()

        # Seed powers
        powers_data = [
            {'name': 'super strength', 'description': 'gives the wielder super-human strengths'},
            {'name': 'flight', 'description': 'gives the wielder the ability to fly through the skies at supersonic speed'},
            {'name': 'super human senses', 'description': 'allows the wielder to use her senses at a super-human level'},
            {'name': 'elasticity', 'description': 'can stretch the human body to extreme lengths'},
        ]

        powers = []
        for power_data in powers_data:
            power = Power(**power_data)
            powers.append(power)
            db.session.add(power)

        # Seed heroes
        heroes_data = [
            {'name': 'Kamala Khan', 'super_name': 'Ms. Marvel'},
            {'name': 'Doreen Green', 'super_name': 'Squirrel Girl'},
            {'name': 'Gwen Stacy', 'super_name': 'Spider-Gwen'},
            {'name': 'Janet Van Dyne', 'super_name': 'The Wasp'},
            {'name': 'Wanda Maximoff', 'super_name': 'Scarlet Witch'},
            {'name': 'Carol Danvers', 'super_name': 'Captain Marvel'},
            {'name': 'Jean Grey', 'super_name': 'Dark Phoenix'},
            {'name': 'Ororo Munroe', 'super_name': 'Storm'},
            {'name': 'Kitty Pryde', 'super_name': 'Shadowcat'},
            {'name': 'Elektra Natchios', 'super_name': 'Elektra'},
        ]

        heroes = []
        for hero_data in heroes_data:
            hero = Hero(**hero_data)
            heroes.append(hero)
            db.session.add(hero)

        db.session.commit()

        # Seed hero powers
        strengths = ['Strong', 'Weak', 'Average']
        for hero in heroes:
            # Assign 1-3 random powers to each hero
            num_powers = random.randint(1, 3)
            selected_powers = random.sample(powers, num_powers)
            for power in selected_powers:
                strength = random.choice(strengths)
                hero_power = HeroPower(hero=hero, power=power, strength=strength)
                db.session.add(hero_power)

        db.session.commit()
        print('Database seeded successfully!')

if __name__ == '__main__':
    seed_database()
