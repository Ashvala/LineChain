class Interp_text:
    def init(str):
        self.str_to_parse = str
        
    def parser(self,str):
        arr_str = tokenize(str)
        return str
        
    def tokenize(self, str):
        return str.split("->")
        
        
        
string = "(midi)->(osc)->(adsr)-<[{->(stereo1), {->(reverbsc)->(stereo2)}]"
text_instance = Interp_text()