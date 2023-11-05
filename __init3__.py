# 全注释版Excel格式的邮箱批量发送——全部邮箱发送后提示

# 导入smtplib模块，这个模块是Python的标准库，用于发送邮件
import smtplib  # 导入smtplib模块，用于发送邮件
# 导入email模块中的MIMEText类，这个类用于创建MIME文本邮件对象
from email.mime.text import MIMEText  # 导入email模块中的MIMEText类，用于创建MIME文本邮件对象

# 导入xlrd模块，这个模块是Python的标准库，用于读取Excel文件
import xlrd  # 导入xlrd模块，用于读取Excel文件

# 设置SMTP服务器的授权码，例如，QQ邮箱的授权码
secretPass = 'brnhdxmvtqrwbeid'  # SMTP服务器授权码

# 打开Excel文件，返回一个Workbook对象，代表Excel文件
data = xlrd.open_workbook('1.xls')  # 打开Excel文件

# 获取第一个sheet（默认索引为0）
sheet = data.sheets()[0]  # 选中sheet1

# 设置你想要获取数据的列的索引，这里我们设置为0，即第一列
col_index = 0  # 选择你想要获取数据的列的索引

# 从sheet中获取整列的数据，返回一个列表
column_values = sheet.col_values(col_index)  # 获取整列的数据


# 定义一个函数用于发送QQ邮箱
def sendqqmail(sender_email, sender_pass, rec_email_list, subject, message):
    # 创建一个MIMEText对象，用于表示邮件内容
    msg = MIMEText(message)  # 创建一个MIMEText对象，用于表示邮件内容

    # 设置邮件主题
    msg['Subject'] = subject  # 设置邮件主题

    # 设置发件人邮箱地址
    msg['From'] = sender_email  # 设置发件人邮箱地址

    # 设置收件人邮箱地址列表，用逗号隔开
    msg['To'] = ','.join(rec_email_list)  # 设置收件人邮箱地址列表，用逗号隔开

    # 使用SMTP_SSL协议登录QQ邮箱的SMTP服务器（smtp.qq.com，465端口）
    with smtplib.SMTP_SSL('smtp.qq.com', 465) as smtp:  # 使用SMTP_SSL协议登录QQ邮箱的SMTP服务器（smtp.qq.com，465端口）
        # 使用提供的发件人邮箱和授权码进行登录
        smtp.login(sender_email, sender_pass)  # 使用提供的发件人邮箱和授权码进行登录
        print('QQ邮箱——SMTP服务登录成功！')  # 打印登录成功信息
        print('收信人：', end='')  # 不换行输出（打印收信人列表）
        print(column_values)  # 打印收信人列表（这里应该是从Excel文件中读取的邮箱列表）
        smtp.send_message(msg)  # 发送邮件（通过SMTP服务器发送邮件）
        print('邮件发送完毕')  # 打印邮件发送完成信息（所有邮件都已经发送完毕）
        smtp.quit()  # 关闭SMTP连接，这也将触发真正的邮件发送。


def main():
    sender_email = '1638276310@qq.com'
    emailpass = secretPass
    sub_msg = '测试python发送邮件'
    content = '这是我的第一个python发送邮件测试'
    sendqqmail(sender_email, emailpass, column_values, sub_msg, content)


if __name__ == '__main__':
    main()
