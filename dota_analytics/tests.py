from unittest import mock


# Create your tests here.
from dota_analytics.models import TrainData


class FetchParseDataTest:
    def mocked_trainData(args):
        return "Hey"

    @mock.patch(TrainData.objects.all().values()[:1], side_effect=mocked_trainData)
    def deparseTrainDataTest(self):
        x = TrainData.objects.all().values()[:1]
        print(x)
