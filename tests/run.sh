#!/bin/bash

echo -n "running gen-case-classes ... "
TOP=$(cd `dirname $0` > /dev/null; pwd -P)
cd "$TOP" || exit 1
rm -rf out || exit 1
../scripts/magic-property -o out --custom-ints my_ints test.h test.m || exit 1
cd out || exit 1
clang -I../../objective-c -ObjC -fobjc-arc -Werror -c test.h test.m || exit 1
echo "ok"
