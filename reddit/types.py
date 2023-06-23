from dataclasses import dataclass

SubredditName = str


@dataclass()
class RedditDataTable:
    """Data class for Reddit data table"""

    author: str
    is_original_content: bool
    type: str
    num_comments: int
    score: float
    # subreddit_name: str
    subreddit_id: str
    title: str
    ups: int
    upvote_ratio: float
    body: str
    down: int
    likes: int


@dataclass()
class Comment:
    author: str = ""
    type: str = "comment"
    body: str = ""
    down: int = 0
    likes: int = 0
    # subreddit_name: SubredditName = ""
    subreddit_name_prefixed: str = ""
    subreddit_id: str = ""
    contraversiality: float = 0.0
    ups: int = 0
    author_flair_type: str = ""


# All Comment fields:
# 'STR_FIELD'
# 'mark_unread'
# 'no_follow'
# 'downvote'
# 'award'
# 'mod_note'
# 'edit'
# 'total_awards_received'
# 'author_flair_type'
# 'uncollapse'
# 'controversiality'
# 'collapsed_reason_code'
# 'can_gild'
# 'awarders'
# 'locked'
# 'unblock_subreddit'


@dataclass()
class Submission:
    author: str = ""
    is_original_content: bool = False
    num_comments: int = 0
    score: float = 0.0
    subreddit_name: SubredditName = ""
    subreddit_name_prefixed: str = ""
    type: str = "submission"
    subreddit_id: str = ""
    title: str = ""
    ups: int = 0
    upvote_ratio: float = 0.0
    view_count: int = 0
    created: int = 0
    id: str = ""
    likes: str = ""


# All Submission fields:
# all_awardings
# allow_live_comments
# approved_at_utc
# approved_by
# archived
# author
# author_flair_background_color
# author_flair_css_class
# author_flair_richtext
# author_flair_template_id
# author_flair_text
# author_flair_text_color
# author_flair_type
# author_fullname
# author_is_blocked
# author_patreon_flair
# author_premium
# award
# awarders
# banned_at_utc
# banned_by
# can_gild
# can_mod_post
# category
# clear_vote
# clicked
# comment_limit
# comment_sort
# comments
# content_categories
# contest_mode
# created
# created_utc
# crosspost
# delete
# disable_inbox_replies
# discussion_type
# distinguished
# domain
# downs
# downvote
# duplicates
# edit
# edited
# enable_inbox_replies
# flair
# fullname
# gallery_data
# gild
# gilded
# gildings
# hidden
# hide
# hide_score
# id
# id_from_url
# is_created_from_ads_ui
# is_crosspostable
# is_gallery
# is_meta
# is_original_content
# is_reddit_media_domain
# is_robot_indexable
# is_self
# is_video
# likes
# link_flair_background_color
# link_flair_css_class
# link_flair_richtext
# link_flair_template_id
# link_flair_text
# link_flair_text_color
# link_flair_type
# locked
# mark_visited
# media
# media_embed
# media_metadata
# media_only
# mod
# mod_note
# mod_reason_by
# mod_reason_title
# mod_reports
# name
# no_follow
# num_comments
# num_crossposts
# num_reports
# over_18
# parent_whitelist_status
# parse
# permalink
# pinned
# poll_data
# post_hint
# preview
# pwls
# quarantine
# removal_reason
# removed_by
# removed_by_category
# reply
# report
# report_reasons
# save
# saved
# score
# secure_media
# secure_media_embed
# selftext
# selftext_html
# send_replies
# shortlink
# spoiler
# stickied
# subreddit
# subreddit_id
# subreddit_name_prefixed
# subreddit_subscribers
# subreddit_type
# suggested_sort
# thumbnail
# thumbnail_height
# thumbnail_width
# title
# top_awarded_type
# total_awards_received
# treatment_tags
# unhide
# unsave
# ups
# upvote
# upvote_ratio
# url
# url_overridden_by_dest
# user_reports
# view_count
# visited
# whitelist_status
# wls
