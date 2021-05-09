import datetime
import requests
import config
from mailer import send_mail


class VaccineSlots(object):
    def __init__(self, min_age_limit, districts, pincodes):
        self.__min_age_limit = min_age_limit
        self.__district_ids = districts
        self.__pincodes = pincodes

    @property
    def min_age_limit(self):
        return self.__min_age_limit

    @property
    def district_id(self):
        return self.__district_ids

    @property
    def pincodes(self):
        return self.__pincodes

    def __parse_data(self, data):
        centers = data['centers']
        data = []
        for center in centers:
            sessions = center['sessions']
            for session in sessions:
                config.logger.info('Center Details Address:%s Name:%s DistrictName:%s StateName:%s Session:%s ' % (
                center['address'], center['name'], center['district_name'], center['state_name'], session))
                if session['available_capacity'] >= config.VACCINE_MINIMUM_AVAILABLE_CAPACITY and session[
                    'min_age_limit'] == self.min_age_limit:
                    data.append(
                        {'name': center['name'], 'address': center['address'], 'district': center['district_name'],
                         'block_name': center['block_name'], 'state': center['state_name'], 'session': session})
        if data:
            config.logger.info('Mailing Details:%s' % data)
            send_mail(data)
        else:
            config.logger.info('No Slots Available')

    def get_vaccine_slots(self):
        base = datetime.datetime.today()
        date_list = [base + datetime.timedelta(days=x) for x in range(config.NUMDAYS)]
        date_str = [x.strftime("%d-%m-%Y") for x in date_list]
        codes = self.__district_ids if not config.SELECT_PINCODE_QUERY else self.__pincodes
        for code in codes:
            for date in date_str:
                try:
                    if config.SELECT_PINCODE_QUERY:
                        data = requests.get(config.VACCINE_ENDPOINT_PINCODE.format(pincode=code, date=date),
                                            headers={'User-Agent': 'PostmanRuntime/7.26.10'})
                    else:
                        data = requests.get(config.VACCINE_ENDPOINT.format(district_id=code, date=date),
                                            headers={'User-Agent': 'PostmanRuntime/7.26.10'})
                except Exception as e:
                    config.logger.error('Exception in endpoint %s' % str(e))
                    continue
                self.__parse_data(data.json())
        return
