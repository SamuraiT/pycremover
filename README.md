Description
---------
This is `pyc`files remover which removes all the `pyc` files including sub-directory

for what do you need to use
------------
All the time you run a `python` file, you get `pyc` files
if you import `user-defined python module` from another sub directory or current directory.
`pyc` files make direcotry messy sometimes.

So this module can help you to remove all sub-directory's and current-directory's `pyc` files and make the directory looks better when you **run** a `python` file 
by running a python file this way:
```
pyc pyton_file_you_wanna_run.py
```

How to use
-----------
First, clone this
```git
git clone https://github.com/SamuraiT/pycremover ~/pycremover
```
Then add this script into your `.bashrc` file
```
function pyc(){
    python $1
    python ~/pycremover/pycremover.py 
}
```
To run python module, you can run by this command
```
pyc
```

e.g
```
pyc hello.py
```

