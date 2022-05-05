# Basic Formatting, List of Data Elements and Locations
# Input is based on specified values in https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/fetaldeath/2020fetaluserguide.pdf
# Rules are specified as an (unsorted) list of tuples, each tuple consists of 3 values
# 1 (String) Data Item Label (Use Colons to Denote Sub-Categories, Use NO SPACES)
# 2 (Integer) Location Start
# 3 (Integer) Location Stop (End of Range, or Repeat Start Location if Not Specified)

def Fetal_2020():
	Fetal_2020 = [
		('Version', 7, 7),
		('GEN:Tabulation_Flags', 10, 10),
		('GEN:Data_Year', 11, 14),
		('GEN:Data_Month', 15, 16),
		('GEN:Delivery_Time', 21, 24),
		('GEN:Day_of_Week', 25, 25),
		('GEN:Territory_of_Occurence', 26, 27), # P.30
		('GEN:Occurence_FIPS_County', 30, 32), # P.30
		('GEN:Occurence_County_Population', 33, 33), # P.30
		('GEN:Delivery_Place_Revised', 34, 34), # P.30
		('GEN:Delivery_Place_Recoded', 52, 52), # P.31
		('GEN:Record_Type', 130, 130), # P.36 UNCLEAR as to IF applies to MOTHER or FETUS
		('GEN:Residency_Status', 131, 131), # P.36
		('PRENATAL:Month_Began', 202, 203),
		('MOTHER:Age_Imputed', 84, 84), # P.31
		('MOTHER:Reported_Age', 85, 85), # P.31
		('MOTHER:Age:Single_Year', 86, 87), # P.31
		('MOTHER:Age:Recode_14', 88, 89), # P.32
		('MOTHER:Age:Recode_9', 90, 90), # P.32
		('MOTHER:Age:Extended', 86, 90), # Pointless; See *Single_Year, *Recode_9, *Recode_14
		('MOTHER:Birth_Country', 91, 92), # P.33
		('MOTHER:Birth_State_Recode', 97, 97), # P.33
		('MOTHER:Residence_Postal_State', 102, 103), # P.33
		('MOTHER:FIPS_County', 104, 106), # P.34
		('MOTHER:County_Population', 112, 112), # P.34
		('MOTHER:Race:Extended', 132, 136), # Pointless; See *Recode_6, *Recode_15, *Recode_31
		('MOTHER:Race:Recode_31', 132, 133), # P.37
		('MOTHER:Race:Recode_6', 134, 134), # P.38
		('MOTHER:Race:Recode_15', 135, 136), # P.38
		('MOTHER:Race_Imputed', 138, 138), # P.38
		('MOTHER:Hispanic_Origin:Extended', 142, 144), # P.39 Lines 139-141 are Filler, See *I, *II, *III
		('MOTHER:Hispanic_Origin:I', 142, 142), # P.38
		('MOTHER:Hispanic_Origin:II', 143, 143), # P.39
		('MOTHER:Hispanic_Origin:III', 144, 144), # P.39
		('MOTHER:Education_Revised', 145, 145),
		('MOTHER:Height_Inches', 243, 244), # P.42
		('FATHER:Age:Extended', 177, 180), # Redundant, See *Reported_Age_Used, *Combined_Age, *Reported_Age_Recoded_11
		('FATHER:Age:Reported_Age_Used', 172, 172), # P.40
		('FATHER:Age:Combined_Age', 177, 178), # P.40
		('FATHER:Age:Reported_Age_Recoded_11', 179, 180), # P.40
		('PREGNANCY:Prior_Births_Now_Living', 181, 182), # P.40
		('PREGNANCY:Prior_Births_Now_Dead', 183, 184), # P.40
		('PREGNANCY:Live_Birth_Order_Recode', 187, 187),
		('PREGNANCY:Birth_Interval_Extended', 197, 201), # Pointless; See *Interval_Since_*
		('PREGNANCY:Interval_Since_Last_Live_Birth_Recode', 197, 199), # P.41
		('PREGNANCY:Interval_Since_Last_Live_Birth_Recode_11', 200, 201), # P.41
		('PREGNANCY:Month_Prenatal_Care_Began_Revised', 202, 203), # P.41
		('PREGNANCY:Month_Prenatal_Care_Began_Recode_Revised', 204, 204), # P.41
		('OTHER:Place_of_Delivery', 34, 52), # Pointless, See 'GEN:Delivery_Place_Revised'. Per P.31, Lines 53-83 are Filler
		('OTHER:WIC_Receipt', 229, 229),
		('MEDICAL:Cigarettes:Tobacco_Extended', 230, 238), # Pointless; See *Cigarette*
		('MEDICAL:Cigarettes:Before_Pregnancy', 230, 231), # P.42
		('MEDICAL:Cigarettes:1st_Trimester', 232, 233), # P.42
		('MEDICAL:Cigarettes:2nd_Trimester', 234, 235), # P.42
		('MEDICAL:Cigarettes:3rd_Trimester', 236, 237), # P.42
		('MEDICAL:Cigarette:Recode_Revised', 238, 238), # P.42
		('MEDICAL:PrePregnancy_BMI_Extended', 245, 249), # Pointless Redundant, See *Cigarette*
		('MEDICAL:PrePregnancy_BMI', 245, 248), # P.42
		('MEDICAL:PrePregnancy_BMI_Recode', 249, 249), # P.42
		('MEDICAL:PrePregnancy_Weight_Recode', 253, 255), # P.43
		('MEDICAL:Risk_Factors_Revised:Extended', 257, 262), # Pointless Redundant, See [Below]
		('MEDICAL:Risk_Factors_Revised:Prepregnancy_Diabetes', 257, 257), # P.43
		('MEDICAL:Risk_Factors_Revised:Gestational_Diabetes', 258, 258), # P.43
		('MEDICAL:Risk_Factors_Revised:Prepregnancy_Hypertension', 259, 259), # P.43
		('MEDICAL:Risk_Factors_Revised:Gestational_Hypertension', 260, 260), # P.43
		('MEDICAL:Risk_Factors_Revised:Hypertension_Eclampsia', 261, 261), # P.43
		('MEDICAL:Risk_Factors_Revised:Infertility_Treatment', 262, 262), # P.43
		('MEDICAL:Fertility_Enhancing_Drugs', 263, 263), # P.43
		('MEDICAL:Asst_Reproductive_Technology', 264, 264), # P.43
		('MEDICAL:Previous_Cesareans', 265, 265), # P.43
		('MEDICAL:Previous_Cesareans_Num', 266, 267), # P.44
		('MEDICAL:Method_of_Delivery_Revised:Extended', 274, 277), # P.44
		('MEDICAL:Method_of_Delivery_Revised:Fetal_Presentation', 274, 274), # P.44
		('MEDICAL:Method_of_Delivery_Revised:Route_and_Method_of_Delivery', 275, 275), # P.44
		('MEDICAL:Method_of_Delivery_Revised:Trial_of_Labor_Attempted', 276, 276), # P.44
		('MEDICAL:Method_of_Delivery_Revised:Delivery_Method_Recode_Revised', 277, 277), # P.44
		('MEDICAL:Method_of_Delivery_Recode', 280, 280),
		('MEDICAL:Maternal_Morbidity:Extended', 281, 282), # Pointless Redundant, See [Below]
		('MEDICAL:Maternal_Morbidity:Ruptured_Uterus', 281, 281), # P.45
		('MEDICAL:Maternal_Morbidity:Admit_to_Intensive_Care', 282, 282), # P.45
		('MEDICAL:Attendant_at_Delivery', 283, 283), # Re-Classified from OTHER to MEDICAL
		('MEDICAL:Plurality_Recode', 283, 283), # P.45
		('FETUS:Month_Year_of_Delivery', 11, 16), # Redundant, See 'GEN:Data_Year' 'GEN:Data_Month'
		('FETUS:Time_of_Delivery', 21, 24), # Redundant, See 'GEN:Delivery_Time'
		('FETUS:Day_of_Week_of_Delivery', 25, 25), # Redundant, See 'GEN:Day_of_Week'
		('FETUS:Plurality', 301, 301),
		('FETUS:Plurality_Imputed', 303, 303),
		('FETUS:Sex', 316, 316),
		('FETUS:Sex_Imputed', 317, 317), # P.46
		('GESTATION:Last_Normal_Menses_Month', 318, 319), # P.46
		('GESTATION:Last_Normal_Menses_Year', 322, 325), # P.46
		('GESTATION:Gestation_Imputed', 329, 329), # P.46
		('GESTATION:Obstentric_Estimate_of_Gestation_Used', 330, 330), # P.46
		('GESTATION:Extended', 331, 335),
		('GESTATION:Detail_in_Weeks', 331, 332), # P.46
		('GESTATION:Recode_12', 333, 334), # P.47
		('GESTATION:Recode_5', 335, 335), # P.47
		('GESTATION:Obstentric_Gestation', 336, 337), # P.47
		('GESTATION:Combined_Gestation_Used', 338, 338), # P.47
		('GESTATION:Estimate_Extended', 340, 344), # Redundant, See 'Obstentric_Estimate_Edited', 'Combined_Estimate_*'
		('GESTATION:Obstentric_Estimate_Edited', 340, 341), # P.47
		('GESTATION:Combined_Estimate_Recode_12', 342, 343), # P.47
		('GESTATION:Combined_Estimate_Recode_5', 344, 344), # P.48
		('FETUS:Weight:Extended', 349, 355), # Redundant, See [Below]
		('FETUS:Weight:Detain_in_Grams', 349, 352), # P.48
		('FETUS:Weight:Recode_14', 353, 354), # P.48
		('FETUS:Weight:Recode_4', 355, 355), # P.48
		('FETUS:Estimated_Time_of_Death', 357, 357), # P.49
		('FETUS:Autopsy_Performed', 358, 358), # P.49
		('FETUS:Histological_Placental_Exam_Performed', 359, 359), # P.49
		('FETUS:Results_Used_in_Cause', 360, 360), # P.49
		('Residence_Reporting_Flags', 372, 440), # TODO Expand These
		('CAUSE:Initiating_Cause_Condition_Code', 2603, 2607),
		('CAUSE:Initiating_Fetal_Recode', 2643, 2645),
		('CAUSE:Initiating_Cause_Condition_Flag', 2651, 2651),
		]
	return Fetal_2020