import requests, csv
import base64
import getpass

#name of csv file
csvFile = 'userlist.csv'

#ask for user input
host = raw_input("MailInABox Domain: ")
host = "https://"+host
adminUser = raw_input("Admin Email: ")
adminPassword = getpass.getpass('Password:')

headers = { 'Authorization' : 'Basic %s' % base64.b64encode(adminUser+":"+adminPassword),
'Content-Type': 'application/x-www-form-urlencoded' }

#MailinaBox Endpoint
url = host+"/admin/mail/users/add"

#Open CSV File
with open('./'+csvFile) as usercsv:
 rows = csv.reader(usercsv,delimiter=',')
#Set Row Counter
 p=1
 for row in rows:
    payload = 'email='+row[0]+'&password='+row[1]
    response = requests.request("POST", url, headers=headers, data = payload)
#Report to User The Result
    if response.status_code != 200:
       sCode = ' failed to import'
    else :
       sCode = ' was added successfully'
    print 'Row '+str(p)+' '+str(response.text)+' '+row[0]+sCode
#Increase Counter
    p += 1

#End the Script
 print "\n\nEmail Import Process Completed"
