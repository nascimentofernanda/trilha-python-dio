#Neste problema, você deverá ler 3 palavras que definem o tipo de animal 
# possível segundo o esquema abaixo, da esquerda para a direita.  
# Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

#Entrada
#A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, 
# com todas as letras minúsculas.

#Saída
#Imprima o nome do animal correspondente à entrada fornecida.

a=input()
b=input()
c=input()

d="vertebrado"
e="invertebrado"

f="ave"
g="mamifero"

h="inseto"
i="anelideo"

j="carnivoro"
k="onivoro"
l="herbivoro"
m="hematofago"

if a==d and b==f and c==j:
    print("aguia")
elif a==d and b==f and c==k:
    print("pomba")
elif a==d and b==g and c==k:
    print("homem")
elif a==d and b==g and c==l:
    print("vaca")
elif a==e and b==h and c==m:
    print("pulga")
elif a==e and b==h and c==l:
    print("lagarta")
elif a==e and b==i and c==m:
    print("sanguessuga")
else:
    print("minhoca")