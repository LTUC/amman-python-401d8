from django.test import TestCase
from django.urls import reverse


class TestSnack(TestCase):
    # Test the status response code
    def test_status_code(self):
        url = reverse('snacks_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    # Test the templates if they inherit from the right base
    def test_template(self):
        url = reverse('snacks_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snacks_list.html')
        self.assertTemplateUsed(response, '_base.html')


class TestSnackDetail(TestCase):

    def test_detail_view(self):
        url = reverse('snack_detail', args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_detail.html')
        # self.assertTemplateUsed(response, '_base.html')

    # we need to test status code
    # we need to test template

