import os
import json

class Destination:
    def __init__(self, path):
        self.path = path
        self.keys = []

    def AddKey(self, key):
        self.keys.append(key)

    def IsHit(self, word):
        if(word in self.keys): return True
        else: return False

    def SetKyeList(self, keyList):
        slef.keys = keyList

def UpCd():
    os.chdir('..')

def ProjectRoot():
    while():
        ls = os.listdir('.')
        if('.svn' in ls): break
        if('.git' in ls): break
        UpCd()

def MakeDestinations():
    i130 = Destination('C1000_Deliverables/0100_ContInfo/0130_PreDsgnVerif')
    i130.AddKey('sekkei')
    i130.AddKey('predsgn')
    i130.AddKey('130')
    return i130

print(MakeDestinations().IsHit('sekkei'))
# ProjectRoot()
# print(os.getcwd())
