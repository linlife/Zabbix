#!/bin/bash
LOGFILE="/tmp/SMS.log"
:>"$LOGFILE"
exec 1>"$LOGFILE"
exec 2>&1

MOBILE_NUMBER=$1
MESSAGE_UTF8=$3
XXD="/usr/bin/xxd"
CURL="/usr/bin/curl"
TIMEOUT=5

MESSAGE_ENCODE=$(echo "$MESSAGE_UTF8" | ${XXD} -ps | sed 's/\(..\)/%\1/g' | tr -d '\n')

URL="******************=${MOBILE_NUMBER}&smscontent=${MESSAGE_ENCODE}"

set -x
${CURL} -s --connect-timeout ${TIMEOUT} "${URL}"
