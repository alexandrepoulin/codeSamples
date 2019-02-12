import smtplib
import psutil


##main loop

programName = 'WolframKernel.exe'
programName = 'main.exe'

while(True):
    try:
        process_names = [[proc.cpu_percent(0.1),proc.name()] for proc in psutil.process_iter()]
        process_names.sort()
        ##check to see if WolframKernel is using alot of process, if not, its done
        if programName not in [x[1] for x in process_names[-5:]]:
            ##Sets up the email sending (loging in and such)
            smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login('pythonscriptacc@gmail.com', 'QWERTYUIOP')
            ##send the email.
            smtpObj.sendmail('pythonscriptacc@gmail.com', 'alexpoulice@gmail.com', 'Subject: Process Complete.\nYou\'re Mathematica process is done!')
            break
    except:
        pass    

smtpObj.quit()







