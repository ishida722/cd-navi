import os
import sys
import json
import posixpath

class Navigator:
    def __init__(self, jsondb):
        self.db = json.load(jsondb)
        self.destination = None

    def IsHit(self, word):
        self.destination = None
        if(word in self.db):
            self.destination = self.db[word]
            return True
        else: return False

class Driver:
    def cwd(self):
        return os.getcwd().replace(os.path.sep, '/')

    def UpCd(self):
        os.chdir('..')

    def GoToProjectRoot(self):
        while(True):
            ls = os.listdir('.')
            if('.svn' in ls): break
            elif('.git' in ls): break
            elif('.root' in ls): break
            self.UpCd()

    def GoToTrueRoot(self):
        while(True):
            ls = os.listdir('.')
            if('.root' in ls): break
            self.UpCd()

    def MakeTrueRootPath(self):
        self.GoToTrueRoot()
        self.trueRoot = self.cwd()

    def __init__(self):
        self.currentDir = self.cwd()
        self.GoToProjectRoot()
        self.projectRoot = self.cwd()

args = sys.argv
driver = Driver()
all_path = driver.currentDir

if(len(args) < 2):
    print(all_path)
    sys.exit()

db = posixpath.join(driver.projectRoot, '.fcdindex.json')
json_file = open(db, 'r')
navigator = Navigator(json_file)
json_file.close()

if(navigator.IsHit(args[1])):
    all_path = posixpath.join(driver.projectRoot, navigator.destination)

print(all_path)
sys.exit()
