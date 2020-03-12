__author__ = 'Liquid'
#Prompt the user to input the window measurement in cm
#Add a bit for hems
#Work out how many widths of cloth will be needed
#and figure out the total length of material for each curtain (in cm)
#Double the amount of material because there are two curtains
#Divede by 10 to get the number of meters
#Work out how much it'll cost
#Print the results

roll_width = 140
price_per_meter = 5
win_height = input('Enter window height (cm): ')
win_width = input('Enter window width (cm): ')

#Converrting strings to integers
curt_width = float(win_width) * 0.75 + 20
curt_length = float(win_height) + 15

#Total width and length for two curtains in meters
widths = curt_width / roll_width
total_length = curt_length * widths
total_length = (total_length*2)/10

#Price for total material
price = total_length*price_per_meter

#Print the results
print("You\'ll need", total_length, "meters of cloth", "for", price)
