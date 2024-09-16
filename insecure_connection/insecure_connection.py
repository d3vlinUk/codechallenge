
def ftp_connection_noncompliant():
    import ftplib
    cnx = ftplib.FTP("ftp://anonymous@example.com")