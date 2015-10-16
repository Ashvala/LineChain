class Interp_text:
    def init(str):
        self.str_to_parse = str

    def parser(self,str):
        arr_str = self.tokenize(str)
        return str

    def tokenize(self, str):
        arr_str1 = str.split("->") #split signal chain direction
        for item in arr_str1:
            print item
        return arr_str1




string = "(midi)->(osc)->(adsr)-<[{->(stereo1), {->(reverbsc)->(stereo2)}]"
text_instance = Interp_text()
print text_instance.parser(string)
