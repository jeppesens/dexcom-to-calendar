#!/bin/bash

if $VSCODE_DEBUGGING ; then
    echo "⏳ Waiting for VS Code debugger to attach ⏳"
    watchmedo auto-restart -d . -p '*.py' -R -- python -m debugpy --wait-for-client --listen 0.0.0.0:10009 worker.py
else
    echo "If you want to debug with VS Code set VSCODE_DEBUGGING=true"
    watchmedo shell-command --patterns="*.py;*.txt" --recursive --command='supervisord -c config/worker_supervisor.conf' .
fi
