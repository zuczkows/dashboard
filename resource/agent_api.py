from flask_restful import Resource, reqparse
from flask import render_template, make_response
from models.data_collector import DataCollector
from schemas.report import ReportSchema

report_schema = ReportSchema()


def get(env: str, service: str, version: float):
    items = [
        report_schema.dump(item)
        for item in DataCollector.find_by_suite_and_version(
            env=env, service=service, version=version
        )
    ]
    try:
        version = items[0].get("version")
        env = items[0].get("env")
    except:
        return make_response(render_template("404.jinja2"))
    return make_response(
        render_template(
            "agent-api-reports.jinja2", reports=items, version=version, env=env
        )
    )


class AgentApi(Resource):
    def get(self):
        return make_response(render_template("agent-api.jinja2"))


class AgentApiLabs30(Resource):
    def get(self):
        return get(env="labs", service="agent-api", version=3.0)


class AgentApiLabs31(Resource):
    def get(self):
        return get(env="labs", service="agent-api", version=3.1)


class AgentApiLabs32(Resource):
    def get(self):
        return get(env="labs", service="agent-api", version=3.2)


class AgentApiLabs33(Resource):
    def get(self):
        return get(env="labs", service="agent-api", version=3.3)


class AgentApiStaging30(Resource):
    def get(self):
        return get(env="staging", service="agent-api", version=3.0)


class AgentApiStaging31(Resource):
    def get(self):
        return get(env="staging", service="agent-api", version=3.0)


class AgentApiStaging32(Resource):
    def get(self):
        return get(env="staging", service="agent-api", version=3.0)


class AgentApiStaging33(Resource):
    def get(self):
        return get(env="staging", service="agent-api", version=3.0)


class AgentApiProduction30(Resource):
    def get(self):
        return get(env="prod", service="agent-api", version=3.0)


class AgentApiProduction31(Resource):
    def get(self):
        return get(env="prod", service="agent-api", version=3.0)


class AgentApiProduction32(Resource):
    def get(self):
        return get(env="prod", service="agent-api", version=3.0)


class AgentApiProduction33(Resource):
    def get(self):
        return get(env="prod", service="agent-api", version=3.0)
