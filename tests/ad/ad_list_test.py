import pytest
from rest_framework import status

from ads.serializers import AdListSerializer, AdDetailSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_list(client):
    ad_list = AdFactory.create_batch(4)
    response = client.get("/ad/")
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {"count": 4,
                             "next": None,
                             "previous": None,
                             "results": AdListSerializer(ad_list, many=True).data}


@pytest.mark.django_db
def test_ad_retrieve(client):
    ad = AdFactory.create()
    response = client.get(f"/ad/{ad.pk}/")
    assert response.status_code == status.HTTP_200_OK
    assert response.data == AdDetailSerializer(ad).data
