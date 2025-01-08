class PasswordValidator:
    """A class for validating password strength and requirements.
    This class provides functionality to validate passwords against common security requirements
    and check password strength based on various criteria.
    Attributes:
        min_length (int): Minimum required length for the password. Defaults to 8.
        require_uppercase (bool): Whether password must contain uppercase letters. Defaults to True.
        require_lowercase (bool): Whether password must contain lowercase letters. Defaults to True.
        require_numbers (bool): Whether password must contain numbers. Defaults to True.
        require_special (bool): Whether password must contain special characters. Defaults to True.
        special_chars (str): String containing allowed special characters.
    Methods:
        validate(password): Validates a password against all requirements.
        check_password_strength(password): Evaluates password strength and returns a score.
    """
    def __init__(self, min_length=8, require_uppercase=True, require_lowercase=True, 
                 require_numbers=True, require_special=True):
        self.min_length = min_length
        self.require_uppercase = require_uppercase
        self.require_lowercase = require_lowercase
        self.require_numbers = require_numbers
        self.require_special = require_special
        self.special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    def validate(self, password):
        errors = []
        
        # Check minimum length
        if len(password) < self.min_length:
            errors.append(f"Password must be at least {self.min_length} characters long")
        
        # Check for uppercase letters
        if self.require_uppercase and not any(c.isupper() for c in password):
            errors.append("Password must contain at least one uppercase letter")
        
        # Check for lowercase letters
        if self.require_lowercase and not any(c.islower() for c in password):
            errors.append("Password must contain at least one lowercase letter")
        
        # Check for numbers
        if self.require_numbers and not any(c.isdigit() for c in password):
            errors.append("Password must contain at least one number")
        
        # Check for special characters
        if self.require_special and not any(c in self.special_chars for c in password):
            errors.append("Password must contain at least one special character")
        
        return {
            'is_valid': len(errors) == 0,
            'errors': errors
        }

    def check_password_strength(self, password):
        strength = 0
        
        if len(password) >= self.min_length:
            strength += 1
        if any(c.isupper() for c in password):
            strength += 1
        if any(c.islower() for c in password):
            strength += 1
        if any(c.isdigit() for c in password):
            strength += 1
        if any(c in self.special_chars for c in password):
            strength += 1
        
        return {
            'strength': strength,
            'score': strength * 20,  # Returns a score from 0-100
            'rating': ['Very Weak', 'Weak', 'Medium', 'Strong', 'Very Strong'][strength-1 if strength > 0 else 0]
        }