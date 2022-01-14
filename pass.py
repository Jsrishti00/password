import random
import array


def generate_random_password():
	## picking random characters from the list
  # traverse the temporary password array and append the chars
  # to form the password
  password = []
  for x in temp_pass_list:
    password.append(x)
  
  ## shuffling the resultant password
  random.shuffle(password)

  
  count = 0
  c = 0
  for j in range(length):
    if(password[j].isdigit()):
      count = count+1
    if(not password[j].isalnum()):
      c = c+1
      
  for i in range(length):
    if(count==2):
        pass
    else:
      while(count<2 and not password[i].isdigit()):
        password[i] = random.choice(DIGITS)
        count+=1
    
  for k in range(length):
    if(c==1):
      pass
    else:
      while(c<1 and not password[i].isalnum()):
        password[i] = random.choice(SYMBOLS)
        c+=1
  

  f = password[0]
  l = password[-1]
  if(not f.isalpha() or not l.isalpha()):
    s = random.choice(UPCASE_CHARACTERS) + random.choice(LOCASE_CHARACTERS)
    m = random.choice(UPCASE_CHARACTERS) + random.choice(LOCASE_CHARACTERS)
    first = random.choice(s)
    last = random.choice(m)
    password[0] = first
    password[-1] = last

  
  print("".join(password))




## length of password from the user
length = int(input("Enter password length: "))

# declaring arrays of the character that we need in out password
# Represented as chars to enable easy string concatenation
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']

# combining all the character arrays above to form one array
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS + DIGITS


# randomly selecting at least one character from each character set above
rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)


# combining the character randomly selected above
# at this stage, the password contains only 4 characters but
# we want a certain length character password
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol 

## shuffling the characters
random.shuffle(COMBINED_LIST)

# now that we are sure we have at least one character from each
# set of characters, we fill the rest of
# the password length by selecting randomly from the combined
# list of character above.
#(length-4) bcz 4 characters are already present
for x in range(length-4): 
	temp_pass = temp_pass + random.choice(COMBINED_LIST)

	# convert temporary password into array and shuffle to
	# prevent it from having a consistent pattern
	# where the beginning of the password is predictable
	temp_pass_list = array.array('u', temp_pass)
	random.shuffle(temp_pass_list)


## invoking the function
generate_random_password()
