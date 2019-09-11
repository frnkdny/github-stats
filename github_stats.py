import sys
import requests
import os
from datetime import datetime, timedelta

assert os.environ.get('TOKEN')
token = os.environ.get('TOKEN')

assert os.environ.get('GIT_USER')
login = os.environ.get('GIT_USER')

d = {}
url_commits = []
commit_dates = []


def create_dict(num_days_ago):
    for day in range(num_days_ago, -1, -1):
        days_ago = datetime.utcnow() - timedelta(day)
        date_only_days_ago = days_ago
        date_only_days_ago_str = str(date_only_days_ago)[:10]
        d[date_only_days_ago_str] = 0


def count_user_commits(user):
    base_url = "https://api.github.com/"
    r = requests.get(base_url + 'users/%s/repos' % user, auth=(login, token))
    if r.status_code == 200:
        repos = r.json()
        for repo in repos:
            if repo['fork'] is not True:
                url_commits.append(repo['url'] + '/commits')
    else:
        print "[ERROR] GET Response status code: %s" % r.status_code


def get_commits():
    print "[INFO] Successfully found github repos"
    for url_commit in url_commits:
        print url_commit
        nr = requests.get(url_commit)
        if nr.status_code == 200:
            commits = nr.json()
            for commit in commits:
                commit_dates.append(commit['commit']['author']['date'])
            commits_one_per_line = str("\n".join(commit_dates))
        else:
            print "[ERROR] GET Response status code: %s" % nr.status_code
            if nr.status_code == 403:
                print "[INFO] Check for rate-limiting: curl https://api.github.com/rate_limit"
                # https://developer.github.com/v3/#rate-limiting
            sys.exit(1)
    return commits_one_per_line


def update_dict(commits_one_per_line):
    commits = commits_one_per_line.split()
    for commit in commits:
        commit_date_only = commit[:10]
        if commit_date_only in d:
            d[commit_date_only] += 1


def main():
    if len(sys.argv) != 3:
        print "python github_stats.py <github_user> <days_of_history>"
        sys.exit(1)
    github_user = sys.argv[1]
    print "Github username:%s" % github_user
    num_days_ago = int(sys.argv[2])
    print  "Days of history:%s" % num_days_ago

    create_dict(num_days_ago)
    count_user_commits(github_user)
    if len(url_commits) != 0:
        dict_str = get_commits()
        update_dict(dict_str)
        print "[INFO] Dates and Count of github contribution history:"
        for k in sorted(d.keys()):
            if d[k] > 0:
                print k, d[k]
    else:
        print "[INFO] No URLs have public activity."


if __name__ == '__main__':
    main()
