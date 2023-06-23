# Data Types

comment (implements votable | created)
type	name	description
String	approved_by	who approved this comment. null if nobody or you are not a mod
String	author	the account name of the poster
String	author_flair_css_class	the CSS class of the author's flair. subreddit specific
String	author_flair_text	the text of the author's flair. subreddit specific
String	banned_by	who removed this comment. null if nobody or you are not a mod
String	body	the raw text. this is the unformatted text which includes the raw markup characters such as ** for bold. <, >, and & are escaped.
String	body_html	the formatted HTML text as displayed on reddit. For example, text that is emphasised by * will now have <em> tags wrapping it. Additionally, bullets and numbered lists will now be in HTML list format. NOTE: The HTML string will be escaped. You must unescape to get the raw HTML.
special	edited	false if not edited, edit date in UTC epoch-seconds otherwise. NOTE: for some old edited comments on reddit.com, this will be set to true instead of edit date.
int	gilded	the number of times this comment received reddit gold
boolean	likes	how the logged-in user has voted on the comment - True = upvoted, False = downvoted, null = no vote
String	link_author	present if the comment is being displayed outside its thread (user pages, /r/subreddit/comments/.json, etc.). Contains the author of the parent link
String	link_id	ID of the link this comment is in
String	link_title	present if the comment is being displayed outside its thread (user pages, /r/subreddit/comments/.json, etc.). Contains the title of the parent link
String	link_url	present if the comment is being displayed outside its thread (user pages, /r/subreddit/comments/.json, etc.). Contains the URL of the parent link
int	num_reports	how many times this comment has been reported, null if not a mod
String	parent_id	ID of the thing this comment is a reply to, either the link or a comment in it
List<thing>	replies	A list of replies to this comment
boolean	saved	true if this post is saved by the logged in user
int	score	the net-score of the comment
boolean	score_hidden	Whether the comment's score is currently hidden.
String	subreddit	subreddit of thing excluding the /r/ prefix. "pics"
String	subreddit_id	the id of the subreddit in which the thing is located
String	distinguished	to allow determining whether they have been distinguished by moderators/admins. null = not distinguished. moderator = the green [M]. admin = the red [A]. special = various other special distinguishes http://redd.it/19ak1b