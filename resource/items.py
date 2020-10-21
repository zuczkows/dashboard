from flask_restful import Resource, reqparse
from flask import render_template, make_response
from resource.data_collector import DataCollector


class Items(Resource):
    def get(self, post_id):
        items = [item.json() for item in DataCollector.find_all()]
        post = items[0]
        if not post:
            return (
                render_template(
                    "404.jinja2", message=f"A post with id {post_id} was not found."
                ),
                404,
            )
        return make_response(render_template("post.jinja2", post=post))
