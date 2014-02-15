#!/bin/sh
for i in `ls outdirb`
do
  N=`echo $i | awk -F '.' '{ print $1 }'`
  convert -threshold 30 outdirb/$i outdir/$N.png
done
