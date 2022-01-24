from django import forms

class NumberValidator:
    def validate(self, password, user=None):
        first_character = password[0]
        if first_character.isdigit():
            raise forms.ValidationError("First digit can not be a number")
    
    def get_help_text(self):
        return "First Digit can not be a number"


class CharacterValidator:
    def validate(self, password, user=None):
        is_upper = True
        is_lower = True
        is_special = True
        is_digit = True
        for ch in password:
            if ch >="A" and ch<="Z":
                is_upper = False
            elif ch >= "a" and ch<="z":
                is_lower = False
            elif ch.isdigit():
                is_digit = False
            else:
                is_special = False
        
        if is_upper or is_lower or is_special:
            raise forms.ValidationError("Must have at least one Uppercase, Lowercase and Special character")
            
    
    def get_help_text(self):
        return "Must have at least one Uppercase, Lowercase and Special character"