auth_data = {'username': "test",
             'password': "5k8j9NTo292xcuRGYQVCzTUMzaw3Rt"
             }

config = { "path":"/path/to/your/videos",
           "site":"https://peertube.satoshishop.de",
           "channel":"testchannel",
           "channelID":None, #if you don't change it, we'll use the channel name to get it from the site
           "privacy":1, #1 = public and 2 = private
           "commentsEnabled":True,
           "exclude_list":["/exclude/file","/exclude/folder"]
         }

file_extensions = [".flv",".mp4",".wmv",".webm",".mkv",".3gpp",".mov",".asf",".mpeg"]