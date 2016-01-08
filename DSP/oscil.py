import pyaudio
import wave
import sys
import struct
from math import *

def trig(f, amp=1,freq=1):
  def s(degs):
    return -(amp*f((freq*radians(degs))))
  return s

def my_sin(x):
    return sin(x)

def oscil(ampl, freq, func, file):
  size = 44100
  frate = 44100.0
  new_list = [freq]
  sin_wave_move = 1
  amp = ampl * 32767
  sines = []
  '''
  sines = []
  for y in new_list:
    for x in range(size):
      print sin(pi*y*(x/frate))
  sines.append(sin(pi*y*(x/frate)))
  '''
  if func == "sine":
    sin_list = [trig(sin, 1, freq)]
    sines = calc(1,size, 10, sin_list)
  if func == "square":
    sq_list = [trig(my_sin,(4.0/pi)/(n), freq) for n in range(1,1000,2)] #square
    sines = calc(1,size, 10, sq_list)
  if func == "sawtooth":
    t_list = [trig(my_sin,(2.0/pi)/(n), freq) for n in range(1,3)] #saw
    sines = calc(1,size, 10, t_list)
  if func == "funky":
    s_list = [trig(sin,(2.0/pi)/log((n*n)+1), freq) for n in range(1,1000)] #rounder
    sines = calc(1,size, 10, s_list)

  wav_file = wave.open(file, "w")
  nchannels = 1
  samples = 2
  framer = int(frate)
  wav_file.setparams((nchannels, samples, framer, size, "NONE", "not compressed"))
  print "Generating!"
  for s in sines:
      wav_file.writeframes(struct.pack('h', int(s*amp)))
  wav_file.close()

def calc(increment_val, end,highlight, func_list):
  x_scale = 1.5
  y_scale = 200
  i = 0
  arr = []
  while (i <= end):
    amp = sum([s(i) for s in func_list])
    arr.append(amp)
    i += increment_val
  return arr

if __name__ == "__main__":
    print "generating a sinewave"
    fname = "t1.wav"
    t_list = [trig(my_sin,(2.0/pi)/(n), n) for n in range(1,3)] #saw
    calc(1,720, 10 ,t_list) #Triangle wave fourier series expansion
    oscil(0.5, 440,"sine", fname)
    CHUNK = 1024
    wf = wave.open(fname, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(CHUNK)

    while data != '':
      stream.write(data)
      data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()
