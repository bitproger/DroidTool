import subprocess
import os
def check():
    result = subprocess.check_output("adb devices",shell=True)
    print(result.decode().split())
    return result.decode().split()

def install(path):
    os.system(f"adb install {path}")


def reboot(type):
    os.system(f"adb reboot {type}")



