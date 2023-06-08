# List 

rupali_cart= ["apple","orange","oil","rice"]
print(rupali_cart[0]) 
print(rupali_cart[0:3]) # [apple , orange , oil] 
rupali_cart[0] = "mango" # it'll replace first item
print(rupali_cart)

sonali_cart = rupali_cart[:]
sonali_cart[1] = "jam"
print(sonali_cart)