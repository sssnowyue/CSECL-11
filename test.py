# # -*- coding: utf-8 -*-
# from email.mime.text import MIMEText
# from email.header import Header
# from smtplib import SMTP_SSL

# #qq邮箱smtp服务器
# host_server = 'smtp.qq.com'
# #sender_qq为发件人的qq号码
# sender_qq = '1123146105'
# #pwd为qq邮箱的授权码
# pwd = 'voxuytjaoyfpgegd'
# #发件人的邮箱
# sender_qq_mail = '1123146105@qq.com'
# #收件人邮箱
# receiver = 'sssnowyue@163.com'
# #邮件的正文内容
# mail_content = '你好，我是来自知乎的'
# #邮件标题
# mail_title = 'HIT 的邮件'

# #ssl登录
# smtp = SMTP_SSL(host_server)
# #set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
# smtp.set_debuglevel(1)
# smtp.ehlo(host_server)
# smtp.login(sender_qq, pwd)

# msg = MIMEText(mail_content, "plain", 'utf-8')
# msg["Subject"] = Header(mail_title, 'utf-8')
# msg["From"] = sender_qq_mail
# msg["To"] = receiver
# smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
# smtp.quit()

# Authentication methods the server supports:
    authlist = self.esmtp_features["auth"].split()

    # List of authentication methods we support: from preferred to
    # less preferred methods. Except for the purpose of testing the weaker
    # ones, we prefer stronger methods like CRAM-MD5:
    preferred_auths = [AUTH_LOGIN, AUTH_CRAM_MD5, AUTH_PLAIN]

    # Determine the authentication method we'll use
    authmethod = None
    for method in preferred_auths:
        if method in authlist:
            authmethod = method
            break

# Authentication methods the server supports:
authlist = self.esmtp_features["auth"].split()

# List of authentication methods we support: from preferred to
# less preferred methods. Except for the purpose of testing the weaker
# ones, we prefer stronger methods like CRAM-MD5:
preferred_auths = [AUTH_CRAM_MD5, AUTH_PLAIN,AUTH_LOGIN]

# Determine the authentication method we’ll use
authmethod = None
for method in preferred_auths:
if method in authlist:
authmethod = method
break
