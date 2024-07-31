#!/bin/bash


curpath=$(dirname "$(realpath $0)")
cd "$curpath"

export SSLKEYLOGFILE="$curpath/sslkeylog.log"

if [ ! -f "$SSLKEYLOGFILE" ]; then
    touch "$SSLKEYLOGFILE"
fi


KEYLOG_AGENT="$curpath/extract-tls-secrets-4.0.0.jar"
APP=build/libs/okhttp2.jar

if [ ! -f "$APP" ]; then
    echo "Building the app"
    ./gradlew build
    # ./gradlew build --refresh-dependencies
fi

if [ -f "$KEYLOG_AGENT" ]; then
    java -javaagent:"$KEYLOG_AGENT=$SSLKEYLOGFILE" -jar "$APP"
else
    # java -Djavax.net.debug=ssl -jar "$APP"
    java -jar "$APP"
fi
