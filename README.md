# Add New Issue/Pull Request to Project

![GitHub license](https://img.shields.io/github/license/huangjien/add2project.svg)
![Latest Version](https://img.shields.io/github/v/release/huangjien/add2project?color=orange&label=latest%20release)

In GitHub, you can add new issues and pull requests to your project.

But they will not automatically appear in your project. This action will add the issue/pull request to your project.

## Prerequisites:
1. You must have a Github Personal Access Token.
2. You must have a project in your GitHub account.
3. You must have at least on column in your project.

## How to use this action:

```
name: Add New Issue/Pull Request to Project
on:
  issues:
    types: [opened]
  pull_requests:
    types: [opened]
env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    GITHUB_CONTEXT: ${{ github }}
    PROJECT_NAME: <project name>
    COLUMN_NAME: <column name>
    EVENT_TYPE: Issue|PullRequest
    
jobs:
  add_2_project:
    runs-on: ubuntu-latest
    steps:
        - name : checkout repo content
          uses: actions/checkout@v2
        - name: setup ptyhon
          uses: actions/setup-python@v2
          with:
            python: "3.8"
        - name: execute python script
          run: |
            python -m pip install pyGIthub
            pythn ./.github/add_to_project.py
```


## FAQ:


## License:
[LICENSE : MIT]: # ( ./LICENSE )