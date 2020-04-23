#!/bin/bash
# Program:
# Program helps initiate app files:
# 1. create urls.py in app's home directory
# 2. create templates directory, where html file with the same name as appName will be created
# 3. create static directory, which concludes src/css/appName.css and src/js
# shell must be executed in webApp directory. important!
# some configuration should be set manually in setting.py. important!
# Usage:
# ./initApp.sh appName
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin/:~/bin
export PATH

appName=$1

# create standard urls.py
cat $(pwd)'/lib/urlsDemo.py' > $(pwd)'/'$appName'/urls.py'

# create templates directory and related files
mkdir -p $(pwd)'/'$appName'/templates/'$appName
cat $(pwd)'/lib/demo.html' > $(pwd)'/'$appName'/templates/'$appName'/'$appName'.html'

# create static directory and related files
mkdir -p $(pwd)'/'$appName'/static/'$appName'/src/css'
mkdir -p $(pwd)'/'$appName'/static/'$appName'/src/js'
touch $(pwd)'/'$appName'/static/'$appName'/src/css/'$appName'.css'