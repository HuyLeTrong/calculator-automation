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

    def test_subtraction(self):
        self.wait.until(EC.element_to_be_clickable((By.NAME, "One"))).click()
        self.wait.until(EC.element_to_be_clickable((By.NAME, "Minus"))).click()
        self.wait.until(EC.element_to_be_clickable((By.NAME, "One"))).click()
        self.wait.until(EC.element_to_be_clickable((By.NAME, "Equals"))).click()

        Expression = self.wait.until(
            EC.presence_of_element_located((By.NAME, "Expression is 1 Minus ( 1=")))

        Display = self.wait.until(
            EC.presence_of_element_located((By.NAME, "Display is 0")))

        
        self.assertEqual(
            Expression.get_attribute("Name"), 
            "Expression is 1 Minus ( 1=",
            "Expression does not match expected value"
        )
        self.assertEqual(
            Display.get_attribute("Name"),
            "Display is 0", 
            "Display does not match expected value"
        )

    def test_negative_subtraction(self):
        self.wait.until(EC.element_to_be_clickable((By.NAME, "Two"))).click()
        self.wait.until(EC.element_to_be_clickable((By.NAME, "Minus"))).click()
        self.wait.until(EC.element_to_be_clickable((By.NAME, "One"))).click()
        self.wait.until(EC.element_to_be_clickable((By.NAME, "Positive negative"))).click()

        self.wait.until(EC.element_to_be_clickable((By.NAME, "Equals"))).click()

        Expression = self.wait.until(
            EC.presence_of_element_located((By.NAME, "Expression is 2 Minus ( -1=")))

        Display = self.wait.until(
            EC.presence_of_element_located((By.NAME, "Display is 3")))

        
        self.assertEqual(
            Expression.get_attribute("Name"), 
            "Expression is 2 Minus ( -1=",
            "Expression does not match expected value"
        )
        self.assertEqual(
            Display.get_attribute("Name"),
            "Display is 3", 
            "Display does not match expected value"
        )

    def test_multiplication(self):
        self.wait.until(EC.element_to_be_clickable((By.NAME, "One"))).click()
        self.wait.until(EC.element_to_be_clickable((By.NAME, "One"))).click()
        self.wait.until(EC.element_to_be_clickable((By.NAME, "Multiply by"))).click()
        self.wait.until(EC.element_to_be_clickable((By.NAME, "Three"))).click()
        self.wait.until(EC.element_to_be_clickable((By.NAME, "Equals"))).click()

        Expression = self.wait.until(
            EC.presence_of_element_located((By.NAME, "Expression is 11 × 3=")))
        Display = self.wait.until(
            EC.presence_of_element_located((By.NAME, "Display is 33")))

        
        self.assertEqual(
            Expression.get_attribute("Name"), 
            "Expression is 11 × 3=",
            "Expression does not match expected value"
        )
        self.assertEqual(
            Display.get_attribute("Name"),
            "Display is 33", 
            "Display does not match expected value"
        )