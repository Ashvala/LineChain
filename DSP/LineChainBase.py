'''
The primary idea for now is very simple: revamp the parser to create a more
coherent set of outputs to a bunch of unit generators.
Currently, you can probably create oscillators and chain them into ADSRs. By default
'''
import math
import json
import re
from LineChainUnits import *


UnitsArr = return_ugens()
class LineChain:
    def __init__(self, str):
        self.str = str

    def ret_str(self):
        return str

    def create_tokens(self):
        arr = self.str.split("-<") #split first at -<
        for item in arr:
            if item[0] != "[":
                return item.split("->")

    def parse(self):
        parse_tree = []
        def parse_args(unit_dict, args):
            str_to_parse = args[0:len(args)-1]
            unit_dict
            return str_to_parse

        def parse_ugens(str1):
            str_to_parse = str1[1:]
            for Units in UnitsArr:
                Unit = json.loads(Units)
                if str_to_parse == Unit['name']:
                    print "Appended"
                    parse_tree.append({'name': Unit['name']})

        arr =  self.create_tokens()
        print len(arr)

        for item in arr:
            # Check lengths here. Standard length is two. No more, no less.
            arr = item.split(":")
            if len(arr) == 2:
                parse_ugens(arr[0])
                print parse_args(parse_tree, arr[0],arr[1])
        print parse_tree
        return parse_tree





#All the test code goes here:

if __name__ == "__main__":
    str = "(oscil:0.4,440,*)-<[{->(stereo1)}, {->(stereo2)}]"
    #str = "(osc:0.4,440,*)->(adsr:2,1,1,0.1)-<[{->(stereo1)}, {->(stereo2)}]]"
    LineChainInstance = LineChain(str)
    LineChainInstance.parse()
