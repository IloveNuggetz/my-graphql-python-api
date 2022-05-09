from . import db


class Philosopher(db.Model):
    wikidataUrl = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(63))
    imageUrl = db.Column(db.String(255))
    minBirthYear = db.Column(db.Integer)
    maxBirthYear = db.Column(db.Integer)
    minDeathyear = db.Column(db.Integer)
    maxDeathyear = db.Column(db.Integer)

    def to_dict(self):
        return {
            "wikidataUrl": self.wikidataUrl,
            "name": self.name,
            "imageUrl": self.imageUrl,
            "minBirthYear": self.minBirthYear,
            "maxBirthYear": self.maxBirthYear,
            "minDeathyear": self.minDeathyear,
            "maxDeathyear": self.minDeathyear,
        }


class WikimediaProject:

    def __init__(self, name, endpoints):
        self.name = name
        self.endpoints = endpoints
