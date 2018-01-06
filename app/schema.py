from app.models import Gebiete
from app import ma


class CountrySchema(ma.ModelSchema):
    class Meta:
        model = Gebiete



# country_schema = CountrySchema()
countries_schema = CountrySchema(many=True)


