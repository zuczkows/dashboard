from flask_restful import Resource, reqparse
from flask import render_template, make_response
from models.data_collector import DataCollector

class AgentApi(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_all()]
        posts = {}
        for number, item in enumerate(items, 1):
            posts[number] = item 
        return make_response(render_template('agent-api.jinja2', posts=posts))
        

class AgentApiLabs30(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_all()]
        posts = {}
        for number, item in enumerate(items, 1):
            posts[number] = item 
        return make_response(render_template('agent-api-labs-30.jinja2', posts=posts))

class AgentApiLabs31(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_all()]
        posts = {}
        for number, item in enumerate(items, 1):
            posts[number] = item 
        return make_response(render_template('agent-api-labs-31.jinja2', posts=posts))

class AgentApiLabs32(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_all()]
        posts = {}
        for number, item in enumerate(items, 1):
            posts[number] = item 
        return make_response(render_template('agent-api-labs-32.jinja2', posts=posts))

class AgentApiLabs33(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_all()]
        posts = {}
        for number, item in enumerate(items, 1):
            posts[number] = item 
        return make_response(render_template('agent-api-labs-33.jinja2', posts=posts))

class AgentApiStaging30(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_all()]
        posts = {}
        for number, item in enumerate(items, 1):
            posts[number] = item 
        return make_response(render_template('agent-api30.jinja2', posts=posts))

class AgentApiStaging31(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_all()]
        posts = {}
        for number, item in enumerate(items, 1):
            posts[number] = item 
        return make_response(render_template('agent-api.jinja2', posts=posts))

class AgentApiStaging32(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_all()]
        posts = {}
        for number, item in enumerate(items, 1):
            posts[number] = item 
        return make_response(render_template('agent-api.jinja2', posts=posts))

class AgentApiStaging33(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_all()]
        posts = {}
        for number, item in enumerate(items, 1):
            posts[number] = item 
        return make_response(render_template('agent-api.jinja2', posts=posts))

class AgentApiProduction30(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_all()]
        posts = {}
        for number, item in enumerate(items, 1):
            posts[number] = item 
        return make_response(render_template('agent-api30.jinja2', posts=posts))

class AgentApiProduction31(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_all()]
        posts = {}
        for number, item in enumerate(items, 1):
            posts[number] = item 
        return make_response(render_template('agent-api.jinja2', posts=posts))

class AgentApiProduction32(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_all()]
        posts = {}
        for number, item in enumerate(items, 1):
            posts[number] = item 
        return make_response(render_template('agent-api.jinja2', posts=posts))

class AgentApiProduction33(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_all()]
        posts = {}
        for number, item in enumerate(items, 1):
            posts[number] = item 
        return make_response(render_template('agent-api.jinja2', posts=posts))

