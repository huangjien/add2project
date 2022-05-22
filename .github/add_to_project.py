import os
from github import Github

github = Github(os.getenv('GITHUB_TOKEN'))
context = os.getenv('GITHUB_CONTEXT')
repo = context.get('repository')
project = [p for p in repo.get_projects() if p.name == os.getenv('PROJECT_NAME')][0]
column = [c for c in project.get_columns() if c.name == os.getenv('COLUMN_NAME')][0]

id = 0
type = "Issue"
if context.get('event').contains('pull_request'):
    type = "PullRequest"
    id = context.get('event').get('pull_request').get('id')
else:
    id = context.get('event').get('issue').get('id')
column.create_card(content_id = id, content_type = type)

