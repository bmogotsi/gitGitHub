# Padd or Indent
# https://www.geeksforgeeks.org/add-padding-to-a-string-in-python/
import textwrap
try:
    while   True:
        count = 0
        nums=[1,3,4,11,12,15,100,130,155,1000,1234,9876]
        for i in nums:
            paddedL=f"{i:>5}".ljust(6, "-")
            paddedR=f"{i:>5}"
            padded = textwrap.fill(str(i).center(1),5)
            paddedStrip=str(i).rjust(5,"0")
            print(f"{i}.   {i:>5}.  {paddedL}             {paddedR}               {padded}           {paddedStrip}")
            
        break
        # or
        
        # Using Python f-strings
        # F-strings allow us to specify padding directly within the string using alignment specifiers. 
        # It is efficient and concise for quick formatting tasks.
        count = 0
        nums=[1,3,4,11,12,15,100,130,155,1000,1111234,9876]
        for i in nums:
            print(f"{i:>5}.")
        #  :> aligns the string to the right.
        #  10 specifies the total width of the padded string, including the text.
            
            
        # or 
        s = "Python"
        
        # Left-align with dashes
        left_padded = s.ljust(10, "-")
        
        # Right-align with dashes
        right_padded = s.rjust(10, "-")
        
        # Center-align with dashes
        center_padded = s.center(10, "-")
        
        print(left_padded)
        print(right_padded)
        print(center_padded)
        """
        Python----
        ----Python
        --Python--
        """
        
        # or 
        # textwrap module provides advanced formatting features and can be used for padding in more complex scenarios.
        import textwrap
        
        s = "Python"
        padded = textwrap.fill(s.center(10), width=10)
        print(padded)
        #  textwrap.fill() formats the text to fit within the specified width.
        #  Combined with center(width), it ensures equal padding on both sides.
        
        
        # or
        # Using String Concatenation
        # We can manually add padding by calculating the required number of characters and concatenating them to the string.
        s = "Python"
        width = 10
        # Add padding
        padded = " " * (width - len(s)) + s  # Right-align
        print(padded)
        
        exit()
        exit()
    
except Exception as e:
    print(f"Something went wrong...:  {str(e)}")