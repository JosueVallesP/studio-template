# PreToolUse hook on every connector tool (mcp__*). Anything that sends, posts, books or changes
# something in public in the person's name asks first: the app shows its own approval prompt, so the
# person's yes is a click in the app, never a line Claude says it heard. Reading passes untouched.
# skills/setup-sources ("Publishing") holds the rule in words; this makes it hold on a bad run too.
#
# A connector is named by the person when they add it, and new ones appear all the time, so the match
# is on what the tool does (its action words) and on platform words anywhere in its name, never on a
# short list of vendors: a guard is only as tight as its least-guarded way out.
import json, re, sys
try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(0)
name = str(d.get("tool_name") or "")
low = name.lower()
if not low.startswith("mcp__"):
    sys.exit(0)
tool = low.rsplit("__", 1)[-1]
server = low[5:].rsplit("__", 1)[0] if "__" in low[5:] else ""

def ask(why):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "ask",
        "permissionDecisionReason": why + " Show the person exactly what goes out, where and when, and go ahead "
            "only on their yes for this one (skills/setup-sources, Publishing)."}}))
    sys.exit(0)

# A tool named for reading (get_post_stats, list_scheduled_posts, search_threads) passes.
if re.match(r"(get|list|read|search|fetch|find|show|query|count|describe|view|check|discover|whoami|download)([_\-]|$)", tool):
    sys.exit(0)

# 1. Anywhere: a tool whose name says it sends or publishes.
if re.search(r"(^|[_\-])(publish|send|tweet|repost|retweet|broadcast)([_\-]|s?$)|send[_\-]?(message|email|mail|later)|(create|schedule)[_\-](post|tweet|thread|story|reel|scheduled)", tool):
    ask("This sends or publishes something in the person's name.")

# 2. Automations that run on their own and may post (Make, Zapier, n8n and the like).
if re.search(r"make|zapier|n8n|pipedream|ifttt", server) and re.search(r"(^|[_\-])(run|trigger|activate|execute|replay)", tool):
    ask("This runs an automation that may post or send something in the person's name.")

# 3. Posting and email tools: any write. Email drafts stay drafts, so they pass.
POSTING = r"blotato|metricool|authoredup|buffer|typefully|hypefury|taplio|hootsuite|publer|later|linkedin|twitter|threads|bluesky|instagram|facebook|tiktok|youtube|pinterest|substack|beehiiv|convertkit|kit|mailchimp|ghost|medium|wordpress|webflow|framer|gmail|outlook|sendgrid|resend|postmark"
WRITE = r"(^|[_\-])(create|schedule|reschedule|post|update|edit|delete|remove|cancel|upload|queue|add|move|set|reply|comment|share|like|follow|connect|invite|draft)"
ON_POSTING = re.search(r"(^|[_\-])(" + POSTING + r")($|[_\-])", server)
if ON_POSTING and re.search(WRITE, tool):
    if re.search(r"gmail|outlook|sendgrid|resend|postmark", server) and re.search(r"draft|label|trash|spam|archive", tool):
        sys.exit(0)
    ask("This changes something on a platform where the person posts or sends.")

# 4. Website, blog and campaign tools inside bigger connectors (HubSpot's blog, pages and campaigns).
if re.search(r"hubspot|wordpress|webflow|ghost|framer", server) and re.search(r"blog|landing|website|page|campaign|social|email", tool) and re.search(r"(^|[_\-])(manage|create|update|publish|delete|schedule)", tool):
    ask("This can change a public page, a blog post or a campaign in the person's name.")
sys.exit(0)
