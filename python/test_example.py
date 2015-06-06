from base_test_case import BaseTestCase
import unittest

def check_records_count(driver, ass, value, num):
    main_window = driver.find_element_by_id('MainWindow')

    search_string = main_window.find_element_by_id('QueryMW')
    search_string.send_keys(str(value))

    search_button = main_window.find_element_by_id('SearchMW')
    search_button.click()

    products_list = main_window.find_element_by_id('ProductsMW')
    product_items = products_list.find_elements_by_class_name('ListViewItem')

    ass(len(product_items), num)

class IdTest(BaseTestCase):
   def test_find_1(self):
       check_records_count(self.driver, self.assertEqual, 1, 1)
   def test_find_2(self):
       check_records_count(self.driver, self.assertEqual, 2, 1)
   def test_find_3(self):
       check_records_count(self.driver, self.assertEqual, 3, 1)
   def test_find_4(self):
       check_records_count(self.driver, self.assertEqual, 4, 1)
   def test_find_5(self):
       check_records_count(self.driver, self.assertEqual, 5, 1)
   def test_find_6(self):
       check_records_count(self.driver, self.assertEqual, 6, 1)
   def test_find_7(self):
       check_records_count(self.driver, self.assertEqual, 7, 1)
   def test_find_8(self):
       check_records_count(self.driver, self.assertEqual, 8, 1)
   def test_find_9(self):
        check_records_count(self.driver, self.assertEqual, 9, 0)

# class ExampleTest(BaseTestCase):
#      def test_example(self):
#          main_window = self.driver.find_element_by_id('MainWindow')
#
#          search_string = main_window.find_element_by_id('QueryMW')
#          search_string.send_keys('3')
#
#          search_button = main_window.find_element_by_id('SearchMW')
#          search_button.click()
#
#          products_list = main_window.find_element_by_id('ProductsMW')
#          product_items = products_list.find_elements_by_class_name('ListViewItem')
#
#          self.assertEqual(len(product_items), 1)


if __name__ == '__main__':
    unittest.main()
