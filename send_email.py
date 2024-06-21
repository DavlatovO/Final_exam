import smtplib

sender_email = "davlatovoybek26@gmail.com"
receiver_email = input("Receiver_email: ")

subject = input("SUBJECT: ")
message = input("MESSAGE: ")

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(sender_email, "muco infq rxeg nyzh")
server.sendmail(sender_email, receiver_email, text)

print("Email has been sent to " + receiver_email)

