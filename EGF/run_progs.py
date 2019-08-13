#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:55:50 2019

@author: vidale
"""

import os
os.environ['PATH'] += os.pathsep + '/usr/local/bin'
os.chdir('/Users/vidale/Documents/GitHub/LAB-EGF')

from pro2_get_Z       import get_Z
from pro2_get_N       import get_N
from pro2_get_E       import get_E
from pro3_plot_sgrams import plot_sgrams
from plot_EGFs        import plot_EGFs
from re_pro2_get_Z       import re_get_Z

os.chdir('/Users/vidale/Documents/PyCode/LAB/Pydata')

#%% define common parameters, but have none so far

#%% Treatment to compare events
#%% Cull seismic section for common stations

all_indices = [0,1,2,4,5,6,7,8,9,10,11,12,14,15]
get_indices = [17]
plot_indices = [6]
freqmin = 0.2
freqmax = 1.5
filt = 1

#for i in get_indices:
#	print('Getting event ' + str(i))
#	get_Z(select_event=i)
#	get_N(select_event=i)
#	get_E(select_event=i)

for i in plot_indices:
	print('Plotting event ' + str(i))
	plot_sgrams(i, component = 'Z', freqmin=freqmin, freqmax=freqmax, filt = filt)
	plot_sgrams(i, component = 'N', freqmin=freqmin, freqmax=freqmax)
	plot_sgrams(i, component = 'E', freqmin=freqmin, freqmax=freqmax)

#station = 'PDR'
#freqmin = 0.1
#freqmax = 1.0
#plot_EGFs(comp='ZZ',sta=station,freqmin=freqmin,freqmax=freqmax)
#plot_EGFs(comp='TT',sta=station,freqmin=freqmin,freqmax=freqmax)

#for i in get_indices:
#	print('Getting event ' + str(i))
#	re_get_Z(select_event=i)
#	get_N(select_event=i)
#	get_E(select_event=i)
