# 导入smtplib模块，这个模块是Python的标准库，用于发送电子邮件
import smtplib  # 导入SMTP库，用于发送邮件

# 从email模块中导入MIMEText类，这个类用于创建文本邮件的MIME消息对象
from email.mime.text import MIMEText  # 从email模块导入MIMEText类，用于创建邮件内容

# 定义一个变量，存储QQ邮箱的SMTP服务器授权码，此授权码用于登录QQ邮箱SMTP服务器
secretPass = 'brnhdxmvtqrwbeid'  # SMTP服务器授权码

# 打开一个Excel文件，并读取其中的数据
import xlrd  # 导入xlrd库，用于读取Excel文件

data = xlrd.open_workbook('1.xls')  # 打开Excel文件
sheet = data.sheets()[0]  # 选中第一个sheet

# 选择你想要获取数据的列的索引
col_index = 0  # 选择你想要获取数据的列的索引
column_values = sheet.col_values(col_index)  # 获取整列的数据，这里假设数据在第一列


# 定义一个函数，用于发送指定邮箱的邮件
def sendqqmail(sender_email, sender_pass, rec_email_list, subject, message):
    # 使用MIMEText类创建一个邮件消息对象，其中message参数是邮件的内容
    msg = MIMEText(message)  # 创建一个MIMEText对象，用于存储邮件内容

    # 设置邮件的主题
    msg['Subject'] = subject  # 设置邮件的主题

    # 设置邮件的发件人邮箱和收件人邮箱
    msg['From'] = sender_email  # 设置邮件的发件人邮箱
    msg['To'] = ','.join(rec_email_list)  # 设置邮件的收件人邮箱列表，用逗号隔开

    # 使用smtplib模块的SMTP_SSL类创建一个SSL连接对象，连接到QQ邮箱SMTP服务器，其中'smtp.qq.com'是SMTP服务器地址，465是端口号
    # 在这个类中，有两个方法login和send_message，分别用于登录和发送邮件
    with smtplib.SMTP_SSL('smtp.qq.com', 465) as smtp:  # 创建一个SMTP对象，连接到SMTP服务器
        # 使用login方法登录SMTP服务器，参数sender_email和sender_pass分别是发件人的邮箱地址和授权码
        smtp.login(sender_email, sender_pass)  # 登录SMTP服务器
        print('QQ邮箱——SMTP服务登录成功！')  # 如果登录成功，打印一条消息
        print('收信人：', end='')  # 不换行输出，打印收信人信息
        print(column_values)  # 打印收信人邮箱列表
        smtp.send_message(msg)  # 使用send_message方法发送邮件，参数msg是要发送的邮件消息对象
        print('邮件发送完毕')  # 发送成功后，打印一条消息
        smtp.quit()  # 关闭SMTP连接
        # 退出SMTP登录状态


# 定义一个主函数，用于运行整个程序
def main():
    # 发件人邮箱地址
    sender_email = '1638276310@qq.com'
    # 发件人的邮箱授权码
    emailpass = secretPass
    # 收件人邮箱列表，这里假设从Excel文件中读取的邮箱列表存储在column_values变量中
    rec_email_list = column_values
    # 邮件主题
    sub_msg = '测试python发送邮件'
    # 邮件正文内容
    content = '这是我的第一个python发送邮件测试'
    # 调用sendqqmail函数，发送邮件
    sendqqmail(sender_email, emailpass, rec_email_list, sub_msg, content)  # 发送邮件


# 如果这个文件被直接运行，而不是作为模块被导入，那么执行main函数，这是Python的标准模式
if __name__ == '__main__':
    main()  # 执行main函数，运行整个程序
