import getpass
from fabric import api
from fabric.contrib.console import confirm
import subprocess


class Site(object):

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def run(self, cmd):
        with api.cd(self.dir):
            api.sudo(cmd, user=self.user_id)

    def deploy(self):
        self.git_pull()
        self.update_packages()
        self.run('venv/bin/python manage.py migrate')
        self.run('venv/bin/python manage.py collectstatic --noinput')
        self.restart()

    def git_pull(self):
        self.run("find . -name '*.pyc' -delete")
        self.run("git fetch origin && git reset --hard origin/master")

    def git_tag(self):
        self.run(
            "git tag | sort -g | tail -n 1 | sed s/$/+1/ | bc | xargs git tag")
        self.run("git push --tags && git push")

    def update_packages(self):
        self.run("./venv/bin/pip install -r requirements.txt")

    def restart(self):
        self.run("touch reload")

PROD = Site(
    dir='/home/ideavote-web/ideavote.co/',
    user_id='ideavote-web'
)

api.env.hosts = ['ideavote.co']


@api.task
def deploy():
    """
    """
    # mac-only command, just for fun
    try:
        subprocess.call(['say', '"Ship! Ship! Ship!"'])
    except:
        pass
    print "ship! ship! ship!"

    api.env.user = api.prompt(
        "Username on prod server:", default=getpass.getuser())

    should_tag = tag()

    PROD.deploy()

    if should_tag:
        PROD.git_tag()


@api.task
def restart():
    PROD.restart()


def tag():
    if not confirm("Give new tag for this deployment?"):
        if confirm("Are you sure?", default=False):
            return False
        else:
            tag()
    else:
        return True
