import os
import ultralytics
from IPython import display
home_dir  = os.getcwd()
home_dir = home_dir+"/app"
print(home_dir)
video_dir = home_dir+"/videos/traffic_1.mp4"
ultralytics.checks()