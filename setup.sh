#!/usr/bin/env bash
# exit on failure
set -e

run_command(){
 echo -e "\e[33mCommand: $@\e[0m"
 $@
}

info() {
 echo " $@"
}

download_file_if_not_present() {
 #params?<url> <target file>
 if [ ! -f $2 ]
 then
  wget $1 -O $2
 else
  info "Found file $1"
 fi
}

uncompress_file() {
 unzip $1
}

get_database_Emotion6() {
 url="http://chenlab.ece.cornell.edu/people/kuanchuan/publications/Emotion6.zip"
 filename=$(basename $url)
 run_command download_file_if_not_present $url $filename
 run_command uncompress_file $filename
 rm $filename
}

if [ ! -d Emotion6 ]
then
 run_command get_database_Emotion6
else
 info Emotion6 database is already downloaded
fi
./generate_Emotion6_lists.sh