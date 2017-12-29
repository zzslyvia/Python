from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice
from com.android.monkeyrunner.easy import EasyMonkeyDevice,By


device = MonkeyRunner.waitForConnection(5,'KWG5T16A26015662')


device.startActivity(component='net.skjr.tdqc.rebateanycity/.StartActivity')

# easy_device=EasyMonkeyDevice(device)

device.touch(By.id(':id/et_phone'),MonkeyDevice.DOWN_AND_UP)
device.type('18099999999')

device.touch(By.id('id/et_pwd'),MonkeyDevice.DOWN_AND_UP)
device.type('000000')

easy_device.touch(By.id('id/et_code'),MonkeyDevice.DOWN_AND_UP)
device.type('9854')

easy_device.press(By.id('id/et_pwd'),MonkeyDevice.DOWN_AND_UP)



