import datetime
from dateutil.relativedelta import relativedelta
import random
import pandas as pd


def helper_date_parser(date_string):
    try:
        us_format = '%m/%d/%Y'
        return datetime.datetime.strptime(date_string,us_format).date()
    except ValueError:
        py_format = '%Y-%m-%d'
        return datetime.datetime.strptime(date_string,py_format).date()


class Cat:
    def __init__(self,name,dob,male=True,intact=True):
        self.name = name
        self.male = male
        if type(dob) == str:
            self.dob = helper_date_parser(dob)
        else:
            self.dob = dob
        self.age_in_yrs = round(((abs(datetime.date.today()-self.dob).days)/365),1)
        self.intact = intact
        self.info_dict = {'Name': self.name, 'Male Gender': self.male, 'Date of Birth': self.dob, 'Age': self.age_in_yrs, 'Intact?':self.intact}
    
    def get_name(self):
        return self.name
    
    def get_all_details(self):
        return self.info_dict
    
class Clowder():
    clowder = {}

    def __init__(self,name):
        self.clowder_name = name
        self.clowder_dict = {self.clowder_name: self.clowder}
        
    def cat_moves_in(self,cat_object,arrival_date=datetime.date.today()):
        if type(arrival_date) == str:
            arrival_date = helper_date_parser(arrival_date)
        self.clowder[cat_object.get_name()] = [cat_object, arrival_date]
    
    def cat_family_moves_in(self,list_of_cat_objects,arrival_date=datetime.date.today()):
        if type(arrival_date) == str:
            arrival_date = helper_date_parser(arrival_date)
        for cat in list_of_cat_objects:
            self.cat_moves_in(cat,arrival_date)
            
    def adoption(self, name):
        del self.clowder[name]

    def update_move_in_date(self, cat_name, new_date):
        
        if type(new_date) == str:
            new_date = helper_date_parser(new_date)
        self.clowder[cat_name][1] =new_date
    
    def get_clowder_dict(self):
        clowder_dict = {}
        clowder_dict_all = {}
        for key, value in self.clowder.items():
            clowder_dict[key] = [value[0].info_dict, value[1]]
        clowder_dict_all[self.get_clowder_name()] = clowder_dict
        return clowder_dict_all
    
    def get_member_info(self,name):
        return self.clowder[name]
        
    def get_clowder_name(self):
        return self.clowder_name
    
    def get_clowder_names(self):
        return list(self.clowder.keys())
    
    def get_move_in_dates(self):
        return list(x[1] for x in list(self.clowder.values()))
    
    def _get_clowder_objs(self):
        return list(self.clowder.values())
    
    def _get_clowder_summary(self):
        clowder_df = pd.DataFrame(columns=['Name','Age','Male','Intact','Arrival_Date'])
        for cat in self.clowder.keys():
            row_list = [cat,self.clowder[cat][0].age_in_yrs,self.clowder[cat][0].male,self.clowder[cat][0].intact,self.clowder[cat][1]]
            clowder_df.loc[len(clowder_df)] = row_list
        return clowder_df
        
    def _check_for_breeding_criteria(self):
        
        gestation_days = (datetime.date.today() - relativedelta(days=65))
   
        df = self._get_clowder_summary()
        potential_breeders = df[(df['Age'] > 0.99) & (df['Intact'] == True) & (df['Arrival_Date'] < gestation_days)]
        genders = potential_breeders['Male'].nunique()
        if genders > 1:
            return potential_breeders
        
    def current_clowder_status(self,test_seed = False):
        breeders = self._check_for_breeding_criteria()
        
        if breeders is not None:
    
            if test_seed:
                random.seed(test_seed)
                
            num_moms = breeders['Male'].value_counts().get(False,0)
  
            dob = datetime.date.today()
            
            for i in range(num_moms):
            
                num_kittens = random.randint(1,9)

                for j in range(num_kittens):
                    kitten_name = 'mom_' + str(i) + '_kitten_' + str(j) + '_' + str(dob)
                    self.clowder[kitten_name] = [Cat(kitten_name,dob,male=random.choice([True,False]),intact=True),dob]
        
        print(len(self.clowder))
        print(self.get_clowder_names())

