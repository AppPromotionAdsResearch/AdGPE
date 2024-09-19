import os
import subprocess
import sys
import pandas as pd
import argparse
import time
# Add the droidbot directory to the system path
#sys.path.append('//')
nowTime = time.strftime('%Y.%m.%d-%H.%M.%S')

parser = argparse.ArgumentParser(description="Run the droidbot script for APK analysis.")
# parser.add_argument("apk_name", help="Name of the APK file to analyze.")
parser.add_argument("-d", "--serialNumber", help="Input the serial number of the device")
parser.add_argument('-i', '--input_dir')
parser.add_argument('-p', '--policy')
args = parser.parse_args()
timeout='300'
from start import main
def run_droidbot(apk_name,pkg_name):
    """
    Runs the droidbot script for the given APK name and returns the ads found.
    """
    if 'random' in args.policy:

        sys.argv = ['droidbot', '-a', f'{args.input_dir}/{apk_name}.apk',
                '-o', f'output_dir/{pkg_name}_{args.policy}_{timeout}/', '-keep_env', '-keep_app', '-timeout', timeout,'-d', args.serialNumber,
                '-policy',args.policy.split('-')[0],'-random']
    else:
        sys.argv = ['droidbot', '-a', f'{args.input_dir}/{apk_name}.apk',
                '-o', f'output_dir/{pkg_name}_{args.policy}_{timeout}/', '-keep_env', '-keep_app', '-timeout', timeout,'-d', args.serialNumber,
                '-policy',args.policy]

    return main()

def process_apks(apk_list):
    """
    Processes each APK in the list up to 20 times or until 3 iterations with no ads.
    """
    df={'pkg_name':[],'ad':[],'sha':[],'time':[]}
    begin_time=time.time()
    for pkg_name,apk in apk_list:
        no_ads_count = 0
        found_ads=[]
        for iteration in range(5):
            print(f"Processing {apk}, iteration {iteration + 1}")
            ads = run_droidbot(apk,pkg_name)

            if not ads:
                no_ads_count += 1
                print(f"No ads found for {apk} in iteration {iteration + 1}.")
            else:
                previous_len=len(list(set(found_ads)))
                found_ads.extend(ads)
                current_len=len(list(set(found_ads)))
                if previous_len==current_len:
                    no_ads_count+=1
                else:
                    no_ads_count = 0  # Reset the count if ads are found
                    print(f"Ads found for {apk} in iteration {iteration + 1}: {ads}")

            if no_ads_count >= 3:
                print(f"Skipping to next APK after 3 consecutive iterations with no ads for {apk}.")
                break
        df['pkg_name'].append(pkg_name)
        df['ad'].append(list(set(found_ads)))
        df['sha'].append(apk)
        end_time=time.time()
        df['time'].append(end_time-begin_time)
        pd.DataFrame(df).to_csv(f'data/{args.serialNumber}_{nowTime}_{args.policy}.csv',index=False)
        os.system(f'adb -s {args.serialNumber} uninstall {pkg_name}')

if __name__=='__main__':
    df=pd.read_csv('data/apk_index.csv') # This should be the index file of your apks
    apk_list = list(df[['pkg_name', 'sha']].itertuples(index=False, name=None))
    process_apks(apk_list)
