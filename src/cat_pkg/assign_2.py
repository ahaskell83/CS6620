from flask import Flask, request, jsonify
import datetime
from dateutil.relativedelta import relativedelta

def helper_date_parser(date_string):
    try:
        us_format = '%m/%d/%Y'
        return datetime.datetime.strptime(date_string,us_format).date()
    except ValueError:
        py_format = '%Y-%m-%d'
        return datetime.datetime.strptime(date_string,py_format).date()

app = Flask(__name__)
    
clowders = {}

@app.route("/clowders",methods=["GET"])
def return_all_clowders():
    return jsonify(Clowders =list(clowders.keys())), 200

@app.route("/clowders/<string:clowder_name>",methods=["GET"])
def return_named_clowders(clowder_name):
    if clowder_name not in clowders:
        return jsonify (Error = "Please enter a valid clowder name"), 400
    else:
        return jsonify(Clowders = clowders[clowder_name]), 200

@app.route('/clowders', methods=['POST'])
def return_post_clowder():
    new_clowder = request.get_json()
    clowder_name = list(new_clowder.keys())[0]
    clowders[clowder_name] = new_clowder[clowder_name]
    return jsonify(Clowder_Name = list(new_clowder.keys())[0], Clowder_Size = len(clowders)), 201

@app.put('/clowders/<string:clowder_name>/<string:cat_name>')
def return_put_new_cat_info(clowder_name, cat_name):
    clowder_dict = clowders[clowder_name]
    cat_dict = clowder_dict[cat_name]
    new_info = request.get_json()
    
    if new_info.get("New_Date") is not None:
        if type(new_info['New_Date']) == str:
            new_date = helper_date_parser(new_info['New_Date'])
        cat_dict[1] = new_date
    
    elif new_info.get('New_Name') is not None:
        new_name = new_info.get('New_Name')
        old_name = cat_dict[0]['Name']
        cat_dict[0]['Name'] = new_info['New_Name']
        if  cat_dict[0].get('Former_Names') is not None:
            cat_dict[0]['Former_Names'].append(old_name)
        else:
            cat_dict[0]['Former_Names'] = [old_name]
        clowder_dict[new_name] = cat_dict
    
    elif new_info.get("Intact") is not None:
        cat_dict[1]['Intact'] = new_info.get('Intact')
        
    else:
        return jsonify(Error = "Please input data in valid format"), 402
    
    return jsonify (Updated_Cat = cat_dict), 202   
    

@app.delete('/clowders/<string:clowder_name>')
def return_delete_clowder(clowder_name):
    if clowder_name not in clowders:
        return jsonify(Error = "Please enter a valid clowder name"), 403
    
    del_data = clowders[clowder_name]
    del clowders[clowder_name]
    return jsonify (Deleted_Clowder = del_data, Clowders_size = len(clowders)), 203

@app.delete('/clowders/<string:clowder_name>/<string:cat_name>')
def return_adoption(clowder_name, cat_name):

    if clowder_name not in clowders:
        return jsonify(Error = "Please enter a valid clowder name"), 403
    elif cat_name not in clowders[clowder_name]:
        return jsonify(Error = "Please enter a valid cat name"), 403        
        
    clowder_dict = clowders[clowder_name]
    del clowder_dict[cat_name]
    
    return jsonify(message = cat_name + " has been adopted!"), 203
   

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=3000) 