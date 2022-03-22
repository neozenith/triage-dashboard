# Standard Library
import os
import sys
from itertools import islice

# Third Party
from dotenv import load_dotenv
from github import Github
from rich import print

from .issues import get_issues
from .pulls import get_pulls


def main(repo_slug, access_token=None):
    """Main entry point to the program."""
    g = Github(access_token)
    r = g.get_repo(repo_slug)
    N = 1

    open_issues, closed_issues = get_issues(r)

    for issue in islice(open_issues, 0, N):
        print(issue)

    for issue in islice(closed_issues, 0, N):
        print(issue)

    open_pulls, closed_pulls = get_pulls(r)
    for pull in islice(open_pulls, 0, N):
        print(pull)
    #
    #  for pull in islice(closed_pulls, 0, N):
    #      print(pull)


if __name__ == "__main__":
    args = sys.argv

    load_dotenv()
    access_token = os.environ.get("GH_ACCESS_TOKEN", None)
    main(repo_slug=args[1], access_token=access_token)
