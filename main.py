import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("marriage_divorce_india_with_id.csv")

#Chaging currency type; INR to USD
df["Income Level (INR per month)"] = df["Income Level (INR per month)"] * 0.012
df.rename(columns={"Income Level (INR per month)":"Income Level (USD per month)"}, inplace=True)

df_qualitative_variables = df[["Marriage Type", "Education Level", "Caste/Religion", "Urban/Rural", "Family Involvement", "Divorce Status"]]

content = {
    "Christian": df_qualitative_variables[df_qualitative_variables["Caste/Religion"] == "Christian"].sum(),
    "Hindu": df_qualitative_variables[df_qualitative_variables["Caste/Religion"] == "Hindu"].sum(),
    "Jain": df_qualitative_variables[df_qualitative_variables["Caste/Religion"] == "Jain"].sum(),
    "Muslim": df_qualitative_variables[df_qualitative_variables["Caste/Religion"] == "Muslim"].sum(),
    "Other": df_qualitative_variables[df_qualitative_variables["Caste/Religion"] == "Other"].sum(),
    "Sikh": df_qualitative_variables[df_qualitative_variables["Caste/Religion"] == "Sikh"].sum()
}
labels_castel = list(content.values())

fig, ax = plt.subplots(
    figsize=(10,5)
)

ax.stackplot(range(len(labels_castel)), list(content.values()), labels=labels_castel)
ax.legend(loc='upper left', reverse=True)
ax.set_ylabel("Quantity")
ax.set_xlabel("Caste/Religion")
plt.show()