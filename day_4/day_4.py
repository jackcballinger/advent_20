import re

with open('puzzle_input.txt') as f:
    data = [{y.split(':')[0]:y.split(':')[1] for y in x.replace('\n',' ').split(' ') if y.split(':')[0] != 'cid'} for x in f.read().split('\n\n')]
    
# part 1
print(sum([1 if len(x) == 7 else 0 for x in data]))

# part 2
class Validator:
    def __init__(self, passport):
        self.passport = passport
        
    def _validate_birth_year(self, birth_year):
        return (len(birth_year)==4) and (1920<=int(birth_year)<=2002)
    
    def _validate_issue_year(self, issue_year):
        return (len(issue_year)==4) and (2010<=int(issue_year)<=2020)

    def _validate_expiration_year(self, expiration_year):
        return (len(expiration_year)==4) and (2020<=int(expiration_year)<=2030)
    
    def _validate_height(self, height):
        return bool(re.compile('(:?^(1[5-8][0-9]|19[0-3])(cm)$|^(5[9]|[6][0-9]|7[0-6])(in)$)').match(height))
    
    def _validate_hair_colour(self, hair_colour):
        return bool(re.compile('^#([0-9a-f]){6}$').match(hair_colour))
    
    def _validate_eye_colour(self, eye_colour):
        return eye_colour in ['amb','blu','brn','gry','grn','hzl','oth']
    
    def _validate_passport_id(self, passport_id):
        return bool(re.compile('^[0-9]{9}$').match(passport_id))
    
    def validate_passport(self):
        return all(
            elem in passport for elem in ['byr','iyr','eyr','hgt','hcl','ecl','pid']
        ) and len(self.passport) >= 7 and all(
            [
                    self._validate_birth_year(self.passport['byr']),
                    self._validate_issue_year(self.passport['iyr']),
                    self._validate_expiration_year(self.passport['eyr']),
                    self._validate_height(self.passport['hgt']),
                    self._validate_hair_colour(self.passport['hcl']),
                    self._validate_eye_colour(self.passport['ecl']),
                    self._validate_passport_id(self.passport['pid'])
            ]
        )
print(sum([Validator(passport).validate_passport() for passport in data]))