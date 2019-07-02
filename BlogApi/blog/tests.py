from django.test import TestCase

# Create your tests here.
item = "apple,mango,banana"
x = item.split(',')
for x in x:
    print(x)