import requests

borough = 1
block = 20
lot = 1
url = f"https://a810-dobnow.nyc.gov/Publish/WrapperPP/PublicPortal.svc/getPublicPortalBinDetailsFromBisGet/{borough}%7C{block}%7C{lot}/PP"

payload = {}
headers = {
    'Cookie': '_ga_W77SGPGVEF=GS1.1.1685712955.5.0.1685712955.0.0.0; _ga_RTXXDWQQS0=GS1.1.1685712955.5.0.1685712955.0.0.0; _ga_TVM7LC4V3D=GS1.1.1691063659.6.0.1691063664.0.0.0; _ga_F2HZY1HS3P=GS1.1.1691741051.1.0.1691741054.0.0.0; RT="z=1&dm=a810-dobnow.nyc.gov&si=a7146b30-185c-402f-a6ed-35b347a580b4&ss=lnk63z21&sl=0&tt=0"; RT="z=1&dm=nyc.gov&si=87e0hr1f8bm&ss=lnsjgyq6&sl=0&tt=0"; _ga_K9V6JKDZGX=GS1.1.1697450373.8.0.1697450375.0.0.0; _abck=3E7B12FDA25395D8287FE4701760F5AC~0~YAAQO3xBF9YtrzeLAQAAGrlvPArH+391iGexVHZVH+LyegbHgmFszoyRtHH0v/keuMGT7kobVinfPwhUBtIq5UntrWjqjqVuRt3Ow4YCrTlsA0hLMPIYnUq7NARBCL3mUS0ymWVcCFua3c5EY66T9fVGLoYnVyTcDmly0P4UBI7kVP65arzBcX6iK+fh3jPkRDC+dHU+qzyfxd7OGMj7+3QG/ooU3TY7r/aF8JV4c5fcGpySuR6uqhSurZPiMisUYUI1eyg32KH9eyR2EvZVqDdPfXCxj9ZcrzCw02LULQ/E+nHFif+dSe/iI5wqOLnvsynSBQY3j9Y0cmMP+ECp/ko5RAsY8B+eisl/dM/L3WcVc+j68DPqhfX9qoo3hghxUDeeZ0V4JOpf8RyqSNgcFQ7Oc8vV~-1~-1~-1; bm_sz=38428A16CA3E657552909CDDF215A2CF~YAAQO3xBF9ktrzeLAQAAGrlvPBXdqYS3Dzrv4XlVSu9nH1JVwzl5dzy1Wb+5fqRrlcoYRDjCttl1tlXw8ZJQIvHkYf2rh4z9CQ/xC2ndLq7q4LjEXzCA3F0O08qNv7xSc/4fwAzwAoEWcZq4vL8SPNiNzlWXVNDQD6wff7HDmh7mk/vnYZ3QwkewZESmr6oTT4kYVI1GpLc6Pzp6QTvsl/6f2at8C5gXXci0sepAfuOjtPIx+Qw5DWMxQeG7xLkStipn+KifGRV+XBWl9ddzXEM9sTztRM/mofmzdWXHVXM=~3749173~4536390; _ga_863DM8YSJL=GS1.1.1697526037.12.0.1697526037.0.0.0; _ga=GA1.2.609920701.1682577764; _gid=GA1.2.906844422.1697526038; ASP.NET_SessionId=xnzwial1bkwxoyby2z0xsp5b; amp_6e403e=lwNsLa64O3lNBxWNGrPD1l.cHBhdGVsLmRhdGFzb3NAZ21haWwuY29t..1hcu6vj9s.1hcu6vj9s.0.1.1; ak_bmsc=0A0439153B92682587B964187CB1D45D~000000000000000000000000000000~YAAQzjoiF9c+FSGLAQAArxYVPRVewKGYJ4D7WpGLDSu1h1L3VBU1x0ddbGVjgYSnvuS5/K36Eu1uUJGpQUCjospcLNHUFFFyWrem4ifwko0GyTy2HcrXPp19PaON1UDoJGp3UKnFE2ylclBQgQs4Lp/XzHNsce3QJlnwOk+k7sF6INXcm7O/YKr0bjPRXf3siu1zdJbMt17ZMfq5juBXeBN2acWPZHotZ3GMQtsmlC3sqp3bfglyC6e5i/eybvcc512nIYTYNDi93oUufwJcED0tfmLQ6alAGJX7nDQJNBm9kaqn2u7885qzb4Xb/rKe+FGIKzfMRSfBwxJY6MgsuOh5ZxZlmQK4oyirzN7uxooR/H8HwPZN2apeOxK4xAg0Q9XKWM6q1Q==',
    'userbrowserid': 'gdI43qLdRSeTXxxEVWjVlQ=='
}
print('request initiated')
response = requests.request("GET", url, headers=headers, data=payload)
print('request finished')
print(response.text)
