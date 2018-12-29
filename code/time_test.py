import serial
import timeit

s = serial.Serial('/dev/ttyUSB0', 57600)

def foo(s):
    def inner():
        s.flush()
        count = 0
        while count < 10000:
            count += 1
            x = s.read(1)
    return inner

print(timeit.timeit(foo(s), number=5))
