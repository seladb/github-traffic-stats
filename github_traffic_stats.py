import github
import pickledb
import json
import argparse
import csv
import sys

def collect(db, user, passwd, token, repo, org):
    if org is None:
        org = user

    if token is not None:
        user = None
        password = None

    gh = github.GitHub(username=user, password=passwd, access_token=token)
    try:
        gh.repos(org, repo).get()
    except:
        sys.exit('Username/org "' + org + '" or repo "' + repo + '" not found in github')

    if user is not None and org != user:
        try:
            gh.repos(org, repo).collaborators(user).get()
        except:
            sys.exit('Username "' + user + '" does not have collaborator permissions in repo "' + repo + '"')
    views_14_days = gh.repos(org, repo).traffic.views.get()
    found_new_data = False
    for view_per_day in views_14_days['views']:
        timestamp = view_per_day['timestamp']
        data = { 'uniques': view_per_day['uniques'], 'count': view_per_day['count']}
        if db.get(timestamp) is None:
            db.set(timestamp, json.dumps(data))
            print timestamp, data
            found_new_data = True
        else:
            db_data = json.loads(db.get(timestamp))
            if db_data['uniques'] < data['uniques']:
                db.set(timestamp, json.dumps(data))
                print timestamp, data
                found_new_data = True
    if not found_new_data:
        print 'No new traffic data was found for ' + org + '/' + repo
    db.dump()


def view(db):
    sorted_by_ts = db.getall()
    sorted_by_ts.sort()
    for ts in sorted_by_ts:
        print ts, db.get(ts)
    print len(sorted_by_ts), 'elements'


def export_to_csv(csv_filename, db):
    with open(csv_filename, 'wb') as csvfile:
        fieldnames = ['timestamp', 'count', 'uniques']
        csvwriter = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
        csvwriter.writeheader()
        sorted_by_ts = db.getall()
        sorted_by_ts.sort()
        for ts in sorted_by_ts:
            json_data = json.loads(db.get(ts))
            csvwriter.writerow({'timestamp': ts, 'count': json_data['count'], 'uniques': json_data['uniques']})
        print csv_filename + ' written to disk' 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['collect', 'view', 'exportcsv'])
    parser.add_argument('-u', '--github_user', action='store')
    parser.add_argument('-p', '--github_password', action='store')
    parser.add_argument('-t', '--github_access_token', action='store')
    parser.add_argument('-o', '--github_org', action='store')
    parser.add_argument('-r', '--github_repo', action='store')
    parser.add_argument('-v', '--view', help='view DB content', action='store_true')
    parser.add_argument('-csv', '--export_csv', help='export DB content to CSV file', action='store_true')

    args = parser.parse_args()

    db = pickledb.load('{repo}_views.db'.format(repo=args.github_repo), False)

    if args.action == 'view':
        if args.github_repo is None:
            sys.exit('You need to provide github repo: -r|--github_repo')
        view(db)
    elif args.action == 'exportcsv':
        if args.github_repo is None:
            sys.exit('You need to provide github repo: -r|--github_repo')
        export_to_csv('{repo}.csv'.format(repo=args.github_repo), db)
    else:
        if args.github_repo is None:
            sys.exit('You need to provide github repo: -r|--github_repo')
        if args.github_access_token is None and (args.github_user is None or args.github_password is None):
            sys.exit('You need to provide either github username & password or github access token: -u|--github_user, -p|--github_password, -t|--github_access_token');
        if args.github_access_token is not None and args.github_user is None and args.github_org is None:
            sys.exit('When providing access token, please provide either repo user or repo org: -u|--github_user, -o|--github_org')
        collect(db=db, user=args.github_user, passwd=args.github_password, token=args.github_access_token, repo=args.github_repo, org=args.github_org)

if __name__ == "__main__":
    main()
