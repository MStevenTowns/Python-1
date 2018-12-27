import subprocess
import os
import platform

print platform.system()
if (platform.system().lower()=="windows"):
    print "I restarted your computer"
    subprocess.call(["shutdown", "-f", "-r", "-t", "30"])
else:
    os.system("shutdown -h now")
