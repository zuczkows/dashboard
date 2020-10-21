from db import db
from typing import Dict, Union

ItemJson = Dict[str, Union[int, str, float]]


class DataCollector(db.Model):
    __tablename__ = "reports"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer,  nullable=False)
    version = db.Column(db.Float,  nullable=False)
    passed = db.Column(db.Integer,  nullable=False)
    total = db.Column(db.Integer,  nullable=False)
    suite = db.Column(db.String,  nullable=False)
    service = db.Column(db.String,  nullable=False)
    link = db.Column(db.String,  nullable=False)
    env = db.Column(db.String,  nullable=False)

    def json(self) -> ItemJson:
        return {
            "suite": self.suite,
            "version": self.version,
            "env": self.env,
            "date": self.date,
            "passed": self.passed,
            "total": self.total,
            "link": self.link,
            "service": self.service,
        }

    @classmethod
    def find_by_suite(cls, name: str) -> "DataCollector":
        return cls.query.filter_by(suite=name).all()

    @classmethod
    def find_by_suite_and_version(
        cls, service: str, version: float, env: str
    ) -> "DataCollector":
        return cls.query.filter_by(service=service, version=version, env=env).all()

    @classmethod
    def find_all(cls) -> "DataCollector":
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
