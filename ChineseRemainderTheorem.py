from Crypto.Util.number import *
import gmpy2
from gmpy2 import *

mod_list = [3, 4, 5]
rem_list = [2, 1, 3]

m_list = []
y_list = []

M = 1
for i in range(len(mod_list)):
	M *= mod_list[i]

for i in range(len(mod_list)):
	m_list.append(M/mod_list[i])

for i in range(len(m_list)):
	for j in range(len(rem_list)):
		if(i==j):
			y_list.append(inverse(m_list[i], mod_list[i]))
			
x = 0
for i in range(3):
	x = x + (m_list[i] * rem_list[i] * y_list[i])

x1 = x %  M
print(x1)

