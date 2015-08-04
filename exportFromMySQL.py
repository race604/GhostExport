#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys, getopt, os
import MySQLdb as mdb
import getpass

filename = os.path.basename(__file__)

def usage():
	print 'usage: %s [-options] [values]' % filename
	print '   or: %s [--options=values]' % filename
	print '  options:'
	print '    -u, --user: MySQL db user name, default is root'
	print '    -p, --pass: MySQL db user password, default is empty'
	print '    -d, --database: MySQL database name, default is blogdb'
	print '    -o, --output: output directory, default is posts'
	print '    -h, --help: print help'

opts, args = getopt.getopt(sys.argv[1:], "hpu:pd:o:",
	["help","user=","pass","database=","output="])

con = None
user = 'root'
password = ''
dbname = 'blogdb'
outDir = 'posts'

if not os.path.isdir(outDir):
	os.makedirs(outDir)

for op, value in opts:
	if op in ("-u", "--user"):
		user = value
	elif op in ("-p", "--pass"):
		password = getpass.getpass()
	elif op in ("-d", "--database"):
		dbname = value
	elif op in ("-o", "--output"):
		outDir = value
	elif op in ("-h", "--help"):
		usage()
		sys.exit()

try:
	con = mdb.connect('localhost', user, password, dbname)
	cur = con.cursor()
	cnt = cur.execute('select id,slug,title,markdown,published_at from posts')
	print 'Total %s posts' % cnt
	posts = cur.fetchmany(cnt)
	for row in posts:
		print "post: %s" % row[1]

		output = open(outDir + "/" + row[1]+'.md', 'w')
		output.write("title: \"%s\"\n" % row[2])
		output.write("date: %s\n" % row[4])
		output.write("tags: [")
		tagcnt = cur.execute('select name from posts_tags join tags on posts_tags.tag_id = tags.id where posts_tags.post_id = %s' % row[0])
		for i in range(tagcnt):
			if i > 0 :
				output.write(' ,')
			tag = cur.fetchone()
			output.write("%s" % tag)
		output.write("]\n")
		output.write("---\n")

		output.write(row[3])
		output.close()

	print 'export finish, OK!'

except mdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
finally:
    if con:
        con.close()
