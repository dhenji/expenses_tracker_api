#!/usr/bin/env bash

PG_PATH="/run/secrets/pg_user_password"

if [[ ! -f "$PG_PATH" ]]; then
    echo "Missing Flway requirements: ${PG_PATH}" >&2
    exit 1
fi

export FLYWAY_PASSWORD="$(cat ${PG_PATH})"

exec flyway "$@"
