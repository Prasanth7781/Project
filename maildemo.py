import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('prasanth160601@gmail.com','sai123M@')
server.sendmail('prasanth160601@gmail.com','marisarlasaiprasanth791@gmail.com','From Python')
print("Mail Sent")
