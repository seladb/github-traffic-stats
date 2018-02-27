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
2018-02-22T00:00:00Z {'count': 153, 'uniques': 45}
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
2018-02-22T00:00:00Z {'count': 10153, 'uniques': 1045}
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
2018-02-22T00:00:00Z {'count': 153, 'uniques': 45}
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
2018-02-05T00:00:00Z {"count": 200, "uniques": 30}
2018-02-06T00:00:00Z {"count": 150, "uniques": 35}
2018-02-07T00:00:00Z {"count": 220, "uniques": 40}
2018-02-08T00:00:00Z {"count": 260, "uniques": 45}
2018-02-09T00:00:00Z {"count": 240, "uniques": 30}
2018-02-10T00:00:00Z {"count": 50, "uniques": 20}
2018-02-11T00:00:00Z {"count": 80, "uniques": 30}
2018-02-12T00:00:00Z {"count": 150, "uniques": 50}
2018-02-13T00:00:00Z {"count": 200, "uniques": 60}
2018-02-14T00:00:00Z {"count": 280, "uniques": 20}
2018-02-15T00:00:00Z {"count": 100, "uniques": 40}
2018-02-16T00:00:00Z {"count": 250, "uniques": 30}
2018-02-17T00:00:00Z {"count": 200, "uniques": 35}
2018-02-18T00:00:00Z {"count": 200, "uniques": 65}
2018-02-19T00:00:00Z {"count": 250, "uniques": 100}
2018-02-20T00:00:00Z {"count": 150, "uniques": 40}
2018-02-21T00:00:00Z {"count": 150, "uniques": 50}
2018-02-22T00:00:00Z {"count": 150, "uniques": 35}
18 elements
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

The requirements for this script are described in [requirements.txt](https://github.com/seladb/github-traffic-stats/blob/master/requirements.txt).

Installation without virtualenv:
```
python pip install -r requirements.txt
```

Installation with virtualenv (linux/Mac):
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
