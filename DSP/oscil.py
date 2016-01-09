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

  if func == "sine":
    sin_list = [trig(sin, 1, 1)]
    sines = calc(1,size,sin_list)
  if func == "square":
    sq_list = [trig(my_sin,(4.0/pi)/(n), n) for n in range(1,1000,2)] #square
    sines = calc(1,size, sq_list)
  if func == "sawtooth":
    t_list = [trig(my_sin,(2.0/pi)/(n), n) for n in range(1,1000)] #saw
    sines = calc(1,size,t_list)
#  if func == "funky":
#    s_list = [trig(sin,(2.0/pi)/log((n*n)+1), n) for n in range(1,100)] #rounder
#    sines = calc(1,size,s_list)

  wav_file = wave.open(file, "w")
  nchannels = 1
  samples = 2
  framer = int(frate)
  wav_file.setparams((nchannels, samples, framer, size, "NONE", "not compressed"))
  print "Generating!"
  for s in sines:
      wav_file.writeframes(struct.pack('h', int(s*amp)))
  wav_file.close()

def calc(increment_val,end,func_list):
  i = 0
  arr = []
  while (i <= end):
    amp = sum([s(i) for s in func_list])
    arr.append(amp)
    i += increment_val
  return arr

if __name__ == "__main__":
    fname = "t1.wav"
    oscil(0.5, 440,"sawtooth", fname)
    print "initalizing playback"
    CHUNK = 1024
    wf = wave.open(fname, 'rb')
    p = pyaudio.PyAudio()
#    calc funky regardless:
    s_list = [trig(sin,(2.0/pi)/log((n*n)+1), n) for n in range(1,100)] #rounder
    print calc(1,720,s_list)

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
    print "playback terminated"
    p.terminate()
