convertingdirection = input(" Do you want to convert a temperature in degrees Celsius to Fahrenheit or Fahrenheit to Celsius? ")
if convertingdirection == "degrees Celsius to Fahrenheit" or convertingdirection == "to degrees Fahrenheit":
    temperaturevalue = input(" How many degrees Celsius? ")
    if isinstance(temperaturevalue, int):
        print(int(temperaturevalue) * 9 / 5 + 32)
    else:
        print(float(temperaturevalue) * 9 / 5 + 32)
elif convertingdirection == "degrees Fahrenheit to Celsius" or convertingdirection == "to degrees Celsius":
    temperaturevalue = input(" How many degrees Fahrenheit? ")
    if isinstance(temperaturevalue, int):
        print(int((temperaturevalue - 32) * 5 / 9))
    else:
        print((float(temperaturevalue) - 32) * 5 / 9)
