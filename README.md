# GhostExport

This is an utility to export posts from [Ghost blog](https://ghost.org/download/) database.
The output are markdown files for all posts, file name is the post slug.
The output files can be used in [Hexo](https://hexo.io/) directly, so this utils helps you
migrating blog from Ghost to Hexo.

## Usage:
```
usage: exportFromMySQL.py [-options] [values]
   or: exportFromMySQL.py [--options=values]
  options:
    -u, --user: MySQL db user name, default is root
    -p, --pass: MySQL db user password, default is empty
    -d, --database: MySQL database name, default is blogdb
    -o, --output: output directory, default is posts
    -h, --help: print help
```

example:

    $ ./exportFromMySQL.py -u race604 -d ghost_prod -p

## Requirement

* Python
* mysql-python

## LICENSE

The MIT License (MIT)

Copyright (c) 2015
