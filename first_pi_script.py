import serial

ser = serial.Serial('/dev/ttyUSB0')

ser.flushInput()
ser.flushOutput()

while True:
    bytesToRead = ser.inWaiting()
    readBytes   = ser.read(bytesToRead)
    print readBytes
