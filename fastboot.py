import subprocess
import os
def check():
    return subprocess.check_output("fastboot devices",shell=True).decode().split()

def reboot(type):
    os.system(f"fastboot reboot {type}")