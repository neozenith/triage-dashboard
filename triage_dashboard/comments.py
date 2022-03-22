# Standard Library
from datetime import datetime
from typing import Optional

from .schema import CommentRecord, CommentSummary


def summarise_comments(comments: list[CommentRecord]) -> CommentSummary:
    """Summarise key elements from the series of comments."""
    created: Optional[datetime] = None
    last_updated: Optional[datetime] = None
    maintainer_first_commented_at: Optional[datetime] = None
    maintainer_commented: bool = False
    maintainer_last_commentor: bool = False

    total_comments = len(comments)

    for i, comment in enumerate(comments):
        # First comment
        if i == 0:
            created = comment.created_at

        # Last comment
        if i == total_comments - 1:
            maintainer_last_commentor = comment.is_maintainer
            last_updated = comment.updated_at

        # First maintainer comment
        if not maintainer_commented and comment.is_maintainer:
            maintainer_commented = True
            maintainer_first_commented_at = comment.created_at

    return CommentSummary(
        created, last_updated, maintainer_first_commented_at, maintainer_commented, maintainer_last_commentor
    )
