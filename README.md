# github-traffic-stats

![Python test](https://github.com/seladb/github-traffic-stats/workflows/Python%20test/badge.svg)

A small Python project to pull and store traffic stats for GitHub projects using GitHub API.

Currently GitHub provides only 14 days of traffic data to a repo. This data includes the number of views and the number of unique visitors for each day. 

But what happens if you want to store and view more than 14 days of data?
This script aims to collect and aggregate the data and then store it in a simple NoSQL DB which can later be viewed and analyzed.

## Usage ##

There are 3 modes of operation: **collect**, **view** and **exportcsv**

### Collect ###

Collect last 14-days traffic data from GitHub and store it in the DB. The DB is pickleDB which is a really simple NoSQL DB which is stored in a local file.

Usage:

#### Collect traffic data for a repo: ####

`python github_traffic_stats.py collect -u [github-user] -r [github-repo] -t [github-access-token]`

Where:
 - `[github-user]` is the GitHub user who owns this repo
 - `[github-repo]` is the GitHub repository to pull stats on
 - `[github-access-token]` is the GitHub personal access token

Example:

```
python github_traffic_stats.py collect -u seladb -r pcapplusplus -t ******
2018-02-22T00:00:00Z {'count': 153, 'uniques': 45}
```


#### Collect traffic data for an organization repo: ####

`python github_traffic_stats.py collect -o [github-org] -u [github-user] -r [github-repo] -t [github-access-token]`

Where:
 - `[github-org]` is the repo organization (for example: google for repo protobuf)
 - `[github-user]` is the GitHub user who has access to traffic stats in this repo
 - `[github-repo]` is the GitHub repository to pull stats on
 - `[github-access-token]` is the GitHub personal access token

Example:

```
python github_traffic_stats.py collect -o pcapplusplus -u seladb -r pcapplusplus.github.io -t ******
2020-05-27T00:00:00Z {"uniques": 2, "count": 6}
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
2020-05-15T00:00:00Z {"uniques": 41, "count": 162}
2020-05-16T00:00:00Z {"uniques": 32, "count": 149}
2020-05-17T00:00:00Z {"uniques": 38, "count": 177}
2020-05-18T00:00:00Z {"uniques": 63, "count": 291}
2020-05-19T00:00:00Z {"uniques": 92, "count": 412}
2020-05-20T00:00:00Z {"uniques": 68, "count": 277}
2020-05-21T00:00:00Z {"uniques": 75, "count": 381}
2020-05-22T00:00:00Z {"uniques": 55, "count": 323}
2020-05-23T00:00:00Z {"uniques": 36, "count": 185}
2020-05-24T00:00:00Z {"uniques": 32, "count": 193}
2020-05-25T00:00:00Z {"uniques": 75, "count": 317}
2020-05-26T00:00:00Z {"uniques": 67, "count": 360}
2020-05-27T00:00:00Z {"uniques": 71, "count": 403}
2020-05-28T00:00:00Z {"uniques": 67, "count": 340}
2020-05-29T00:00:00Z {"uniques": 18, "count": 82}
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

This script requires Python 3 (Python 2.7 is no longer supported).

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
Collecting pickleDB==0.9.2 (from -r requirements.txt (line 2))
Collecting simplejson==3.17.0 (from -r requirements.txt (line 3))
Installing collected packages: githubpy, simplejson, pickleDB
Successfully installed githubpy-1.1.0 pickleDB-0.9.2 simplejson-3.17.0
(venv)$
```
