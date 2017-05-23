from django.test import TestCase
from .models import PromiseModel

class PromiseModelTestCase(TestCase):

    def setUp(self):
        self.promise = "I won't eat non naturally occuring sugars."
        self.promiseList = PromiseModel(promise=self.promise)

    def testCanCreatePromise(self):
        startCount = PromiseModel.objects.count()
        self.promiseList.save()
        endingCount = PromiseModel.objects.count()
        self.assertNotEqual(startCount, endingCount)
