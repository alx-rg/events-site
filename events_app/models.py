"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref
import enum

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    email = db.Column(db.String(99), nullable=False)
    phone = db.Column(db.String(12), nullable=False) 
    events_attending = db.relationship('Event', secondary='guest_event', back_populates='guests')

# - id: primary key
# - name: String column
# - email: String column
# - phone: String column
# - events_attending: relationship to "Event" table with a secondary table


# STRETCH CHALLENGE: Add a field `event_type` as an Enum column that denotes the
# type of event (Party, Study, Networking, etc)
# class event_type(enum.Enum):
#     Networking = 1
#     Study = 2
#     Party = 3
#     Sports = 4
#     VideoGames = 5
#     Chill = 6

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String)
    date_and_time = db.Column(db.DateTime)
    guests = db.relationship('Guest', secondary='guest_event', back_populates='events_attending')
    # event_type = db.Column(db.Enum('event_type'), default=event_type.Study)

# - id: primary key
# - title: String column
# - description: String column
# - date_and_time: DateTime column
# - guests: relationship to "Guest" table with a secondary table

# - event_id: Integer column (foreign key)
# - guest_id: Integer column (foreign key)

guest_event_table = db.Table('guest_event',
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
    )