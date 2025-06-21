import smtplib

email = "codepractice74@gmail.com" #my email for practice
password = "fqbiewztfpkkpxtb" 

with smtplib.SMTP("smtp.gmail.com" , port=587) as connection:
    connection.starttls()
    connection.login(user=email , password=password)
    
    connection.sendmail(from_addr=email , to_addrs="codepractice47@yahoo.com" ,
                        msg="Subject:This is testing masssage \n\nTesting content.")
    
