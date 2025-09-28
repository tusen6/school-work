# === CS 115 Lab 2 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name:Zhaochen Weng
#
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System."

#
# === CS 115 Lab 2 ===

import lab2
import unittest
# You can access vali_date as lab2.vali_date in this file.

class TestCases(unittest.TestCase):
    def test_vali_date_case_1(self):
        """
        Tests that the date May 15th registers as valid.
        """
        self.assertTrue(lab2.vali_date(5, 15))

#check if month valid
    def test_vali_date_case_2(self):
        self.assertFalse(lab2.vali_date(13,4))
        self.assertTrue(lab2.vali_date(12,4))
        self.assertFalse(lab2.vali_date(0,4))
        self.assertFalse(lab2.vali_date(-1,4))
        self.assertTrue(lab2.vali_date(1,4))

#check if day valid
    def test_vali_date_case_3(self):
        for i in [1,3,5,7,8,10,12]:
            self.assertTrue(lab2.vali_date(i,31))
            self.assertFalse(lab2.vali_date(i,32))

        for i in [4,6,9,11]:
            self.assertTrue(lab2.vali_date(i,30))
            self.assertFalse(lab2.vali_date(i,31))

        self.assertTrue(lab2.vali_date(2,29))
        self.assertFalse(lab2.vali_date(2,30)) 
        
if __name__ == "__main__":
    unittest.main()
