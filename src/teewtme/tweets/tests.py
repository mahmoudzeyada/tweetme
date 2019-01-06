from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Tweet
User=get_user_model()

class TweetModelTest(TestCase):
    def setUp(self):
        random_user=User.objects.create(username="dnjldflkdfjlkfdjlk")
    def test_tweet_item(self):
        obj = Tweet.objects.create(
        user=User.objects.first(),
        content="jlfefr"
        )
        self.assertTrue(obj.content=="jlfefr")
    def test_tweet_url(self):
        obj=Tweet.objects.create(
        user=User.objects.first(),
        content="f;dkrk"
        )
        absolute_url= reverse("tweets:details",kwargs={"pk":obj.id})
        self.assertEqual(obj.get_absolute_url(),absolute_url)
