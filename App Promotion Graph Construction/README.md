# Data preparation
First, have a bunch of apk files to be explored. 

In this work, we download the full list from https://androzoo.uni.lu/.
We then use IDM to download the apk files to local.

```shell
python download_androzoo.py
```


# Ad-oriented UI Exploration 
The proposed Ad-oriented UI Exploration is implemented based on droidbot.
Most customization can be found in `record_ads.py`

```shell
python droidad.py -d <serial_number> -i <input_apk_dir> -p <policy_name>
```
- **<serial_number>** is the serial number of your phone, which is connected with the computer and Developer Options is already set
- **<input_apk_dir>** is the folder where you put the APK files that need to be explored. Two example apks are provided under the `data` folder
- To run the prosed ad-oriented UI exploration, **<policy_name>** should be 'dfs_greedy'.
- - 'bfs_greedy' is the BFS version
- - 'bfs' or 'dfs' is the original Droidbot
- - 'ad_bfs' or 'ad_dfs' is the Large Language Model assisted exploration, which is under developing

After running this command, the output logs will be generated under the directory `output_dir`.
The exploration results will be save into the `data` folder.


# Graph Construction

```shell
python graph_construction.py
```
Run this command and you can get two csv files of the nodes and links of the App Promotion Graph.

Note that this repo does not include the script to crawl Google Play and VirusTotal.  
To crawl VirustTotal, you need to write an email to VirusTotal official to obtain an advanced API.  







