from django.test import SimpleTestCase
from orders.forms import CustomerLoginForm, PhoneInput

class TestForms(SimpleTestCase):
    def test_customer_login_form_valid_data(self):
        form = CustomerLoginForm(data={
            'phone' : '9176877108',
        })

        self.assertTrue(form.is_valid())
        