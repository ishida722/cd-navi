import os
import sys
import json
import posixpath
import click

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
        os.chdir(os.path.expanduser('~'))

    def MakeTrueRootPath(self):
        self.GoToTrueRoot()
        self.trueRoot = self.cwd()

    def __init__(self):
        self.currentDir = self.cwd()
        self.GoToProjectRoot()
        self.projectRoot = self.cwd()

@click.command()
@click.argument('key')
@click.option('--trueroot', '-t', is_flag=True)
def cmd(key, trueroot):
    driver = Driver()
    all_path = driver.currentDir
    if trueroot:
        driver.MakeTrueRootPath()
        root_path = driver.trueRoot
    else:
        root_path = driver.projectRoot

    db = posixpath.join(root_path, '.fcdindex.json')
    json_file = open(db, 'r')
    navigator = Navigator(json_file)
    json_file.close()

    if(navigator.IsHit(key)):
        all_path = posixpath.join(root_path, navigator.destination)

    print('cd ' + all_path)
    sys.exit()

def main():
    cmd()

if __name__ == '__main__':
    main()
