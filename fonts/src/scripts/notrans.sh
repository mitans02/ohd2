#!/bin/sh
for i in `ls outdirt`
do
  convert outdirt/$i \( +clone -alpha opaque -fill white -colorize 100% \) +swap -sample 1200% -geometry 300x300 -compose Over -composite -alpha off outdir/$i.bmp
done
