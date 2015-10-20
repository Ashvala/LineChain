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
#        self.parseBool = True
        self.parse_arrays()
        return arr_str

    def tokenize(self):
        splitable = False
        try:
            print self.str.index("-<")
            print self.check_array(self.str)
            print "new_arr"
            splitable = True
            new_splits = self.str.split("-<")
            print new_splits
        except:
            print "no array"

        arr_str1 = self.str.split("->") #split signal chain direction
        return arr_str1

    def check_array_item(self,token):
        initial_parse_cond = False
        if token[0:3] == "{->" and token[len(token)-1] == "}":
            initial_parse_cond = True
            return initial_parse_cond
        else:
            return initial_parse_cond

    def parse_arr_item(self, item):
        item_to_parse = item[1:-1]
        if item_to_parse[0:2] != "->":
            print "Oh, incorrect input syntax!"
        else:
            parse_items = item.split("->")
            self.parse(item)
        print item_to_parse

    def parse_arrays(self):
        array_to_parse = self.identify_array()[1:-1].split(",")
        try:
            for token in array_to_parse:
                token_parse = self.check_array_item(token.strip())
                if token_parse == True:
                    self.parse_arr_item(token.strip())
            return array_to_parse
        except:
            return array_to_parse

    def identify_array(self):
        arr_index = self.str.index("[")
        try:
            m = re.search("\[(.*[a-z]?)\]", self.str) #RE for sq brackets
            return m.group(0)
        except:
            return 0

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
    str = "(osc:0.4,440,*)->(adsr:2,1,1,0.1)-<[{->(stereo1)}, {->(stereo2)}]"
    print str
    LineChainInstance = LineChain(str)
    print LineChainInstance.parse()
    print LineChainInstance.csd_str
    #    print LineChainInstance.CsoundOrcGen()
