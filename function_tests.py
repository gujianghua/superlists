from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):
        # 她去看了这个应用的首页
        self.browser.get('http://localhost:8000')
        # 她注意到网页的标题和头部都包含“To-Do”这个词
        self.assertIn('Todo',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Todo',header_text)
        # 应用邀请她输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a todo item')
        # 她在一个文本框中输入了“Buy peacock feathers”（购买孔雀羽毛）
        inputbox.send_keys('Buy peacock feathers')
        # 她按回车键后，页面更新了
        # 待办事项表格中显示了“1: Buy peacock feathers”
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(rows.text == '1: Buy peacock feathers'for row in rows),"Error")

        self.fail('Finish  the test!')
if __name__ == '__main__':
    unittest.main(warnings='ignore')
