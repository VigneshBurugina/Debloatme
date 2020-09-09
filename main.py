import os
from time import sleep


def uninstall(i,cmd):
    os.chdir(os.path.join(BASE_DIR,'adb'))
    os.system(f"adb {cmd} --user 0 {i}")
    return 0


BASE_DIR = os.getcwd()
with open(os.path.join(BASE_DIR,'applist.txt'),'r') as fl:
    data = fl.readlines()

while True:
    print("Disable or Uninstall?","1 - Disable", "2 - Uninstall",sep='\n')
    inp = int(input("Choose (1/2): "))
    if inp == 2:
        cmd = 'uninstall'
        break
    elif inp == 1:
        cmd = ' shell pm disable-user'
        break

for i in data:
    print(i)
    i,j = i.split(" | ")
    print(f"Uninstalling {j} -- {i}")
    uninstall(i,cmd)
    sleep(0.5)