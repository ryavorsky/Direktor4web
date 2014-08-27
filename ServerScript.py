#!/usr/bin/env python
import time

def refreshPage() :
    f = open('index.html','w')
    head = '<html><head>Test page</head><body>'
    tail = '</body></html>'
    content = head + 'Hello, World!<br/> Current time is '+ time.asctime() + tail
    f.close()

def clicks() :
    N = 10
    for i in range(N) :
        print 'Step number', i, ' Out of', N, time.asctime()
        refreshPage()
        time.sleep(10)  # Delay for 10 seconds)

clicks()