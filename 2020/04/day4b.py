REQUIRED_FIELDS = ('byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:')
REQUIREMENTS = {
    'byr': lambda val: 1920 <= int(val) <= 2002,
    'iyr': lambda val: 2010 <= int(val) <= 2020,
    'eyr': lambda val: 2020 <= int(val) <= 2030,
    'hgt': lambda val: val.endswith('cm') and 150 <= int(val[:-2]) <= 193 or val.endswith('in') and 59 <= int(val[:-2]) <= 76,
    'hcl': lambda val: val.startswith('#') and len(val) == 7,
    'ecl': lambda val: any(val == color for color in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')),
    'pid': lambda val: val.isdigit() and len(val) == 9,
    'cid': lambda val: True
}

with open('input.txt') as file:
    passports = file.read().split('\n\n')

valid_passports = 0
for passport in passports:
    if all(field in passport for field in REQUIRED_FIELDS):
        passport_map = [field.split(':') for field in passport.split()]
        if all(REQUIREMENTS[field](value) for field, value in passport_map):
            valid_passports += 1

print(valid_passports)
