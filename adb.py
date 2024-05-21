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


def list_apps():
    return subprocess.check_output("adb shell pm list packages",shell=True).decode().split()

def remove(app):
    os.system(f"adb shell pm uninstall -k --user 0 {app}")
