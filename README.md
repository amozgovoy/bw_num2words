# BW num2words
first, clone the repo:
```
git clone https://github.com/amozgovoy/bw_num2words.git
cd bw_num2words
```

the function:
```
bw_num2words.py
```

the unit test:
```
test_bw_num2words.py
```

the code should work with Python 3.x

to use the function in your own app:
```python
from bw_num2words import solution
print(solution(125))
```

```
One-Hundred Twenty Five
```

to run the unittest:
```
python -m unittest -v test_num2words.py
```

```
testNumber0 (test_bw_num2words.TestIfnum2wordsIsCorrect) ... ok
testNumber1000 (test_bw_num2words.TestIfnum2wordsIsCorrect) ... ok
testNumber1100 (test_bw_num2words.TestIfnum2wordsIsCorrect) ... ok
testNumber119 (test_bw_num2words.TestIfnum2wordsIsCorrect) ... ok
testNumber12 (test_bw_num2words.TestIfnum2wordsIsCorrect) ... ok
testNumber256 (test_bw_num2words.TestIfnum2wordsIsCorrect) ... ok
testNumber692 (test_bw_num2words.TestIfnum2wordsIsCorrect) ... ok
testNumberMinus1 (test_bw_num2words.TestIfnum2wordsIsCorrect) ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.004s

OK
```