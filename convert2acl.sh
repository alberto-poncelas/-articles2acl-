#!/bin/bash

CURRENTDIR="$( cd "$(dirname "$0")" ; pwd -P )"
PRECEEDINGSDIR=$1


SCRIPT_CUT=$CURRENTDIR/Tools/script_cut.py
SCRIPT_EASY2ACL=$CURRENTDIR/Tools/easy2acl/easy2acl.py
ANTHOLOGY=$CURRENTDIR/Tools/ACLPUB/anthologize


cd $PRECEEDINGSDIR


python3 $SCRIPT_CUT
python3 $SCRIPT_EASY2ACL


perl $ANTHOLOGY/anthologize.pl proceedings anthology


for DIR in anthology/*/*; do 
  [[ -d $DIR ]] || continue
  echo "Creating Anthology XML for $DIR"
  python3 $ANTHOLOGY/anthology_xml.py $DIR -o $DIR/$(basename $DIR).xml
done  


CONFNAME=$(cat meta | grep "abbrev" | sed 's/abbrev //g')
tar czhvf "$CONFNAME"_anthology.tgz anthology




#in case of several proceedings folder
#for DIR in data/*; do
#  [[ -d $DIR/proceedings ]] || continue
#  echo "Creating symlinks for $DIR"
#  perl $ANTHOLOGY/anthologize.pl $DIR/proceedings anthology
#done

