def inverter_string(s):
    resultado = ""

    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]

    return resultado

    if __name__ == "__main__":
        string_original = "Exemplo de string"
        string_resultado = inverter_string(string_original)
        print(f"String original: {string_original}")
        print(f"String invertida: {string_resultado}")