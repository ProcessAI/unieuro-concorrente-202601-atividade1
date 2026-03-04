import hashlib
import time

def md5_string(texto):
    return hashlib.md5(texto.encode('utf-8')).hexdigest()

def buscahash4(hashbuscado):
    for d1 in range(10):
        for d2 in range(10):
            for d3 in range(10):
                for d4 in range(10):
                    combinacao = f"{d1}{d2}{d3}{d4}"
                    hash = md5_string(combinacao)
                    #print(hash)
                    if hashbuscado == hash:
                        print(f"achei!!!!!{d1}{d2}{d3}{d4}")
                        return f"{d1}{d2}{d3}{d4}"
                    

def buscahash7(hashbuscado):
    for d1 in range(10):
        for d2 in range(10):
            for d3 in range(10):
                for d4 in range(10):
                    for d5 in range(10):
                        for d6 in range(10):
                            for d7 in range(10):
                                combinacao = f"{d1}{d2}{d3}{d4}{d5}{d6}{d7}"
                                hash = md5_string(combinacao)
                                # print(hash)
                                if hashbuscado == hash:
                                    print(f"achei!!!!!{combinacao}")
                                    return combinacao

def buscahash8(hashbuscado):
    for d1 in range(10):
        for d2 in range(10):
            for d3 in range(10):
                for d4 in range(10):
                    for d5 in range(10):
                        for d6 in range(10):
                            for d7 in range(10):
                                for d8 in range(10):
                                    combinacao = f"{d1}{d2}{d3}{d4}{d5}{d6}{d7}{d8}"
                                    hash = md5_string(combinacao)
                                    if hashbuscado == hash:
                                        print(f"achei!!!!!{combinacao}")
                                        return combinacao

def buscahash9(hashbuscado):
    for d1 in range(10):
        for d2 in range(10):
            for d3 in range(10):
                for d4 in range(10):
                    for d5 in range(10):
                        for d6 in range(10):
                            for d7 in range(10):
                                for d8 in range(10):
                                    for d9 in range(10):
                                        combinacao = f"{d1}{d2}{d3}{d4}{d5}{d6}{d7}{d8}{d9}"
                                        hash = md5_string(combinacao)
                                        if hashbuscado == hash:
                                            print(f"achei!!!!!{combinacao}")
                                            return combinacao
                                        
def buscahash10(hashbuscado):
    for d1 in range(10):
        for d2 in range(10):
            for d3 in range(10):
                for d4 in range(10):
                    for d5 in range(10):
                        for d6 in range(10):
                            for d7 in range(10):
                                for d8 in range(10):
                                    for d9 in range(10):
                                        for d10 in range(10):
                                            combinacao = f"{d1}{d2}{d3}{d4}{d5}{d6}{d7}{d8}{d9}{d10}"
                                            hash = md5_string(combinacao)
                                            print(hash)
                                            if hashbuscado == hash:
                                                print(f"achei!!!!!{d1}{d2}{d3}{d4}{d5}{d6}{d7}{d8}{d9}{d10}")
                                                return f"{d1}{d2}{d3}{d4}{d5}{d6}{d7}{d8}{d9}{d10}"
inicio = time.time()

#hashbuscado = "6495cf7ca745a9443508b86951b8e33a"
#buscahash4(hashbuscado)

#hashbuscado = "3fd5c2a0df1ce9dc01f0698adc57c72b"
#buscahash10(hashbuscado)

#hashbuscado = "944050de61b9309955ccbce77fe31a9a"
#buscahash7(hashbuscado)

#hashbuscado = "bd751840405d78c41501c8823c50b696"
#buscahash8(hashbuscado)

hashbuscado = "ca6ae33116b93e57b87810a27296fc36"
buscahash9(hashbuscado)

fim = time.time()

print(f"Tempo de execução: {fim - inicio:.4f} segundos")