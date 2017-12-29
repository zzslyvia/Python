#coding=utf-8
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice
from com.android.monkeyrunner.recorder import MonkeyRecorder as recorder

device = MonkeyRunner.waitForConnection(5,'KWG5T16A26015662')

recorder.start(device)


# device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)

# device.reboot()

# device.wake()

# display=device.getProperty('build.version.release')

# device.type('monkeyrunner')

# # 多个设备

# device1=MonkeyRunner.waitForConnection()
# device2=MonkeyRunner.waitForConnection()

# #对比截屏
# result = device.takeSnapshot()

# Pic2 = MonkeyRunner.loadImageFromeFile('G:\\picture1.png')

# if(result.sameAs(Pic2,0.9)):
#     print("success")

# else: 
#     print("failure")



# # 单击操作

# device.touch(200,300,"DOWN_AND_UP")

# # 屏幕操作
# for i in range(1,4):
#     device.drag((180,180),(600,600),0.1,10)

# t = time.strftime("%Y-%m-%d-%X",time.localtime())

# result=device.takeSnapshot()

# result.writeToFile('F:/img/'+t+'.png','png')


# if(device):
#     print "device is OK"
# else:
#     print "device is ...Please..退出"
# sys.exit(1)


# device.removePackage('net.skjr.tdqc.rebateanycity')

# # 定义按钮坐标的函数
# def  getBtnPoint(btn):
#     print btn
#     point = device.getHierarchyViewer().getAbsoluteCenterOfView(btn)
#     return point

# askView = getChildView('id/bt_login',5)
# askPpoint = getBtnPoint(askView)
# device.touch(askPpoint.x,askPpoint.y,'DOWN_AND_UP')



    


















