from ma import ma
from models.data_collector import DataCollector


class ReportSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DataCollector
        load_instance = True
