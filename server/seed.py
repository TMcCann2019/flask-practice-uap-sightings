# import app
# import model and db instance
from app import app
from faker import Faker
from models import Sighting, db

# Define seeding functions (optional: use Faker to help generate fake data)
def clear_database():
    Sighting.query.delete()

def create_sightings():
    sightings = []
    fake = Faker()

    s1 = Sighting(
        date=fake.date(),
        time=fake.time(),
        location=fake.city(),
        shape_of_craft=fake.word(),
        approximate_size=fake.random_int(min=1, max=100),
        approximate_speed=fake.random_int(min=1, max=100),
        description=fake.sentence(),
        reporter=fake.name(),
        reporter_sober=fake.random_int(min=0, max=1),
    )
    sightings.append(s1)

    s2 = Sighting(
        date=fake.date(),
        time=fake.time(),
        location=fake.city(),
        shape_of_craft=fake.word(),
        approximate_size=fake.random_int(min=1, max=100),
        approximate_speed=fake.random_int(min=1, max=100),
        description=fake.sentence(),
        reporter=fake.name(),
        reporter_sober=fake.random_int(min=0, max=1),
    )
    sightings.append(s2)

    s3 = Sighting(
        date=fake.date(),
        time=fake.time(),
        location=fake.city(),
        shape_of_craft=fake.word(),
        approximate_size=fake.random_int(min=1, max=100),
        approximate_speed=fake.random_int(min=1, max=100),
        description=fake.sentence(),
        reporter=fake.name(),
        reporter_sober=fake.random_int(min=0, max=1),
    )
    sightings.append(s3)

    db.session.add_all(sightings)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        clear_database()
        create_sightings()
        pass
