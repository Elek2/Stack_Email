import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email:
	def __init__(self, gmail_smtp, gmail_imap, port, login, password):
		self.gmail_smtp = gmail_smtp
		self.gmail_imap = gmail_imap
		self.port = port
		self.login = login
		self.password = password

	def send_message(self, subject, recipients, message):
		msg = MIMEMultipart()
		msg['From'] = self.login
		msg['To'] = ', '.join(recipients)
		msg['Subject'] = subject
		msg.attach(MIMEText(message))

		ms = smtplib.SMTP(self.gmail_smtp, self.port)
		# identify ourselves to smtp gmail client
		ms.ehlo()
		# secure our email with tls encryption
		ms.starttls()
		# re-identify ourselves as an encrypted connection
		# ms.ehlo()

		ms.login(self.login, self.password)
		ms.sendmail(self.login, msg['To'], msg.as_string())

		ms.quit()

	def receive_message(self, header):
		mail = imaplib.IMAP4_SSL(self.gmail_imap)
		mail.login(self.login, self.password)
		mail.list()
		mail.select("inbox")
		criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
		result, data = mail.uid('search', criterion)
		assert data[0], 'There are no letters with current header'
		latest_email_uid = data[0].split()[-1]
		result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
		raw_email = data[0][1]
		email_message = email.message_from_string(raw_email)
		mail.logout()
		return email_message


if __name__ == '__main__':

	email_params = dict(
		gmail_SMTP="smtp.gmail.com",
		gmail_IMAP="imap.gmail.com",
		email_port=587,
		email_login='login@gmail.com',
		email_password='qwerty'
	)

	send_params = dict(
		subject='Subject',
		recipients=['vasya@email.com', 'petya@email.com'],
		message='Message'
	)

	client = Email(*email_params.values())
	client.send_message(*send_params.values())
	client.receive_message(None)
