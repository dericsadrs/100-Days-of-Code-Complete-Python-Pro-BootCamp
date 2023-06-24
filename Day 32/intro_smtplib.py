import smtplib

my_email = "example@gmail.com"
password = "password"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user = my_email, password = password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs= "sendto@gmail.com",
        msg="Subject: Hello\n\n This is the body of my email"

    )