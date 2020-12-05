import wmi

def getTemps():
    monitor = wmi.WMI(namespace="root\OpenHardwareMonitor")
    temperature_info = monitor.Sensor()
    temp_dictionary = {}
    for sensor in temperature_info:
        if (sensor.SensorType==u'Temperature'):
            temp_dictionary[sensor.Name] = sensor
    return temp_dictionary['GPU Core']


print(getTemps())