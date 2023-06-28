# Premium_calculator_htmlflask

# SDE Hiring Assignment
# Problem: 
Generating premium for the selected sum insured, age, city tier, and tenure for a user. 
# Data Provided:
Raw CSV file with a premium of individual age, and rate card logic for all the member combinations. 
# Attached csv:
Rate-Card-Data
# Rate Card Logic: 
Given premium data of individual members of age 0-90 member. 
Create premium in the following combination based on the below logic: 
1a - Single Individual
 2a - Two Individual 
1a, 1c - Single Individual, Single Child 
1a, 2c	 1a, 3c	 1a,4c	 2a,1c	 2a,2c	 2a,3c 	2a,4c 

 <img width="506" alt="Capture" src="https://github.com/learnwithjj/Premium_calculator_htmlflask/assets/83998131/43197fbe-62c6-4521-9369-fbe2328909c6">
 <br/>
 
# Note:
•	floater discount is only applicable for more than one insured member and not to a single individual 1a cases. <br/>
•	in cases apart from 1a where a floater discount is given, it's not applicable to the highest member age but the rest of the member age gets a 50% discount as shown above.

# Tech stack required: 
HTML And CSS <br/>
Flask framework and MongoDB on the backend.

# Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
