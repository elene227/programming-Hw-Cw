def reach_pump(distan, m, gallons):

    max = m * gallons

    return max >= distan

pump_dist = 50
m = 25
gallons = 2

print(reach_pump(pump_dist, m, gallons))
