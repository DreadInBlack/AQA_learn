import Pages.elements_page


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = Pages.elements_page.TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            text_box_page.fill_all_fields()
            output_name, output_email, output_cur_address, output_per_address = text_box_page.check_filled_from()
            print(output_name)
            print(output_email)
            print(output_cur_address)
            print(output_per_address)
