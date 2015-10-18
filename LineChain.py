import re
import csnd6

class LineChain:
    csd_str = "aout="
    def __init__(self,str):
        self.str = str

    def ugens_handler(self, str, vars):
        if str == "osc":
            return "oscili(%s)" %vars
        else:
            return "{0}({1})".format(str, vars)

    def parse(self):
        arr_str = self.tokenize()
        for ugens in arr_str:
            new_unit = ugens[1:-1]
            try:
                var_index = new_unit.index(":")
                if arr_str.index(ugens) == len(arr_str) -1:
                    self.csd_str +=self.ugens_handler(new_unit[0:var_index], new_unit[var_index+1:])
                else:
                    self.csd_str +=self.ugens_handler(new_unit[0:var_index], new_unit[var_index+1:]) + "+"
            except:
                var_index = -1

        return arr_str

    def tokenize(self):
        arr_str1 = self.str.split("->") #split signal chain direction
        return arr_str1

    def identify_array(self):
        arr_index = self.str.index("[")
        m = re.search("\[(.*[a-z]?)\]", self.str) #RE for sq brackets
        return m.group(0)

    def CsoundOrcGen(self): # Orchestra generator
        self.parse()
        orc_str = '''
sr=44100
nchnls=1
ksmps=32
0dbfs=1.0

instr 1
{0}
out aout
endin
'''.format(self.csd_str)
        return orc_str

    def CSDOutStr(self): #Just the audio out string
        self.parse()
        print self.CsoundOrcGen()

    def CsoundExec(self): # Execute Csound
        c = csnd6.Csound()
        c.SetOption("-odac")
        c.CompileOrc(self.CsoundOrcGen())
        score = "i 1 0 4"
        c.ReadScore(score)
        c.Start()
        while(c.PerformKsmps == 0):
            pass
        c.Stop()

str = "(osc:0.4,440)->(adsr:2,4,1,0.1)"
text_instance = LineChain(str)
text_instance.CsoundExec()
