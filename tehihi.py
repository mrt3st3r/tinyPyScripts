# __author__ = MrT3st3r

import requests

r = requests.get("https://www.tehihi.school.nz/").text.count("Our out of zone enrolments open shortly.")
print('OUT OF ZONE ENROLMENT IS OPEN!') if r == 0 else print('enrolment is NOT open!')
