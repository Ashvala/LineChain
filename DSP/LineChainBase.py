'''
The primary idea for now is very simple: revamp the parser to create a more
coherent set of outputs to a bunch of unit generators.
Currently, you can probably create oscillators and chain them into ADSRs. By default
'''
import math
import json
import re


class LineChain:
    def __init__(self, str):
        self.str = str
        return self.parse()

    def ret_str(self):
        return str

    def create_tokens(self):
        arr = self.str.split("-<") #split first at -<
        for item in arr:
            if item[0] != "[":
                return item.split("->")

    def parse(self):
        def parse_args(unit_dict, args):
            str_to_parse = args[0:len(args)-1]
            return str_to_parse

        def parse_ugens(str1):
            str_to_parse = str1[1:]

            return str_to_parse

        arr =  self.create_tokens()
        print len(arr)

        for item in arr:
            # Check lengths here. Standard length is two. No more, no less.
            arr = item.split(":")
            unit_dict = {}
            print parse_ugens(arr[0])
            print parse_args(unit_dict, arr[1])



#All the test code goes here:

if __name__ == "__main__":
    str = "(osc:0.4,440,*)->(adsr:2,1,1,0.1)-<[{->(stereo1)}, {->(stereo2)}]"
    LineChainInstance = LineChain(str)
