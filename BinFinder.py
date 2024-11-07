import pandas as pd
import requests
from openpyxl import load_workbook

# Load the Excel file
file_path = 'your_excel_file.xlsx'
df = pd.read_excel(file_path)

# Define the API endpoint and headers
api_endpoint = 'https://a810-dobnow.nyc.gov/Publish/WrapperPP/PublicPortal.svc/getPublicPortalBinDetailsFromBisGet/'  # Replace with your API endpoint
headers = {
    'Authorization': 'Bearer your_token',
    'Accept': '*/*',
    'Cookie': '_ga_W77SGPGVEF=GS1.1.1685712955.5.0.1685712955.0.0.0; '
              '_ga_RTXXDWQQS0=GS1.1.1685712955.5.0.1685712955.0.0.0; '
              '_ga_TVM7LC4V3D=GS1.1.1691063659.6.0.1691063664.0.0.0; '
              '_ga_F2HZY1HS3P=GS1.1.1691741051.1.0.1691741054.0.0.0; '
              'RT="z=1&dm=a810-dobnow.nyc.gov&si=a7146b30-185c-402f-a6ed-35b347a580b4&ss=lnk63z21&sl=0&tt=0"; '
              'RT="z=1&dm=nyc.gov&si=87e0hr1f8bm&ss=lnsjgyq6&sl=0&tt=0"; '
              '_ga_K9V6JKDZGX=GS1.1.1697450373.8.0.1697450375.0.0.0; '
              'NSC_mc_qfstjtuhspvq_dppljf=ffffffff9eb44f1c45525d5f4f58455e445a4a42378b; '
              '_abck=3E7B12FDA25395D8287FE4701760F5AC~0~YAAQO3xBF9YtrzeLAQAAGrlvPArH+391iGexVHZVH+LyegbHgmFszoyRtHH0v'
              '/keuMGT7kobVinfPwhUBtIq5UntrWjqjqVuRt3Ow4YCrTlsA0hLMPIYnUq7NARBCL3mUS0ymWVcCFua3c5EY66T9fVGLoYnVyTcDmly0P4UBI7kVP65arzBcX6iK+fh3jPkRDC+dHU+qzyfxd7OGMj7+3QG/ooU3TY7r/aF8JV4c5fcGpySuR6uqhSurZPiMisUYUI1eyg32KH9eyR2EvZVqDdPfXCxj9ZcrzCw02LULQ/E+nHFif+dSe/iI5wqOLnvsynSBQY3j9Y0cmMP+ECp/ko5RAsY8B+eisl/dM/L3WcVc+j68DPqhfX9qoo3hghxUDeeZ0V4JOpf8RyqSNgcFQ7Oc8vV~-1~-1~-1; bm_sz=38428A16CA3E657552909CDDF215A2CF~YAAQO3xBF9ktrzeLAQAAGrlvPBXdqYS3Dzrv4XlVSu9nH1JVwzl5dzy1Wb+5fqRrlcoYRDjCttl1tlXw8ZJQIvHkYf2rh4z9CQ/xC2ndLq7q4LjEXzCA3F0O08qNv7xSc/4fwAzwAoEWcZq4vL8SPNiNzlWXVNDQD6wff7HDmh7mk/vnYZ3QwkewZESmr6oTT4kYVI1GpLc6Pzp6QTvsl/6f2at8C5gXXci0sepAfuOjtPIx+Qw5DWMxQeG7xLkStipn+KifGRV+XBWl9ddzXEM9sTztRM/mofmzdWXHVXM=~3749173~4536390; _ga_863DM8YSJL=GS1.1.1697526037.12.0.1697526037.0.0.0; _ga=GA1.2.609920701.1682577764; _gid=GA1.2.906844422.1697526038; _gat_gtag_UA_128025137_1=1; bm_mi=15DF1B9B042DC987E59BCC3EEE8B3EF4~YAAQO3xBFxMvrzeLAQAANcJvPBX1E/UARSJ5YMkOJAMu0j83QNnxycR6+hUf5OdWpnxFk40e5ycsqeWgRqBCrg28CCd54LDMkPw5OvNZwFR5LfFuJeY442B/lAiBiE2bF4/HXHt91zojXpBWccEI0enzLoW248SYkxlbobIG9zRIbJp0Uttes+zFHDS48Zv2PTfI6yq1LGGbTrdIk72wEI17mxSKa60QqlhxDzS/r60P8zc2HxC02/sUv+CaEP4Yl4gG0V7lLQYMDTRF7VQmWywC/aolq0Kono9vFYwACZqOxU4LiU6ardMf0+wX6sPA1bdbzgo7HQoiJcbR7ZUEMISrYgKuDNKH~1; ASP.NET_SessionId=xnzwial1bkwxoyby2z0xsp5b; amp_6e403e=lwNsLa64O3lNBxWNGrPD1l.cHBhdGVsLmRhdGFzb3NAZ21haWwuY29t..1hcu6vj9s.1hcu6vj9s.0.1.1; ak_bmsc=F6F495CACE917298AE3591068F2FA5EE~000000000000000000000000000000~YAAQO3xBF+8wrzeLAQAAU9FvPBVZDhs+qcnVWrz/T9fCuxtEVtaMy3kVX07A9MLd/Fd5FBQQpu2rJCjntCRz5hkusKE58BW65VnBIraIGTvFvgX2m6wZpWbkpsXF8AZzhoBCK0DOlAvg0QoK/0fZEKDx22coC8Dx8BTwDxBErv4A9Y+WPAWGwqVkt9JvPcAbsAsjo/9u3IW+VZ75KDQLGzrmNjP/l/aM7oQKvi9IDKdprS0TDptkL81xBtaYxtqO+/Q5M94+vUu4++jVqH1gep5tud35RnZ2bo/636Pmok+JNpu7gxW69Zw2mRcG5ISM7hWMjZKTv7OedfpsKuGop3SGqeOjaIfgMiVAsozEvavHVqNjTWJy9sJSfUt0rwLA7g+UisUmlNfixpUufPvl87YJhfLmixssxcNEPUyVEB8AIGG3Ytaloi2qlywJJOvnNF/d8WKeXWM9G+aQPOfqvAjO0fdBSm2wzv6/CL1sgDl3WGeW4uoozleOg8SFMGuUDz8lepmzpoJi76VblO4BwYXYRgRyusLBzj8Cz7tleerjZg==; bm_sv=5E27351CDFA2FF6EC42ED9B009D7BA73~YAAQO3xBFyE0rzeLAQAATe1vPBULQQZM5sA6pygl2RjdhPVH+/o1csTmWzcvk9cDnHoPj3QBkVZDpPux3GaGEu0Zu2vkkGiSFUcU6B4Aqx5Q6jOZc24FJl4MbvuyPQHPQNLG3JavjTWxRg68Aj3EyeG0NTfNL5eMbAG/Ses3JVoxlHPhldoLiNSMNEsp69i/xuGPKIKZmJAaybdntE5zorr8l85thdQUjA6c16n8oT/PNRpEDw5TNLxDRtrW~1',
    'userbrowserid': 'gdI43qLdRSeTXxxEVWjVlQ=='
    # Replace with your API token
}


# Function to make API requests and extract BIN numbers
def get_bin_numbers(row):
    url = f"{api_endpoint}/{row['Borough']}%7C{row['block']}%7C{row['Lot']}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return ', '.join(data.get('BINs', []))
    else:
        return ''


# Apply the function to each row
df['BINs'] = df.apply(get_bin_numbers, axis=1)

# Update the Excel file with the new data
with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
    writer.book = load_workbook(file_path)
    df.to_excel(writer, sheet_name='Sheet1', index=False)

print("BIN numbers updated in the Excel file.")
