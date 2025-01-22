# Data preparation
First, prepare APKs files to be explored. Put them into `data` folder. 

In this work, we download the FULL LIST from https://androzoo.uni.lu/.
We then use IDM to download the apk files to local.

In this repo, we provide a sample index file in `data/apk_index.csv`. To download using IDM, run this script
```shell
python download_androzoo.py
```


# Ad-oriented UI Exploration 
The proposed Ad-oriented UI Exploration is implemented based on droidbot.
Most customization can be found in `record_ads.py`.

Before running the script, make sure you install the clipper application from https://github.com/majido/clipper in your phone/emulator.

To perform AdGPE's UI exploration on a given APK, run this script
```shell
python droidad.py -d <serial_number> -i <input_apk_dir> -p <policy_name>
```
- **<serial_number>** is the serial number of your phone, which is connected with the computer and Developer Options is already set.
- **<input_apk_dir>** is the folder where you put the APK files that need to be explored. 
- To run AdGPE, **<policy_name>** should be 'dfs_greedy'.
- - 'bfs_greedy' is AdGPE(bfs)
- - 'bfs' or 'dfs' is Droidbot
- - 'ad_bfs' or 'ad_dfs' is the Large Language Model assisted exploration, which is under developing

Two example apks are provided under the `data` folder
You can run a demo
```shell
python droidad.py -i data -p bfs_greedy
```
After running this command, the output logs will be generated under the directory `output_dir`.
The exploration results will be save into `data` folder.


# Graph Construction

```shell
python graph_construction.py
```
Run this command and you can get two csv files of the nodes and links of the App Promotion Graph.

Note that this repo does not include the script to crawl Google Play and VirusTotal.  
To crawl VirustTotal, you need to email VirusTotal official to obtain an advanced API.  







