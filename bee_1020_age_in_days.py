# Ashrafi Abir
inp = int(input())
algorithom1 = inp%365
year = int(inp/365)
algorithom3 = algorithom1%30
month = int(algorithom1/30)
day = algorithom3
print(f"{year} ano(s)")
print(f"{month} mes(es)")
print(f"{day} dia(s)")
