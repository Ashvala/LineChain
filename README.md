# LineChain

Simple signal chains as a single line.

---

## Syntax:


As an example, let's consider the string:

```
(midi)->(osc)->(adsr)-<[{->(stereo1)}, {->(reverbsc)->(stereo2)}]

```
The idea is that it breaks up the signal chain like this: 

- MIDI note number goes in as input to an oscillator
- The output of the oscillator goes into an ADSR
- The output of the ADSR gets split into an array, where the left output is sent out dry and the right output is sent into a reverb and then out to the right channel. 


### More Details: 

- Anything inside the rounded brackets is a unit generator, a la Csound's opcodes. 

- To pass signals around, you use the ```->``` symbol, which essentially also indicates signal direction. 

- To split a signal, use the ```-<``` symbol. This always must lead to an array. The number of items in the array defines the number of multipled outs that the thing leads to. 

- To create an array, use ```[]```, like you would in any other language. 

- Items in arrays use the ```{->}``` syntax, indicating that they are receiving input.

### Unit generator:

You can define values for controlling the parameters in a unit generator. As an example:

```
(osc:0.7,440)->(adsr:2,4,1,0.1)
```

### Outputs:

####Output to the DAC: 

Example for mono:

```
(osc:0.4,440)->(adsr:2,4,1,0.1)->(mono)

```

Example for stereo: 

```
(osc:0.4,440)->(adsr:2,4,1,0.1)-<[{->(stereo1)}, {->(stereo2)}]

```

#### To a variable: 

Example: 


```
(osc:0.4,440)->(adsr:2,4,1,0.1)->(var:a1)

```


### Multi-line 

Example: 

```
(osc:0.4,440)->(adsr:2,4,1,0.4)->(var:a1)
(osc:0.6,440)->(adsr:4,3,2,1)->(var:a2)
(a1+a2)-> (mono)

```

