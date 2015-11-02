#!/usr/bin/python
import argparse
import json
import urllib2
import os
import subprocess
import re

parser = argparse.ArgumentParser(
         description='Mirror all GitHub repos for a given user locally.')
parser.add_argument('--forks', dest='forks',
    action='store_true', help='Include forked repos')
parser.add_argument('--user', dest='user',
    action='store', type=str, required=True, help='GitHub user name to sync')
parser.add_argument('--directory', dest='directory',
    action='store', type=str, required=True, help='Directory to store repos in')
parser.set_defaults(forks=False)
args = parser.parse_args()

os.chdir(args.directory)
f = urllib2.urlopen("https://api.github.com/users/%s/repos" % args.user)
repo_list = json.loads(f.read())

for repo in repo_list:
    name, url = repo["name"], repo["clone_url"]
    if re.search("[^A-z0-9-_]", name):
        print "Skipping invalid name", name
        continue
    if re.search("[^A-z0-9-_:/.]", url):
        print "Skipping invalid url", url
        continue
    if repo["private"]:
        print "Skipping private repo", name
        continue
    if repo["fork"] and not args.forks:
        print "Skipping forked repo", name
        continue
    if not os.path.exists(name):
        print "New repo", name
        subprocess.check_output(["git", "clone", "--mirror", url, name], stderr=subprocess.STDOUT)
    os.chdir(name)
    print "Updating", name
    subprocess.check_output(["git", "remote", "update"])
    os.chdir("..")
