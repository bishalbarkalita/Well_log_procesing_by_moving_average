#!/usr/bin/env python
# coding: utf-8




import pandas as pd
import lasio as ls
import numpy as np
import matplotlib.pyplot as plt
import missingno as msno




data_frame_kimzey=pd.read_csv('file_path',delimiter=',')
data_frame_kimzey.head(len(data_frame_kimzey))




def well_plot(df):
    # df=pd.read_csv(data_path,delimiter=',')
    fig = plt.subplots(figsize=(10,20))

    #Set up the plot axes
    ax1 = plt.subplot2grid((1,5), (0,0), rowspan=1, colspan = 1) 
    ax2 = plt.subplot2grid((1,5), (0,1), rowspan=1, colspan = 1)
    ax3 = plt.subplot2grid((1,5), (0,2), rowspan=1, colspan = 1)
    ax4 = plt.subplot2grid((1,5), (0,3), rowspan=1, colspan = 1)
    ax5 = plt.subplot2grid((1,5), (0,4), rowspan=1, colspan = 1)

    ax1.plot("GR", "Depth", data =df , color = "green") # Call the data from the well dataframe
    ax1.set_title("Gamma") # Assign a track title
    # ax1.set_xlim(0, 200) # Change the limits for the curve being plotted
    ax1.set_ylim(max(df['Depth']), min(df['Depth'])) # Set the depth range
    # ax1.set_ylim(max(df['Depth']), 3136)
    ax1.xaxis.set_ticks_position("top")
    ax1.spines["top"].set_position(("outward", 1.02))
    ax1.grid() # Display the grid

    ax2.plot("ILD_log10", "Depth", data = df, color = "red")
    ax2.set_title("LLD")
    # ax2.set_xlim(1.95, 2.95)
    ax2.set_ylim(max(df['Depth']), min(df['Depth']))
    ax2.xaxis.set_ticks_position("top")
    ax2.spines["top"].set_position(("outward", 1.02))
    ax2.grid()

    ax3.plot("DeltaPHI", "Depth", data = df, color = "purple")
    ax3.set_title("DeltaPHI")
    # ax3.set_xlim(140, 40)
    ax3.set_ylim(max(df['Depth']), min(df['Depth']))
    ax3.xaxis.set_ticks_position("top")
    ax3.spines["top"].set_position(("outward", 1.02))
    ax3.grid()
    
    ax4.plot("PHIND", "Depth", data = df, color = "red")
    ax4.set_title("PHIND")
    # ax4.set_xlim(140, 40)
    ax4.set_ylim(max(df['Depth']), min(df['Depth']))
    ax4.xaxis.set_ticks_position("top")
    ax4.spines["top"].set_position(("outward", 1.02))
    ax4.grid()
    
    ax5.plot("PE", "Depth", data = df, color = "orange")
    ax5.set_title("PE")
    # ax5.set_xlim(140, 40)
    ax5.set_ylim(max(df['Depth']), min(df['Depth']))
    ax5.xaxis.set_ticks_position("top")
    ax5.spines["top"].set_position(("outward", 1.02))
    ax5.grid()
    plt.show()
    
    
    
    
def well_one_plot(df):
    # df=pd.read_csv(data_path,delimiter=',')
    fig = plt.subplots(figsize=(10,20))

    #Set up the plot axes
    ax1 = plt.subplot2grid((1,1), (0,0), rowspan=1, colspan = 1)
    
    print('Give the well parameter')
    well_p=str(input())
    print('Give the minimum depth')
    min_depth_w=float(input())
    print('Give the maximum depth')
    max_depth_w=float(input())
    
    print('Give the colour of the plot')
    colour=str(input())
    print('Give the linewidth')
    lin=float(input())
    
    ax1.plot(well_p, "Depth", data =df , color =colour,linewidth=lin) # Call the data from the well dataframe
    ax1.set_title(well_p) # Assign a track title
    # ax1.set_xlim(0, 200) # Change the limits for the curve being plotted
    ax1.set_ylim(max_depth_w, min_depth_w) # Set the depth range
    # ax1.set_ylim(max(df['Depth']), 3136)
    ax1.xaxis.set_ticks_position("top")
    ax1.spines["top"].set_position(("outward", 1.02))
    ax1.grid() # Display the grid
    plt.show()
    
    
    
def well_two_plot(df):
    fig = plt.subplots(figsize=(10,20))

    #Set up the plot axes
    ax1 = plt.subplot2grid((1,1), (0,0), rowspan=1, colspan = 1)
    
    print('Give the well parameter')
    well_p=str(input())
    print('Give the minimum depth')
    min_depth_w=float(input())
    print('Give the maximum depth')
    max_depth_w=float(input())
    
    print('Give the colour of the plot other than blue')
    colour=str(input())
    print('Give the linewidth')
    lin=float(input())
    
    ax1.plot(well_p, "Depth", data =df , color =colour,linewidth=lin) # Call the data from the well dataframe
    ax1.plot(well_p+'_processed', "Depth", data =df , color ='blue',linewidth=lin)
    ax1.set_title(well_p) # Assign a track title
    # ax1.set_xlim(0, 200) # Change the limits for the curve being plotted
    ax1.set_ylim(max_depth_w, min_depth_w) # Set the depth range
    ax1.xaxis.set_ticks_position("top")
    ax1.spines["top"].set_position(("outward", 1.02))
    ax1.grid() # Display the grid
    plt.show()
    
    
    def processes_data(data_path):
    df=pd.read_csv(data_path,delimiter=',')
    msno.matrix(df)
    df.describe()
    
   
        
    print('Give the minimum depth from where the moving average should be done')
    min_depth=float(input())
    print('Give the maximum depth from where the moving average should be done')
    max_depth=float(input())
    print('Write the well log for which the moving average should be done')
    well_parameter=str(input())
    print('Give the window value')
    window_value=int(input())
   
    parameter=df[df.index>=np.where(df['Depth']==min_depth)[0][0]]['GR']
    parameter=parameter[parameter.index<=np.where(df['Depth']==max_depth)[0][0]]
    
    parameter_rolling=parameter.rolling(window=window_value,min_periods=1).mean()
    
    
    print('Give the minimum depth from where the data should be replaced with processed data')
    min_depth_p=float(input())
    print('Give the maximum depth upto where the data should be replaced with processed data')
    max_depth_p=float(input())
    
    if((well_parameter+'_processed' in df.columns)==False):
        df[well_parameter+'_processed']=df[well_parameter]
        
        
    indices_min=np.where(df['Depth']==min_depth_p)[0][0]
    indices_max=np.where(df['Depth']==max_depth_p)[0][0]

    for i in range(indices_min,indices_max+1):
        df[well_parameter+'_processed'][i]=parameter_rolling[i]
    
    
    
    
    return df



df.to_csv('file_path',index=None)

