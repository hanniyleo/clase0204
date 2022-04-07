from ast import Sub
from math import prod

prods = ["martillo  5000","clavos  800","alicate  4000","pintura  8000"]
comuna=["la cisterna 3500, san ramon  2500", "san miguel  1000", "santiago  3500"]
i=0
sub=0
pro=0

print("------------------")
print("Lista para compra")
print("------------------")
print()


print("lista de productos disponibles para elegir")
print()
print(prods)
print()
print("cantidad de productos que compraras: ")
pro = int(input())
print()
print(comuna)
print("igrese el valor de despacho segun su comuna, si no desea despacho, digite 0: ")
com = int(input())


while i<pro:
    print("lista de productos disponibles para elegir : ")
    print(prods)
    print("Ingrese valor de producto numero ", i+1, "valor: ")
    val = int(input())
    print("cantidad que desea llevar de el producto elegido: ")
    cant = int(input())
    subpro = val*cant
    sub=sub+subpro
    i+=1
    totalF=sub + com
    print ("se vendieron: ", pro, "productos")
    print ("subtotal: ", sub)
    print("el total con despacho:" , totalF)
    
    
   

