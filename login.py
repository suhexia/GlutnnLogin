from requests import Session
from requests.exceptions import ConnectTimeout
from textwrap import dedent
import robobrowser
from datetime import datetime
from ddddocr import DdddOcr
from os.path import exists
from os import system
from socket import gethostname,gethostbyname
from json import dumps,loads
from re import sub
from time import sleep

import ctypes, sys

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48",
}


class WebsiteLogin:
    def __init__(self) -> None:
        self.session = Session()
        self.nowTime = str(datetime.now())
        self.bpssUSERNAME = ""
        self.bpssBUSPWD = ""
        self.bpssVERIFY = ""

    def infoGet(self):
        fileCheck = exists("info.json")
        if fileCheck is False:
            print("初次使用，请按步骤输入你的登录信息：")
            userName = input("首先请输入登录的手机号（宽带注册的手机号）：")
            passwd = input("然后输入登录密码（没修改过应该都是123456）")
            if userName and passwd:
                print("好极了，已为您创建登录信息文件...")
                with open("info.json", "w")as wf:
                    wf.write(dumps({
                        "userId": str(userName),
                        "passwd": str(passwd)
                    },
                    indent= 4
                ))
        
        with open("info.json", "r")as rf:
            info = loads(rf.read())
        self.bpssUSERNAME = info["userId"]
        self.bpssBUSPWD = info["passwd"]

    def GetVarify(self):
        ocr = DdddOcr(show_ad=False)
        url = "http://221.7.244.134:8080/verifycode.jpg?" + self.nowTime
        resp = self.session.get(url, headers=headers).content
        # Image.open(BytesIO(resp)).show()
        return ocr.classification(resp)

    def GetLocalIp(self):
        hostname = gethostname()
        return gethostbyname(hostname)

    def submitForm(self):  # sourcery skip: extract-method
        self.infoGet()
        b = robobrowser.RoboBrowser(parser="lxml", session=self.session)
        while True:
            try:
                b.open("http://221.7.244.134:8080/login_gx.jsp",timeout=5)
                break
            except ConnectTimeout:
                print("连接异常，正在尝试重新连接，按ctrl+c结束")
        # b.open("http://119.91.228.94/hexia/")
        form = b.get_form(action="/login.do")
        if form is not None:
            form["bpssUSERNAME"].value = self.bpssUSERNAME
            form["bpssBUSPWD"].value = self.bpssBUSPWD
            form["bpssVERIFY"].value = self.GetVarify()
            b.submit_form(form)
        return b
    
    def AfterSubmit(self):
        b = self.submitForm()
        body = b.find("td", class_="font_red")
        if body is None:
            err = str(b.find("script").text).strip()
            textGet = sub(r"alert|\(\"|\"\)", "", err)
            return {"status":"faild","message":textGet}
        return {"status":"success","message":"登录成功"}
    
    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False


if __name__ == "__main__":
    if not WebsiteLogin().is_admin():
    # 如果非管理员，则用管理员权限重新启动该脚本
        hinstance = ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        exit(0)

    started = WebsiteLogin()
    status = started.AfterSubmit() 
    while status["status"] == "faild":
        rtext = status["message"]
        if "验证码" in rtext:
            print("验证码错误，正在重新尝试...\n")
            status = started.AfterSubmit()
            sleep(1)
        elif "密码或开户地有误" in rtext:
            print("您输入的帐号,密码或开户地有误,请重新输入\n" 
                  "出现此错误的原因可能有:\n"
                  "1.你输入的账号密码确实出了问题\n"
                  "（会改json的自己改【info.json】不会改json的就删掉【info.json】重新运行软件）\n"
                  "2.你的校园网网络已经登录完成，无需重复登录")
            break
        else:
            print(rtext)
            break
    if status["status"] == "success":
        rtInfo = f"""
            登录成功！
            用户名：{started.bpssUSERNAME}
            登录ip：{started.GetLocalIp()}
            登录时间：{started.nowTime}
            """
        print(dedent(rtInfo))
    system("pause")
