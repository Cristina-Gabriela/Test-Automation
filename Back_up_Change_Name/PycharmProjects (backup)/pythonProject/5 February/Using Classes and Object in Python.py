class Beach:
    location = 'Cape Cod'


cape_cod_beach = Beach()
beach_2 = Beach()
print(cape_cod_beach.location, beach_2.location)
cape_cod_beach.location = "Cancun"
print(cape_cod_beach.location, beach_2.location)

