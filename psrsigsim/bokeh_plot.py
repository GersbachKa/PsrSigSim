from __future__ import (absolute_import,division,print_function,unicode_literals)

from bokeh.io import output_notebook

import bokeh.plotting as bplt
from bokeh.models import Range1d
import numpy as np
from . import PSS_utils as utils


def bokeh_filter_bank(signal_object, grid=False, N_pulses=1, start_time=0,
                      phase=False, notebook=False, **kwargs):
    try:
        nBins_per_period = int(signal_object.MetaData.pulsar_period//signal_object.TimeBinSize)
    except:
        raise ValueError('Need to sample pulses')

    stop_bin = N_pulses*nBins_per_period
    time = len(signal_object.signal[0,:])
    stop_time = start_time + N_pulses * nBins_per_period * signal_object.TimeBinSize
    img = signal_object.signal[:,:stop_bin] #Better name later
    print(signal_object.first_freq)
    print(signal_object.last_freq)
    fig = bplt.figure(#plot_height=(400),plot_width=(400),
                      title='Filter Bank',
                      x_range = Range1d(start_time,stop_time),
                      y_range = Range1d(signal_object.first_freq,signal_object.last_freq),
                      x_axis_label = 'Observation Time (ms)',
                      y_axis_label = 'Frequency (Mhz)')            #MODIFIED
    #fig = bplt.figure(plot_height=(10*img.shape[0]),plot_width=(10*img.shape[0]),
    #                  title='Filter Bank',
    #                  x_range = [start_time,stop_time],
    #                  y_range = [signal_object.first_freq, signal_object.last_freq],
    #                  x_axis_label = 'Observation Time (ms)',
    #                  y_axis_label = 'Frequency (Mhz)')            #MODIFIED


    #fig.image(image=[np.flipud(img)], x=[0], y=[signal_object.first_freq], dw=[stop_time], dh=[signal_object.last_freq], palette='Plasma256')
    fig.image(image=[img], x=[0], y=[1400], dw=[stop_time], dh=[signal_object.last_freq], palette='Plasma256')


    if notebook:
        fig.plot_height = 700
        fig.plot_width = 700
        fig.y_range = Range1d(signal_object.first_freq,signal_object.last_freq*2)
        output_notebook()
        bplt.show(fig)
    else:
        fig.plot_height = 400
        fig.plot_height = 700
        return fig