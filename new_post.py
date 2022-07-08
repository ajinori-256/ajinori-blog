#!/usr/bin/python3
import os
from nanoid import generate
import glob

from subprocess import run, PIPE
files = glob.glob("./content/posts/*")
nanoid="hoge.md"#generate('1234567890abcdef', 20)
while 1:
	nanoid=generate('1234567890abcdef', 20)
	if not ((nanoid+".md") in files) :
		print(nanoid)
		break
title=input("title=")
print(title)
path=os.path.dirname(__file__)
cmd="hugo new \"posts/"+nanoid+".md\""
print(cmd)
a = run(cmd, stdout=PIPE, shell=True, cwd=path,
        universal_newlines=True, timeout=10)

with open(path+"/content/posts/"+nanoid+".md") as f:
    s = f.read()
    s=s.format(title=title) 
    print(s)

with open(path+"/content/posts/"+nanoid+".md", mode='w') as f:
    f.write(s)
#"hugo new posts/"+nanoid+".md"
a = run("gedit "+path+"/content/posts/"+nanoid+".md", stdout=PIPE, shell=True, cwd=path,
        universal_newlines=True, timeout=10)
