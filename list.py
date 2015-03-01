import pandas as pd
import os
import numpy as np

l = list()
names = list()
m = [0]
for i in os.listdir("c:/users/aron/programmering/python"):
    if i.endswith(".csv") and i.endswith("#") == False:
        print(i)
        a = pd.read_csv( open("c:/users/aron/programmering/python/" + i, "rb"))
        l.append(a)
        m.append(len(a))
        names.append(str(i)[4:5])
                     

        
n = len(l)

unique_ids = list(set(sum(map( lambda x: x['id'].tolist(), l),[])))

M = np.empty([len(unique_ids),1]).astype(int)
for i in l:
    print i['id']
    M = np.append(M,(np.array(map(lambda x: int(x in i['id'].values),  unique_ids)).reshape( len(unique_ids),1)), axis=1)
    
df = pd.DataFrame(M)
df.column = names

G = [sum(df.loc[k,:]) for k in range(0,df.shape[0])]
censored = [df.loc[k,df.shape[1]-1] == 1 for k in range(0,df.shape[0])]

res = pd.DataFrame({'id': unique_ids,
                    'start': np.repeat(0,df.shape[0]),
                    'stop': G,
                    'censored': censored}   )
            #np.append
