from models import Dog

def create_table(base, engine):
    """
    Create the Dog table in the database.
    """
    base.metadata.create_all(engine)

def save(session, dog):
    """
    Save a Dog instance to the database.
    """
    session.add(dog)
    session.commit()    

def get_all(session):
    """
    Retrieve all Dog instances from the database.
    """
    return session.query(Dog).all()

def find_by_name(session, name):
    """
    Find a Dog instance by its name.
    """
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    """
    Find a Dog instance by its ID.
    """
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    """
    Find a Dog instance by its name and breed.
    """
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

def update_breed(session, dog, breed):
    """
    Update the breed of a Dog instance.
    """
    dog.breed = breed
    session.commit()
    return dog