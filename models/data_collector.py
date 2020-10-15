from db import db


class DataCollector(db.Model):
    __tablename__ = "reports"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer)
    version = db.Column(db.Float)
    passed = db.Column(db.Integer)
    total = db.Column(db.Integer)
    suite = db.Column(db.String)
    service = db.Column(db.String)
    link = db.Column(db.String)
    env = db.Column(db.String)


    def __init__(self, suite, version, date, passed, total, link, service, env):
        self.suite = suite
        self.date = date
        self.version = version
        self.passed = passed
        self.total = total
        self.link = link
        self.service = service
        self.env = env

    def json(self):
        return {
            "suite": self.suite,
            "version": self.version,
            "env": self.env,
            "date": self.date,
            "passed": self.passed,
            "total": self.total,
            "link": self.link,
            "service": self.service
        }

    @classmethod
    def find_by_suite(cls, name):
        return cls.query.filter_by(suite=name).all()

    @classmethod
    def find_by_suite_and_version(cls, service, version, env):
        return cls.query.filter_by(service=service, version=version, env=env).all()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
