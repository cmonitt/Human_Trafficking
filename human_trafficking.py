import pandas as pd
import numpy as np
import pyarrow.feather as feather
import plotly.express as pl
import plotly.graph_objects as go

# creates a new df to change df_ht ISO2 to ISO3 for plotly
iso_data = pd.read_feather(r"C:\DataSci\Projects\Data Practice\ht_region_lookup.ft")
iso_data = iso_data[['ISO2', 'ISO3']]
# converts df to dict for easy replace function
iso_dict = dict(iso_data.values)

# creates new df_ht
df_ht = pd.read_feather(r"C:\DataSci\Projects\Data Practice\ht.ft")
# replaces ISO2 to ISO3 for citizenship
df_ht = df_ht.replace({"citizenship": iso_dict})

bool_names = [ 'majorityStatusAtExploit', 'majorityEntry', 'meansOfControlDebtBondage', 
                 'meansOfControlTakesEarnings', 'meansOfControlRestrictsFinancialAccess', 'meansOfControlThreats', 'meansOfControlPsychologicalAbuse', 'meansOfControlPhysicalAbuse', 
                 'meansOfControlSexualAbuse', 'meansOfControlFalsePromises', 'meansOfControlPsychoactiveSubstances', 'meansOfControlRestrictsMovement', 
                 'meansOfControlRestrictsMedicalCare', 'meansOfControlExcessiveWorkingHours', 'meansOfControlUsesChildren', 'meansOfControlThreatOfLawEnforcement', 
                 'meansOfControlWithholdsNecessities', 'meansOfControlWithholdsDocuments', 'meansOfControlOther', 'meansOfControlNotSpecified', 
                 'isForcedLabour', 'isSexualExploit', 'isOtherExploit', 'isSexAndLabour', 'isForcedMarriage', 'isForcedMilitary', 'isOrganRemoval', 'isSlaveryAndPractices', 
                 'typeOfLabourAgriculture', 'typeOfLabourAquafarming', 'typeOfLabourBegging', 'typeOfLabourConstruction', 'typeOfLabourDomesticWork', 
                 'typeOfLabourHospitality', 'typeOfLabourIllicitActivities', 'typeOfLabourManufacturing', 'typeOfLabourMiningOrDrilling', 'typeOfLabourPeddling', 
                 'typeOfLabourTransportation', 'typeOfLabourOther', 'typeOfLabourNotSpecified', 'typeOfSexProstitution', 'typeOfSexPornography', 
                 'typeOfSexRemoteInteractiveServices', 'typeOfSexPrivateSexualServices', 'isAbduction', 'recruiterRelationIntimatePartner', 
                 'recruiterRelationFriend', 'recruiterRelationFamily', 'recruiterRelationOther', 'recruiterRelationUnknown']
col_categ = ['Datasource', 'gender', 'ageBroad', 'majorityStatus',  'citizenship','yearOfRegistration','RecruiterRelationship', 'CountryOfExploitation', ]
citizenship= ([])
drop_col = ['gender', 'ageBroad', 'typeOfExploitConcatenated', 'meansOfControlConcatenated', 'typeOfLabourConcatenated', 'typeOfSexConcatenated']


def main():
    """main function"""
    # change last two parameters to change what years you want to look between
    # leave last one blank for just one year
    make_df_year(df_ht, 2002, 2021)

def make_map(df, year:str):
    """Given dataframe ir will make the world heat map"""
    # creates figure
    fig = go.Figure(data=go.Choropleth(locations = df['citizenship'], z = df['Count'], colorscale='Inferno', autocolorscale=True))
    # changes title
    fig.update_layout(title={'text':f'<b>Human-Trafficking Heatmap based on victims citizenship for {year}'})
    fig.show()
    return

def make_df_year(df, start_y, ending_y = 0):
    """Given the year it will make a dataframe with only the given year"""
    years = []
    # make list of available years to check the input is correct
    for year in np.sort(df['yearOfRegistration'].unique()):
        years.append(year)
    # print(f'years list: {years}')
    # check if only one year
    if ending_y == 0:
        if start_y in years:
            year_df = df.loc[df['yearOfRegistration'] == start_y]
            year_df = year_df.groupby(['citizenship'])['citizenship'].count().reset_index(name='Count')
            make_map(year_df, str(start_y))
            return
        else:
            print("Can't")
    # between years
    else:
        if start_y in years and ending_y in years:
            year_df = df[df['yearOfRegistration'].between(start_y, ending_y)]
            year_df = year_df.groupby(['citizenship'])['citizenship'].count().reset_index(name='Count')
            make_map(year_df, f'{start_y} to {ending_y}')
            return
        else:
            print("Can't")

main()