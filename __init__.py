# 导入smtplib模块，这个模块是Python的标准库，用于发送电子邮件
import smtplib

# 从email模块中导入MIMEText类，这个类用于创建文本邮件的MIME消息对象
from email.mime.text import MIMEText

# 定义一个变量，存储QQ邮箱的SMTP服务器授权码，此授权码用于登录QQ邮箱SMTP服务器
secretPass = 'brnhdxmvtqrwbeid'  # SMTP服务器授权码


# 定义一个函数，用于发送指定邮箱的邮件
def sendqqmail(sender_email, sender_pass, rec_email, subject, message):
    # 使用MIMEText类创建一个邮件消息对象，其中message参数是邮件的内容
    msg = MIMEText(message)

    # 设置邮件的主题
    msg['Subject'] = subject

    # 设置邮件的发件人邮箱
    msg['From'] = sender_email

    # 设置邮件的收件人邮箱
    msg['To'] = rec_email

    # 使用smtplib模块的SMTP_SSL类创建一个SSL连接对象，连接到QQ邮箱SMTP服务器，其中'smtp.qq.com'是SMTP服务器地址，465是端口号
    # 在这个类中，有两个方法login和send_message，分别用于登录和发送邮件
    with smtplib.SMTP_SSL('smtp.qq.com', 465) as smtp:
        # 使用login方法登录SMTP服务器，参数sender_email和sender_pass分别是发件人的邮箱地址和授权码
        smtp.login(sender_email, sender_pass)
        # 如果登录成功，打印一条消息
        print('登录邮箱成功！')
        # 使用send_message方法发送邮件，参数msg是要发送的邮件消息对象
        smtp.send_message(msg)
        # 发送成功后，打印一条消息
        print('邮件发送完毕')
        # 关闭SMTP服务连接
        smtp.quit()


# 定义一个主函数，用于运行整个程序
def main():
    # 定义发件人的邮箱地址
    sender_email = '1638276310@qq.com'  # 发信人邮箱
    # 定义发件人的邮箱授权码
    emailpass = secretPass  # 邮箱授权码
    # 定义收件人的邮箱地址
    to_email = 'm13834960171@163.com'  # 收信人邮箱
    # 定义邮件的主题
    sub_msg = '测试python发送邮件'  # 邮件主题
    # 定义邮件的正文内容
    content = '这是我的第一个python发送邮件测试'  # 邮件正文内容
    # 调用sendqqmail函数，发送邮件
    sendqqmail(sender_email, emailpass, to_email, sub_msg, content)  # 发送邮件


# 如果这个文件被直接运行，而不是作为模块被导入，那么执行main函数，这是Python的标准模式
if __name__ == '__main__':
    main()
