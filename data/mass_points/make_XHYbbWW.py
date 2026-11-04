'''
Script to generate the JSON file for CMS B2G-23-007 X->H(bb)Y(WW->4q) analysis
'''
import pandas as pd
import json, sys

# Columns are:  [MX, MY, Expected  2.5, Expected 16.0, Expected 50.0, Expected 84.0, Expected 97.5, Observed]
df = pd.read_csv('datacards-B2G-23-007/input/v2/combined_limits.csv')

# Metadata
collaboration  = "CMS"
year           = "2025"
sqrt_s         = 13.0
decay_channel  = "X->S(WW)H(bb)"
units          = "fb"
includes_decay = True

mass_list = {
    "collaboration": collaboration,
    "year": year,
    "sqrt_s": sqrt_s,
    "decay_channel": decay_channel,
    "units": units,
    "includes_decay": includes_decay
}

mass_points = []

n=len(df)
skip=0
done=0

mxmy = []

for index, row in df.iterrows():
    mX = row['MX']
    mS = row['MY']
    mxmy.append(f'{int(mX)},{int(mS)}\n')
    if mX >= 3000:
        skip += 1
        continue
    else:
        done += 1
    mass_point = {
        "mX": mX,
        "mS": mS,
        "observed_limit": row["Observed"],
        "expected_limit": row["Expected 50.0"],
        "expected_limit_m1": row["Expected 16.0"],
        "expected_limit_p1": row["Expected 84.0"],
        "expected_limit_m2": row["Expected  2.5"],
        "expected_limit_p2": row["Expected 97.5"],
        "resolvable": True
    }
    mass_points.append(mass_point)

print(f'Ran on {done}/{n} signals. Skipped {skip}/{n} signals with MX>=3000 GeV...')

mass_list["mass_points"] = mass_points

with open("SWWHbb_CMS_boosted.json", "w") as fp:
    json.dump(mass_list, fp, indent=4)

with open('MXMS.txt','w') as fp:
    for i in mxmy:
        fp.write(i)

