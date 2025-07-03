def zero_fuel(distance_to_pump, mpg, fuel_left):
    max = mpg * fuel_left
    
    return max >= distance_to_pump