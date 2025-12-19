#!/bin/bash
history -c && rm -f ~/.bash_history
pkill -f go && pkill -f python
chmod 400 *
echo "🌑 DEACTIVATED."

