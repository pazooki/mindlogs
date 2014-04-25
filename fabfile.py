"""
Usage:
    - fab remote-env start
    - fab remote-env stop
    - fab remote-env update
    - fab remote-env restart
"""
from fabric.api import *
from git import Repo

try:
    from config import secrets
except ImportError:
    from config import secrets_test as secrets

import os

env.abs_path = os.getcwd()
env.project = os.path.basename(env.abs_path)
env.user = secrets.USER
env.git_url = secrets.GIT_URL
env.repo = Repo(env.abs_path)
env.active_branch = env.repo.active_branch
env.python_exec = '/usr/bin/python2.7'
ENVS = {
    'dev': {
        'branch_name': 'dev',
        'venv': '%s_dev' % env.project,
        'path': '/srv/%s_dev/' % env.project,
        'hosts': 'mindlogs.org',
    },
    'master': {
        'branch_name': 'master',
        'venv': '%s_master' % env.project,
        'path': '/srv/%s_master/' % env.project,
        'hosts': secrets.ALLOWED_HOSTS,
    }
}

current_env = ENVS.get(env.active_branch)
denv = dict(env)
denv.update(current_env)

logs = {
    'uwsgi': '/var/log/uwsgi/%(project)s_%(branch_name)s.log' % denv,
    'nginx_access': 'access_%(project)s_%(branch_name)s.log' % denv,
    'nginx_error': 'error_%(project)s_%(branch_name)s.log' % denv
}


def init():
    with shell_env(VIRTUALENVWRAPPER_PYTHON=denv.get('python_exec')):
        run('mkvirtualenv -p %(python_exec)s %(venv)s' % denv)
    sudo('mkdir %(path)s' % denv)
    sudo('sudo chown mindlogger:mindlogger %(path)s' % denv)
    run('git clone %(git_url)s -b %(branch_name)s %(path)s' % denv)
    put('config/secrets.py', '%(path)s/config/secrets.py' % denv, use_sudo=False)
    setup()
    db_up()


def nuke():
    run('rmvirtualenv %(venv)s' % denv)
    sudo('rm -rf %(path)s' % denv)


def setup():
    with cd(current_env.get('path')):
        vrun('pip install -r requirements.txt')


def db_up():
    with cd(current_env.get('path')):
        vrun('python manage.py syncdb')
        vrun('python manage.py migrate')
        vrun('python manage.py collectstatic --noinput')


def vrun(cmd):
    run('$WORKON_HOME/%(venv)s/bin/%(cmd)s' % {'venv': current_env.get('venv'), 'cmd': cmd})


def update():
    stop()
    with cd(denv.get('path')):
        run('git pull')
        setup()
    start()


def stop():
    sudo('sudo service nginx stop')
    sudo('pgrep uwsgi | xargs sudo kill -9')


def start():
    sudo('sudo service nginx start')
    sudo('/usr/bin/uwsgi --emperor /etc/uwsgi/vassals --uid %(user)s --gid %(user)s > %(uwsgi_log)s 2>&1 &' % {
        'user': denv.get('user'),
        'uwsgi_log': logs.get('uwsgi'),
    })


def restart():
    stop()
    start()


def ssh():
    local("""ssh %(user)s@%(hosts)s""" % denv)