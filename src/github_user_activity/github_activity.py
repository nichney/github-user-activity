#!/usr/bin/python
# Script is getting github user's activity
# features:

from urllib.request import urlopen
from urllib.error import HTTPError
import argparse
import json
from pprint import pprint
from collections import defaultdict
from typing import Dict

from .event_handler import Handler


def collect_info(raw_activity: list, fil: str = "DefaultEvent") -> list:
    """Collect to hash table by [event_type][which repo]: how namy times"""
    handler = Handler()
    info: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for event in raw_activity:
        event_type = event.get("type")
        repo_name = event.get("repo", {}).get("name")
        if fil != "DefaultEvent" and event_type != fil:
            continue
        if event_type and repo_name:
            info[event_type][repo_name] += 1

    printable_activities = []

    for event, subdict in info.items():
        sub_h = handler.handler_map.get(event)
        printable_activities.extend(sub_h(subdict))
    return printable_activities


def fetch_activity(args) -> bool:
    """Fetch activities by api and print it. Return False if there is an error, True otherwise"""
    if not args.username:
        print("Username required")
        return False
    try:
        with urlopen(f"https://api.github.com/users/{args.username}/events") as r:
            body = r.read()
            activity = json.loads(body)
            del body  # delete unused data

            # collect all info, like count how many times pushed
            if args.filter:
                printable_info = collect_info(activity, args.filter)
            else:
                printable_info = collect_info(activity)

            for i in printable_info:
                print(f"-- {i}")

        return True

    except HTTPError:
        print(f"Error: there is no user named '{args.username}'")
        return False


def main():
    parser = argparse.ArgumentParser(
        prog="github-activity",
        description="CLI script to fetch recent activity of GitHub user",
    )
    parser.add_argument("username")
    parser.add_argument(
        "--filter",
        choices=[event for event in Handler().handler_map.keys()],
        help="filter user's activity by event type",
    )
    parser.set_defaults(func=fetch_activity)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
