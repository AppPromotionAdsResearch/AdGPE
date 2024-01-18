import time
import pandas as pd
from subprocess import call
import os


def IDMDownload(df):
    IDM = r'C:\\Program Files (x86)\\Internet Download Manager\\IDMan.exe' # By default in Windows
    DownPath = '<The path to download apks >' # e.g., r'C:\\Users\\username\\Downloads\\apks\\{}\\'.format(folder)
    api = '<Your Androzoo API Key>'
    url_pre = "https://androzoo.uni.lu/api/download?apikey="+ api +"&sha256="
    for sha256 in df.sha256:
        url = url_pre + sha256
        OutPutFileName = sha256 + '.apk'
        call([IDM, '/d', url, '/p', DownPath, '/f', OutPutFileName, '/n', '/a'])

if __name__=='__main__':

    df=pd.read_csv('<apk index file>') # Only the SHA of apks are required
    # df.columns=['pkg_name','sha256','path']
    IDMDownload(df)





