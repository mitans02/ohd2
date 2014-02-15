#!/bin/sh

USAGE="$0 path-to-pngdir path-to-outdir"
if [ "$1" = "" -o "$2" = "" ]; then
  echo $USAGE
  exit 1
fi

for f in `ls $1`
do
#  convert $1/$f \( +clone -alpha opaque -fill white -colorize 100% \) +swap \
#   -compose Over -composite -alpha off -rotate 270 $2/$n.png
   convert $1/$f -crop "100x100+0+0" -rotate 270 -flop -geometry 128x128 png32:$2/$f
done
