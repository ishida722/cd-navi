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

json_string = '''
 {
     "1000":"C1000_*",
     "sekkei":"C1000_*/0100_*/0130_*",
     "130":"C1000_*/0100_*/0130_*",
     "qa":"C1000_*/0300_*/0320_*",
     "C1000_*/0300_*/0320_*":320,
     "plan":"C1000_*/0200_*/0220_*",
     "C1000_*/0200_*/0220_*":220,
     "yotei":"C1000_*/0200_*/0220_*/DevSched_Soft",
     "devsched":"C1000_*/0200_*/0220_*/DevSched_Soft",
     "dsgn":"C1000_*/0400_*",
     "400":"C1000_*/0400_*",
     "bug*":"C1000_*/0400_*/0410_*",
     "410":"C1000_*/0400_*/0410_*",
     "gizjirok*":"C1000_*/0400_*/0420_*",
     "420":"C1000_*/0400_*/0420_*",
     "480":"C1000_*/0400_*/0480_*",
     "sheet":"C1000_*/0400_*/0480_*",
     "chkcode":"C1000_*/0400_*/0480_*/CodeRevChkList",
     "chkintegresult":"C1000_*/0400_*/0480_*/FctnIntegTestResultRevChkList",
     "chkintegspec":"C1000_*/0400_*/0480_*/FctnIntegTestSpecRevChkList",
     "warikomi":"C1000_*/0400_*/0480_*/IntrptVerifSh",
     "intr*":"C1000_*/0400_*/0480_*/IntrptVerifSh",
     "5k0":"C1000_*/0500_*/05K0_*",
     "test":"C1000_*/0600_*",
     "600":"C1000_*/0600_*",
     "6Kk0":"C1000_*/0600_*/06K0_*",
     "integ*":"C1000_*/0600_*/06K0_*",
     "qac":"C1000_*/0600_*/06J0_*/QacCheckResult",
     "spec":"C2000_*/C2100_*",
     "2100":"C2000_*/C2100_*",
     "func*":"C2000_*/C2100_*/C2110_*/0020_*",
     "20":"C2000_*/C2100_*/C2110_*/0020_*",
     "2000":"C2000_*",
     "naibu":"C2000_*/C2100_*/C2120_*",
     "2120":"C2000_*/C2100_*/C2120_*",
     "2200":"C2000_*/C2200_*",
     "manage":"C2000_*/C2200_*",
     "nittei":"C2000_*/C2200_*/C2210_*",
     "2210":"C2000_*/C2200_*/C2210_*",
     "2400":"C2000_*/C2400_*",
     "rule*":"C2000_*/C2400_*",
     "housin":"junpToC1000_*/0200_*/0220_*/SoftDsgnPlcyVerifResults"
 }
'''


print(json.dumps(json_string))
print(MakeDestinations().IsHit('sekkei'))
# ProjectRoot()
# print(os.getcwd())
