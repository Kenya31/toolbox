#!/bin/bash
LINE_TOKEN="##REDUCTED##"
LINE_API="https://notify-api.line.me/api/notify"
TARGET_URL="https://example.com/"
LAST_MD5_FILE=".last_md5"
LAST_MD5=""
CURR_MD5_FILE=".curr_md5"
CURR_MD5=""
WGET_LOG="./wget.log"
WGET_DOC="./index.html"
STOP_FILE=".stop"
SLEEP_SECS="60"
MESSAGE_FILE="message"

while [ ! -f "${STOP_FILE}" ]
do
    wget -o "${WGET_LOG}" -O "${WGET_DOC}" "${TARGET_URL}"

    CURR_MD5=$(md5sum ${WGET_DOC} | awk '{print $1}')
    echo "${CURR_MD5}" > "${CURR_MD5_FILE}"

    if [ -f "${LAST_MD5_FILE}" ]
    then
        LAST_MD5=$(cat "${LAST_MD5_FILE}")
        if [ "${LAST_MD5}" = "${CURR_MD5}" ]
        then
            # echo "いっしょやで"
            # なにもしない
            :
        else
            echo "いっしょやないで"
            # メッセージ送信
            MESSAGE=$(cat "${MESSAGE_FILE}")

            ## LINE
            curl -X POST -H "Authorization: Bearer ${LINE_TOKEN}" -F "message=${MESSAGE}" "${LINE_API}"
        fi
    else
        echo "初回起動やで"
    fi

    echo "${CURR_MD5}" > "${LAST_MD5_FILE}"
    rm -f "${WGET_DOC}"
    sleep ${SLEEP_SECS}
done

rm -f "${STOP_FILE}"