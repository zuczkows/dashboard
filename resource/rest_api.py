from flask_restful import Resource, reqparse
from flask import render_template, make_response
from models.data_collector import DataCollector


class RestApi(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_all()]
        posts = {}
        for number, item in enumerate(items, 1):
            posts[number] = item
        return make_response(render_template("rest-api.jinja2", posts=posts))
