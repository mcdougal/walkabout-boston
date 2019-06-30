#!/bin/bash

for f in `ls --color=never photos`; do
    echo $f
    identify -verbose "photos/$f" | grep "exif:DateTime:"
done