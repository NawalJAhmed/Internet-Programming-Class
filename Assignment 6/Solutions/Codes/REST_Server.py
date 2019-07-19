#Author: Nawal Ahmed
#Internet Programming
#Assignment 6

# import flask micro-framework and necessary modules we will need
from flask import Flask
from flask_restful import Resource, Api
from json import dumps

import sys

# add db_utils as search path for import modules
sys.path.insert(0, 'db_util')

# import all utility functions from db_util
from db_util.db_help import *

# initialise app
app = Flask(__name__)
api = Api(app)
        

# Get a list of all areas
class Get_all_areas(Resource):
    def get(self):
        return get_all_areas()

# Get all locations for the given area id
class Get_locations_for_area(Resource):
    def get(self, area):
        return get_locations_for_area( area )
        
# Get all the measurements for the given location id
class Get_measurements_for_location(Resource):
    def get(self, location):
        return get_measurements_for_location( location) 
        
# Get all the categories to which the given area belongs
class Get_categories_for_area(Resource):
    def get(self, area):
        return get_categories_for_area(area)

# Get the average measurement for the given area
class Get_average_measurement_for_area(Resource):
    def get(self, area):
        return get_average_measurement_for_area(area)

# Get the number of locations in the given area
class Get_number_of_locations_in_area(Resource):
    def get(self, area):
        return get_number_of_locations_in_area(area)


# Add requests handlers to Sever and specify route for each request
api.add_resource(Get_all_areas, '/area') # Route_1
api.add_resource(Get_locations_for_area, '/area/<int:area>/location') # Route_2
api.add_resource(Get_measurements_for_location, '/location/<int:location>/measurement') # Route_3
api.add_resource(Get_categories_for_area, '/area/<int:area>/category') # Route_4
api.add_resource(Get_average_measurement_for_area, '/area/<int:area>/average_measurement') # Route_5
api.add_resource(Get_number_of_locations_in_area, '/area/<int:area>/number_locations') # Route_6


if __name__ == '__main__':
	# run the app and specify access port
     app.run(port='12345')
