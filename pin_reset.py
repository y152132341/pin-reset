import time
import logging
import argparse
import json
from appium import webdriver


class PinReset:
    def __init__(self):
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
        self.log = logging.getLogger(__name__)

        with open('config.json', 'r') as json_file:
            configs = json.load(json_file)
            self.driver = configs['appium_web_driver']
            self.appium_url = configs['appium_url']
            self.ui_elements = configs['ui_elements']


    def run(self, args):
        self.log.info('LAUNCHING REMOTE CONTROL')
        self.driver = webdriver.Remote(self.appium_url, self.driver)

        self.log.info('ACCEPT Ts&Cs')
        self.driver.find_element_by_id(self.ui_elements['accept_ts_and_cs']).click()
        time.sleep(3)

        self.log.info('SELECT TV ICON')
        self.driver.find_element_by_xpath(self.ui_elements['tv_icon']).click()
        time.sleep(3)

        self.log.info('BROWSE PANASONIC')
        self.driver.find_element_by_id(self.ui_elements['devices_search_box']).send_keys('Panasonic')
        time.sleep(3)

        self.log.info('SELECT THE FIRST ELEMENT')
        self.driver.find_elements_by_xpath(self.ui_elements['first_panasonic_listed'])[0].click()
        time.sleep(3)

        self.log.info('TURN ON TV')
        self.driver.find_elements_by_xpath(self.ui_elements['power_button'])[0].click()
        time.sleep(5)

        self.log.info('GO TO THE MAIN MENU')
        self.driver.find_elements_by_xpath(self.ui_elements['menu_button'])[0].click()
        time.sleep(5)

        down_key = [(715, 1752)]
        right_key = [(1128, 1307)]

        self.log.info('NAVIGATE TO SETTINGS')
        for i in range(0, 4):
          self.driver.tap(down_key)
          time.sleep(1)

        self.log.info('SELECT SETTINGS')
        self.driver.tap(right_key)
        time.sleep(1)

        self.log.info('NAVIGATE TO SYSTEM SETTINGS')
        for i in range(0, 6):
          self.driver.tap(down_key)
          time.sleep(1)

        self.log.info('SELECT SYSTEM SETTINGS')
        self.driver.tap(right_key)
        time.sleep(1)

        self.log.info('NAVIGATE TO RESET TO FACTORY SETTINGS')
        self.driver.tap(down_key)
        time.sleep(1)

        self.log.info('SELECT RESET TO FACTORY SETTINGS')
        self.driver.tap(right_key)

        self.log.info('SCROLL TO NUMERIC PAD')
        self.driver.swipe(500, 1700, 500, 1000, 400)

        # these values are the numeric pad keys from 0 to 9
        key = [19, 9, 10, 11, 12, 13, 14, 15, 16, 17]

        for n in range(0, 10000):
          # format numbers to PIN style: 0 = 0000, 1 = 0001, etc.
          pin = str(n).zfill(4)
          self.log.info('TRYING NUMBER ' + pin)

          # extracting every digit from PIN
          digits = [int(i) for i in pin]

          # tapping digits one by one
          for d in digits:
            self.driver.find_elements_by_xpath(self.ui_elements['numeric_pad'].replace("$KEY_NUMBER", str(key[d])))[0].click()
            time.sleep(1)


def main(args):
    PinReset().run(args)


if __name__ == '__main__':
    import logging.config
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # KeyboardInterrupt -> ^C

    parser = argparse.ArgumentParser(description='Runs Appium PinReset automation script')
    parser.add_argument('--debug', action='store_true', help='Debug flag')
    args = parser.parse_args()

    main(args)
