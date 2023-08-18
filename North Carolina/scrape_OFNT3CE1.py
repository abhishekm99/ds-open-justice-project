import pandas as pd

with open("OFNT3CE1.dat", "r") as file:
    data = file.read()

# for line in data.splitlines():
#     if len(line) > 1:
#         temp = {
#             "OFFENDER NC DOC ID NUMBER": line[0:0+7].strip(),
#             "COUNTY OF CONVICTION CODE": line[12:12+30].strip(),
#             "PRIMARY OFFENSE CODE": line[203:203+30].strip(),
#             "DATE OFFENSE COMMITTED - BEGIN": line[263:263+10].strip(),
#             "DATE OFFENSE COMMITTED - END": line[273:273+10].strip(),
#             "PRIMARY FELONY/MISDEMEANOR CD.": line[298:298+30].strip(),
#             "PRIOR RCD. POINTS/CONVICTIONS": line[358:358+3].strip(),
#             "MINIMUM SENTENCE LENGTH": line[391:391+7].strip(),
#             "MAXIMUM SENTENCE LENGTH": line[398:398+7].strip(),
#             "CREDITS FOR JAIL DAYS SERVED": line[650:650+5].strip(),
#             "SENTENCE CONVICTION DATE": line[760:760+10].strip(),
#             "SENTENCE EFFECTIVE(BEGIN) DATE": line[770:770+10].strip(),
#             "DATE OF LAST UPDATE": line[861:861+10].strip(),
#         }
#     break
# print(temp)

df = pd.DataFrame(
    [
        {
            "OFFENDER NC DOC ID NUMBER": line[0:0+7].strip(),
            "COUNTY OF CONVICTION CODE": line[12:12+30].strip(),
            "PRIMARY OFFENSE CODE": line[203:203+30].strip(),
            "DATE OFFENSE COMMITTED - BEGIN": line[263:263+10].strip(),
            "DATE OFFENSE COMMITTED - END": line[273:273+10].strip(),
            "PRIMARY FELONY/MISDEMEANOR CD.": line[298:298+30].strip(),
            "PRIOR RCD. POINTS/CONVICTIONS": line[358:358+3].strip(),
            "MINIMUM SENTENCE LENGTH": line[391:391+7].strip(),
            "MAXIMUM SENTENCE LENGTH": line[398:398+7].strip(),
            "CREDITS FOR JAIL DAYS SERVED": line[650:650+5].strip(),
            "SENTENCE CONVICTION DATE": line[760:760+10].strip(),
            "SENTENCE EFFECTIVE(BEGIN) DATE": line[770:770+10].strip(),
            "DATE OF LAST UPDATE": line[861:861+10].strip(),
        }
        for line in data.splitlines()
        if len(line) > 1
    ]
)

print(df.head())
df.to_csv('county_details.csv')