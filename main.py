# Create a program that can compute the area of a trapezoid
from pyscript import display, document

def calculating_area(e):
    document.getElementById('output').innerHTML = " "
    base1 = float(document.getElementById('base1').value)
    base2 = float(document.getElementById('base2').value)
    height = float(document.getElementById('height').value)
    area = 0.5 * (base1 + base2) * height

    display(f'The area of the trapezoid is {area}')