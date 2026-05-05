import unittest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CalculatorSetupTeardownTest (unittest.TestCase):

    def setUp(self):
        desired_caps = {
            "app": "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App",
            "platformName": "Windows",
            "deviceName": "WindowsPC",
            "AutomationName": "Windows"
        }
        self.driver = webdriver.Remote(
            command_executor="http://127.0.0.1:4723",
            desired_capabilities=desired_caps
        )
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        try:
            close_calculator = self.wait.until(EC.element_to_be_clickable((By.NAME, "Close Calculator")))
            close_calculator.click()
        except TimeoutException:
            pass
        self.driver.quit()

    # def test_calculator_launches(self):
    #     # Minimal test — just verify calculator opened successfully
    #     self.assertIsNotNone(self.driver.session_id)


if __name__ == "__main__":
    unittest.main()