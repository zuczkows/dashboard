from flask_restful import Resource, reqparse
from models.data_collector import DataCollector


class ApptestDataCollector(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "date", type=int, required=True, help="This field cannot be left blank!"
    )
    parser.add_argument(
        "passed", type=int, required=True, help="This field cannot be left blank!"
    )
    parser.add_argument(
        "total", type=int, required=True, help="This field cannot be left blank!"
    )
    parser.add_argument(
        "suite", type=str, required=True, help="This field cannot be left blank!"
    )
    parser.add_argument(
        "link", type=str, required=True, help="This field cannot be left blank!"
    )
    parser.add_argument(
        "version", type=float, required=True, help="This field cannot be left blank!"
    )
    parser.add_argument(
        "service", type=str, required=True, help="This field cannot be left blank!"
    )
    parser.add_argument(
        "env", type=str, required=True, help="This field cannot be left blank!"
    )


    @classmethod
    def post(cls):
        ''' POST method which saves apptests results. '''

        data = ApptestDataCollector.parser.parse_args()
        data = DataCollector(**data)

        try:
            data.save_to_db()
        except:
            return {"message": "An error occurred while inserting the item."}, 500

        return data.json(), 201

class ApptestDataCollectorList(Resource):
    def get(self):
        items = [item.json() for item in DataCollector.find_all()]
        return {"reports": items}, 200