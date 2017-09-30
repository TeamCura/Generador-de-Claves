#Generador de claves

import random
import string
password = '01234546789ABCDEF'.join(random.choice(string.ascii_uppercase + string.digits) for x in range(2))
 
print password
