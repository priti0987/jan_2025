from datetime import datetime

import pywhatkit


# print(datetime.now().strftime("%H"))
phone_number=""
pywhatkit.sendwhatmsg("phone_number","test",int(datetime.now().strftime("%H")),int(datetime.now().strftime("%M"))+1)