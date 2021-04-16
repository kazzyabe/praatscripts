import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("boundary_tones.csv")
df = pd.DataFrame(data, columns = data.columns)

def difference(s,qs,m,qe,e):
    '''
        Calculate the difference of f0 at start and end
        ** need boundary_tones.csv extracted by boundary_tone.praat
            Filename,Label,Start,f0_start,Quo_start,f0_quostart,Mid,f0_mid,Quo_end,f0_quoend,End,f0_end
                                   s                    qs             m               qe           e
    '''
    if s != "--undefined--":
        start = s
    elif qs != "--undefined--":
        start = qs
    else:
        start = "--undefined--"
    

    if e != "--undefined--":
        end = e
    elif qe != "--undefined--":
        end = qe
    else:
        end = "--undefined--"

    print(start, end)
    if (start != "--undefined--") and (end != "--undefined--"):
        start = float(start)
        end = float(end)
        res = end - start
    else:
        res = "--undefined--"
    return res

df["Diff"] = df.apply(lambda d: difference(d['f0_start'],
                        d['f0_quostart'], d['f0_mid'], d['f0_quoend'], d['f0_end'])
                        ,axis=1)

df.to_csv("Participants/boundary_tones_diff.csv", index=False)