# Standard Library
from typing import Iterable, Tuple

# Third Party
from github.Issue import Issue
from github.PaginatedList import PaginatedList
from github.Repository import Repository

from .comments import summarise_comments
from .constants import MAINTAINERS
from .schema import CommentRecord, IssueRecord


def get_issues(r: Repository) -> Tuple[Iterable[IssueRecord], Iterable[IssueRecord]]:
    """Fetched trimmed datastructure of Issues."""
    open_issues = process_issues(r.get_issues(state="open"))
    closed_issues = process_issues(r.get_issues(state="closed"))
    return (open_issues, closed_issues)


def process_issues(issues: PaginatedList) -> Iterable[IssueRecord]:
    """Process the Issues into a generator stream of dataclass IssueRecords."""
    for i in issues:
        yield process_issue(i)


def process_issue(issue: Issue) -> IssueRecord:
    """Convert Issue into dataclass IssueRecord."""
    comments = [
        CommentRecord(
            id=c.id,
            url=c.html_url,
            user=c.user.login,
            created_at=c.created_at,
            updated_at=c.updated_at,
            is_maintainer=c.user.login in MAINTAINERS,
        )
        for c in issue.get_comments()
    ]

    summary = summarise_comments(comments)

    distinct_reactions = len(set((r.user.login for r in issue.get_reactions())))

    return IssueRecord(
        number=issue.number,
        state=issue.state,
        user=issue.user.login,
        is_maintainer=issue.user.login in MAINTAINERS,
        created_at=issue.created_at,
        updated_at=issue.updated_at,
        closed_at=issue.closed_at,
        url=issue.html_url,
        milestone=issue.milestone.title if issue.milestone else None,
        assignees=[a.login for a in issue.assignees],
        labels=[label.name for label in issue.get_labels()],
        reactions_count=distinct_reactions,
        comment_count=issue.comments,
        first_commented_at=summary.created,
        last_comment_updated_at=summary.last_updated,
        maintainer_first_commented_at=summary.maintainer_first_commented_at,
        maintainer_commented=summary.maintainer_commented,
        maintainer_last_commentor=summary.maintainer_last_commentor,
    )
