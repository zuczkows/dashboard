from db import db


class DataCollector(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer)
    passed = db.Column(db.Integer)
    total = db.Column(db.Integer)


    def __init__(self, date, passed, total):
        self.date = date
        self.passed = passed
        self.total = total

    def json(self):
        return {
            "date": self.date,
            "passed": self.passed,
            "total": self.total
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
