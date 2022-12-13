# NUME
**_Nume_ is module that allows easy calculations on engineering numbers used in electronics and
other fields of science and engineering. You can calculate the full range of _quecto_ (_10e-30_) to
_quetta_ (_10e + 30_), combined with the standard math module we get a powerful python calculation
tool. The nume module, which is actually an electronics-focused calculator, can be used in your
own scripts or in prototyping in the console, IDLE or other IDE.**

The _nume.py_ module is based on the _EEngine.py_ module which can also be used in your own
scripts. The package uses no additional dependencies other than the python standard libraries.
_Nume.py_ and _Eengine_.py are open source modules, if you get measurable financial gains by using
nume, please support me.

## REQUIREMENTS
x64 Linux, Windows10+, MacOs,

Python 3+.

## INSTALLATION
Linux, MacOs, Windows:
_Eengine.py_ modules, _nume.py_ need to be copied to the directory (your own or general) containing
the python modules.

The _ss.py_ script can be of help to specify the boot directory on Linux or other systems. If our modules are in
a different directory, and preferably in _/home/name_user/bin/python_, it is worth running the _ss.py_
script from there, thanks to which we will get the start path to this directory:

> python3 ss.py

## TUTORIAL - EASY
Before using the nume module in IDLE, the nume module needs to be imported:

```python
import nume as e
```

or

```python
import nume
```

or

```python
import nume*
```

Calculation of current of esistor R1 of 5.1kΩ:

```python
v= 12         #voltage 12V
r1= e.k(5.1)  #resistor 5.1kΩ
```

then calkulate:

```python
i= v/r1
res= e.unit(i)
print(res)

(2.352941176470588, 'm')  #current ≈2.35mA
```

Converting the obtained number to the scientific format:

```python
res= e.sci(i) #lub e.sci((2.352941176470588, 'm'))
print(res)

'2.352941176470588e-03'
```

Calculation of resistor limiting the current to 50mA at voltage of 12V:

```python
r= v/e.m(50)          #R= V/50mA
res= e.unit(r)
print(res)

(240.0, '')           #240.0Ω
```

however, we do not have such a resistor, so the closest value in the E12 series will be:

```python
res= e.valofrow(i)
print(res)

220.0
```

If this value does not suit us, we need to use a parallel connection, e.g. two resistors. We have a
510Ω resistor and we are looking for a second resistor for 240Ω parallel resistance:

```python
res= e.parajointfind(240, 510)
print(res)

453.3333333333333
```

however, we did not find the correct value in E12 series. Only in the series of E96:

```python
res= e.valofrow(453) #value is inappropriate
print(res)
470.0

res= e.valofrow(453, 'E96')          #value ok
print(res)
453.0
```

Calculation of the 22n capacitor impedance at 500Hz and 1.5kHz:

```python
import nume*
import math
for freq in (k(0.5), k(1.5)):
  res= unit(1/(2*math.pi*freq*n(22)))
  print(res)

(14.468631190172303, 'k')
(4.822877063390768, 'k')
```

The value of 5.1k, 500k expressed in M():

```python
res= k(5.1)/M(1)
print(res)

0.0051                  #0.0051MΩ

res= k(500)/M(1)
print(res)

0.5                     #0.5MΩ

res= 500/m(1)           #500 expressed in m(0.001)
print(res)

500000.0                #500000m
```
