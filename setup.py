import os
import subprocess

path = "R:/Pennington/Projects/Active_Projects/Marcus_SBI/Database_Managment/AAT_OABM/Personalised-CBM_4.18.22"
os.chdir(path)
    
for folder, subpath in zip(['Image Ratings', 'Participants'], ['/Assets', '']):
    if folder not in os.listdir(path + subpath):
        os.mkdir(path + subpath + '/' + folder)

newpath = "R:/Pennington/Projects/Active_Projects/Marcus_SBI/Database_Managment/AAT_OABM/Personalised-CBM_4.18.22/Assets"
os.chdir(newpath)
subprocess.call("make_hold_out.py", shell=True)
subprocess.call("fetch_images.py", shell=True)
subprocess.call("concat_images.py", shell=True)