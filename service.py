from flask import Flask, jsonify, render_template
from flask_restful import Api

from resource.items import Items
from resource.data_collector import ApptestDataCollector, ApptestDataCollectorList
from resource.home import HomePage
from resource.agent_api import *
from resource.customer_api import CustomerApi
from resource.rest_api import RestApi
from resource.integration import Integration
from ma import ma
from marshmallow import ValidationError

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

api.add_resource(HomePage, "/reports")
api.add_resource(ApptestDataCollector, "/api/v1/collect/")
api.add_resource(ApptestDataCollectorList, "/items")
api.add_resource(AgentApi, "/reports/agent-api")
api.add_resource(AgentApiLabs30, "/reports/agent-api/labs/v3.0")
api.add_resource(AgentApiLabs31, "/reports/agent-api/labs/v3.1")
api.add_resource(AgentApiLabs32, "/reports/agent-api/labs/v3.2")
api.add_resource(AgentApiLabs33, "/reports/agent-api/labs/v3.3")
api.add_resource(AgentApiStaging30, "/reports/agent-api/staging/v3.0")
api.add_resource(AgentApiStaging31, "/reports/agent-api/staging/v3.1")
api.add_resource(AgentApiStaging32, "/reports/agent-api/staging/v3.2")
api.add_resource(AgentApiStaging33, "/reports/agent-api/staging/v3.3")
api.add_resource(AgentApiProduction30, "/reports/agent-api/production/v3.0")
api.add_resource(AgentApiProduction31, "/reports/agent-api/production/v3.1")
api.add_resource(AgentApiProduction32, "/reports/agent-api/production/v3.2")
api.add_resource(AgentApiProduction33, "/reports/agent-api/production/v3.3")
api.add_resource(CustomerApi, "/reports/customer-api")
api.add_resource(RestApi, "/reports/rest-api")
api.add_resource(Integration, "/reports/integration")


if __name__ == "__main__":
    from db import db

    db.init_app(app)
    ma.init_app(app)
    app.run(port=5004, debug=True)
