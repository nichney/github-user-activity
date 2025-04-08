class Handler:

    def handle_watch(self, subdict):
        return [f"Starred {repo}" for repo, times in subdict.items() if times >= 1]

    def handle_push(self, subdict):
        result = []
        for repo, times in subdict.items():
            if times == 1:
                result.append(f"Pushed commit in {repo}")
            else:
                result.append(f"Pushed {times} commits in {repo}")
        return result

    def handle_commit_comment(self, subdict):
        return [
            f"Commented commit in repo {repo}"
            for repo, times in subdict.items()
            if times >= 1
        ]

    def handle_create(self, subdict):
        return [
            f"Created branch, tag or repo in {repo}"
            for repo, times in subdict.items()
            if times >= 1
        ]

    def handle_delete(self, subdict):
        return [
            f"Deleted branch or tag in {repo}"
            for repo, times in subdict.items()
            if times >= 1
        ]

    def handle_fork(self, subdict):
        return [f"Forked {repo}" for repo, times in subdict.items() if times >= 1]

    def handle_gollum(self, subdict):
        return [
            f"Created or updated wiki page for {repo}"
            for repo, times in subdict.items()
            if times >= 1
        ]

    def handle_issue_comment(self, subdict):
        return [
            f"Performed something with comment issue in {repo}"
            for repo, times in subdict.items()
            if times >= 1
        ]

    def handle_issue(self, subdict):
        return [
            f"Done something with issue in {repo}"
            for repo, times in subdict.items()
            if times >= 1
        ]

    def handle_member(self, subdict):
        return [
            f"Collaborate with {repo}" for repo, times in subdict.items() if times >= 1
        ]

    def handle_public(self, subdict):
        return [f"Made {repo} public" for repo, times in subdict.items() if times >= 1]

    def handle_pull_request(self, subdict):
        return [
            f"Performed an action with pull request in {repo}"
            for repo, times in subdict.items()
            if times >= 1
        ]

    def handle_pull_request_review(self, subdict):
        return [
            f"Created pull request review in {repo}"
            for repo, times in subdict.items()
            if times >= 1
        ]

    def handle_pull_request_review_comment(self, subdict):
        return [
            f"Commented pull request review in {repo}"
            for repo, times in subdict.items()
            if times >= 1
        ]

    def handle_pull_request_review_thread(self, subdict):
        return [
            f"Performed something with pull request thread in {repo}"
            for repo, times in subdict.items()
            if times >= 1
        ]

    def handle_release(self, subdict):
        return [
            f"Released something in {repo}"
            for repo, times in subdict.items()
            if times >= 1
        ]

    def handle_sponsor(self, subdict):
        return [
            f"Became a sponsor of {repo}"
            for repo, times in subdict.items()
            if times >= 1
        ]

    @property
    def handler_map(self):
        return {
            "WatchEvent": self.handle_watch,
            "CommitCommentEvent": self.handle_commit_comment,
            "CreateEvent": self.handle_create,
            "DeleteEvent": self.handle_delete,
            "ForkEvent": self.handle_fork,
            "GollumEvent": self.handle_gollum,
            "IssueCommentEvent": self.handle_issue_comment,
            "IssuesEvent": self.handle_issue,
            "MemberEvent": self.handle_member,
            "PublicEvent": self.handle_public,
            "PullRequestEvent": self.handle_pull_request,
            "PullRequestReviewEvent": self.handle_pull_request_review,
            "PullRequestReviewCommentEvent": self.handle_pull_request_review_comment,
            "PullRequestReviewThreadEvent": self.handle_pull_request_review_thread,
            "PushEvent": self.handle_push,
            "ReleaseEvent": self.handle_release,
            "SponsorshipEvent": self.handle_sponsor,
        }
