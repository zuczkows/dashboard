from flask_restful import Resource, reqparse
from flask import render_template, make_response
from models.data_collector import DataCollector
from schemas.report import ReportSchema

report_schema = ReportSchema()


class HomePage(Resource):
    def get(self):
        items = [report_schema.dump(item) for item in DataCollector.find_all()]
        posts = {}
        for number, item in enumerate(items, 1):
            posts[number] = item
        return make_response(render_template("home.jinja2", posts=posts))
