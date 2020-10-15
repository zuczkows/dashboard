from flask_restful import Resource, reqparse
from flask import render_template, make_response
from models.data_collector import DataCollector

class AgentApi(Resource):
    def get(self):
        return make_response(render_template('agent-api.jinja2'))
        

class AgentApiLabs30(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_by_suite_and_version(env='labs', service='agent-api', version=3.0)]
        return make_response(render_template('agent-api-labs-30.jinja2', reports=items))

class AgentApiLabs31(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_by_suite_and_version(env='labs', service='agent-api', version=3.1)]
        return make_response(render_template('agent-api-labs-31.jinja2', reports=items))

class AgentApiLabs32(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_by_suite_and_version(env='labs', service='agent-api', version=3.2)]
        return make_response(render_template('agent-api-labs-32.jinja2', reports=items))

class AgentApiLabs33(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_by_suite_and_version(env='labs', service='agent-api', version=3.3)]
        return make_response(render_template('agent-api-labs-33.jinja2', reports=items))

class AgentApiStaging30(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_by_suite_and_version(env='staging', service='agent-api', version=3.0)]
        return make_response(render_template('agent-api-staging-30.jinja2', reports=items))

class AgentApiStaging31(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_by_suite_and_version(env='staging', service='agent-api', version=3.1)]
        return make_response(render_template('agent-api-staging-31.jinja2', reports=items))

class AgentApiStaging32(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_by_suite_and_version(env='staging', service='agent-api', version=3.2)]
        return make_response(render_template('agent-api-staging-32.jinja2', reports=items))

class AgentApiStaging33(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_by_suite_and_version(env='staging', service='agent-api', version=3.3)]
        return make_response(render_template('agent-api-staging-33.jinja2', reports=items))

class AgentApiProduction30(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_by_suite_and_version(env='prod', service='agent-api', version=3.0)]
        return make_response(render_template('agent-api-prod-30.jinja2', reports=items))

class AgentApiProduction31(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_by_suite_and_version(env='prod', service='agent-api', version=3.1)]
        return make_response(render_template('agent-api-prod-31.jinja2', reports=items))

class AgentApiProduction32(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_by_suite_and_version(env='prod', service='agent-api', version=3.2)]
        return make_response(render_template('agent-api-prod-32.jinja2', reports=items))

class AgentApiProduction33(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_by_suite_and_version(env='prod', service='agent-api', version=3.3)]
        return make_response(render_template('agent-api-prod-33.jinja2', reports=items))

