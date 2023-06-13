# 桂理工南宁分校—校园网自动登录脚本
![网络登录](https://github.com/suhexia/GlutnnLogin/assets/55019115/bd5b5764-be65-43ff-9f9a-4cdf00df1543)

> 呃，这是我们学校的网络登录系统，如果别的学校也是同样的系统，你也可以试试，但我不保证都可以执行，我只对我的学校进行了本地测试

## 安装方法
 1. GitHub release：[GitHub](https://github.com/suhexia/GlutnnLogin/releases)
 2. 阿里云盘：[阿里云盘](https://www.aliyundrive.com/s/d8FqDZb3i8A)  提取码：z66r
 3. 百度云盘：[百度网盘](https://pan.baidu.com/s/1nl4goIG-DFF_oMxM1aP4mg?pwd=vmn2)   提取码：vmn2
 > ***安装最好别选c盘，如果你只有c盘的话你得看看下面的【关于Windows权限异常】这块的内容***
 
## 实现功能
### 1. 对账号密码的自动保存及自动登录
![保存账户](https://github.com/suhexia/GlutnnLogin/assets/55019115/fd84d7cc-97c7-4362-8be8-d964fe9a6ff4)

### 2. 自动检测错误类型，并给予提示
![检测错误](https://github.com/suhexia/GlutnnLogin/assets/55019115/688faa0b-11ad-4aad-b5ac-56c0bf0f69d2)

### 3. 自动识别验证码，并更正错误的和难以识别的验证码（上图有）

### 4. 登录成功智能反馈
![登录成功](https://github.com/suhexia/GlutnnLogin/assets/55019115/53263474-b734-43df-98a1-b14934e47037)

### 5. 无法连接登录站时，自动刷新连接状态
![刷新](https://github.com/suhexia/GlutnnLogin/assets/55019115/5f7761f0-4c88-4a56-9f36-03872fcec802)


## 开发中功能
- 自动检测网络状态，在网络需要登录时自动更新
- 开机后台自启动，保持服务状态
- 管理员权限自动获取，避免c盘无权限情况

## 关于Windows权限异常
- **~~这个目前还没找到很好的解决方案，可以在程序-属性-兼容性-以管理员身份运行**~~（在ver1.0.3更新了权限检测）
- **详细的可以看[设置管理员权限](https://zhuanlan.zhihu.com/p/135435104)的【03-快捷方式属性-兼容性设置]】这块**
	
## 注意事项
 - **项目免费开放使用，可以分享，严禁售卖**
 - **项目使用的登录方法与正常登录一致，经本人及宿舍测试了半个月后均无异常，安全性可以保证**

## 开发者&贡献
<a href="https://github.com/suhexia/GlutnnLogin/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=suhexia/GlutnnLogin" height='100px' width='100px'/>
</a>
