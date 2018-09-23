#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    tmp_data = []


    ### your code goes here

    for i in range(len(predictions)):
        ## print "i: ", i, " prediction: ", predictions[i], " age: ", ages[i], " net_worth: ", net_worths[i]
        error_i = abs(predictions[i] - net_worths[i])
        ## print "Error: ", error_i
        tupl = (ages[i], net_worths[i], error_i)
        ## print tupl
        tmp_data.append(tupl)

    output = sorted(tmp_data, key=lambda x: x[-1])
    idx = int(len(predictions)*0.9)
    cleaned_data = output[0:idx]
    return cleaned_data

