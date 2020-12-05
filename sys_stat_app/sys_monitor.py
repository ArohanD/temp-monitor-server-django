import wmi
import pythoncom

def getTemps():
    pythoncom.CoInitialize()
    monitor = wmi.WMI(namespace="root\OpenHardwareMonitor")
    temperature_info = monitor.Sensor()
    temp_dictionary = {}
    for sensor in temperature_info:
        if (sensor.SensorType==u'Temperature'):
            temp_dictionary[sensor.Name] = {
                'Name': sensor.Name,
                'SensorType': sensor.SensorType,
                'Min': sensor.Min,
                'Max': sensor.Max,
                'Value': sensor.Value,
                'Identifier': sensor.Identifier
            }
    return temp_dictionary