import re

class LineChain:
    def __init__(self,str):
        self.str = str

    def parse(self):
        arr_str = self.tokenize()
        for ugens in arr_str:
            new_unit = ugens[1:-1]
            print new_unit
            try:
                var_index = new_unit.index(":")
            except:
                var_index = -1
#            print var_index
            if var_index != -1:
                print new_unit[0:new_unit.index(":")]
        return arr_str

    def tokenize(self):
        arr_str1 = self.str.split("->") #split signal chain direction
        return arr_str1

    def identify_array(self):
        arr_index = self.str.index("[")
        m = re.search("\[(.*[a-z]?)\]", self.str) #RE for sq brackets
        return m.group(0)


str = "(osc:0.4,440)->(adsr:2,4,1,0.1)->(mono)"
text_instance = LineChain(str)
text_instance.parse()
