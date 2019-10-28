#!/bin/sh
set -e
if [ -f web/tmp/pids/server.pid ]; then
  rm web/tmp/pids/server.pid
fi

exec "$@"
