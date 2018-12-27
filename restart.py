import subprocess
import os
import platform

if (platform.system().lower()=="windows"):
    subprocess.call(["shutdown", "-f", "-r", "-t", "30"])
else:
    os.system("shutdown -h now")
