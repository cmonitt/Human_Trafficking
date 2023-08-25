import pandas as pd
import pyarrow.feather as feather

col_raw = """yearOfRegistration	Datasource	gender	ageBroad	majorityStatus	majorityStatusAtExploit	majorityEntry	citizenship	meansOfControlDebtBondage	meansOfControlTakesEarnings	
meansOfControlRestrictsFinancialAccess	meansOfControlThreats	meansOfControlPsychologicalAbuse	meansOfControlPhysicalAbuse	meansOfControlSexualAbuse	meansOfControlFalsePromises	
meansOfControlPsychoactiveSubstances	meansOfControlRestrictsMovement	meansOfControlRestrictsMedicalCare	meansOfControlExcessiveWorkingHours	meansOfControlUsesChildren	
meansOfControlThreatOfLawEnforcement	meansOfControlWithholdsNecessities	meansOfControlWithholdsDocuments	meansOfControlOther	meansOfControlNotSpecified	meansOfControlConcatenated	
isForcedLabour	isSexualExploit	isOtherExploit	isSexAndLabour	isForcedMarriage	isForcedMilitary	isOrganRemoval	isSlaveryAndPractices	typeOfExploitConcatenated	
typeOfLabourAgriculture	typeOfLabourAquafarming	typeOfLabourBegging	typeOfLabourConstruction	typeOfLabourDomesticWork	typeOfLabourHospitality	typeOfLabourIllicitActivities	
typeOfLabourManufacturing	typeOfLabourMiningOrDrilling	typeOfLabourPeddling	typeOfLabourTransportation	typeOfLabourOther	typeOfLabourNotSpecified	typeOfLabourConcatenated	
typeOfSexProstitution	typeOfSexPornography	typeOfSexRemoteInteractiveServices	typeOfSexPrivateSexualServices	typeOfSexConcatenated	isAbduction	RecruiterRelationship	
CountryOfExploitation	recruiterRelationIntimatePartner	recruiterRelationFriend	recruiterRelationFamily	recruiterRelationOther	recruiterRelationUnknown
"""
col1_raw = "ISO2	ISO3	Country	Countrydescription	UNRegion	UNSubRegion	IOMRegion"

col_list = [x.strip() for x in col_raw.split()]
DATA_PATH = r"C:\DataSci\Projects\Data Practice\The Global K-anon Dataset 15 July 2021.xlsx"
DATA_REGION_PATH = r"C:\DataSci\Projects\Data Practice\CTDC Global K-anon Dataset DATA DICTIONARY version 20210825.xlsx"


xlsx = pd.ExcelFile(DATA_PATH)
df_xlsx = xlsx.parse(sheet_name="CTDC_K_anon_ds", names=col_list)
df_xlsx.to_feather(r"C:\DataSci\Projects\Data Practice\ht.ft")

col1_list = [x.strip() for x in col1_raw.split()]
xlsx1 = pd.ExcelFile(DATA_REGION_PATH)
df_xlsx1 = pd.read_excel(xlsx1, sheet_name="Region")
df_xlsx1.to_feather(r"C:\DataSci\Projects\Data Practice\ht_region_lookup.ft")