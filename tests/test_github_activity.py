import unittest
from unittest.mock import patch, MagicMock
from github_user_activity import collect_info, fetch_activity
import argparse
import json

class TestGithubUserActivity(unittest.TestCase):

    def test_collect_info_basic(self):
        raw_activity = [
            {"type": "PushEvent", "repo": {"name": "repo1"}},
            {"type": "PushEvent", "repo": {"name": "repo1"}},
            {"type": "WatchEvent", "repo": {"name": "repo2"}}
        ]
        result = collect_info(raw_activity)
        self.assertIn("Pushed 2 commits in repo1", result)
        self.assertIn("Starred repo2", result)
        self.assertEqual(len(result), 2)

    def test_collect_info_missing_fields(self):
        raw_activity = [
            {"type": "PushEvent"},
            {"repo": {"name": "repo1"}},
            {}
        ]
        result = collect_info(raw_activity)
        self.assertEqual(result, [])

    @patch("github_user_activity.urlopen")
    def test_fetch_activity_success(self, mock_urlopen):
        fake_data = json.dumps([
            {"type": "PushEvent", "repo": {"name": "repo1"}},
            {"type": "WatchEvent", "repo": {"name": "repo2"}}
        ]).encode('utf-8')

        mock_response = MagicMock()
        mock_response.read.return_value = fake_data
        mock_urlopen.return_value.__enter__.return_value = mock_response

        parser = argparse.ArgumentParser()
        parser.add_argument("username")
        args = parser.parse_args(["dummyuser"])

        success = fetch_activity(args)
        self.assertIsNone(success)  # because function only prints, doesn't return anything

    @patch("github_user_activity.urlopen", side_effect=Exception("User not found"))
    def test_fetch_activity_fail(self, mock_urlopen):
        parser = argparse.ArgumentParser()
        parser.add_argument("username")
        args = parser.parse_args(["nouser"])

        result = fetch_activity(args)
        self.assertFalse(result)
