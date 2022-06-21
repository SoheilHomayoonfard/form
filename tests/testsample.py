from django.test import TestCase, Client

from shop.forms import PersonalInformation


class TestPersonalForm(TestCase):
    def setUp(self):
        self.client = Client()

    def test_form_is_valid(self):
        form_data = {
            'gender': 'm',
            'full_name': 'Soheil This Is Title Homayoon',
            'age': 21,
            'height': 185
        }
        form = PersonalInformation(data=form_data)
        self.assertTrue(form.is_valid(), 'Error')
