from django.test import TestCase

from catalog.serializers import SingerSrlz
from catalog.models import Singer


class SingerSrlzTestCase(TestCase):
    def test_singer_srlz(self):
        s1 = Singer.objects.create(name="Leps")
        s2 = Singer.objects.create(name="bilan")
        data = SingerSrlz([s1, s2], many=True).data
        expected_data = [
            {
                "id": s1.id,
                "name": "Leps"
            },
            {
                "id": s2.id,
                "name": "bilan"
            },
        ]
        self.assertEqual(expected_data, data)
