# -*- coding: utf-8 -*-

from pydub import AudioSegment as AS
import matplotlib.pyplot as plt
import sys

args = sys.argv

if (2 != len(args)):
    print('')
    print('Usage: python %s <MP3 file>' % (args[0]))
    print('')
    exit(-1)
else:
    soundFile = args[1].strip()

sound_data = AS.from_mp3(soundFile)
samples = sound_data.get_array_of_samples()
per_sec = len(samples) / 19
# samples[x:y] x, yを調整して表示したいところを決める。
#plt.plot(samples[int(per_sec * 6 + per_sec/4):int(per_sec * 15 + per_sec/3)])
plt.plot(samples[0:])
plt.show()
