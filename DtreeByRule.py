def DtreeRule(df):
    p=0     #for counting class + in A16
    n=0     #for counting class - in A16
    tp = 0  #for counting correct prediction class +
    tn = 0  #for counting correct prediction class -

    for i in range(0,len(df)):
        ##Level 1
        #Right node
        if (df.iloc[i]['A9'] == 'f'):       # A9 = f
            n+=1       #Class - 
            if(df.iloc[i]['A16'] == '-'):   #Check if prediction is correct
                tn+=1   #true negative
        
        #Level 1
        #Left Nodes
        elif (df.iloc[i]['A9'] == 't'):     # A9 = t
            #Level 2
            #X0XXX
            if( df.iloc[i]['A14'][1] == '0'):
                #Class +
                #X00XX , X02XX, X03XX, X04XX, X05XX, X08XX
                if( df.iloc[i]['A14'][2] == '0' or df.iloc[i]['A14'][2] == '2'or df.iloc[i]['A14'][2] == '3' or df.iloc[i]['A14'][2] == '4' or df.iloc[i]['A14'][2] == '5' or df.iloc[i]['A14'][2] == '8' ):
                    p+=1
                    if(df.iloc[i]['A16'] == '+'):   #Check if prediction is correct
                        tp+=1   #true positive
                #Class -
                #X06XX, X07XX, X09XX
                elif( df.iloc[i]['A14'][2] == '7'  or df.iloc[i]['A14'][2] == '6' or df.iloc[i]['A14'][2] == '9'):
                    n+=1
                    if(df.iloc[i]['A16'] == '-'):   #Check if prediction is correct
                        tn+=1   #true negative

                #X01XX
                elif (df.iloc[i]['A14'][2] == '1'):
                    #Level 3
                    if( df.iloc[i]['A6'] == 'c' or 
                        df.iloc[i]['A6'] == 'd' or df.iloc[i]['A6'] == 'cc'  or  
                        df.iloc[i]['A6'] == 'm' or df.iloc[i]['A6'] == 'r'
                        or df.iloc[i]['A6'] == 'q'  or df.iloc[i]['A6'] == 'w' or 
                        df.iloc[i]['A6'] == 'x' or df.iloc[i]['A6'] == 'aa'):
                        #Class +
                        p+=1
                        if(df.iloc[i]['A16'] == '+'):   #Check if class + prediction is correct
                            tp+=1       #true positive

                    elif( df.iloc[i]['A6'] == 'ff' or df.iloc[i]['A6'] == 'i' or df.iloc[i]['A6'] == 'j' or df.iloc[i]['A6'] == 'k'or df.iloc[i]['A6'] == 'e'):
                        #Class -
                        n+=1
                        if(df.iloc[i]['A16'] == '-'):   #Check if class - prediction is correct
                            tn+=1       #true negative

                ## Post pruning give better accuracy ###
                # A14 = X02XX
                elif (df.iloc[i]['A14'][2] == '2'):
                    if( df.iloc[i]['A6'] == 'c' or 
                        df.iloc[i]['A6'] == 'd' or df.iloc[i]['A6'] == 'cc'  or  
                        df.iloc[i]['A6'] == 'm' or df.iloc[i]['A6'] == 'r'
                        or df.iloc[i]['A6'] == 'q'  or df.iloc[i]['A6'] == 'w' or 
                        df.iloc[i]['A6'] == 'x' or df.iloc[i]['A6'] == 'ff'):
                        #Class +
                        p+=1
                        if(df.iloc[i]['A16'] == '+'):   #Check if class + prediction is correct
                            tp+=1     #true positive

                    elif( df.iloc[i]['A6'] == 'aa' or df.iloc[i]['A6'] == 'i' or df.iloc[i]['A6'] == 'j' or df.iloc[i]['A6'] == 'k'or df.iloc[i]['A6'] == 'e'):
                        #Class -
                        n+=1
                        if(df.iloc[i]['A16'] == '-'):   #Check if class - prediction is correct
                            tn+=1     #true negative

                # A14 = X03XX 
                elif (df.iloc[i]['A14'][2] == '3'):
                    if( df.iloc[i]['A6'] == 'c' or df.iloc[i]['A6'] == 'e' or
                        df.iloc[i]['A6'] == 'cc'  or df.iloc[i]['A6'] == 'aa' or  
                        df.iloc[i]['A6'] == 'm' or df.iloc[i]['A6'] == 'r'
                        or df.iloc[i]['A6'] == 'q'  or df.iloc[i]['A6'] == 'w' or 
                        df.iloc[i]['A6'] == 'x' or df.iloc[i]['A6'] == 'ff' or df.iloc[i]['A6'] == 'i'):
                        #Class +
                        p+=1
                        if(df.iloc[i]['A16'] == '+'):   #Check if class + prediction is correct
                            tp+=1     #true positive

                    elif( df.iloc[i]['A6'] == 'd'  or df.iloc[i]['A6'] == 'j' or df.iloc[i]['A6'] == 'k'):
                        #Class -
                        n+=1
                        if(df.iloc[i]['A16'] == '-'):   #Check if class - prediction is correct
                            tn+=1     #true negative

                #A14 = X04XX            
                elif (df.iloc[i]['A14'][2] == '4'):
                    if( df.iloc[i]['A6'] == 'c' or 
                         df.iloc[i]['A6'] == 'cc'  or  
                        df.iloc[i]['A6'] == 'm' or df.iloc[i]['A6'] == 'r'
                        or df.iloc[i]['A6'] == 'q'  or df.iloc[i]['A6'] == 'w' or 
                        df.iloc[i]['A6'] == 'x' or df.iloc[i]['A6'] == 'ff' or df.iloc[i]['A6'] == 'i'):
                        #Class +
                        p+=1
                        if(df.iloc[i]['A16'] == '+'):   #Check if class + prediction is correct
                            tp+=1     #true positive

                    elif( df.iloc[i]['A6'] == 'd' or df.iloc[i]['A6'] == 'aa'  or df.iloc[i]['A6'] == 'j' or df.iloc[i]['A6'] == 'k'or df.iloc[i]['A6'] == 'e'):
                        #Class -
                        n+=1
                        if(df.iloc[i]['A16'] == '-'):   #Check if class - prediction is correct
                            tn+=1     #true negative

            
            #A14 = X1XXX or X2XXX 
            elif( df.iloc[i]['A14'][1] == '1' or df.iloc[i]['A14'][1] == '2' ):
                #Class +
                p+=1
                if(df.iloc[i]['A16'] == '+'):   #Check if prediction is correct
                        tp+=1       #true positive
            
        
    return p,n,tp,tn

