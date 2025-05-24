import datetime
import math

def helper_date_parser(date_string):
    us_format = '%m/%d/%Y'
    return datetime.datetime.strptime(date_string,us_format).date()

class Cat:
    def __init__(self,name,dob,male=True,intact=True):
        self.name = name
        self.male = male
        self.dob = dob
        date_dob = helper_date_parser(dob)
        self.age_in_yrs = math.floor((abs(datetime.date.today()-date_dob).days)/365)
        self.intact = intact
    
    def get_name(self):
        return self.name
    
class Clowder:
    def __init__(self):
        self.clowder = {}
        
    def cat_moves_in(self,cat_object):
        self.clowder[cat_object.get_name()] = cat_object
    
    def cat_family_moves_in(self,list_of_cat_objects):
        pass
    
    def get_clowder_names(self):
        return self.clowder.keys()
    
    def _get_clowder_obj(self):
        return self.clowder.values()
