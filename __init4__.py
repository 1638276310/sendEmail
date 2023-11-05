# 使用QQ邮箱发送附带附件的邮件
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

secretPass = 'brnhdxmvtqrwbeid'  # SMTP服务器授权码


def send_email(sender_email, sender_pass, recipient_email, subject, message, attachment_paths):
    # 创建邮件对象
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    # 添加附件正文
    msg.attach(MIMEText(message, 'plain'))
    # 添加邮件附件
    for attachment_path in attachment_paths:
        if attachment_path.endswith('.jpg'):
            with open(attachment_path, 'rb') as attachment:
                part = MIMEImage(attachment.read())
                part.add_header('Content-Disposition', 'attachment', filename=attachment_path)
                msg.attach(part)
        elif attachment_path.endswith('.xlsx'):
            with open(attachment_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment', filename=attachment_path)
                msg.attach(part)
        elif attachment_path.endswith('.txt'):
            with open(attachment_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment', filename=attachment_path)
                msg.attach(part)
    with smtplib.SMTP_SSL('smtp.qq.com', 465) as smtp:
        smtp.login(sender_email, sender_pass)
        print('QQ邮箱——SMTP服务登录成功！')
        smtp.send_message(msg)
        print('邮件发送完毕')
        smtp.quit()  # 关闭SMTP连接


sender_email = '1638276310@qq.com'  # 发信人邮箱
sender_pass = secretPass  # 邮箱授权码
to_email = 'm13834960171@163.com'  # 收信人邮箱
sub_msg = '测试python发送邮件'  # 邮件主题
content = '这是我的第一个python发送邮件测试'  # 邮件正文内容
attachment_paths = [
    '1.xlsx',
    '1.jpg',
    'emails.txt'
]


def main():
    send_email(sender_email, sender_pass, to_email, sub_msg, content, attachment_paths)  # 发送邮件


if __name__ == '__main__':
    main()
