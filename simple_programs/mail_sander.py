import smtplib
import ssl

massage = v('texting to send email  3 !! using python sorry!!!')
to_address = ['vigneshwarreddy7780@gmail.com','m.vigneshwer7780@gmail.com','srmvrmlynr@gmail.com','mudhireddynandu@gmail.com']
sem = ssl.create_default_context()
tie_server = smtplib.SMTP_SSL('smtp.gmail.com',465,context = sem)
tie_server.login('mvijju193@gmail.com','hfgt nyxu qucx uwhw')
tie_server.sendmail('mvijju193@gmail.com',to_address,massage)