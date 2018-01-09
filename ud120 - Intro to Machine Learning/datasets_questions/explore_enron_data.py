#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "There are", len(enron_data), "data points(i.e. people) in the Enron dataset"
print "For each person,", len(enron_data.values()[0]), "features are available"
print "There are", sum([value['poi'] for value in enron_data.values()]), "POIs in the dataset"

print "The total value of the stock belonging to James Prentice is", enron_data["PRENTICE JAMES"]["total_stock_value"]
print "We have", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"], "messages from Wesley Colwell to POIs"
print "The value of stock options exercised by Jeff Skilling is", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print "Total payments of Jeff Skilling is", enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Total payments of Kenneth Lay is", enron_data["LAY KENNETH L"]["total_payments"]
print "Total payments of Andrew Fastow is", enron_data["FASTOW ANDREW S"]["total_payments"]

print len([1 for value in enron_data.values() if value['salary'] != "NaN"]), "folks have a quantified salary"
print len([1 for value in enron_data.values() if value['email_address'] != "NaN"]), "folks have a known email address"

total_payments_nan = len([1 for value in enron_data.values() if value['total_payments'] == "NaN"])
print round(100.0*total_payments_nan/len(enron_data)), "% of people in the dataset have 'NaN' for their total payments"
total_payments_nan_poi = len([1 for value in enron_data.values() if value['poi'] and value['total_payments'] == "NaN"])
print round(100.0*total_payments_nan_poi/len(enron_data)), "% of POIs in the dataset have 'NaN' for their total payments"
