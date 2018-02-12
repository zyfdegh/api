from tests.test_case import TestCase
from ip import anonymize_ip, detect_country


class TestApi(TestCase):
    def test_detect_country(self):
        self.assertEqual('US', detect_country('8.8.8.8'))
        self.assertRaises(ValueError, detect_country, 'not an ip')
        self.assertEqual(None, detect_country('127.0.0.1'))

    def test_anonymize_ip(self):
        self.assertEqual('1.2.3.X', anonymize_ip('1.2.3.4'))
        self.assertRaises(ValueError, anonymize_ip, '1.2.3.4.5')
        self.assertRaises(ValueError, anonymize_ip, 'abc')
