import json

jlist = [
    {
        "name": "oscil",
        "args": "float,float",
        "args_count": 2,
        "args_list": "amp, freq",
        "unit_desc": "A typical oscillator",
        "default_args": [0.5, 440]
    },
    {
        "name": "adsr",
        "args": "float,float,float,float",
        "args_count": 4,
        "args_list": "attack,decay,sustain,release",
        "unit_desc": "Standard ADSR",
        "default_args": [0.4, 4, 0.6, 1]
    },
    {
        "name": "stereo1",
        "args": "",
        "args_count": 0,
        "args_list": "",
        "unit_desc": "Stereo channel 1"
    },
    {
        "name": "stereo2",
        "args": "",
        "args_count": 0,
        "args_list": "",
        "unit_desc": "Stereo channel 2"
    },
    {
        "name": "mono",
        "args": "",
        "args_count": 0,
        "args_list": "",
        "unit_desc": "mono"
    }
]


def return_ugens():
    UnitsArr = []
    for item in jlist:
        UnitsArr.append(json.dumps(item))
    return UnitsArr
