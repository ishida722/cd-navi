import os
import sys
import json
import posixpath
import click

class Navigator:
    def __init__(self, jsondb):
        self.db = json.load(jsondb)
        self.destination = None

    def IsRoot(self, word):
        if word=='root': return True
        if word=='r'   : return True

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

    def chdir(path):
        os.chdir(path)

    def GoToRoot(self):
        while(True):
            ls = os.listdir('.')
            if('.svn' in ls): break
            elif('.git' in ls): break
            elif(self.cwd()==self.home): break
            elif(self.cwd()=='/'): break
            self.UpCd()
        self.currentDir = self.cwd()

    def GoToTrueRoot(self):
        os.chdir(os.path.expanduser('~'))

    def MakeTrueRootPath(self):
        self.GoToTrueRoot()
        self.trueRoot = self.cwd()

    def __init__(self):
        self.currentDir = self.cwd()
        self.home = os.path.expanduser('~')

def MakeCommand(initPath, key):
    driver = Driver()
    driver.chdir(initPath)
    driver.GoToRoot()

    db = posixpath.join(driver.currentDir, '.fcdindex.json')
    with open(db, 'r') as json_filer:
        navigator = Navigator(json_file)

    if(navigator.IsHit(key)):
        all_path = posixpath.join(driver.currentDir, navigator.destination)
    else:
        all_path = initPath

    return 'cd ' + all_path + '\n'

@click.command()
@click.argument('key')
@click.option('--trueroot', '-t')
def cmd(key, trueroot):
    current = os.path.expanduser('~')
    home = os.path.expanduser('~')
    commands =[]

    if trueroot:
        commands.append(MakeCommand(home, trueroot))
    commands.append(MakeCommand(current, key))

    for command in commands:
        print(command)

    sys.exit()

def main():
    cmd()

if __name__ == '__main__':
    main()
