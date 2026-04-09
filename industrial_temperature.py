def trigger_alarm(temperatures, threshold= 80):
    tr= []
    for sensor in temperatures:
        if temperatures[sensor] > threshold:
            tr.append(sensor)
    return tr
