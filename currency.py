money = float(input("How much money do you have?"))
end = money * 100
benjamin_franklin = end // 10000
end = end - (benjamin_franklin * 10000)
grant = end // 5000
end = end - (grant * 5000)
andrew_jackson = end // 2000
end = end - (andrew_jackson * 2000)
alexander_hamilton = end // 1000
end = end - (alexander_hamilton * 1000)
abe_liclon = end // 500
end = end - (abe_liclon * 500)
george_washington = end // 100
end = end - (abe_liclon * 100)
change = 100 * end




print(benjamin_franklin)
print(grant)
print(andrew_jackson)
print(alexander_hamilton)
print(abe_liclon)
print(george_washington)
print(end)
