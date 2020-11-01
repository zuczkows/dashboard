from flask_restful import Resource
from flask import request
from models.data_collector import DataCollector
from schemas.report import ReportSchema

report_schema = ReportSchema()
report_schema_list = ReportSchema(many=True)


class ApptestDataCollector(Resource):
    @classmethod
    def post(cls):
        """ POST method which saves apptests results. """
        report = report_schema.load(request.get_json())
        try:
            report.save_to_db()
        except:
            return {"message": "An error occurred while inserting the item."}, 500
        return report_schema.dump(report), 201


class ApptestDataCollectorList(Resource):
    def get(self):
        return {"reports": report_schema_list.dump(DataCollector.find_all())}, 200
