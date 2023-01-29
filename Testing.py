from DtreeByRule import *
#For testing
def testing(test):

    p,n,tp,tn = DtreeRule(test)     #Call function by rule
                                #return number of correct prediction and total number of prediction

    accuracy = ((tp+tn)/len(test))*100      #calculate accuracy
                                            # total number of correct prediction / total number of prediction 

    print("p =  ", p)
    print("n =  ", n)
    print("tp =  ", tp)
    print("tn =  " , tn)
    print("Accuracy =  %5.3f" % accuracy ,"%")