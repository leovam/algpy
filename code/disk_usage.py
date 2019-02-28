import os

def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendent"""
    total = os.path.getsize(path)       #account for direct usage
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
    print ('{0:<7}'.format(total), path)
    return total

if __name__ == '__main__':
    disk_usage('E:\\Dropbox\\algpy')