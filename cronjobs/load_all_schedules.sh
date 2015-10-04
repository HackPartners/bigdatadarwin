#!/bin/bash


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

# Get all XML files to load
list=($currPath/*_v8.xml)

# Run the python script with our venv
for file in "${list[@]}"; 
    do echo $file;
    $venvpath $pyscript "$file";
    # Notify success
    echo "File $file Downloaded" | mail -s "Schedule File $file Downloaded" "alejandro@hackpartners.com";
done
