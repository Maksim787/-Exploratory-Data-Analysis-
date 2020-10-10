import pandas as pd
import matplotlib.pyplot as plt
import datetime

new_line = '\n' + '-' * 50 + '\n'
start_line = '-' * 50 + '\n'


def println(*args):
    print(start_line, *args, end=new_line)


# columns = ['DATE OCC', 'AREA NAME', 'Crm Cd Desc',
#               'Vict Age', 'Vict Sex', 'Vict Descent',
#               'Weapon Desc', 'LOCATION', 'Cross Street',
#               'LAT', 'LON']
# column_names = ['Date', 'Area', 'Type of crime',
#                    'Victim Age', 'Victim Sex', 'Victim Descent',
#                    'Weapon', 'Location', 'Cross Street',
#                    'Lat', 'Lon']

columns = ['DATE OCC', 'Crm Cd Desc', 'Weapon Desc']

column_names = ['Date', 'Type of crime', 'Weapon']

# df_2019 = pd.read_csv("https://data.lacity.org/api/views/63jg-8b9z/rows.csv")
df_2019 = pd.read_csv("Crime_Data_from_2010_to_2019.csv", usecols=columns)

# df_2020 = pd.read_csv("https://data.lacity.org/api/views/2nrs-mtv8/rows.csv")
df_2020 = pd.read_csv("Crime_Data_from_2020_to_Present.csv", usecols=columns)

# println(df_2019.columns)
# println(df_2019.head())

# println(df_2020.columns)
# println(df_2020.head())


# Названия столбцов
# println(df_2019.columns)
# println(df_2020.columns)

# Верхние 5 строк
# println(df_2019.head())
# println(df_2020.head())

df_2019['DATE OCC'] = pd.to_datetime(df_2019['DATE OCC'])
df_2020['DATE OCC'] = pd.to_datetime(df_2020['DATE OCC'])

df_2019 = df_2019[df_2019['DATE OCC'] <= pd.to_datetime("09/30/2019")]
df_2020 = df_2020[df_2020['DATE OCC'] <= pd.to_datetime("09/30/2020")]

df_2019 = df_2019[df_2019['DATE OCC'] >= pd.to_datetime("01/01/2019")]

df_2019.columns = column_names
df_2020.columns = column_names

# # Описание данных
# # println(df_2019.head())
# # println(df_2019.info())
# # println(df_2019.describe())
#
# # println(df_2020.head())
# # println(df_2020.info())
# # println(df_2020.describe())
#
# # Самые частые преступления
# # crime_type_2019 = df_2019['Type of crime'].value_counts()
# # println(crime_type1)
#
# # crime_type_2020 = df_2020['Type of crime'].value_counts()
# # println(crime_type)
#
# # Самое частое оружие
# # crime_weapon_2019 = df_2019['Weapon'].value_counts()
# # println(crime_weapon1)
# #
# # crime_weapon_2020 = df_2020['Weapon'].value_counts()
# # println(crime_weapon)
#
# # Тип: оружие или вид преступления.
# # an_object = "Type of crime"
# an_object = "Weapon"
#
# # Объект анализа:
# type_of_crime = "HAND GUN"
# # type_of_crime = "VEHICLE - STOLEN"
# # type_of_crime = "VANDALISM - FELONY ($400 & OVER, ALL CHURCH VANDALISMS)"
#
# used_df_2019 = df_2019[['Date', an_object]]
# used_df_2020 = df_2020[['Date', an_object]]
#
# used_df_2019 = used_df_2019[used_df_2019[an_object] == type_of_crime]
# used_df_2019.index = used_df_2019['Date']
# used_df_2019 = used_df_2019.groupby(used_df_2019.index.month).agg({'Date': 'first', an_object: 'count'})
# # println(used_df_2019)
#
# used_df_2020 = used_df_2020[used_df_2020[an_object] == type_of_crime]
# used_df_2020.index = used_df_2020['Date']
# used_df_2020 = used_df_2020.groupby(used_df_2020.index.month).agg({'Date': 'first', an_object: 'count'})
# # println(used_df_2020)
#
# used_df_2019['Date'] = used_df_2019['Date'].apply(lambda x: x.strftime("%m"))
# # println(used_df_2019)
#
# used_df_2020['Date'] = used_df_2020['Date'].apply(lambda x: x.strftime("%m"))
# # println(used_df_2020)
#
# plt.bar(used_df_2019['Date'], used_df_2019[an_object])
# plt.bar(used_df_2020['Date'], used_df_2020[an_object])
#
# plt.xticks(rotation=60)
# plt.title(type_of_crime)
# plt.show()
#

# ----------------------------------------------------------------------------
# Тип: оружие или вид преступления.
an_object = "Type of crime"
# an_object = "Weapon"

# Объект анализа:
list_of_types1 = [
    "INDECENT EXPOSURE",
    "BUNCO, PETTY THEFT",
    "CHILD ANNOYING (17YRS & UNDER)",
    "SHOPLIFTING - PETTY THEFT ($950 & UNDER)",
    "THEFT PLAIN - PETTY ($950 & UNDER)",
    "THEFT, PERSON",
    "ARSON",
    "ASSAULT WITH DEADLY WEAPON ON POLICE OFFICER",
    "BURGLARY",
    "VEHICLE - STOLEN",
    "VEHICLE - ATTEMPT STOLEN",
]
list_of_types2 = [
    "REVOLVER",
    "SEMI-AUTOMATIC PISTOL",
    "STICK",
    "UNKNOWN FIREARM",
    "VEHICLE"
]
list_of_types = list_of_types2
your_list = True
if not your_list:
    list_of_types = df_2020[an_object].value_counts().index
# ----------------------------------------------------------------------------

# Цикл для прочсёта преступлений >= 100
for type_of_crime in list_of_types:
    if your_list:
        if type_of_crime in df_2020["Type of crime"].value_counts().index:
            an_object = "Type of crime"
        elif type_of_crime in df_2020["Weapon"].value_counts().index:
            an_object = "Weapon"
        else:
            print()
            print("NOT FOUND: " + type_of_crime)
            print()

    used_df_2019 = df_2019[['Date', an_object]]
    used_df_2019 = used_df_2019[used_df_2019[an_object] == type_of_crime]
    used_df_2020 = df_2020[['Date', an_object]]
    used_df_2020 = used_df_2020[used_df_2020[an_object] == type_of_crime]
    print()
    print(type_of_crime)
    print("Count 2019:", used_df_2019.size)
    print("Count 2020:", used_df_2020.size)
    print()

    # if used_df_2019.size < 100:
    #     break

    used_df_2019.index = used_df_2019['Date']
    used_df_2019 = used_df_2019.groupby(used_df_2019.index.month).agg({'Date': 'first', an_object: 'count'})

    used_df_2020.index = used_df_2020['Date']
    used_df_2020 = used_df_2020.groupby(used_df_2020.index.month).agg({'Date': 'first', an_object: 'count'})

    # used_df_2019['Date'] = used_df_2019['Date'].apply(lambda x: x.strftime("%Y-%m"))
    # used_df_2020['Date'] = used_df_2020['Date'].apply(lambda x: x.strftime("%Y-%m"))
    # println(used_df_2019)
    # println(used_df_2020)
    # plt.bar(used_df_2019['Date'], used_df_2019[an_object])
    # plt.bar(used_df_2020['Date'], used_df_2020[an_object])

    used_df_2019['Date'] = used_df_2019['Date'].apply(lambda x: x.strftime("%m"))
    used_df_2020['Date'] = used_df_2020['Date'].apply(lambda x: x.strftime("%m"))
    plt.bar(used_df_2020['Date'], 100 * used_df_2020[an_object] / used_df_2019[an_object] - 100)
    plt.xticks(rotation=60)
    plt.ylabel("% change")
    plt.title(type_of_crime)
    plt.show()
