urldecode() { : "${*//+/ }"; echo -e "${_//%/\\x}"; }
urldecode `echo JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTM4JTMxJTY1JTMxJTY2JTM3JTYxJTYx | base64 -D`
