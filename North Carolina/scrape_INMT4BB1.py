import pandas as pd

with open("INMT4BB1.dat", "r") as file:
    data = file.read()

# for line in data.splitlines():
#     if len(line) > 1:
#         temp = {
#             "INMATE DOC NUMBER": line[0:0+7].strip(),
#             "INMATE COMMITMENT PREFIX": line[7:7+2].strip(),
#             "INMATE SENTENCE COMPONENT": line[9:9+3].strip(),
#             "INMATE COMPUTATION STATUS FLAG": line[12:12+30].strip(),
#             "SENTENCE BEGIN DATE (FOR MAX)": line[42:42+10].strip(),
#             "ACTUAL SENTENCE END DATE": line[52:52+10].strip(),
#             "PROJECTED RELEASE DATE (PRD)": line[62:62+10].strip(),
#             "PAROLE DISCHARGE DATE": line[72:72+10].strip(),
#             "PAROLE SUPERVISION BEGIN DATE": line[82:82+10].strip(),
#         }
#     break
# print(temp)

df = pd.DataFrame(
    [
        {
            "INMATE DOC NUMBER": line[0:0+7].strip(),
            "INMATE COMMITMENT PREFIX": line[7:7+2].strip(),
            "INMATE SENTENCE COMPONENT": line[9:9+3].strip(),
            "INMATE COMPUTATION STATUS FLAG": line[12:12+30].strip(),
            "SENTENCE BEGIN DATE (FOR MAX)": line[42:42+10].strip(),
            "ACTUAL SENTENCE END DATE": line[52:52+10].strip(),
            "PROJECTED RELEASE DATE (PRD)": line[62:62+10].strip(),
            "PAROLE DISCHARGE DATE": line[72:72+10].strip(),
            "PAROLE SUPERVISION BEGIN DATE": line[82:82+10].strip(),
        }
        for line in data.splitlines()
        if len(line) > 1
    ]
)

print(df.head())
df.to_csv('sentence_and_release_details.csv')