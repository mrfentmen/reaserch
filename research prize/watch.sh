#!/bin/bash
R="/Users/dtaxk/Desktop/research prize/state"
H="/Users/dtaxk/Desktop/research prize"
mkdir -p "$R"
for f in "$R/beal6.log" "$R/quick.log" "$R/riemann_loop.log"; do
  if [ -f "$f" ]; then S=$(stat -f%z "$f" 2>/dev/null || echo 0); if [ "$S" -gt 10485760 ]; then tail -2000 "$f" > "$f.tmp" && mv "$f.tmp" "$f"; fi; fi
done
alive_bun() { kill -0 $1 2>/dev/null && ps -p $1 -o comm= 2>/dev/null | grep -q bun; }
if [ -f "$R/beal_6000_7_0_1_5001.pid" ]; then P=$(cat "$R/beal_6000_7_0_1_5001.pid"); alive_bun $P || nohup bun "$H/beal.ts" 6000 7 0 1 5001 >> "$R/beal6.log" 2>&1 & else nohup bun "$H/beal.ts" 6000 7 0 1 5001 >> "$R/beal6.log" 2>&1 & fi
if [ -f "$R/quick.pid" ]; then P=$(cat "$R/quick.pid"); alive_bun $P || nohup bun "$H/quick.ts" 1000000 >> "$R/quick.log" 2>&1 & else nohup bun "$H/quick.ts" 1000000 >> "$R/quick.log" 2>&1 & fi
if [ -f "$R/riemann.pid" ]; then P=$(cat "$R/riemann.pid"); alive_bun $P || nohup bun "$H/riemann_loop.ts" 200 >> "$R/riemann_loop.log" 2>&1 & else nohup bun "$H/riemann_loop.ts" 200 >> "$R/riemann_loop.log" 2>&1 & fi
ls "$R"/*found.txt 2>/dev/null && echo "HIT - check found files"
