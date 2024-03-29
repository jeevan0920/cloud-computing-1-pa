#**********************
#*
#* Progam Name: MP1. Membership Protocol.
#*
#* Current file: submit_new.py
#* About this file: Submission python script.
#* Python3 version of submit.py
#* 
#***********************

import urllib.request
import urllib.parse
import hashlib
import random
import email
import email.message
import email.encoders
import io
import sys
import subprocess
import json
import os

""""""""""""""""""""
""""""""""""""""""""
class NullDevice:
    def write(self, s):
        pass

def submit():   
    print('==\n== [sandbox] Submitting Solutions \n==')
    
    (login, password) = loginPrompt()
    if not login:
        print('!! Submission Cancelled')
        return

    output = subprocess.Popen(['sh', 'run.sh', str(0)], stdout=subprocess.PIPE).communicate()[0]
    submissions = [source(i) for i in range(3)]
    submitSolution(login, password, submissions)

# =========================== LOGIN HELPERS - NO NEED TO CONFIGURE THIS =======================================

def loginPrompt():
    """Prompt the user for login credentials. Returns a tuple (login, password)."""
    (login, password) = basicPrompt()
    return login, password

def basicPrompt():
    """Prompt the user for login credentials. Returns a tuple (login, password)."""
    login = input('Login (Email address): ')
    password = input('One-time Password (from the assignment page. This is NOT your own account\'s password): ')
    return login, password

def partPrompt():
    print('Hello! These are the assignment parts that you can submit:')
    counter = 0
    for part in partFriendlyNames:
        counter += 1
        print(str(counter) + ') ' + partFriendlyNames[counter - 1])
    partIdx = int(input('Please enter which part you want to submit (1-' + str(counter) + '): ')) - 1
    return (partIdx, partIds[partIdx])

def submit_url():
    """Returns the submission url."""
    return "https://www.coursera.org/api/onDemandProgrammingScriptSubmissions.v1"

def submitSolution(email_address,password, submissions):
    """Submits a solution to the server. Returns (result, string)."""

    values = {
        "assignmentKey": akey,
        "submitterEmail": email_address,
        "secret": password,
        "parts": {
            partIds[0]: {
                "output": submissions[0]
            },
            partIds[1]: {
                "output": submissions[1]
            },
            partIds[2]: {
                "output": submissions[2]
            }
        }
    }
    url = submit_url()
    data = json.dumps(values).encode('utf-8')
    req = urllib.request.Request(url, data)
    req.add_header('Content-Type', 'application/json')
    req.add_header('Cache-Control', 'no-cache')
    response = urllib.request.urlopen(req)
    return

## This collects the source code (just for logging purposes) 
def source(partIdx):
    # open the file, get all lines
    with open("dbg.%d.log" % partIdx, 'r') as f:
        src = f.read() 
    return src

def cleanup():
    for i in range(3):
        try:
            os.remove("dbg.%s.log" % i)
        except:
            pass

akey = 'Mj8OkgI-EeaTLQonT2FRpw'
# the "Identifier" you used when creating the part
partIds = ['b9m9h', 'MxUat', '8ATm3']
# used to generate readable run-time information for students
partFriendlyNames = ['Single Failure', 'Multiple Failure', 'Message Drop Single Failure'] 

submit()

cleanup()
