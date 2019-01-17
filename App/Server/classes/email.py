#Used to handle a email class
import getpass
import smtplib

class Email:
    def __init__(self, settings):
        email = settings.get_data("email")
        self.address = email["address"]
        self.server = email["server"], email["port"]
        self.password = getpass.getpass()

    def send(self, to, subject, text):
        server = smtplib.SMTP_SSL(*self.server)
        server.ehlo()
        server.login(self.address, self.password)
        body = '\r\n'.join(['To: %s' % to,
                    'From: %s' % self.address,
                    'Subject: %s' % subject,
                    '', text])
        server.sendmail(self.address, to, body)
        server.close()
