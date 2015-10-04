#!/bin/bash

### Functions
function sendEmail {
    # This function sends an email to notify.
    # Args
    #   $1 string The subject of the email
    #   $2 string The body of the email
    echo $2 | mail -s $1 "alejandro@hackpartners.com";
}


### Main Program

# Get absolute path
currPath="`dirname \"$0\"`"              # relative
currPath="`( cd \"$currPath\" && pwd )`"  # absolutized and normalized
if [ -z "$currPath" ] ; then
  # error; for some reason, the path is not accessible
  # to the script (e.g. permissions re-evaled after suid)
  echo "Error reading path. Not permissioned."
  exit 1  # fail
fi
echo "$currPath"

# Set Executables
venvpath="$currPath/../venv/bin/python"
pyscript="$currPath/FileLoader.py"

# Download file
file="file_downloaded.xml"
zipfile="$file.gz"
path=$(dirname $0)
echo $path
wget "ftp://ftpuser:A!t4398htw4ho4jy@datafeeds.nationalrail.co.uk/*_v8.xml.gz" -O "./$zipfile"

# Unzip file contents
gunzip "./$zipfile"

# Run the python script with our venv
echo "Loading $file"
$venvpath $pyscript $file

echo "File loaded. Removing"
rm "$file"

# Notify success
body="Schedule File $file Succeeded Upload"
sendEmail "$body" "$body"
