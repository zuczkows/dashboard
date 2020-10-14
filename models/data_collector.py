from db import db


class DataCollector(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer)
    passed = db.Column(db.Integer)
    total = db.Column(db.Integer)
    suite = db.Column(db.String)
    link = db.Column(db.String)


    def __init__(self, suite, date, passed, total, link):
        self.suite = suite
        self.date = date
        self.passed = passed
        self.total = total
        self.link = link

    def json(self):
        return {
            "suite": self.suite,
            "date": self.date,
            "passed": self.passed,
            "total": self.total,
            "link": self.link
        }

    @classmethod
    def find_by_suite(cls, name):
        return cls.query.filter_by(suite=name).all()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
