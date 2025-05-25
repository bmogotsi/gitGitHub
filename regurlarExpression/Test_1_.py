
# https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html#

import re

class TestRegexNumbers:
    @staticmethod
    def main():
        input_str = "abc00123xyz456_0"  # Input String for matching
        regex_str = r"[0-9]+"           # Regex to be matched

        # Step 1: Compile a regex
        pattern = re.compile(regex_str)

        # Step 2: Allocate a matching engine from the compiled regex pattern,
        #         and bind to the input string
        matcher = pattern.finditer(input_str)

        # Step 3: Perform matching and Process the matching results
        # Try finditer(), which finds all matches
        for match in matcher:
            print(f'find() found substring "{match.group()}" starting at index {match.start()} and ending at index {match.end()}')

        # Reset matcher for matches() and lookingAt()
        matcher = pattern.fullmatch(input_str)
        if matcher:
            print(f'matches() found substring "{matcher.group()}" starting at index {matcher.start()} and ending at index {matcher.end()}')
        else:
            print("matches() found nothing")

        matcher = pattern.match(input_str)
        if matcher:
            print(f'lookingAt() found substring "{matcher.group()}" starting at index {matcher.start()} and ending at index {matcher.end()}')
        else:
            print("lookingAt() found nothing")

        # Try re.sub(), which replaces the first match
        replacement_str = "**"
        output_str = re.sub(pattern, replacement_str, input_str, count=1)  # first match only
        print(output_str)

        # Try re.sub(), which replaces all matches
        replacement_str = "++"
        output_str = re.sub(pattern, replacement_str, input_str)  # all matches
        print(output_str)

# Call the main method
TestRegexNumbers.main()