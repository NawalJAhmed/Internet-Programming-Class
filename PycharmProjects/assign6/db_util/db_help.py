
from db_util.db import do_command, do_insert

# /area Get a list of all areas
def get_all_areas():
    rslt = do_command(
        'select * from area',
    )
    if len(rslt) > 0:
        return rslt
    else:
        return None

# /area/(\d+)/location Get all locations for the given area id
def get_locations_for_area(area):
    rslt = do_command(
        'select * from location where location_area = ?',
        [area]
    )
    if len(rslt) > 0:
        return rslt
    else:
        return None

# /location/(\d+)/measurement Get all the measurements for the given location id
def get_measurements_for_location(location):
    rslt = do_command(
        'select * from measurement where measurement_location = ?',
        [location]
    )
    if len(rslt) > 0:
        return rslt
    else:
        return None

# /area/(\d+)/category Get all the categories to which the given area belongs
def get_categories_for_area(area):
    rslt = do_command(
        'select * from category inner join category_area on category_area.category_id=category.category_id where area_id = ?',
        [area]
    )
    if len(rslt) > 0:
        return rslt
    else:
        return None

# /area/(\d+)/average_measurement Get the average measurement for the given area
def get_average_measurement_for_area(area):
    rslt = do_command(
        'select measurement.value from measurement inner join location on measurement_location=location.location_id where location_area = ?',
        [area]
    )
    if len(rslt) > 0:
        ret_val=0
        for entry in rslt:
            ret_val+=entry['value']
        return ret_val/(len( rslt))
    else:
        return None

# /area/(\d+)/number_locations Get the number of locations in the given area
def get_number_of_locations_in_area(area):
    rslt=get_locations_for_area(area)
    if len(rslt) > 0:
        return len( rslt)
    else:
        return None