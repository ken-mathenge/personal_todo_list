from fabric.api import local


def deploy():
    local('python setup.py sdist bdist_wheel')
    local('twine upload dist/*')
    local('rm dist/*')
