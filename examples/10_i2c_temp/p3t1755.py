import machine, time

P3T_ADDR = 72

i2c = machine.I2C(5, scl=machine.Pin('P1_17'), sda=machine.Pin('P1_16'))

class P3T1755:
    def __init__(self, i2c, addr):
        self.addr = addr
        self.i2c = i2c

        self.i2c.writeto(self.addr, b'\x00')

    def read(self):
        temp_raw = i2c.readfrom(self.addr, 2)
        temp_converted = ((temp_raw[0] << 4) | (temp_raw[1] >> 4)) * 0.0625
        return temp_converted

ts = P3T1755(i2c, P3T_ADDR)

while(True):
    print("Temperature: {:.2f} Deg.C".format(ts.read()))
    time.sleep_ms(100)
