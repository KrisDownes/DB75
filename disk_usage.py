import os

def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path,filename)
            total += disk_usage(childpath)
    print(f"{0:<7}".format(total),path)
    return total 
if __name__=="__main__":
    fp = input("what path do you want to test? :")
    disk_usage(fp)           