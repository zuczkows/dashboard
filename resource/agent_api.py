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

class AgentApi30(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_all()]
        posts = {}
        for number, item in enumerate(items, 1):
            posts[number] = item 
        return make_response(render_template('agent-api30.jinja2', posts=posts))

class AgentApi31(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_all()]
        posts = {}
        for number, item in enumerate(items, 1):
            posts[number] = item 
        return make_response(render_template('agent-api.jinja2', posts=posts))

class AgentApi32(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_all()]
        posts = {}
        for number, item in enumerate(items, 1):
            posts[number] = item 
        return make_response(render_template('agent-api.jinja2', posts=posts))

class AgentApi33(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_all()]
        posts = {}
        for number, item in enumerate(items, 1):
            posts[number] = item 
        return make_response(render_template('agent-api.jinja2', posts=posts))

