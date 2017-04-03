import os

def UpCd():
    os.chdir('..')

def ProjectRoot():
    while():
        ls = os.listdir('.')
        if('.svn' in ls): break
        if('.git' in ls): break
        UpCd()

print(os.getcwd())
