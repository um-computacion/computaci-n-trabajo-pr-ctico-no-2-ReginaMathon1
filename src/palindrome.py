def is_palindrome(palabra: str) -> bool:
    palabra = palabra.replace(" ", "").lower().replace(".", "").replace(",", "").replace(":", "").replace(";", "").replace("!", "").replace("?", "")
    for index in range(len(palabra)):
        if palabra[index] != palabra[-(index + 1)]:
            return False
    return True