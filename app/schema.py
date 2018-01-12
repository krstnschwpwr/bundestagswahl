from app.models import Gebiete, Stimmen, Parteien
from app import ma


class CountrySchema(ma.ModelSchema):
    class Meta:
        model = Gebiete


class DetailsSchema(ma.ModelSchema):
    class Meta:
        model = Stimmen


class ParteienSchema(ma.ModelSchema):
    class Meta:
        model = Parteien


# country_schema = CountrySchema()
countries_schema = CountrySchema(many=True)
details_schema = DetailsSchema(many=True)
parteien_schema = ParteienSchema(many=True)
