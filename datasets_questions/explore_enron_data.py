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

poi_count = 0

for name in enron_data:
    elem = enron_data[name]
    print name, ' ', elem['poi']
    if elem['poi'] :
        poi_count = poi_count +1

print 'POI count ', poi_count

enron_data['PRENTICE JAMES']['total_stock_value']


enron_data['COLWELL WESLEY']['from_this_person_to_poi']

enron_data['SKILLING JEFFREY K']['exercised_stock_options']

p_skilling = enron_data['SKILLING JEFFREY K']['total_payments']

p_lay = enron_data['LAY KENNETH L']['total_payments']

p_fastow = enron_data['FASTOW ANDREW S']['total_payments']

salary_number = 0

for name in enron_data:
    elem = enron_data[name]
##    print name, ' ', elem['salary']
    if elem['salary'] != 'NaN' :
        salary_number = salary_number + 1

print "Number of people with salary number: ", salary_number

ntotal_number = 0

for name in enron_data:
    elem = enron_data[name]
##    print name, ' ', elem['total_payments']
    if elem['total_payments'] == 'NaN' :
        ntotal_number = ntotal_number + 1

print " "
print "Number of people with no total payment number: ", ntotal_number

numb = len(enron_data)
perc = 100.0 * ntotal_number/numb
print " which is ", perc, "% of the total entries."


poi_ntotal_count = 0

for name in enron_data:
    elem = enron_data[name]
##    print name, ' ', elem['poi']
    if elem['poi'] and elem['total_payments'] == 'NaN':
        poi_ntotal_count = poi_ntotal_count + 1
        
print " "
print "Number of poi with no total payment number: ", poi_ntotal_count

perc_poi = 100.0 * poi_ntotal_count/poi_count
print " which is ", perc_poi, "% of the total poi entries."

