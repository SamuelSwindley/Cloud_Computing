import sys
import time
import numpy as np
import urllib2

if (not(len(sys.argv) == 5 or len(sys.argv) == 4)) :
    print "Incorrect Parameters: Enter URL, 'normal' or 'poisson', and the mean+standard deviation or arrival rate"
    sys.exit()

url = sys.argv[1]

if (sys.argv[2] == 'normal') :
    mean = sys.argv[3]
    std = sys.argv[4] 
    while (True) :
        urllib2.urlopen(url)
        time.sleep(np.random.normal(float(mean), float(std), 1)[0])
elif (sys.argv[2] == 'poisson') :
    rate = sys.argv[3]
    while (True) :
        urllib2.urlopen(url)
        time.sleep(np.random.poisson(float(rate), 1)[0])
else :
    print "The second parameter must be 'normal' or 'poisson'"
    sys.exit()

sys.exit()
    






