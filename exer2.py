import phonenumbers
from phonenumbers import geocoder,carrier,timezone

my_str_number = input("Please enter a phone no:")
my_number = phonenumbers.parse(my_str_number,"GB")


print(phonenumbers.is_valid_number(my_number))
print(geocoder.description_for_number(my_number, 'en'))
print(carrier.name_for_number(my_number,"en"))
print(timezone.time_zones_for_number(my_number))
