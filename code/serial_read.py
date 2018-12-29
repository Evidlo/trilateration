import serial
import struct
import datetime
import wave
import time
import numpy as np
import scipy.signal
from scipy.interpolate import interp1d
import sys
import subprocess

# import wave, struct, math

# sample_rate = 5882.4 # hertz
# sample_rate = 5882.4 # hertz
sample_rate = 5882.4 / 3 # hertz
# sample_rate = 8000 # hertz

wave_x = wave.open('sound_x.wav','w')
wave_y = wave.open('sound_y.wav','w')
wave_z = wave.open('sound_z.wav','w')
wave_x.setnchannels(1) # mono
wave_y.setnchannels(1) # mono
wave_z.setnchannels(1) # mono
wave_x.setsampwidth(1)
wave_y.setsampwidth(1)
wave_z.setsampwidth(1)
wave_x.setframerate(sample_rate)
wave_y.setframerate(sample_rate)
wave_z.setframerate(sample_rate)

# for i in range(int(duration * sampleRate)):
#     value = int(32767.0*math.cos(frequency*math.pi*float(i)/float(sampleRate)))
#     data = struct.pack('<h', value)
#     wavef.writeframesraw( data )

# wavef.writeframes('')
# wavef.close()

# s = serial.Serial('/dev/ttyACM0', 115200)
# s = serial.Serial('/dev/ttyUSB2', 57600)
s = serial.Serial('/dev/ttyUSB0', 57600)
# s = serial.Serial('/dev/ttyUSB1', 57600)
p = subprocess.Popen('while :; do mpv chirp.wav &> /dev/null; done', stdout=subprocess.PIPE, shell=True)
time.sleep(1)

def sample():
    count = 0
    wait_count = 0
    # s.flushInput()
    x = b''
    y = b''
    z = b''
    while count < sample_rate * 2:
        count += 1
        y += s.read(1)
        z += s.read(1)
        x += s.read(1)
    wave_x.writeframesraw(x)
    wave_y.writeframesraw(y)
    wave_z.writeframesraw(z)

    x = np.fromstring(x, dtype='S1').view(np.uint8).astype(float)
    y = np.fromstring(y, dtype='S1').view(np.uint8).astype(float)
    z = np.fromstring(z, dtype='S1').view(np.uint8).astype(float)
    # compute which stream is microphone X from LSB
    if sum(x % 2) > 50:
        data_x = x
        data_y = y
        data_z = z
    elif sum(y % 2) > 50:
        data_x = y
        data_y = z
        data_z = x
    else:
        data_x = z
        data_y = x
        data_z = y

    return (data_x, data_y, data_z)

count = 0
d1 = []
d2 = []
d1_raw = []
d2_raw = []
d1_up = []
d2_up = []
x = []
x_raw = []
x_up = []
y = []
y_raw = []
y_up = []
z = []
z_raw = []
z_up = []

f = open('/tmp/d2', 'w')
d1_buffer = np.array([])
d2_buffer = np.array([])
s.flushInput()
# while count < 10:
try:
    while True:
        data_x, data_y, data_z = sample()
        data_x_raw = data_x.copy()
        data_y_raw = data_y.copy()
        data_z_raw = data_z.copy()
        upsample = 5
        data_x -= np.mean(data_x)
        data_y -= np.mean(data_y)
        data_z -= np.mean(data_z)
        data_x[np.abs(data_x) < 4] = 0
        data_y[np.abs(data_y) < 4] = 0
        data_z[np.abs(data_z) < 4] = 0
        data_x_up = interp1d(np.arange(len(data_x)), data_x, kind='quadratic')(np.linspace(0, len(data_x) - 1, upsample * len(data_x)))
        data_y_up = interp1d(np.arange(len(data_y)), data_y, kind='quadratic')(np.linspace(0, len(data_y) - 1, upsample * len(data_y)))
        data_z_up = interp1d(np.arange(len(data_z)), data_z, kind='quadratic')(np.linspace(0, len(data_z) - 1, upsample * len(data_z)))
        middle = len(data_x) + 1
        middle_up = upsample * len(data_x) + 1
        search_width = 5
        search_width_up = search_width * upsample
        # delay_1 = np.argmax(np.correlate(data_x - np.mean(data_x), data_y - np.mean(data_y), mode='full')[middle - search_width:middle + search_width + 1])
        # delay_2 = np.argmax(np.correlate(data_x - np.mean(data_x), data_z - np.mean(data_z), mode='full')[middle - search_width:middle + search_width + 1])
        # delay_1_raw = np.argmax(np.correlate(data_x_raw - np.mean(data_x_raw), data_y_raw - np.mean(data_y_raw), mode='full')[middle - search_width:middle + search_width + 1]) - search_width
        # delay_2_raw = np.argmax(np.correlate(data_x_raw - np.mean(data_x_raw), data_z_raw - np.mean(data_z_raw), mode='full')[middle - search_width:middle + search_width + 1]) - search_width
        delay_1_raw = np.argmax(np.correlate(data_x_raw - np.mean(data_x_raw), data_y_raw - np.mean(data_y_raw), mode='full')[middle - search_width:middle + search_width + 1]) - search_width
        delay_2_raw = np.argmax(np.correlate(data_x_raw - np.mean(data_x_raw), data_z_raw - np.mean(data_z_raw), mode='full')[middle - search_width:middle + search_width + 1]) - search_width + 1
        delay_1_up = np.argmax(np.correlate(data_x_up - np.mean(data_x_up), data_y_up - np.mean(data_y_up), mode='full')[middle_up - search_width_up:middle_up + search_width_up + 1]) - search_width_up
        delay_2_up = np.argmax(np.correlate(data_x_up - np.mean(data_x_up), data_z_up - np.mean(data_z_up), mode='full')[middle_up - search_width_up:middle_up + search_width_up + 1]) - search_width_up + 1
        # d1.append(delay_1)
        # d2.append(delay_2)
        d1_raw.append(delay_1_raw)
        d2_raw.append(delay_2_raw)
        d1_up.append(delay_1_up)
        d2_up.append(delay_2_up)
        # x.append(data_x)
        # y.append(data_y)
        # z.append(data_z)
        x_raw.append(data_x_raw)
        y_raw.append(data_y_raw)
        z_raw.append(data_z_raw)
        x_up.append(data_x_up)
        y_up.append(data_y_up)
        z_up.append(data_z_up)
        count += 1
        # if np.abs(delay) > 100:
        #     print('delay: not found')
        # else:
        #     print('delay:', delay)
        if len(d1_buffer) > 5:
            d1_buffer = np.delete(d1_buffer, 0)
        if len(d2_buffer) > 5:
            d2_buffer = np.delete(d2_buffer, 0)
        d1_buffer = np.append(d1_buffer, delay_1_up)
        d2_buffer = np.append(d2_buffer, delay_2_up)

        print('delay1:', np.mean(d1_buffer))
        print('delay2:', np.mean(d2_buffer))
        f.write(str(np.mean(d2_buffer)))
        f.write('\n')
except KeyboardInterrupt:
    p.terminate()


p.terminate()

# h = scipy.signal.firwin(9, [50/3, 70/3], pass_zero=False, nyq=sample_rate / 2)
# filt = scipy.signal.lfilter(h, 1, data)

# wavef.writeframesraw(data.tobytes())

# wavef.writeframesraw(data)
# print('len:', len(x))
# print('err:', err_count)
# print('time:', datetime.datetime.now() - start)
# print(s.in_waiting)
# while datetime.datetime.now() - start < datetime.timedelta(seconds=1):
#     pass

    # last_time = datetime.datetime.now()
    # if datetime.datetime.now() - last_time > datetime.timedelta(seconds=0.05):
    #     err_count += 1

    # count += 1
    # x = s.read(1)
    # if ord(x) != 128:
    #     err_count += 1
    # print(ord(x))

    # wavef.writeframesraw(x)

# print(err_count)
# print(count)
print('delay1:', np.mean(d1_up))
print('delay2:', np.mean(d2_up))
wave_x.writeframes(b'')
wave_y.writeframes(b'')
wave_z.writeframes(b'')
wave_x.close()
wave_y.close()
wave_z.close()

# def debug(x, y):
#     plt.subplot(2, 1, 1)
#     plt.plot(x)
#     plt.plot(y)
#     plt.subplot(2, 2, 1)
#     plt.show()
