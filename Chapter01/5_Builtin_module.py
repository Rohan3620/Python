import userModule
print(userModule.swap(10, 20))

from userModule import swap
print(swap(10, 20))

from userModule import *
print(swap(10, 20))

import userModule as u
print(u.swap(10, 20))
