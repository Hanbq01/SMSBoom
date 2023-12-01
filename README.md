# SMSBoom
简单的基于python的短信轰炸程序

# 简单说一下
这个程序的功能很简单，原理是模拟浏览器点击操作进行手机注册发送验证码，不需要后台抓包去请求验证码。

## 注意事项
**需要提前导入selenium包，time包，threading包**<br />
**提前把msedgedriver.exe放入python或者anaconda根目录，并加入path**<br />
msedgedirver.exe链接：<br />
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/#downloads<br />
选择适合自己的版本下载<br />

建议selenium包使用4.0+，4.0以下的确认不可用....<br />

------------
可以自行更改内容用于适配不同的浏览器，比如把代码里有关edge的改成chrome或者firefox。。。。<br />
具体的去看webdriver包里给的接口。。。<br />

------------
这个程序是我的python选修课作业，看网上很多都是一些很复杂的代码，本身也没学好，我就选择了比较简单的selenium。。。<br />
![image](https://github.com/Hanbq01/SMSBoom/assets/127653499/2e619c4b-87c8-4b92-aff8-a1cca0eced9e)<br />
代码很简单，麻烦在寻找不需要机器人验证的可注册网站，如果还能找到这样的网站，可以自己添加<br />
