# cowin-vaccine-slot-availability
To get the vaccine slot availability. It would hit the vaccine endpoint in order to get the vaccine slot of provided district id and age. As soon as vaccine is available, it would send the mail to the given users.

Run Command: python vaccine.py --age <provide age either 18 or 45> --district <provide district Id> --pincode <provide pincode>

We need to either provide the district Id or pincode on command args line.
We can get the district Id from the Cowin Portal.

Above script would hit the vaccine availability endpoint for every 20 sec but this time can be configuratble.

# Configurable Parameters
SELECT_PINCODE_QUERY = True, In case if we are providing the pincode on command line.
SELECT_PINCODE_QUERY = False, In case we are providing the district Id on command line.
GMAIL_USER = 'ENTER EMAIL Id'
GMAIL_PASSWORD = 'ENTER EMAIL PASSWORD'
TO_USERS = ['ENTER LIST OF RECEPIENTS EMAILS']
DELAY_INTERVAL = <--sleep interval from script to hit the cowin endpoint-->
