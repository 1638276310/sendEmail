# Excel格式的邮箱收件批量发送HTML代码内容——全部邮箱发送后提示
# 导入smtplib库，用于发送SMTP邮件
import smtplib
# 导入email.mime.text模块，用于创建MIMEText对象
from email.mime.text import MIMEText

# 导入xlrd库，用于读取Excel文件
import xlrd

# 设置SMTP服务器授权码
secretPass = 'brnhdxmvtqrwbeid'

# 创建MIMEText对象，其中包含HTML邮件内容
msg = MIMEText(f'<h1>HTML邮件内容</h1>', 'html', 'utf-8')

# 打开Excel文件1.xls，并创建一个Workbook对象
data = xlrd.open_workbook('1.xls')  # 打开Excel文件

# 通过Workbook对象获取第一个sheet，并创建一个Sheet对象
sheet = data.sheets()[0]  # 选中sheet1

# 选择你想要获取数据的列的索引，这里设置为0，即第一列
col_index = 0  # 选择你想要获取数据的列的索引

# 通过Sheet对象获取指定列的数据，并创建一个列表
column_values = sheet.col_values(col_index)  # 获取整列的数据


# 定义一个函数，用于发送QQ邮箱
def send_qq_mail(sender_email, sender_pass, rec_email_list, subject):
    # 设置邮件主题
    msg['Subject'] = subject
    # 设置发件人邮箱
    msg['From'] = sender_email
    # 设置收件人列表，用逗号隔开，并通过join方法将其转化为一个字符串列表
    msg['To'] = ','.join(rec_email_list)
    try:
        # 通过SMTP_SSL方法登录SMTP服务器（这里使用QQ邮箱的SMTP服务器）并设置SSL连接（端口465）
        with smtplib.SMTP_SSL('smtp.qq.com', 465) as smtp:
            # 通过login方法登录SMTP服务器，并设置发件人邮箱和授权码（这里使用QQ邮箱的授权码）
            smtp.login(sender_email, sender_pass)
            print('QQ邮箱——SMTP服务登录成功！')
            print('收信人：', end='')  # 不换行输出
            print(column_values)
            # 通过send_message方法发送邮件（这里将所有收件人作为收件人列表发送一封邮件）
            smtp.send_message(msg)
            print('邮件发送完毕')
            smtp.quit()  # 关闭SMTP连接
    except smtplib.SMTPServerDisconnected:  # 如果出现异常：连接意外关闭，则打印提示信息“SMTP登录失败，原因可能是：连接意外关闭”
        print('SMTP登录失败，原因可能是：连接意外关闭')
    except smtplib.SMTPAuthenticationError:  # 如果出现异常：认证失败，则打印提示信息“认证失败”
        print('认证失败')


# 定义一个函数，用于执行主程序逻辑（调用send_qq_mail函数发送邮件）
def main():
    # 设置发件人邮箱和SMTP服务授权码（这里使用QQ邮箱的授权码）
    sender_email = '1638276310@qq.com'
    emailpass = secretPass
    sub_msg = '测试python发送邮件'  # 设置邮件主题
    rec_email_list = column_values  # 从Excel文件中读取邮箱列表
    send_qq_mail(sender_email, emailpass, rec_email_list, sub_msg)  # 调用send_qq_mail()函数发送邮件


if __name__ == '__main__':
    main()
