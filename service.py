from flask import Flask, jsonify, render_template
from flask_restful import Api

from resource.items import Items
from resource.data_collector import ApptestDataCollector, ApptestDataCollectorList
from resource.home import HomePage
from resource.agent_api import AgentApi, AgentApi30, AgentApi31, AgentApi32, AgentApi33
from resource.customer_api import CustomerApi
from resource.rest_api import RestApi
from resource.integration import Integration

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(HomePage,    "/reports")
api.add_resource(ApptestDataCollector, "/api/v1/collect/")
api.add_resource(Items, "/post/<int:post_id>")
api.add_resource(ApptestDataCollectorList, "/items")
api.add_resource(AgentApi,    "/reports/agent-api")
api.add_resource(AgentApi30,  "/reports/agent-api/v3.0")
api.add_resource(AgentApi31,  "/reports/agent-api/v3.1")
api.add_resource(AgentApi32,  "/reports/agent-api/v3.2")
api.add_resource(AgentApi33,  "/reports/agent-api/v3.3")
api.add_resource(CustomerApi, "/reports/customer-api")
api.add_resource(RestApi,     "/reports/rest-api")
api.add_resource(Integration, "/reports/integration")



if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5004, debug=True)
