import unittest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from helpers.setup_teardown import CalculatorSetupTeardownTest

class TestBasicOperations(CalculatorSetupTeardownTest):
    
    def test_addition(self):
        self.wait.until(EC.element_to_be_clickable((By.NAME, "One"))).click()
        self.wait.until(EC.element_to_be_clickable((By.NAME, "Plus"))).click()
        self.wait.until(EC.element_to_be_clickable((By.NAME, "One"))).click()
        self.wait.until(EC.element_to_be_clickable((By.NAME, "Equals"))).click()

        Expression = self.wait.until(
            EC.presence_of_element_located((By.NAME, "Expression is 1 + 1=")))
        Display = self.wait.until(
            EC.presence_of_element_located((By.NAME, "Display is 2")))

        # self.assertIsNotNone(Expression, "Expression element not found")
        # self.assertEqual(Expression.text, "Expression is 1 + 1=", "Expression text does not match expected value")
        # self.assertIsNotNone(Display, "Display element not found")
        # self.assertEqual(Display.text, "Display is 2", "Display text does not match expected value")
        
        self.assertEqual(
            Expression.get_attribute("Name"), 
            "Expression is 1 + 1=",
            "Expression does not match expected value"
        )
        self.assertEqual(
            Display.get_attribute("Name"),
            "Display is 2", 
            "Display does not match expected value"
        )