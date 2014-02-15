#!/bin/sh

USAGE="$0 path-to-pngdir path-to-outdir"
if [ "$1" = "" -o "$2" = "" ]; then
  echo $USAGE
  exit 1
fi

n=0
for f in `ls $1`
do
  convert $1/$f \( +clone -alpha opaque -fill white -colorize 100% \) +swap \
    -compose Over -composite -alpha off -rotate 270 $2/$n.png
  n=`expr $n + 1`
done
