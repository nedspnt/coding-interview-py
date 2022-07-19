# coding-interview-py
To collect the most common coding interview problems


## Counting Elements

### 4.1 FrogRiverOne

```
# poor performance
for i in range(len(A)):
    if set(A[:i+1]) == required_steps:
        return i

# better performance
for i in range(len(A)):
    required_steps.discard(A[i])
    if required_steps == set():
        return i
```


### Trouble Shoots:

If you are running this on Jupyter, please add `argv` and `exit` arguments according below.
```
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
```
https://medium.com/@vladbezden/using-python-unittest-in-ipython-or-jupyter-732448724e31