import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr 
from email.mime.multipart import MIMEMultipart
from email.header import Header


def mail():
    my_sender = 'kalar_63@163.com'    # 发件人邮箱账号
    my_pass = 'yang123456'              # 发件人邮箱密码
    my_user = '719822330@qq.com'      # 收件人邮箱账号，我这边发送给自己
    ret = True
    # try:
    msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
    msg['From'] = formataddr(["FromRunoob", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To'] = formataddr(["FK", my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject'] = "菜鸟教程发送邮件测试"                # 邮件的主题，也可以说是标题

    server = smtplib.SMTP_SSL("smtp.163.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
    server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()  # 关闭连接
    print("发送成功")
    # except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
    #     ret=False
    return ret

def sendmailFile(reportName):
    sender = 'kalar_63@163.com'
    receiver = '1615852611@qq.com'
    smtpserver = 'smtp.163.com'
    username = 'kalar_63@163.com'
    password = 'yang123456'
    mail_title = '主题：这是带附件的邮件'

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header(mail_title, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText('来来来，这是邮件的正文', 'plain', 'utf-8'))

    # 构造附件1（附件为TXT格式的文本）
    # att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
    # att1["Content-Type"] = 'application/octet-stream'
    # att1["Content-Disposition"] = 'attachment; filename="test.txt"'
    # message.attach(att1)

    # # 构造附件2（附件为JPG格式的图片）
    # att2 = MIMEText(open('123.jpg', 'rb').read(), 'base64', 'utf-8')
    # att2["Content-Type"] = 'application/octet-stream'
    # att2["Content-Disposition"] = 'attachment; filename="123.jpg"'
    # message.attach(att2)

    # 构造附件3（附件为HTML格式的网页）
    att3 = MIMEText(open(reportName, 'rb').read(), 'base64', 'utf-8')
    att3["Content-Type"] = 'application/octet-stream'
    print("report  "+reportName)
    att3["Content-Disposition"] = 'attachment; filename="测试报告.html"'
    message.attach(att3)

    smtpObj = smtplib.SMTP_SSL(smtpserver, 465)  # 注意：如果遇到发送失败的情况（提示远程主机拒接连接），这里要使用SMTP_SSL方法
    # smtpObj.connect(smtpserver, 465)
    smtpObj.login(username, password)
    smtpObj.sendmail(sender, receiver, message.as_string())
    print("邮件发送成功！！！")
    smtpObj.quit()

# sendmailFile()