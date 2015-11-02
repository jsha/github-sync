# GitHub Sync

This is a handy tool to mirror and keep updated all GitHub repositories owned
by a given user into a local directory. Usage:

    github-sync.py --user USERNAME --directory ~/repositories/

To keep your repositories up-to-date, run this program regularly in cron. It
will pick up new repositories automatically, but it will not delete repositories
that cease to exist on GitHub. By default, it will not mirror repos that are
forks of other repos. If you redirect stdout to /dev/null, github-sync.py should
be silent except for errors, which go to stderr.

Reminder: [do you know who owns your availability](http://www.whoownsmyavailability.com/)?
