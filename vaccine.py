import time
import datetime
import requests
import argparse
import smtplib

# Vaccine Endpoints
VACCINE_ENDPOINT = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={district_id}&date={date}'
VACCINE_ENDPOINT_PINCODE = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByPin?pincode={pincode}&date={date}'

# Configurable Parameters
SELECT_PINCODE_QUERY = False 
GMAIL_USER = 'ENTER EMAIL Id'
GMAIL_PASSWORD = 'ENTER EMAIL PASSWORD'
TO_USERS = ['ENTER LIST OF RECEPIENTS EMAILS']
DELAY_INTERVAL = 20  #sec

def send_mail(data):

    sent_from = 'VACCINE Available MESSAGE'
    subject = 'OMG Super Important Message'

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, data)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(GMAIL_USER, GMAIL_PASSWORD)
    server.sendmail(sent_from, TO_USERS, email_text)
    server.close()

    print('Email sent!')


class VaccineSlots(object):
    def __init__(self, min_age_limit, district_id, pincode='123401'):
        self.__min_age_limit = min_age_limit
        self.__district_id = district_id
        self.__pincode = pincode

    @property
    def min_age_limit(self):
        return self.__min_age_limit

    @property
    def district_id(self):
        return __district_id

    def __parse_data(self, data):
        centers = data['centers']
        data = []
        for center in centers:
            sessions = center['sessions']
            for session in sessions:
                print(session, center['address'], center['name'])
                if session['available_capacity'] > 0 and session['min_age_limit'] >= self.min_age_limit:
                    data.append(
                        {'name': center['name'], 'address': center['address'], 'district': center['district_name'],
                         'block_name': center['block_name'], 'session': session})
        print(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'), 'Extracted Data: ', data)
        if data:
            send_mail(data)

    def get_vaccine_slots(self):
        numdays = 2
        base = datetime.datetime.today()
        date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
        date_str = [x.strftime("%d-%m-%Y") for x in date_list]
        for date in date_str:
            try:
                if SELECT_PINCODE_QUERY:
                    data = requests.get(VACCINE_ENDPOINT_PINCODE.format(pincode=self.__pincode, date=date), headers={'User-Agent': 'PostmanRuntime/7.26.10'})
                else:
                    data = requests.get(VACCINE_ENDPOINT.format(district_id=self.__district_id, date=date), headers={'User-Agent': 'PostmanRuntime/7.26.10'})
            except Exception as e:
                print('Exception in endpoint %s' % str(e))
                continue
            self.__parse_data(data.json())
        return


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--age", "-a", help="set age", default=18, type=int)
    parser.add_argument("--district", "-d", help="set district", type=int, default=202)
    parser.add_argument("--pincode", "-p", help="set pincode", type=int, default=123401)
    args = parser.parse_args()
    slot = VaccineSlots(args.age, args.district)
    while True:
        slot.get_vaccine_slots()
        time.sleep(DELAY_INTERVAL)


if __name__ == '__main__':
    main()
