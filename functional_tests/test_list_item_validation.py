from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Tatiana goes to the home page accidentally tries to submit
        # an empty list item. She hits enter on the empty input box

        # The home page refreshes, and there is an error message saying
        # that list item cannot be blank

        # She tries again with some text for the item, which now works

        # Perversely, she now decide submit a second blank list item

        # She receives a similar warning on the list page

        # And she can correct it by filling some text in it
        self.fail('Incomplete test')
