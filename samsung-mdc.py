
# Samsung Multiple Display Control (MDC) protocol
#
# I made this simple program to disable the child lock of my Samsung 460DR-S Screens

import serial
  
port = "COM4"
baud = 9600
  
ser = serial.Serial(port, baud, timeout=1)

if ser.isOpen():
     print(ser.name + ' is open...')

DisableChildLockAll = bytearray([0xaa, 0x5D, 0xFE, 0x1, 0x0, 0x5c])
PowerOffAll = bytearray([0xaa, 0x11, 0xFE, 0x1, 0x0, 0x10])
PowerOnAll =  bytearray([0xaa, 0x11, 0xFE, 0x1, 0x1, 0x11])
VideaWallOffAll =  bytearray([0xaa, 0x84, 0xFE, 0x1, 0x0, 0x83])

ser.write(DisableChildLockAll)
out = ser.read()
print('Receiving...')
for c in out:
    print (ord(c))

ser.close()

