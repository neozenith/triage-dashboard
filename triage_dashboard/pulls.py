# Standard Library
from typing import Iterable, Tuple

# Third Party
from github.PaginatedList import PaginatedList
from github.PullRequest import PullRequest
from github.Repository import Repository
from rich import print

from .comments import summarise_comments
from .constants import MAINTAINERS
from .schema import CommentRecord, PullRequestRecord


def get_pulls(r: Repository) -> Tuple[Iterable[PullRequestRecord], Iterable[PullRequestRecord]]:
    """Get all iterable generators for Open and Closed Pulls."""
    open_pulls = process_pulls(r.get_pulls(state="open"))
    closed_pulls = process_pulls(r.get_pulls(state="closed"))
    return (open_pulls, closed_pulls)


def process_pulls(pulls: PaginatedList) -> Iterable[PullRequestRecord]:
    """Create a processing generator for PullRequests."""
    for pr in pulls:
        yield process_pull(pr)


def process_pull(pr: PullRequest) -> PullRequestRecord:
    """Process a single PullRequest into a PullRequestRecord for analytics purposes."""
    comments = []
    reactions = set()
    print(pr.url)

    for c in pr.get_comments():
        reactions.update(set((r.user.login for r in c.get_reactions())))

    comments = [
        CommentRecord(
            id=c.id,
            url=c.html_url,
            user=c.user.login,
            created_at=c.created_at,
            updated_at=c.updated_at,
            is_maintainer=c.user.login in MAINTAINERS,
        )
        for c in pr.get_comments()
    ]

    print("Comments:", comments)
    summary = summarise_comments(comments)

    distinct_reactions = len(reactions)

    return PullRequestRecord(
        number=pr.number,
        state=pr.state,
        user=pr.user.login,
        is_maintainer=pr.user.login in MAINTAINERS,
        created_at=pr.created_at,
        updated_at=pr.updated_at,
        merged_at=pr.merged_at,
        closed_at=pr.closed_at,
        url=pr.html_url,
        milestone=pr.milestone.title if pr.milestone else None,
        assignees=[a.login for a in pr.assignees],
        labels=[label.name for label in pr.get_labels()],
        reactions_count=distinct_reactions,
        comment_count=pr.comments,
        first_commented_at=summary.created,
        last_comment_updated_at=summary.last_updated,
        maintainer_first_commented_at=summary.maintainer_first_commented_at,
        maintainer_commented=summary.maintainer_commented,
        maintainer_last_commentor=summary.maintainer_last_commentor,
    )
