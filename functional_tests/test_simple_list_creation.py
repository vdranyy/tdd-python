from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Tatiana has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get(self.server_url)

        # She notices the page title and header mention to-do list
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1')
        self.assertIn('To-Do', header_text.text)

        # She is invited enter a to-do item straight away
        inputbox = self.get_item_input_box()
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # She types "Buy peacock feathers" into a text box (Tatiana's hobby
        # tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, she is taken to a new URL,
        # and now the page list "1: Buy peacock feathers" as an item in a
        #  to-do list table
        inputbox.send_keys(Keys.ENTER)
        tatiana_list_url = self.browser.current_url
        self.assertRegexpMatches(tatiana_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Tatiana is very methodical)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Now a new user, Vova, comes along to the site.

        # # We use a new browser session to make sure that no
        # # information of Tatiana's is coming through from cookies etc #
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Vova visits the home page. There's no sign of Tatiana's
        # list
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body')
        self.assertNotIn('Buy peacock feathers', page_text.text)
        self.assertNotIn('Use peacock feathers to make a fly', page_text.text)

        # Vova starts a new list by entering a new item. He
        # is less interesting then Tatiana
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Vova gets his unique URL
        vova_list_url = self.browser.current_url
        self.assertRegexpMatches(vova_list_url, '/lists/.+')
        self.assertNotEqual(vova_list_url, tatiana_list_url)

        # Again, there is no trace of Tatiana's list
        page_text = self.browser.find_element_by_tag_name('body')
        self.assertNotIn('Buy peacock feathers', page_text.text)
        self.assertIn('Buy milk', page_text.text)

        # Satisfied, they both go back to sleep
