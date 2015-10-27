/*LineChain functions go here... I think.*/
function LineChain(str){
    this.str = str;
}

LineChain.prototype.getString = function(){
    return this.str
}

LineChain.prototype.ugens_handler = function(str,vars){
    if (str == "osc"){
	return "oscili(" + vars + ")"
    }else{
	return str+"("+vars+")"
    }

}

LineChain.prototype.parse_vars = function(var_str){
    var signal_function;
    try{
	var var_arr = var_str.split(",")
	for (itemIndex in var_arr){
	    item = var_arr[itemIndex].trim()
	    if (var_arr[var_arr.length -1] == "*"){
		signal_function = "*"
	    }else{
		signal_function = "+"
	    }
	}
    }catch(e){
	console.log("::", e)
    }
    return signal_function
}

var csd_str = "aout="

LineChain.prototype.parse = function(){
    var arr_str = this.tokenize()
    for (ugensIndex in arr_str){
	ugens = arr_str[ugensIndex]
	var new_unit = ugens.substring(1, ugens.length-1)
	try{
	    var_index = new_unit.indexOf(":")
	    signal_func = this.parse_vars(new_unit.substring(var_index+1, new_unit.length))
	    split_arr = new_unit.split(":")
	    if (arr_str.indexOf(ugens) == arr_str.length-1){
		csd_str = csd_str +  this.ugens_handler(split_arr[0], split_arr[1])
	    }else{
		if (signal_func == "*"){
		    csd_str = csd_str + this.ugens_handler(split_arr[0], split_arr[1].substring(0,split_arr[1].length-2)) + "*"

		}else{
		    csd_str = csd_str + this.ugens_handler(split_arr[0], split_arr[1]) + "+"
		}
	    }
	}catch(e){
	    console.log(":", e)
	}
    }
}

LineChain.prototype.tokenize = function(){
    return this.str.split("->")
}

/* End LineChain Module here */

var LineChainInstance = new LineChain("(osc:0.4,440,*)->(adsr:2,1,1,0.1)")
LineChainInstance.parse()
console.log(csd_str)
