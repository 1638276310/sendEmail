# 导入smtplib模块，这个模块是Python的标准库，用于发送电子邮件
import smtplib  # 导入SMTP库，用于发送邮件

# 从email模块中导入MIMEText类，这个类用于创建文本邮件的MIME消息对象
from email.mime.text import MIMEText  # 从email模块导入MIMEText类，用于创建邮件内容

# 定义一个变量，存储SMTP服务器的授权码，此授权码用于登录SMTP服务器
secretPass = 'brnhdxmvtqrwbeid'  # SMTP服务器授权码

# 使用with语句打开文件，文件模式为'r'表示读取模式
with open('emails.txt', 'r') as f:
    # 使用read方法读取所有行并使用split方法按换行符'\n'进行分割，得到一个包含所有行数据的列表
    email_data = f.read().split('\n')  # 读取所有行并分割它们

# 初始化一个空列表用于存储有效的邮箱地址
email_list = []

# 遍历email_data列表中的每一行数据
for email in email_data:
    # 如果当前行是空行或者是以'#'开头的注释行，就跳过当前行
    if email.strip() == '' or email.strip()[0] == '#':
        continue
    # 否则，将当前行添加到email_list列表中
    email_list.append(email.strip())  # 添加邮箱地址到列表中


# 定义一个函数，用于发送指定邮箱的邮件
def sendqqmail(sender_email, sender_pass, email_list, subject, message):
    # 使用MIMEText类创建一个邮件消息对象，其中message参数是邮件的内容
    msg = MIMEText(message)  # 创建一个MIMEText对象，用于存储邮件内容

    # 设置邮件的主题
    msg['Subject'] = subject  # 设置邮件的主题

    # 设置邮件的发件人邮箱和收件人邮箱
    msg['From'] = sender_email  # 设置邮件的发件人邮箱
    msg['To'] = ','.join(email_list)  # 设置邮件的收件人邮箱列表，用逗号隔开

    # 使用smtplib模块的SMTP_SSL类创建一个SSL连接对象，连接到SMTP服务器，其中'smtp.qq.com'是SMTP服务器地址，465是端口号
    # 在这个类中，有两个方法login和send_message，分别用于登录和发送邮件
    with smtplib.SMTP_SSL('smtp.qq.com', 465) as smtp:  # 创建一个SMTP对象，连接到SMTP服务器
        # 使用login方法登录SMTP服务器，参数sender_email和sender_pass分别是发件人的邮箱地址和授权码
        smtp.login(sender_email, sender_pass)  # 登录SMTP服务器
        print('成功登录SMTP服务器！')  # 如果登录成功，打印一条消息，提示已成功登录SMTP服务器
        smtp.send_message(msg)  # 使用send_message方法发送邮件，参数msg是要发送的邮件消息对象
        print('邮件发送至 ' + ', '.join(email_list) + ' 完毕')  # 发送成功后，打印一条消息，提示邮件发送完毕及收件人的邮箱列表
        smtp.quit()  # 退出SMTP登录状态，关闭SMTP连接
        # 退出SMTP登录状态


# 定义一个主函数，用于运行整个程序
def main():
    sender_email = '1638276310@qq.com'  # 发件人邮箱地址
    emailpass = secretPass  # 发件人邮箱授权码
    sub_msg = '测试python发送邮件'  # 邮件主题
    content = '这是我的第一个python发送邮件测试'  # 邮件正文内容
    sendqqmail(sender_email, emailpass, email_list, sub_msg, content)  # 发送邮件至指定邮箱列表


# 如果这个文件被直接运行，而不是作为模块被导入，那么执行main函数，这是Python的标准模式
if __name__ == '__main__':
    main()  # 执行main函数，运行整个程序
