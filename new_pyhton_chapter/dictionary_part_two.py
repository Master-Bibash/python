a={} ##it is set not dictionary but set
name_grade={
     "ram":25,
     "shyam":80,
     "ram":40
} ## ram value is replaced with 40
##give length
# print(len(name_grade))
# print(name_grade.get("ram"))
#only print keys
print(name_grade.keys())
print(name_grade.values())
print(name_grade.items())

print('----------------------------------------------------------------')
#nested dictionary
info={
     "name":"biabsh",
     "address":{
          "city":"sindhuli",
          "pincode":123456
     }
}
info["address"]["city"] = "Pakistan"
print(info["address"])