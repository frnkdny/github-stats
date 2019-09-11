**Requirements**

[Requires a github token](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line)

Requires the following ENV variables to be set:
```
export TOKEN=<github_token>
export GIT_USER=<github_login>
```

```
$ python --version
Python 2.7.16

$ pip install -r requirements.txt
```

**Usage**

Calculate the commits made on master for the public account activity of a user.
```
$ python github_stats.py
python github_stats.py <github_user> <days_of_history>
```
*Usage Examples*
```
$ python github_stats.py Dogild 1825
Github username:Dogild
Days of history:1825
[INFO] Successfully found github repos
https://api.github.com/repos/Dogild/Cucapp-demo/commits
https://api.github.com/repos/Dogild/Cucapp-demo-app/commits
https://api.github.com/repos/Dogild/Cucapp-demo-features/commits
https://api.github.com/repos/Dogild/dogild.github.io/commits
https://api.github.com/repos/Dogild/gitstats/commits
https://api.github.com/repos/Dogild/lemondeForFree/commits
[INFO] Dates and Count of github contribution history:
2014-09-22 1
2014-10-06 1
2014-10-20 1
2014-11-10 1
2014-12-12 3
2014-12-17 1
2015-01-08 1
2015-01-20 3
2015-01-29 2
2015-01-30 3
2015-01-31 2
2015-02-03 1
2015-02-04 14
2015-07-16 2
2015-08-03 1
2015-08-04 3
2015-08-05 3
2015-08-07 1
2015-09-23 1
2015-11-05 2
2015-11-24 1
2015-12-04 3
```

```
$ python github_stats.py frnkdny 1000
Github username:frnkdny
Days of history:1000
[INFO] Successfully found github repos
https://api.github.com/repos/frnkdny/calico-scripts/commits
[INFO] Dates and Count of github contribution history:
2017-08-23 1
2017-08-24 3
2017-08-25 1
2017-09-16 1
2017-10-27 1
2017-10-30 1
2017-10-31 4
```

```
$ python github_stats.py Dogild 1825
Github username:Dogild
Days of history:1825
[INFO] Successfully found github repos
https://api.github.com/repos/Dogild/Cucapp-demo/commits
[ERROR] GET Response status code: 403
[INFO] Check for rate-limiting: curl https://api.github.com/rate_limit
```