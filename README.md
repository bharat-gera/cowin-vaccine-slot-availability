# cowin-vaccine-slot-availability
Get vaccine slot Notification. It would hit the vaccine endpoint in order to get the vaccine slot of provided district_id/pincode and age. As soon as vaccine is available in the provided area, it would send the Email to the provided email users.

SETUP requirement: pip3 install -r requirements.txt

Run Command: **python main.py --age (provide age either 18 or 45) --district (provide district Id) --pincode (provide pincode)**

We need to either provide the district Id or pincode parameter on command line arguments. If we don't have district Id, please use pincode.

We can get the district Id from the Cowin Portal.

Above command would hit the vaccine availability endpoint for every 20 sec and this time can be configuratble.

# Configurable Parameters
SELECT_PINCODE_QUERY = True, In case if we are providing the pincode on command line.

SELECT_PINCODE_QUERY = False, In case we are providing the district Id on command line.

GMAIL_USER = 'ENTER EMAIL Id'

GMAIL_PASSWORD = 'ENTER EMAIL PASSWORD'

TO_USERS = ['ENTER LIST OF RECEPIENTS EMAILS']

NUMDAYS = 'Number of future days for which we want the appointment'

DELAY_INTERVAL = "sleep interval to hit the slot availability endpoint"
