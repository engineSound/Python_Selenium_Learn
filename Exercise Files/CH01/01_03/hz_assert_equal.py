from selenium import webdriver

a = "abc"

b = "abc"

try:
    assert a == b
    print("they are equal")

except Exception as e:
    print("they are not equal")

c = "xyz"
try:
    assert a == c
    print("they are equal")

except Exception as e:
    print("they are not equal", format(e))
