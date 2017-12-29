from com.android.monkeyrunner import monkeyrunner as mr
from com.android.monkeyrunner import monkeydevice as md 
from com.android.monkeyrunner import monkeyimage as mi 

# 计算举例

#首页购物流程和门店购物流程

print("device in test cal ....")

d = mr.waitForConnection(5,'KWG5T16A26015662')

mr.sleep()

d.shell('am force-stop net.skjr.tdqc.rebateanycity/.StartActivity')

d.StartActivity(component = 'net.skjr.tdqc.rebateanycity/.StartActivity')

mr.sleep(5)

d.type(123456*123456)

d.press('KEYCODE_ENTER')

mr.sleep(2)

result=d.takeSnapshot()

pic=mr.loadImageFromFile('G:\\picture2')

if (result.sameAs(pic,0.995)):
    print ("pass")

else:
    print ("failure")

