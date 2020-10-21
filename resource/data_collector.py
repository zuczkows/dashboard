from flask_restful import Resource
from flask import request
from models.data_collector import DataCollector
from schemas.report import ReportSchema
from marshmallow import ValidationError

report_schema = ReportSchema()


class ApptestDataCollector(Resource):
    @classmethod
    def post(cls):
        """ POST method which saves apptests results. """

        try:
            report = report_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400


        try:
            report.save_to_db()
        except:
            return {"message": "An error occurred while inserting the item."}, 500

        return report.json(), 201


class ApptestDataCollectorList(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_all()]
        return {"reports": items}, 200
