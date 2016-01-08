import pyaudio
import wave
import sys
import struct
import math

def oscil(ampl, freq, file):
  size = 44100
  frate = 11025.0
  new_list = [freq]
  sin_wave_move = 1
  amp = ampl * 32767
  sines = []
  for y in new_list:
    for x in range(size):
      sines.append(math.sin(sin_wave_move*math.pi*y*(x/frate)))
  wav_file = wave.open(file, "w")
  nchannels = 1
  samples = 2
  framer = int(frate)
  wav_file.setparams((nchannels, samples, framer, size, "NONE", "not compressed"))
  print "Generating!"
  for s in sines:
      wav_file.writeframes(struct.pack('h', int(s*amp/2)))
  wav_file.close()


if __name__ == "__main__":
    print "generating a sinewave"
    fname = "t1.wav"
    oscil(0.5, 440, fname)
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
