# Standard Library
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class CommentSummary:
    """Summarised key metrics from a series of CommentRecords."""

    created: Optional[datetime] = None
    last_updated: Optional[datetime] = None
    maintainer_first_commented_at: Optional[datetime] = None
    maintainer_commented: bool = False
    maintainer_last_commentor: bool = False


@dataclass
class CommentRecord:
    """Minimal representation of Comment for analytics purposes."""

    id: int
    url: str
    user: str
    created_at: datetime
    updated_at: datetime
    is_maintainer: bool = False


@dataclass
class IssueRecord:
    """Minimal representation of an Issue for analytics purposes."""

    number: int
    state: str
    user: str
    is_maintainer: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    closed_at: Optional[datetime]
    url: str
    milestone: Optional[str]
    assignees: list[str]
    labels: list[str]
    reactions_count: int
    comment_count: int
    first_commented_at: Optional[datetime] = None
    last_comment_updated_at: Optional[datetime] = None
    maintainer_first_commented_at: Optional[datetime] = None
    maintainer_commented: bool = False
    maintainer_last_commentor: bool = False


@dataclass
class PullRequestRecord:
    """Minimal representation of a Pull Reuqest for analytics purposes."""

    number: int
    state: str
    user: str
    is_maintainer: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    merged_at: Optional[datetime]
    closed_at: Optional[datetime]
    url: str
    milestone: Optional[str]
    assignees: list[str]
    labels: list[str]
    reactions_count: int
    comment_count: int
    first_commented_at: Optional[datetime] = None
    last_comment_updated_at: Optional[datetime] = None
    maintainer_first_commented_at: Optional[datetime] = None
    maintainer_commented: bool = False
    maintainer_last_commentor: bool = False
