from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice 

device=MonkeyRunner.waitForConnection(5,'9999SKOFRC6TN7SO')

#启动activity（这里启动通兑全城）

device.startActivity(component="net.skjr.tdqc.rebateanycity/.StartActivity")

#登录界面，点击账号输入框

device.touch(636,738,'DOWN_AND_UP') 

#输入手机号

device.type('18099999999')


