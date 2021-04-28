from django.test import SimpleTestCase
from .views import get_time_estimate
# Create your tests here.


class SimpleTest(SimpleTestCase):
    # Arrange
    def test_youtube_api_status_200(self):
        # Act
        status = self.client.get('/api/youtube/term/ok')
        # Assert
        self.assertEqual(status.status_code, 200)

    def test_get_time_estimate_one_hour(self):
        # Act
        result = get_time_estimate(3600)
        # Assert
        self.assertEqual(result, '1 hour ago')
