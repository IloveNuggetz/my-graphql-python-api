from app import db

class Philosopher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(63))
    description = db.Column(db.String(255))
    birth_year = db.Column(db.Integer)
    death_year = db.Column(db.Integer)
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.title,
            "description": self.description,
            "birth_year": str(self.birth_year),
            "death_year": str(self.death_year)
        }
