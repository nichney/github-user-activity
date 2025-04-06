class Handler:
    
    def handle_watch(self, subdict):
        return [f"Starred {repo}" for repo, times in subdict.items() if times >=1]

    def handle_push(self, subdict):
        result = []
        for repo, times in subdict.items():
            if times == 1:
                result.append(f"Pushed commit in {repo}")
            else:
                result.append(f"Pushed {times} commits in {repo}")
        return result

    def handle_commit_comment(self, subdict):
        return [f"Commented commit in repo {repo}" for repo, times in subdict.items() if times >= 1]

    def handle_create(self, subdict):
        return [f"Created branch, tag or repo in {repo}" for repo, times in subdict.items() if times >= 1]

    def handle_delete(self, subdict):
        return []

    def handle_fork(self, subdict):
        return []

    def handle_gollum(self, subdict):
        return []

    def handle_issue_comment(self, subdict):
        return []

    def handle_issue(self, subdict):
        return []

    def handle_member(self, subdict):
        return []

    def handle_public(self, subdict):
        return []

    def handle_pull_request(self, subdict):
        return []

    def handle_pull_request_review(self, subdict):
        return []

    def handle_pull_request_review_comment(self, subdict):
        return []

    def handle_pull_request_review_thread(self, subdict):
        return []

    def handle_release(self, subdict):
        return []

    def handle_sponsor(self, subdict):
        return []

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
         "IssueEvent": self.handle_issue,
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
