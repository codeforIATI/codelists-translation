#!/bin/bash


rm -rf xml
mkdir xml
cd xml

if [ -d IATI-Codelists-NonEmbedded ]; then
    cd IATI-Codelists-NonEmbedded || exit 1
    git pull
    git checkout master
    cd ..
else
    git clone --branch master https://github.com/codeforIATI/IATI-Codelists-NonEmbedded.git
fi

if [ -d Unofficial-Codelists ]; then
    cd Unofficial-Codelists || exit 1
    git pull
    git checkout master
    cd ..
else
    git clone --branch master https://github.com/codeforIATI/Unofficial-Codelists.git
fi

for v in 2.03 1.05; do
    i=$(echo $v | head -c 1)

    if [ -d IATI-Codelists-$i ]; then
        cd IATI-Codelists-$i || exit 1
        git pull
        git checkout version-$v
        cd ..
    else
        git clone --branch version-$v https://github.com/codeforIATI/IATI-Codelists.git IATI-Codelists-$i
    fi
done
