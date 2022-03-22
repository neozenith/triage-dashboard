# Triage Dashboard

Given a github slug, eg `neozenith/triage-dashboard`, scrape the Github API for activity on all issues and pull requests to determine metrics around the current state and progress of inbound requests.

The goal is to focus on the work that has the best ROI for _cognitive bandwidth_ and _volunteer time_ investment.

It should produce a Plotly Dash dashboard with a table of links to exact issues/PRs to drill into.

## Getting Started

Work in Progress...

For my own purposes:
```
poetry install
poetry shell
invoke --list

Available tasks:

  all         Outer development loop.
  format      Autoformat code for code style.
  lint        Linting and style checking.
  main        Inner loop for fast dev feedback.
  test        Run test suite.
  typecheck   Run typechecking tooling.

Default task: main
```

## Concept

Figure out historically what "humming along" looked like. And what signs appeared when slowing down.

Also look at what is "normal variability" in interactions.

Get a better mental model for triage and response times and turn around through data.

## TODO

 - Finish collecting data structures
 - Looks like PRs do not expose reactions in the root comment via API
 - Looks like PyGithub is not consistent in fetching Comments on PRs, will have to resort to raw API calls
 - Work on Data vis
    - Need to think about what metrics are important
    - Monthly open rates
    - Monthly close rates
      - Close rates by staleness
    - Time-triage (time until first maintainer comment)
    - Rank by emoji reaction upvotes
    - Rank by time since last comment
    - Filter by "whose court the ball is in", eg unlabelled, unassigned, no milestone, pending tests label, requires documentation label, is a maintainer the last to have comment, is it stale?
 - Figure out how to do Change Data Capture instead of full history fetch
 - Is there a way to fetch from the API via date range?



## Resources

 - https://docs.github.com/en/rest/guides/getting-started-with-the-rest-api
 - https://pygithub.readthedocs.io/en/latest/introduction.html
 - https://dash.plotly.com/installation
