import argparse
import time
from config import DELAY_INTERVAL, logger
from vaccine import VaccineSlots

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--age", "-a", help="set age", default=18, type=int)
    parser.add_argument("--district", "-d", help="set district", type=str, default='202')
    parser.add_argument("--pincode", "-p", help="set pincode", type=str, default='123401')
    args = parser.parse_args()
    slot = VaccineSlots(args.age, args.district.split(','),args.pincode.split(','))
    while True:
        logger.info('Checking..')
        slot.get_vaccine_slots()
        time.sleep(DELAY_INTERVAL)


if __name__ == '__main__':
    main()
