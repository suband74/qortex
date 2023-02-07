from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from catalog.models import Singer
from catalog.serializers import SingerSrlz


class SingerApiTestCase(APITestCase):
    def test_get(self):
        s1 = Singer.objects.create(name="Leps")
        s2 = Singer.objects.create(name="bilan")
        url = reverse("singer-list")
        srlz = SingerSrlz([s1, s2], many=True).data
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(srlz, response.data)
