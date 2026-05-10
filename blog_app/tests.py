from django.test import TestCase

class BlogAppTests(TestCase):
    def test_basic_status_code(self):
        """Basic test to ensure the test runner finds and executes tests."""
        self.assertEqual(1, 1)