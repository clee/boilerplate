import unittest
from selenium import webdriver
from ConfigParser import ConfigParser


class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
        desired_capabilities['version'] = '6'
        desired_capabilities['platform'] = 'XP'
        desired_capabilities['name'] = 'Testing Selenium 2 in Python at Sauce'

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://dreamhost:9e7ea696-e07b-4687-87ec-06cdb5b54664@ondemand.saucelabs.com:80/wd/hub"
        )
        self.driver.implicitly_wait(30)
        self.config = ConfigParser()

    def test_sauce(self):
        self.config.read('config.ini')
        self.driver.get(self.config.get('boilerplate', 'server'))
        self.assertTrue("Hello" in self.driver.title)

        body = self.driver.find_element_by_xpath('//body')
        self.assertTrue('page content' in body.text)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
