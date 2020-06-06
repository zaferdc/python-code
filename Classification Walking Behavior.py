import pandas as pd
import csv

"""
We paste the new data next to our true data set,
and find which true data it fits the best.
We basically look foor the nearest neighbours,
by looking at the squared error sum.
"""

ErrorRegRight = 0
ErrorRegLeft = 0
ErrorLimpRight = 0
ErrorLimpLeft = 0

with open('Regular - 1 Right.csv') as file:
	x_right_reg = 0
	y_right_reg = 0
	z_right_reg = 0

	reader = csv.reader(file)
	count = 0
	for row in reader:
		errorsum_reg_right = 0
		row[0] = x_right_reg
		row[1] = y_right_reg
		row[2] = z_right_reg
		row[3] = x_right_test
		row[4] = y_right_test
		row[5] = z_right_test
		errorsum = (x_right_reg - x_right_test)**2 + (y_right_reg - y_right_test)**2 + (z_right_reg - z_right_test)**2
		
		ErrorRegRight += errorsum_reg_right
		
		if count > 50:
			break
		count += 1

with open('Regular - 1 Left.csv') as file:
	x_left_reg = 0
	y_left_reg = 0
	z_left_reg = 0

	reader = csv.reader(file)
	count = 0
	for row in reader:
		errorsum_reg_left = 0
		row[0] = x_left_reg
		row[1] = y_left_reg
		row[2] = z_left_reg
		row[3] = x_left_test
		row[4] = y_left_test
		row[5] = z_left_test
		errorsum = (x_left_reg - x_left_test)**2 + (y_left_reg - y_left_test)**2 + (z_left_reg - z_left_test)**2
		
		ErrorRegLeft += errorsum_reg_left
		
		if count > 50:
			break
		count += 1


with open('Limp - 1 Right.csv') as file:
	x_right_limp = 0
	y_right_limp = 0
	z_right_limp = 0

	reader = csv.reader(file)
	count = 0
	for row in reader:
		errorsum_limp_right = 0
		row[0] = x_right_limp
		row[1] = y_right_limp
		row[2] = z_right_limp
		row[3] = x_right_test
		row[4] = y_right_test
		row[5] = z_right_test
		errorsum = (x_right_limp - x_right_test)**2 + (y_right_limp - y_right_test)**2 + (z_right_limp - z_right_test)**2
		
		ErrorLimpRight += errorsum_limp_right
		
		if count > 50:
			break
		count += 1


with open('Limp - 1 Right.csv') as file:
	x_left_limp = 0
	y_left_limp = 0
	z_left_limp = 0

	reader = csv.reader(file)
	count = 0
	for row in reader:
		errorsum_limp_right = 0
		row[0] = x_left_limp
		row[1] = y_left_limp
		row[2] = z_left_limp
		row[3] = x_left_test
		row[4] = y_left_test
		row[5] = z_left_test
		errorsum = (x_left_limp - x_left_test)**2 + (y_left_limp - y_left_test)**2 + (z_left_limp - z_left_test)**2
		
		ErrorLimpRight += errorsum_limp_right
		
		if count > 50:
			break
		count += 1


if ErrorRegLeft < ErrorLimpLeft and ErrorRegRight < ErrorLimpRight:
	print("The subject has no problems in walking.")

if ErrorRegLeft >= ErrorLimpLeft and ErrorRegRight < ErrorLimpRight:
	print("The subject is limping on his left foot.")

if ErrorRegLeft < ErrorLimpLeft and ErrorRegRight >= ErrorLimpRight:
	print("The subject is limping on his right foot.")

if ErrorRegLeft >= ErrorLimpLeft and ErrorRegRight >= ErrorLimpRight:
	print("The subject's walking behavior is walking problematic.)