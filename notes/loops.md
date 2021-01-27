# Loops

## for loops

```for item in iterable_object:  #do something with item```

- Iterable object could be a list, a string, or a range of numbers (range(1,10))
- item is a new variable, it can be called anything you want

- this example will print 1 thorugh 7 
```
for number in range(1, 8):
    print(number)
```

## ranges

- ranges are exclusive, so range(1,10) would start at one and go all the way up to 10 but NOT include 10
- range(1, 10, 2) the last number is a step, it'll skip two every time