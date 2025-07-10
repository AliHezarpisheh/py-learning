"""  
The __format__ method customizes how objects are displayed in f-strings and  
format() calls. It accepts a format_spec (e.g., 'f' for Fahrenheit) to switch  
output formats dynamically.  

Example:  
- `f"{temp}"` → "25.00°C" (default)  
- `f"{temp:f}"` → "77.00°F" (Fahrenheit)  
- `f"{temp:k}"` → "298.15K" (Kelvin)  
"""

from typing import Literal


class Temperature:
    """Represents temperature with customizable string formatting."""

    def __init__(self, celsius: int | float) -> None:
        """Initialize with temperature in Celsius."""
        self.celsius = celsius

    def __format__(self, format_spec: Literal["", "c", "f", "k"]) -> str:
        """
        Format temperature per spec:
        - 'f': Fahrenheit, 'k': Kelvin, default: Celsius.
        """
        if format_spec == "f":
            return f"{((self.celsius * 9/5) + 32):.2f}°F"
        elif format_spec == "k":
            return f"{(self.celsius + 273.15):.2f}K"
        return str(self)

    def __str__(self) -> str:
        """Return Celsius string (e.g., '25.00°C')."""
        return f"{self.celsius:.2f}°C"

    def __repr__(self) -> str:
        """Return unambiguous Celsius string for debugging."""
        return f"{self.celsius:.2f}°C"
