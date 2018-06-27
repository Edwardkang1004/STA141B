#coding=utf-8
import numpy as np


def standardize(rawData):
    """ This function accepts the raw data as input,
        and output the data after the normalization.
    """
    max0 = max(rawData[:,0])
    data0 = (rawData[:,0]/max0).tolist()
    max1 = max(rawData[:, 1])
    data1 = (rawData[:, 1] / max1).tolist()
    max2 = max(rawData[:, 2])
    data2 = (rawData[:, 2] / max2).tolist()

    dataList =[]
    dataList.append(data0)
    dataList.append(data1)
    dataList.append(data2)
    dataTrans = np.array(dataList)
    data = np.transpose(dataTrans)
    return data


def getCategory(fso):
    """This function accepts the normlization data as input,
       and output the free, normal, and high state of the traffic
    """
    center = [[0.09708485, 0.70699728, 0.04538181], [0.46682492, 0.33962301, 0.2320578],
              [0.76133578, 0.23272466, 0.52520497]]
    maxFlow = 272.0
    maxSpeed = 13.65
    maxOccupancu = 15.27
    flowStandard = fso[0]/maxFlow
    speedStandard = fso[1]/maxSpeed
    occuStandard = fso[2]/maxOccupancu
    fsoStandard = [flowStandard,speedStandard,occuStandard]

    d0 =  np.sum(np.square(np.array(fsoStandard) - center[0]))
    d1 =  np.sum(np.square(np.array(fsoStandard) - center[1]))
    d2 =  np.sum(np.square(np.array(fsoStandard) - center[2]))

    if d0==min(d0,d1,d2):
        return 'free'
    elif d1 == min(d0,d1,d2):
        return 'normal'
    else:
        return 'high'


fso = [130,2,7]
print (getCategory(fso))
