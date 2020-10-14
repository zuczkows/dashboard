from flask import Flask, jsonify, render_template
from flask_restful import Api

from resource.items import Items
from resource.data_collector import ApptestDataCollector, ApptestDataCollectorList
from resource.home import HomePage

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(ApptestDataCollector, "/api/v1/collect/")
api.add_resource(Items, "/post/<int:post_id>")
api.add_resource(ApptestDataCollectorList, "/items")
api.add_resource(HomePage, "/")



if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5004, debug=True)
