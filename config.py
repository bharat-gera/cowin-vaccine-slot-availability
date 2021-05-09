#VACCINE ENDPOINTS
VACCINE_ENDPOINT = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={district_id}&date={date}'
VACCINE_ENDPOINT_PINCODE = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByPin?pincode={pincode}&date={date}'

#QUERY ON PINCODE OR DISTRICT BASE
SELECT_PINCODE_QUERY = False

VACCINE_MINIMUM_AVAILABLE_CAPACITY = 2

# mailer config
GMAIL_USER = 'Gmail Email User'
GMAIL_PASSWORD = 'GMAIL PASSWORD'
TO_USERS = ['LIST OF EMAIL RECEIPIENTS']

# Delay interval
DELAY_INTERVAL = 20

# Numdays
NUMDAYS = 2

#importing the module 
import logging
import sys 

#now we will Create and configure logger 
logging.basicConfig(filename="std.log", format='%(asctime)s %(message)s', filemode='a') 
stdout_handler = logging.StreamHandler(sys.stdout)

#Let us Create an object 
logger=logging.getLogger() 

logger.addHandler(stdout_handler)
#Now we are going to Set the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 
