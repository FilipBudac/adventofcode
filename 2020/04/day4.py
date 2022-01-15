REQUIRED_FIELDS = ('byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:')


with open('input.txt') as file:
    passports = file.read().split('\n\n')

print(sum(all(field in passport for field in REQUIRED_FIELDS) for passport in passports))
