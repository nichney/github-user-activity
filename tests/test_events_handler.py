import unittest
import github_user_activity


class TestHandler(unittest.TestCase):

    def setUp(self):
        self.handler = github_user_activity.event_handler.Handler()

    def test_handle_watch(self):
        self.assertEqual(
            self.handler.handle_watch({'repo1': 1, 'repo2': 0}),
            ["Starred repo1"]
        )

    def test_handle_push(self):
        self.assertEqual(
            self.handler.handle_push({'repo1': 1, 'repo2': 3}),
            ["Pushed commit in repo1", "Pushed 3 commits in repo2"]
        )

    def test_handle_commit_comment(self):
        self.assertEqual(
            self.handler.handle_commit_comment({'repo1': 2, 'repo2': 0}),
            ["Commented commit in repo repo1"]
        )

    def test_handle_create(self):
        self.assertEqual(
            self.handler.handle_create({'repo1': 1}),
            ["Created branch, tag or repo in repo1"]
        )

    def test_handle_delete(self):
        self.assertEqual(
            self.handler.handle_delete({'repo1': 1}),
            ["Deleted branch or tag in repo1"]
        )

    def test_handle_fork(self):
        self.assertEqual(
            self.handler.handle_fork({'repo1': 1}),
            ["Forked repo1"]
        )

    def test_handle_gollum(self):
        self.assertEqual(
            self.handler.handle_gollum({'repo1': 1}),
            ["Created or updated wiki page for repo1"]
        )

    def test_handle_issue_comment(self):
        self.assertEqual(
            self.handler.handle_issue_comment({'repo1': 1}),
            ["Performed something with comment issue in repo1"]
        )

    def test_handle_issue(self):
        self.assertEqual(
            self.handler.handle_issue({'repo1': 1}),
            ["Done something with issue in repo1"]
        )

    def test_handle_member(self):
        self.assertEqual(
            self.handler.handle_member({'repo1': 1}),
            ["Collaborate with repo1"]
        )

    def test_handle_public(self):
        self.assertEqual(
            self.handler.handle_public({'repo1': 1}),
            ["Made repo1 public"]
        )

    def test_handle_pull_request(self):
        self.assertEqual(
            self.handler.handle_pull_request({'repo1': 1}),
            ["Performed an action with pull request in repo1"]
        )

    def test_handle_pull_request_review(self):
        self.assertEqual(
            self.handler.handle_pull_request_review({'repo1': 1}),
            ["Created pull request review in repo1"]
        )

    def test_handle_pull_request_review_comment(self):
        self.assertEqual(
            self.handler.handle_pull_request_review_comment({'repo1': 1}),
            ["Commented pull request review in repo1"]
        )

    def test_handle_pull_request_review_thread(self):
        self.assertEqual(
            self.handler.handle_pull_request_review_thread({'repo1': 1}),
            ["Performed something with pull request thread in repo1"]
        )

    def test_handle_release(self):
        self.assertEqual(
            self.handler.handle_release({'repo1': 1}),
            ["Released something in repo1"]
        )

    def test_handle_sponsor(self):
        self.assertEqual(
            self.handler.handle_sponsor({'repo1': 1}),
            ["Became a sponsor of repo1"]
        )

    def test_handler_map_keys(self):
        expected_keys = {
            "WatchEvent", "CommitCommentEvent", "CreateEvent", "DeleteEvent",
            "ForkEvent", "GollumEvent", "IssueCommentEvent", "IssuesEvent",
            "MemberEvent", "PublicEvent", "PullRequestEvent",
            "PullRequestReviewEvent", "PullRequestReviewCommentEvent",
            "PullRequestReviewThreadEvent", "PushEvent",
            "ReleaseEvent", "SponsorshipEvent"
        }
        self.assertEqual(set(self.handler.handler_map.keys()), expected_keys)

