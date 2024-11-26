import requests
import json
import pandas as pd
from collections import defaultdict


def get_facts(cik):
    url = 'https://data.sec.gov/api/xbrl/companyfacts/CIK{:>010s}.json'.format(cik)
    headers = {
        "User-Agent": "University of Washington abcurtis@uw.edu"
    }
    res = requests.get(url=url,headers=headers)
    j = json.loads(res.text)

    # Save the JSON output to a file
    json_filename = f'CIK{cik}.json'
    with open(json_filename, 'w') as json_file:
        json.dump(j, json_file, indent=2)
        
    # use this to look at the structure of a single record
    # open('out/tsla.json', 'w').write(json.dumps(result,indent=2))

    o = defaultdict(dict)
    def checker(j,x):
        if x in j:
            return j[x]
        else:
            return None


    for acct in j['facts']['us-gaap']:
        label = j['facts']['us-gaap'][acct]['label']   
        for unit in j['facts']['us-gaap'][acct]['units']:
            for rec in j['facts']['us-gaap'][acct]['units'][unit]:
                #get most recent facts, omit instantaneous
                if 'frame' in rec and 'start' in rec:
                    if rec['frame'][-1] == 'I':
                        continue
                    o[rec['frame']][f'{acct}_{unit}'] = rec['val']
                    o[rec['frame']]['start'] = checker(rec,'start')
                    o[rec['frame']]['end'] = rec['end']
                    o[rec['frame']]['fy'] = rec['fy']
                    o[rec['frame']]['fp'] = rec['fp']
                    o[rec['frame']]['form'] = rec['form']
                    o[rec['frame']]['filed'] = rec['filed']
                
    df = pd.DataFrame.from_dict(o,orient='index')
    df.index.names = ['frame']
    df.reset_index(inplace=True)
    df.insert(loc=1,column='cik',value=cik)
    return df

# use a list of ciks or parse list from file
ciks = ['1108524']

l = []

for k,i in enumerate(ciks):
    l.append(get_facts(i))


# this could be sped up
# delete "join='inner'" for outer join concatenation (default), which gives all xbrl accounts listed
df = pd.concat(l,join='inner',ignore_index=True)
df.sort_values(by=['cik','frame'],inplace=True)
df.to_csv('ACCTG522_Labs/Class01/CKM.csv', index=False)
