# github-traffic-stats
A small Python project to pull and store traffic stats for GitHub projects using GitHub API.

Currently GitHub provides only 14 days of traffic data to a repo. This data includes the number of views and the number of unique visitors for each day. 

But what happens if you want to store and view more than 14 days of data?
This script aims to collect and aggregate the data and then store it in a simple NoSQL DB which can later be viewed and analyzed.

## Usage ##

There are 3 modes of opetation: **collect**, **view** and **exportcsv**

### Collect ###

Collect last 14-days traffic data from GitHub and store it in the DB. The DB is pickleDB which is a really simple NoSQL DB which is stored in a local file.

Usage:

#### Connecting using username & password: ####

`python github_traffic_stats.py collect -r [github-repo] -u [github-user] -p [github-password]`

Where:
 - `[github-repo]` is the GitHub repository to pull stats on
 - `[github-user]` is the GitHub user who owns this repo
 - `[github-password]` is the password of the GitHub user

Example:

```
python github_traffic_stats.py collect -r pcapplusplus -u seladb -p ******
2020-04-28 {'count': 119, 'uniques': 59}
```


#### Connecting using username & password to an organization repo: ####

`python github_traffic_stats.py collect -r [github-repo] -u [github-user] -p [github-password] -o [github-org]`

Where:
 - `[github-repo]` is the GitHub repository to pull stats on
 - `[github-user]` is the GitHub user who has access to traffic stats in this repo
 - `[github-password]` is the password of the GitHub user
 - `[github-org]` is the repo organization (for example: google for repo protobuf)

Example:

```
python github_traffic_stats.py collect -r protobuf -u google-employee1234 -p ****** -o google
2020-05-08 {'count': 110, 'uniques': 41}
```


#### Connecting using GitHub access token: ####

`python github_traffic_stats.py collect -r [github-repo] -t [github-access-token] -o [repo-org]`

Where:
 - `[github-repo]` is the GitHub repository to pull stats on
 - `[github-access-token]` is the GitHub personal access token
 - `[github-org]` is the repo organization or the user who owns the repo (for example: google for repo protobuf or seladb for PcapPlusPlus)

Example:

```
python github_traffic_stats.py collect -r pcapplusplus -t ****** -o seladb
2020-05-08 {'count': 110, 'uniques': 41}
```


### View ###
 
 Open the DB file, read all the data stored and output is to console, sorted by timestamp.
 
 Usage:
 
 `python github_traffic_stats.py view -r [github-repo]`
 
 Where:
 - `[github-repo]` is the GitHub repository to pull stats on

Example:
```
python github_traffic_stats.py view -r pcapplusplus
2020-04-27 {"count": 7, "uniques": 6}
2020-04-28 {"count": 119, "uniques": 59}
2020-04-29 {"count": 143, "uniques": 58}
2020-04-30 {"count": 186, "uniques": 55}
2020-05-01 {"count": 77, "uniques": 40}
2020-05-02 {"count": 49, "uniques": 33}
2020-05-03 {"count": 61, "uniques": 22}
2020-05-04 {"count": 120, "uniques": 63}
2020-05-05 {"count": 172, "uniques": 73}
2020-05-06 {"count": 110, "uniques": 47}
2020-05-07 {"count": 108, "uniques": 49}
2020-05-08 {"count": 110, "uniques": 41}
2020-05-09 {"count": 76, "uniques": 26}
2020-05-10 {"count": 86, "uniques": 34}
2020-05-11 {"count": 59, "uniques": 37}
15 elements
```

### exportcsv ###

Export the DB into a csv file with the format of `[repo_name].csv`

Usage:
 
 `python github_traffic_stats.py exportcsv -r [github-repo]`
 
 Where:
 - `[github-repo]` is the GitHub repository to pull stats on

Example:
```
python github_traffic_stats.py exportcsv -r pcapplusplus
pcapplusplus.csv written to disk
```

## Installation ##

This script requires Python 2.7, I haven't tested it on Python 3 yet.

The requirements for this script are described in [requirements.txt](https://github.com/seladb/github-traffic-stats/blob/master/requirements.txt).

### Installation with pip: ###
```
pip install github_traffic_stats2
```
If you choose this option you'll be able to run the script simply by typing `github_traffic_stats`

### Installation without virtualenv: ###
```
python pip install -r requirements.txt
```

### Installation with virtualenv (linux/Mac): ###
```
$ virtualenv venv
New python executable in venv/bin/python
Installing distribute.........done.
Installing pip................done.
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt
Collecting githubpy==1.1.0 (from -r requirements.txt (line 1))
Collecting pickleDB==0.6.2 (from -r requirements.txt (line 2))
Collecting simplejson==3.13.2 (from -r requirements.txt (line 3))
  Using cached simplejson-3.13.2-cp27-cp27m-win32.whl
Installing collected packages: githubpy, simplejson, pickleDB
Successfully installed githubpy-1.1.0 pickleDB-0.6.2 simplejson-3.13.2
(venv)$
```
