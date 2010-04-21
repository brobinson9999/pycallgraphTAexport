#!/usr/bin/python

import time

def f1():
    f2()
    f2()
    f3()
    time.sleep(5)

def f2():
    time.sleep(3)
    
def f3():
    time.sleep(0.5)    

def runTest():
    import pycallgraphTAexport

    pycallgraphTAexport.start_trace()
    f1()
    pycallgraphTAexport.stop_trace()

    # export normal graph
    pycallgraphTAexport.make_TA_graph('example.ta')

    # export graph, only including functions with total elapsed time >= 1 second
    pycallgraphTAexport.minimumTimeExportThreshold = 1
    pycallgraphTAexport.make_TA_graph('example-1sec.ta')

    # export graph, only including functions with total elapsed time >= 10 seconds
    pycallgraphTAexport.minimumTimeExportThreshold = 10
    pycallgraphTAexport.make_TA_graph('example-10sec.ta')

runTest()
