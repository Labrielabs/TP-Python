def convertir_en_celsius(fahrenheit):
    """
    Convertit une température de Fahrenheit en Celsius.
    :param fahrenheit: Température en Fahrenheit
    :return: Température équivalente en Celsius
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Exemple d'utilisation :
if __name__ == "__main__":
    temperature_fahrenheit = float(input("Entrez la température en Fahrenheit : "))
    temperature_celsius = convertir_en_celsius(temperature_fahrenheit)
    print(f"{temperature_fahrenheit:.2f}°F équivaut à {temperature_celsius:.2f}°C")
