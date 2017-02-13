import smtplib



def sendemail(fromaddr,fromname,subject,msg):
    toaddr = 'odainef@gmail.com'
    frmaddr = 'odainef@gmail.com'
    message = """From: {} <{}>
    To: {} Odaine
    Subject: {}
    {}
    """

    messagetosend = message.format(
                                 fromaddr,
                                 fromname,
                                 toaddr,
                                 subject,
                                 msg)

    # Credentials (if needed)
    username = 'odainef@gmail.com'
    password = 'mwlsnykmwwekpnhy'

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddr, messagetosend)
    server.quit()