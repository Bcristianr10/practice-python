def devolver_distintos (num1, num2,num3):
    numeros = [num1,num2,num3]
    if sum(numeros) > 15:
        return max(numeros)
    if sum(numeros) < 10:
        return min(numeros)
    if sum(numeros) >= 10 or sum(numeros) <= 15:
        return sum(numeros)