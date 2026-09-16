#!/bin/bash
H="/Users/dtaxk/Desktop/research prize"
if pgrep -f "research prize/watch.sh" > /dev/null 2>&1; then exit 0; fi
nohup bash -c 'while true; do bash "/Users/dtaxk/Desktop/research prize/watch.sh"; sleep 60; done' >> "$H/state/supervisor.log" 2>&1 &
