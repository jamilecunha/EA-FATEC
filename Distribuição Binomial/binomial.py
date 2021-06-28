import math

def fatorial(n): 
    fatorial = 1
    while n >= 1:
        fatorial = fatorial * n
        n = n - 1
    return fatorial

def calculaFatorial(n, k):
    return fatorial(n) / (fatorial(k) * fatorial(n-k))

def msg(msg):
    print('=' * 78)
    print('-= %s =-' % msg)
    print('=' * 78)

def main():
    msg('Distribuição Binomial')

    n = float(input("Digite o número de ensaios: "))
    p = float(input("Digite a probabilidade de sucesso: "))
    k = float(input("Digite a quantidade de observação (sucesso): "))
 
    q = 1 - p
    contador = 0
    while (contador <= 10):
        k = contador
        numeroFatorial = calculaFatorial(n, k)
        binomial = numeroFatorial * math.pow(p, k) * math.pow(q, (n-k))

        print("Quantidade de Sucessos (K) ", k, " = %.4f" % binomial, " - ", "{:.1%}".format(binomial))
        contador = contador + 1

if __name__ == '__main__':
    main()