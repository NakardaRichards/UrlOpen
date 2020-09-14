"""
Author:Nakarda Richards
"""

import time
import webbrowser


siteName = input("What site do you want to open: ")

if (siteName == "Youtube" or siteName == "youtube"):

    url1 = ('www.youtube.com')
    webbrowser.open_new_tab(url1)

elif (siteName =="Amazon" or siteName =="amazon"):

    url2 = ('www.amazon.com')
    webbrowser.open_new_tab(url2)



else:
    time.sleep(2.5)
    print("...............")
    time.sleep(3.5)
    print("There is no such site.")