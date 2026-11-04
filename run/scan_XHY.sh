#!/bin/bash
#launch_scan.py --mode "scan" -X 1001 -S 301 -m "TRSMBroken" -d "SbbHtautau" -n 100 -s "zoom" -f -p "medium"
#launch_scan.py --mode "scan" -l -d SWWHbb -i CMS_boosted -n 10000 -s "zoom" -f -p "medium"

mapfile -t file_lines < "../data/mass_points/MXMS.txt"
for line in "${file_lines[@]}"; do 
    IFS=',' read -ra ARR <<< "$line"
    MX=${ARR[0]}
    MS=${ARR[1]}
    echo "Running scan for mass point (${MX},${MS}) ...."
    if [ -f "output/TRSMBroken/scan/SWWHbb/X${MX}_S${MS}/summary_zoom_TRSMBroken_SWWHbb_X${MX}_S${MS}.tsv" ]; then 
        echo "Already ran scan for (${MX},${MS}), skipping...."  
    elif [ "$MX" -ge 3000 ]; then 
        echo "MX >= 3000 GeV, incalculable, skipping...."
    else
        (set -x; launch_scan.py --mode scan -X $MX -S $MS -m TRSMBroken -d SWWHbb -n 10000 -s zoom -f -p medium)
    fi
done
