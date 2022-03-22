# Third Party
from invoke import task
from invoke_common_tasks import format, lint, test, typecheck  # noqa


@task(default=True)
def main(c):
    """Inner loop for fast dev feedback."""
    c.run("python3 -m triage_dashboard 'pyinvoke/invoke'")


@task(pre=[format, lint, typecheck, main])
def all(c):
    """Outer development loop."""
    ...
