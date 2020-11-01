from flask import Flask, jsonify, render_template
from flask_restful import Api

from resource.data_collector import ApptestDataCollector, ApptestDataCollectorList
from resource.home import HomePage
from resource.agent_api import *
from resource.customer_api import CustomerApi
from resource.rest_api import RestApi
from resource.integration import Integration
from ma import ma
from marshmallow import ValidationError
from models.data_collector import DataCollector
from schemas.report import ReportSchema

report_schema_list = ReportSchema(many=True)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


@app.context_processor
def utility_processor():
    def get_total_tests():
        total = 0
        passed = 0
        failed = 0
        xfailed = 0
        data = report_schema_list.dump(DataCollector.find_all())
        for report in data:
            total += report["total"]
            passed += report["passed"]
            failed += report["failed"]
            xfailed += report["xfailed"]
        return [total, passed, failed, xfailed]

    return dict(get_total_tests=get_total_tests)


api.add_resource(HomePage, "/", "/reports")
api.add_resource(ApptestDataCollector, "/api/v1/collect/")
api.add_resource(ApptestDataCollectorList, "/items")
api.add_resource(AgentApi, "/reports/agent-api")
api.add_resource(AgentApiLabs, "/reports/agent-api/labs/<version>")
api.add_resource(AgentApiStaging, "/reports/agent-api/staging/<version>")
api.add_resource(AgentApiProduction, "/reports/agent-api/production/<version>")
api.add_resource(CustomerApi, "/reports/customer-api")
api.add_resource(RestApi, "/reports/rest-api")
api.add_resource(Integration, "/reports/integration")


if __name__ == "__main__":
    from db import db

    db.init_app(app)
    ma.init_app(app)
    app.run(port=5004, debug=True)
