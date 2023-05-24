ps aux | grep python

kill -SIGINT <PID>

ps aux | grep python | awk '{print $2}'

ps aux | grep python | grep -v grep | awk '{print $11}'

pgrep -f python | xargs -I{} ps -p {} -o comm=

ps aux | grep python | awk '{print $2, $11}'



