import re

class LineChain:
    csd_str = "aout="
    parseBool = False
    def __init__(self,str):
        self.str = str

    def ugens_handler(self, str, vars):
        if str == "osc":
            return "oscili({0})".format(vars)
        else:
            return "{0}({1})".format(str, vars)

    def parse_vars(self,var_str):
        signal_function = ""
        try:
            var_arr = var_str.split(",")
            for item in var_arr:
                item = item.strip()
            if var_arr[len(var_arr)-1] == "*":
                signal_function = "*"
            else:
                signal_function = "+"
        except:
            print "Invalid variable syntax!"
            raise
        return signal_function

    def parse(self):
        arr_str = self.tokenize()
        for ugens in arr_str:
            new_unit = ugens[1:-1]
            try:
                var_index = new_unit.index(":")
#               print new_unit[var_index+1:]
                signal_func =  self.parse_vars(new_unit[var_index+1:])
                if arr_str.index(ugens) == len(arr_str) -1:
                    self.csd_str +=self.ugens_handler(new_unit[0:var_index], new_unit[var_index+1:])
                else:
                    if signal_func == "*":
                        self.csd_str +=self.ugens_handler(new_unit[0:var_index], new_unit[var_index+1:new_unit.index(signal_func)-1]) + "*" #this is ugly and needs a rewrite
                    else:
                        self.csd_str +=self.ugens_handler(new_unit[0:var_index], new_unit[var_index+1:]) + "+" # default behavior
            except:
                var_index = -1
        self.parseBool = True
        return arr_str

    def tokenize(self):
        arr_str1 = self.str.split("->") #split signal chain direction
        return arr_str1

    def identify_array(self):
        arr_index = self.str.index("[")
        m = re.search("\[(.*[a-z]?)\]", self.str) #RE for sq brackets
        return m.group(0)

    def CsoundOrcGen(self): # Orchestra generator
        if self.parseBool == False:
            self.parse()

        orc_str = """sr=44100
nchnls=1
ksmps=32
0dbfs=1.0

instr 1
{0}
out aout
endin
        """.format(self.csd_str)
        return orc_str

    def CSDOutStr(self): #Just the audio out string
        if self.parseBool == False:
            self.parse()
        print self.CsoundOrcGen()

if __name__ == "__main__":
    str = "(osc:0.4,440,*)->(adsr:2,1,1,0.1)"
    LineChainInstance = LineChain(str)
    LineChainInstance.parse()
    print LineChainInstance.CsoundOrcGen()
