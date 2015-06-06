from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
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

class MyTest(BaseTestCase):
    def show(self):
        main_window = self.driver.find_element_by_id('MainWindow')

        add_button = main_window.find_element_by_id('AddNewProductMW')
        add_button.click()

        return self.driver.find_element_by_id('AddNewProductWindow')

    def record_count(self):
        main_window = self.driver.find_element_by_id('MainWindow')

        products_list = main_window.find_element_by_id('ProductsMW')
        product_items = products_list.find_elements_by_class_name('ListViewItem')
        return len(product_items)

    def main_window(self):
        return self.driver.find_element_by_id('MainWindow')

    def products(self):
        products_list = self.main_window().find_element_by_id('ProductsMW')
        return products_list.find_elements_by_class_name('ListViewItem')

    def get_nth_product(self, n):
        return self.products()[n].find_elements_by_class_name('TextBlock')[0:4]

    def add_product(self, name):
        res = self.show()
        text = res.find_element_by_id('NameAW')
        text.send_keys(name)
        res.find_element_by_id('AddAW').click()

    def delete_all(self):
        self.main_window().find_element_by_id('DeleteSelectedMW').click()

class IdTest(MyTest):
    def test_find_all_ids(self):
        for i in range(1, self.record_count() + 1):
            check_records_count(self.driver, self.assertGreaterEqual, i, 1)

    def test_find_not_found(self):
        check_records_count(self.driver, self.assertEqual, 99999999, 0)

class NameTest(BaseTestCase):
    def test_find_ms(self):
        check_records_count(self.driver, self.assertEqual, 'Монитор Sony', 1)
    def test_find_mp(self):
        check_records_count(self.driver, self.assertEqual, 'Монитор Panasonic', 1)
    def test_find_md(self):
        check_records_count(self.driver, self.assertEqual, 'Монитор DELL', 1)
    def test_find_pe(self):
        check_records_count(self.driver, self.assertEqual, 'Принтер Epson', 1)
    def test_find_km(self):
        check_records_count(self.driver, self.assertEqual, 'Клавиатура Microsoft', 1)
    def test_find_kl(self):
        check_records_count(self.driver, self.assertEqual, 'Клавиатура Logitec', 1)
    def test_find_mm(self):
        check_records_count(self.driver, self.assertEqual, 'Мышь Microsoft', 1)
    def test_find_tc(self):
        check_records_count(self.driver, self.assertEqual, 'Телефон C1sko', 1)
    def test_find_not_found(self):
        check_records_count(self.driver, self.assertEqual, 'Мой клёвый продукт', 0)

class TypeTest(BaseTestCase):
    def test_find_m(self):
        check_records_count(self.driver, self.assertEqual, 'Монитор', 3)
    def test_find_p(self):
        check_records_count(self.driver, self.assertEqual, 'Принтер', 1)
    def test_find_k(self):
        check_records_count(self.driver, self.assertEqual, 'Клавиатура', 2)
    def test_find_mouse(self):
        check_records_count(self.driver, self.assertEqual, 'Мышь', 1)
    def test_find_t(self):
        check_records_count(self.driver, self.assertEqual, 'Телефон', 1)
    def test_find_not_found(self):
        check_records_count(self.driver, self.assertEqual, 'Мой клёвый продукт', 0)

class VendorTest(BaseTestCase):
    def test_find_s(self):
        check_records_count(self.driver, self.assertEqual, 'Sony', 1)
    def test_find_p(self):
        check_records_count(self.driver, self.assertEqual, 'Panasonic', 1)
    def test_find_d(self):
        check_records_count(self.driver, self.assertEqual, 'DELL', 1)
    def test_find_e(self):
        check_records_count(self.driver, self.assertEqual, 'Epson', 1)
    def test_find_m(self):
        check_records_count(self.driver, self.assertEqual, 'Microsoft', 2)
    def test_find_l(self):
        check_records_count(self.driver, self.assertEqual, 'Logitec', 1)
    def test_find_c(self):
        check_records_count(self.driver, self.assertEqual, 'C1sko', 1)
    def test_find_not_found(self):
        check_records_count(self.driver, self.assertEqual, 'Мой клёвый продукт', 0)

class UpperTest(BaseTestCase):
    def test_find_sony(self):
        check_records_count(self.driver, self.assertEqual, 'SONY', 1)

class LowerTest(BaseTestCase):
    def test_find_sony(self):
        check_records_count(self.driver, self.assertEqual, 'sony', 1)

class CancelTest(MyTest):
    def test_cancel(self):
        count = self.record_count()

        res = self.show()
        res.find_element_by_id('CancelAW').click()

        check_records_count(self.driver, self.assertEqual, '', count)

class AddTest(MyTest):
    def test_add_total_count(self):
        count = self.record_count()

        res = self.show()
        text = res.find_element_by_id('NameAW')
        text.send_keys('Test1')

        res.find_element_by_id('AddAW').click()

        self.assertEqual(count + 1, self.record_count())

    def test_add_name(self):
        count = self.record_count()

        res = self.show()
        text = res.find_element_by_id('NameAW')
        text.send_keys('Test2')

        res.find_element_by_id('AddAW').click()

        check_records_count(self.driver, self.assertEqual, 'Test2', 1)

    def test_add_id(self):
        count = self.record_count()

        res = self.show()
        text = res.find_element_by_id('NameAW')
        text.send_keys('Test3')

        res.find_element_by_id('AddAW').click()

        check_records_count(self.driver, self.assertEqual, count+1, 1)

    def test_add_same_name(self):
        count = self.record_count()

        res = self.show()
        text = res.find_element_by_id('NameAW')
        text.send_keys('Test4')
        res.find_element_by_id('AddAW').click()

        res = self.show()
        text = res.find_element_by_id('NameAW')
        text.send_keys('Test4')
        res.find_element_by_id('AddAW').click()

        self.assertEqual(count + 2, self.record_count())

    def test_long(self):
        long_text = '_' * 999

        res = self.show()
        text = res.find_element_by_id('NameAW')
        text.send_keys(long_text)
        res.find_element_by_id('AddAW').click()

        main_window = self.driver.find_element_by_id('MainWindow')

        products_list = main_window.find_element_by_id('ProductsMW')
        product_items = products_list.find_elements_by_class_name('ListViewItem')
        self.assertEqual(product_items[0].find_elements_by_class_name('TextBlock')[1].get_attribute('Name'), long_text)

class EditTest(MyTest):
    def test_edit1(self):
        main_window = self.driver.find_element_by_id('MainWindow')

        products_list = main_window.find_element_by_id('ProductsMW')
        product_items = products_list.find_elements_by_class_name('ListViewItem')
        id, name,cat, other = product_items[0].find_elements_by_class_name('TextBlock')

        actions = ActionChains(self.driver)

        actions.move_to_element(name)
        actions.double_click()
        actions.perform()

        change_window = self.driver.find_element_by_id('ChangeProductWindow')
        text = change_window.find_element_by_id('NameCW')
        text.send_keys(text.text + '1')
        change_window.find_element_by_id('SaveCW').click()

        products_list = main_window.find_element_by_id('ProductsMW')
        product_items = products_list.find_elements_by_class_name('ListViewItem')
        id2, name2, cat2,other2 = product_items[0].find_elements_by_class_name('TextBlock')

        self.assertEqual(id.get_attribute('Name'), id2.get_attribute('Name'))
        self.assertEqual(name.get_attribute('Name') + '1', name2.get_attribute('Name'))

    def test_edit_category(self):
        id, name, cat, dele = self.get_nth_product(0)

        actions = ActionChains(self.driver)

        actions.move_to_element(self.products()[0])
        actions.double_click()
        actions.perform()

        change_window = self.driver.find_element_by_id('ChangeProductWindow')

        categories = change_window.find_element_by_id('CategoryCW')
        categories.click()

        # Элемент списка НАД save
        change_window.find_element_by_id('SaveCW').click()

        change_window.find_element_by_id('SaveCW').click()

        id2, name2, cat2, dele2 = self.get_nth_product(0)

        self.assertNotEqual(cat.get_attribute('Name'), cat2.get_attribute('Name'))

class SortTest(MyTest):
    def test_reverse(self):
        main_window = self.driver.find_element_by_id('MainWindow')

        products_list = main_window.find_element_by_id('ProductsMW')
        product_items = products_list.find_elements_by_class_name('ListViewItem')
        id, name, cat, other = product_items[0].find_elements_by_class_name('TextBlock')

        main_window.find_element_by_id('SortGroupBoxMW').find_element_by_id('SortDownMW').click()

        products_list = main_window.find_element_by_id('ProductsMW')
        product_items = products_list.find_elements_by_class_name('ListViewItem')
        id2, name2,cat2, other2 = product_items[0].find_elements_by_class_name('TextBlock')

        self.assertNotEqual(id.get_attribute('Name'), id2.get_attribute('Name'))

    def test_keys_sensetive_sort(self):
        self.add_product('н')

        id,name,cat,other = self.get_nth_product(6)
        self.assertEqual(name.get_attribute('Name'), 'н')

    def test_sort_equals(self):
        self.add_product('Test')
        self.add_product('Test')

        ids = []
        for product in self.products():
            ids.append(product.find_elements_by_class_name('TextBlock')[0].get_attribute('Name'))

        self.main_window().find_element_by_id('SortGroupBoxMW').find_element_by_id('SortDownMW').click()

        ids2 = []
        for product in self.products():
            ids2.append(product.find_elements_by_class_name('TextBlock')[0].get_attribute('Name'))

        self.assertEqual(ids[::-1], ids2)

class DeleteTest(MyTest):
    def test_delete(self):
        main_window = self.driver.find_element_by_id('MainWindow')
        products_list = main_window.find_element_by_id('ProductsMW')
        product_items = products_list.find_elements_by_class_name('ListViewItem')
        count1 = self.record_count()
        id, name,cat, dele = product_items[0].find_elements_by_class_name('TextBlock')
        dele.click()
        count2 = self.record_count()
        self.assertEqual(count1 - 1, count2)

class MultiplyDelete(MyTest):
    def test_remove_last(self):
        count1 = self.record_count()

        self.products()[0].click()

        self.driver.execute_script('input: ctrl_click', self.products()[1])
        self.delete_all()

        count2 = self.record_count()

        self.assertEqual(count1 - 2, count2)

if __name__ == '__main__':
    unittest.main()
