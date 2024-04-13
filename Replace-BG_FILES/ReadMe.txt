T1D Exchange
Link to public website: 



Contents of this document:
1. Tables Used in the Case Report Forms – The Case Report Forms folder, in the downloaded zip file, contains PDF files which were used to collect data during the study. The data from these forms were deposited into the tables in the Data Tables folder. The tables used in each CRF are listed below. Fields that were deemed unnecessary for analysis are not included in public data tables (e.g. tracking and administrative information). 

All patient IDs and dates have been de-identified. Some data which may contain identifiable information is not contained within the data files.

2. Table Descriptions & Data Source – The Data Tables folder, in the downloaded zip file, contains the data collected from the study. Each table’s description and data source are listed below.

3. Data Glossary – The data glossary is to be used in conjunction with the CSV files in the Data Tables folder, which is included in the downloaded zip file. The data glossary contains one table per CSV file and gives a description of each field found in the CSV file. 


1. Tables Used in the Case Report Forms

Case Report Form
Table Used
crfAdvEvent.pdf
tblHAdvEvent
crfDeviceProblems.pdf
tblHAEDeviceProblems
crfCompUnblindCGM.pdf
tblHCompUnblindCGM
crfDeviceDtTmVer.pdf
tblHDeviceDtTmVer
crfDeviceIssue.pdf
tblHDeviceIssue
crfDKAEvent.pdf
tblHDKAEvent
crfFollowUp.pdf
tblHFollowUp
crfHypoEvent.pdf
tblHHypoEvent
cftInitialStudyCGM.pdf
tblHInitialStudyCGM
crfInsulin.pdf
tblHInsulin
crfLocalHbA1c.pdf
tblHLocalHbA1c
crfMedicalCondition.pdf
tblHMedicalCondition
crfMedication.pdf
tblHMedication
crfPostRandPtFinalStatus.pdf
tblHPostRandPtFinalStatus
crfQuestDiabTech.pdf
tblHQuestDianTech
crfQuestHypoFear.pdf
tblHQuestHypoFear
crfQuestHypoUnaware.pdf
tblHQuestHypoUnaware
crfRandomization.pdf
tblHRamdonmization
crfRunInVisitStatus.pdf
tblHRunInVisitStatus
crfScreening.pdf
tblHScreening
crfUnsheduledVisit.pdf
tblHUnschedVisit
crfVisitInfo.pdf
tblHVisitInfo

2. Table Descriptions & Data Source 

Table
Description
Data Source
HAdvEvent
One record per Adverse Event Form
crfAdvEvent.pdf
HAEDeviceProblems
One record per Adverse Event and Device Problem form submitted
crfDeviceProblems.pdf
HComplUnblindCGM
One record per Compliance and Initiation of Standard CGM form submitted
crfCompUnblindCGM.pdf
HDeviceBGM
One record per bgm or ketone reading
Protocol H BGM data (Meter and Ketone datp
HDeviceBolus
One record per bolus reading from a pump
Protocol H Pump Bolus data
HDeviceCGM
One record per CGM reading
Protocol H CGM data
HDeviceDtTmVer
One record per Device Date Time Verification form submitted
crfDeviceDtTmVer.pdf
HDeviceEvents
One Record per Device Event
Protocol H Device Events Data
HDeviceIssue
One record per subject per device incident
crfDeviceIssue.pdf
HDeviceUploads
One record per device upload
Protocol H Device Upload information
HDeviceWizard
One record per pump wizard reading
Protocol H Pump Wizard data
HDKAEvent
One record per DKA event form submitted
crfDKAEvent.pdf
HFollowUp
One record per Follow Up visit form submitted
crfFollowUp.pdf
HHypoEvent
One record per Hypoglycemic Event submitted
crfHypoEvent.pdf
HInitialStudyCGM
One record per Initial Study CGM form submitted
cftInitialStudyCGM.pdf
HInsulin
One record per Insulin type per patient
crfInsulin.pdf
HLocalHbA1c
One record per Local HbA1c form submitted
crfLocalHbA1c.pdf
HMedicalCondition
One record per medical condition form
crfMedicalCondition.pdf
HMedication
One record per medications form
crfMedication.pdf
HPostRandPtFinalStatus
One record per Post Rand Final Status form submitted
crfPostRandPtFinalStatus.pdf
tblHPtRoster
One record per Protocol H PtID obtained
Protocol H Roster
HQuestDiabTech
One record per Diabetes Technology Questionnaire submitted
crfQuestDiabTech.pdf
HQuestHypoFear
One record per Hypoglycemia Fear Survey submitted
crfQuestHypoFear.pdf
HQuestHypoUnaware
One record per Clarke Hypoglycemia Unawareness Survey completed
crfQuestHypoUnaware.pdf
HRandomization
One record per Randomization form submitted
crfRandomization.pdf
HRunInVisitStatus
One record per Run In Visit Status form submitted
crfRunInVitalStatus.pdf
Sample
One record per sample per participant per draw type
No CRF
HScreening
One record per Screening form submitted
crfScreening.pdf
HUnschedVisit
One record per Unscheduled Visit form submitted
crfUnscheduledVisit.pdf
HVisitInfo
Visit Information Form
crfVisitInfo.pdf


3. Data Glossary

HAdvEvent 
Description - One record per Adverse Event Form
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



PtID
varchar
Patient Identifier
NO



SiteId 
Int
Site Identifier
NO



AENotifiedDaysFromEnroll
Int
AE Notification days after enrollment
NO



AdverseEventType
varchar
If ocular event, select eye
YES


OD => OD(Right), OS => OS(Left)
AEOnsetDaysFromEnroll
Int
AE Onset date number of days after enrollment
NO



AEPrEnroll
varchar
Is the adverse event a worsening of a pre-existing condition present prior to study entry
NO


Yes, No
AENotedStdyVisExam
varchar
Was the adverse event an abnormality (or worsening of an existing abnormality) identified on a study visit exam
NO


Yes, No
AEIntensity
varchar
Maximum intensity (Severity)
NO


Mild, Moderate, Severe
AERelStdyTrtUncertain
tinyint
Uncertain which treatment/study device caused event
YES


1 => Checked
AERelStdyProc
varchar
Is there a reasonable possibility that the event was caused by a study procedure
NO


Yes, No
AEEffectTrt
varchar
Effect on study treatment/device
NO


No change, Discontinued temporarily, Discontinued permanently, Reduced dose => If study treatment is medication, reduced dose, Reduced use frequency/schedule
AESerious
varchar
Does the event meet criteria for a serious adverse event
NO


Yes, No
AETrt
varchar
Did patient receive treatment for the Adverse Event
NO


Yes, No
AESurg
varchar
Surgery/procedure
YES


Yes, No
AESurgDaysFromEnroll
Int
AE Surgery number of days after enrollment
YES



AEMeds
varchar
Medication
YES


Yes, No
AEOthTrt
varchar
Other Treatment of Adverse Event
YES


Yes, No
AEOutcome
varchar
Outcome
NO


Ongoing (further improvement / worsening possible) => Ongoing (further improvement or worsening possible), Ongoing, medically stable => Ongoing, medically stable (further change not expected), Complete Recovery, Recovered with Sequelae, Fatal
AEResDaysFromEnroll
Int
AE Recovery number of days after enrollment
YES



AEDeathDaysFromEnroll
Int
AE Death number of days from enrollment
YES



AEDeath
tinyint
Criteria Defining Event as Serious Adverse Event: Death
YES


1 => Checked
AEConAnomaly
tinyint
Criteria Defining Event as Serious Adverse Event: Congenital Anomaly
YES


1 => Checked
AELifeThreat
tinyint
Criteria Defining Event as Serious Adverse Event: Life Threatening
YES


1 => Checked
AEHosp
tinyint
Criteria Defining Event as Serious Adverse Event: Hospitalization -- inital or prolonged
YES


1 => Checked
AEDisability
tinyint
Criteria Defining Event as Serious Adverse Event: Significant Disability or Incapacity
YES


1 => Checked
AEOther
tinyint
Criteria Defining Event as Serious Adverse Event: Other
YES


1 => Checked
Weight
smallint
Weight
YES
0


WeightMeas
varchar
Weight Measurement
YES


lbs, kgs
WeightNotAvail
tinyint
Weight: Not available
YES


1 => Checked
AERelLabData
varchar
Relevant Tests/Laboratory Data
YES


Yes, No
AEOthRelHx
varchar
Other relevant history, including preexisting medical conditions (e.g., allergies, pregnancy, smoking and alcohol use, hepatic/renal dysfunction, etc)
YES


Yes, No
AEMedProd
varchar
Concomitant medical products and therapy dates (exclude treatment of event)
YES


Yes, No
AERelStdyDrugDevice
varchar
What is the relationship of the event to study drug/device
YES


Unrelated, Unlikely related, Possibly related, Probably related, Definitely related, Not assessable
AERelStdyDrugDeviceUncertain
tinyint
Uncertain which study drug/device is related to event
YES


1 => Checked

HAEDeviceProblems 
Description - One record per Adverse Event and Device Problem form submitted
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



PtID
varchar
Participant ID
NO



SiteID
Int
Site Identifier
NO



Visit
varchar
Visit
NO



SHSinceLastVis
varchar
Did any of the following occur since last visit: Reportable Hypoglycemic event
NO


Yes, No
DKASinceLastVis
varchar
Did any of the following occur since last visit: Definite or Probable DKA
NO


Yes, No
OthAESinceLastVis
varchar
Did any of the following occur since last visit: Other reportable adverse event
NO


Yes, No
DevProbSinceLastVis
varchar
Did the participant report having any reportable device  problems while using the sensor since the last contact
NO


Yes, No



HComplUnblindCGM 
Description - One record per Compliance and Initiation of Standard CGM form submitted
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



PtID
varchar
Participant ID
NO



SiteID
Int
Site Identifier
NO



Visit
varchar
Visit
NO



CGMMinUse
varchar
Has the CGM been used for at least 11 of 14 days
NO


Yes, No
BGMMinMeas
varchar
Have at least 3 BGM measurements been made per day on 13 of 14 days
NO


Yes, No
CGMGlucUnder60
varchar
Are the CGM glucose values <60 mg/dl less than 10% of the time
NO


Yes, No
UnblindCGMSensor
varchar
Was participant provided with standard CGM and sensor inserted
NO


Yes, No
DtTm1MinCell
varchar
Was the standard CGM date/time set to be within 1 minute of a cell phone
YES


Yes, No
PtRunInStatus
varchar
Indicate status of participant
YES


Participant will repeat blinded CGM use, Participant will be dropped => Participant will be dropped (complete a Pre-randomization Final Status Form)

HDeviceBGM
Description - One record per bgm or ketone reading
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



ParentHDeviceUploadsID
int
RecID from tblHDeviceUploads
NO



PtID
varchar
Participant ID
NO



SiteID
Int
Site Identifier
NO



DeviceDtTmDaysFromEnroll
Int
Device date number of days from enrollment
NO



DeviceTm
Time
Time of device




RecordType
varchar
Type of data (Ketone, BGM, etc.)
NO



RecordSubType
varchar
Record subtype
YES



GlucoseValue
decimal
Glucose value (in md/dL for BGM data, in mmol/L for Ketone data)
NO




HDeviceBolus
Description - One record per bolus reading from a pump
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



ParentHDeviceUploadsID
int
Parent RecID from tblHDeviceUploads
NO



PtID
varchar
Participant ID
NO



SiteID
Int
Site Identifier
NO



DeviceDtTmDaysFromEnroll
Int
Device date number of days from enrollment
NO



DeviceTm
Time
Time of device




BolusType
varchar
Bolus type
NO



InjValue
decimal
Number of units injected (applies to "Injected" BolusType only)
YES



Insulin
varchar
Name of the insulin (applies to "Injected" BolusType only)
YES



Normal
decimal
Number of units of normal bolus
YES



ExpectedNormal
decimal
Expected number of units of normal bolus
YES



Extended
decimal
Number of units for extended delivery
YES



ExpectedExtended
decimal
Expected number of units for extended delivery
YES



Duration
int
Time span over which the bolus was delivered (milliseconds for Tidepool data, minutes for Diasend data)
YES



ExpectedDuration
int
Expected time span over which the bolus should have been delivered (milliseconds for Tidepool data, minutes for Diasend data)
YES




HDeviceCGM 
Description - One record per CGM reading
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



ParentHDeviceUploadsID
int
RecID from tblHDeviceUploads
NO



PtID
varchar
Participant ID
NO



SiteID
Int
Site Identifier
NO



DeviceDtTmDaysFromEnroll
Int
Device date number of days from enrollment
NO



DeviceTm
Time
Device Time
NO



DexInternalDtTmDaysFromEnroll
Int
Internal date number of days from enrollment
NO



DexInternalTm
Time
Internal time
NO



RecordType
varchar
Type of data (CGM, Calibration, etc)
NO



GlucoseValue
decimal
Glucose value (units: mg/dL)
YES




HDeviceDtTmVer
Description - One record per Device Date Time Verification form submitted
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



PtID
varchar
Participant ID
NO



SiteID
Int
Site Identifier
NO



Visit
varchar
Visit
NO



DtTm1MinCell
varchar
Are the date/time on the insulin pump, CGM, and study BGM within 1 minute of a cell phone
YES


Yes, No
CellDtDaysFromEnroll
Int
Cell date number of days from enrollment
YES



CellHr
tinyint
Cell Phone: Time (hour)
YES


1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
CellMin
tinyint
Cell phone: Time (minute)
YES


0 => 00, 1 => 01, 2 => 02, 3 => 03, 4 => 04, 5 => 05, 6 => 06, 7 => 07, 8 => 08, 9 => 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59
CellAmPm
varchar
Cell Phone: Time (AmPm)
YES


AM, PM
CGMDtDaysFromEnroll
Int
CGM Date number of days from enrollment
YES



CGMHr
tinyint
CGM: Time (hour)
YES


1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
CGMMin
tinyint
CGM: Time (minute)
YES


0 => 00, 1 => 01, 2 => 02, 3 => 03, 4 => 04, 5 => 05, 6 => 06, 7 => 07, 8 => 08, 9 => 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59
CGMAmPm
varchar
CGM: Time (AmPm)
YES


AM, PM
StandBGMDtDaysFromEnroll
Int
Stand BGM date number of days from enrollment
YES



StandBGMHr
tinyint
Standard BGM: Time (hour)
YES


1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
StandBGMMin
tinyint
Standard BGM: Time (minute)
YES


0 => 00, 1 => 01, 2 => 02, 3 => 03, 4 => 04, 5 => 05, 6 => 06, 7 => 07, 8 => 08, 9 => 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59
StandBGMAmPm
varchar
Standard BGM: Time (AmPm)
YES


AM, PM
BlindBGMDtDaysFromEnroll
Int
Blind BGM date number of days from enrollment
YES



BlindBGMHr
tinyint
Blinded BGM: Time (hour)
YES


1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
BlindBGMMin
tinyint
Blinded BGM: Time (minute)
YES


0 => 00, 1 => 01, 2 => 02, 3 => 03, 4 => 04, 5 => 05, 6 => 06, 7 => 07, 8 => 08, 9 => 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59
BlindBGMAmPm
varchar
Blinded BGM: Time (AmPm)
YES


AM, PM
PumpDtDaysFromEnroll
Int
Pump date number of days from enrollment
YES



PumpHr
tinyint
Pump: Time (hour)
YES


1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
PumpMin
tinyint
Pump: Time (minute)
YES


0 => 00, 1 => 01, 2 => 02, 3 => 03, 4 => 04, 5 => 05, 6 => 06, 7 => 07, 8 => 08, 9 => 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59
PumpAmPm
varchar
Pump: Time (AmPm)
YES


AM, PM
DtTm1MinCellUnk
tinyint
Unable to determine: Are the date/time on the insulin pump, CGM, and both study BGMs within 1 minute of a cell phone
YES


1 => Checked
CGMNotAtVis
tinyint
CGM device: Participant did not bring device to visit
YES


1 => Checked
StandBGMNotAtVis
tinyint
Standard BGM device: Participant did not bring device to visit
YES


1 => Checked
BlindBGMNotAtVis
tinyint
Blinded BGM device: Participant did not bring device to visit
YES


1 => Checked
PumpNotAtVis
tinyint
Insulin pump: Participant did not bring device to visit
YES


1 => Checked
KetoneMetHr
tinyint
Ketone meter: Hour
YES


1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
KetoneMetMin
tinyint
Ketone meter: Minute
YES


0 => 00, 1 => 01, 2 => 02, 3 => 03, 4 => 04, 5 => 05, 6 => 06, 7 => 07, 8 => 08, 9 => 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59
KetoneMetAMPM
varchar
Ketone meter: AM/PM
YES


AM, PM
KetoneMetNotAtVis
tinyint
Ketone meter: Participant did not bring device to visit
YES


1 => Checked


HDeviceEvents
Description - One Record per Device Event
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



ParentHDeviceUploadsID
int
RecID from tblHDeviceUploads
NO



PtID
varchar
Participant ID
NO



SiteID
Int
Site Identifier
NO



DeviceDtTmDaysFromEnrollDt
Int
Device Date number of days from enrollment
NO



DeviceTm
Time
Device Time
NO



RecordType
varchar
Type of event
NO



TmChFromDaysFromEnrollDt
Int
Time change from number of days from enrollment
YES



TmChFrom
Time
Time change from
YES



TmChToDaysFromEnrollDt
Int
Time change to number of days from enrollment
YES



TmChTo
Time
Time change to
YES



TmChFrom
datetime
Original time of event
YES



TmChTo
datetime
Time changing event to
YES



TmChAgent
varchar
Time Change Agent
YES




HDeviceIssue
Description - One record per subject per device incident
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



PtID
varchar
Patient ID
NO



SiteID
Int
Site Identifier
NO



InvDevice
varchar
Investigated Device
NO



DevIssueType
varchar
Type of device issue
NO


Device malfunction, User error, Inadequate instructions / training, Inadequate labeling, Other
DevIssueOnsetDtDaysFromEnroll
int
Date problem first occurred/was identified
YES
10/01/2014


DevIssueLocation
varchar
Location of Occurrence
NO


Home, Inpatient, Clinic (outpatient), Other
DevIssueFrequency
varchar
Frequency
NO


Single Event, Intermittent, Continuous
DevIssueEffect
varchar
Effect on study treatment/device
NO


No change, Study device modified/adjusted, Study device replaced, Discontinued temporarily, Discontinued permanently
DevIssueReplacedDtDaysFromEnroll
int
Date replaced or modified device first used by participant (leave empty if not applicable or not yet used by subject)
YES
10/01/2014


DevIssueAE
varchar
Is the device issue related to an adverse event
NO


Yes, No
DevIssueAELikely
varchar
If no, please describe the likelihood that the device issue could have led to an adverse event
YES


Not assessable, Not possible, Unlikely, Possibly, Probably, Certainly

HDeviceUploads
Description - One record per device upload
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



PtID
varchar
Participant ID
NO



SiteID
Int
Site Identifier
NO



DeviceManufact
varchar
Device manufacturer(s)
YES



DeviceModel
varchar
Device model
YES



DeviceType
varchar
Device type (CGM, BGM, etc)
YES



InventoryItemDs
varchar
Description of item from inventory tracking (populated for devices tracked through inventory tracking web application)
YES


G4 Platinum Receiver
Standard BGM
Blinded BGM
Visit
varchar
Visit at which data was downloaded from Tidepool
YES



UploadDtTmDaysFromEnroll
int
Number of days from enrollment device uploaded to Tidepool
NO



UploadTm
Time
Time device uploaded to Tidepool
NO



DataSource
varchar
Source of data (Ex: Tidepool, Diasend, etc.)
YES




HDeviceWizard
Description - One record per pump wizard reading
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



ParentHDeviceUploadsID
int
RecID from tblHDeviceUploads
YES



PtID
varchar
Participant ID
YES



SiteID
Int
Site Identifier
NO



DeviceDtTmDaysFromEnroll
int
Device Date – Number of days from enrollment
NO



DeviceTm
Time
Device Time
NO



RecommendedCarb
decimal
Number of units to cover carbs
YES



RecommendedCorrection
decimal
Number of units to cover correction
YES



RecommendedNet
decimal
Recommended net
YES



BgInput
decimal
Blood glucose as inputted into wizard in mg
YES



CarbInput
decimal
Carbohydrates as inputted into wizard in mg
YES



InsulinOnBoard
decimal
Units of insulin on board
YES



InsulinCarbRatio
decimal
Number of mg carbs covered by unit of insulin
YES



InsulinSensitivity
decimal
Number of bgs covered by unit of insulin
YES



BgTargetLow
decimal
Bg target: low range
YES



BgTargetHigh
decimal
Bg target: high range
YES



ParentHDeviceBolusID
int
RecID from tblHDeviceBolus
YES



BgTargetTarget
decimal
Bg target: target
YES



BgTargetRange
decimal
Bg target: range
YES




HFollowUp
Description - One record per Follow Up visit form submitted
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



PtID
varchar
Participant ID
NO



SiteId
Int
Site Identifier
NO



Visit
varchar
Visit
NO



PumpUse
varchar
Is the participant still using an insulin pump
NO


Yes, No
PumpStopDtDaysFromEnroll
int
Pump stop date days from enrollment
YES



CGMUse6Days
varchar
Is the participant using CGM >= 6 days/week (based on review of downloaded CGM data)
NO


Yes, No
CGMUseSkin
tinyint
Reason participant is using CGM less than 6 days a week: Skin irritation
YES


1 => Checked
CGMUseAlarms
tinyint
Reason participant is using CGM less than 6 days a week: Alarms too frequently
YES


1 => Checked
CGMUseAccuracy
tinyint
Reason participant is using CGM less than 6 days a week: Does not provide accurate readings
YES


1 => Checked
CGMUseDifficult
tinyint
Reason participant is using CGM less than 6 days a week: Too difficult to operate
YES


1 => Checked
CGMUseTooBusy
tinyint
Reason participant is using CGM less than 6 days a week: Too busy to use it
YES


1 => Checked
CGMUseForget
tinyint
Reason participant is using CGM less than 6 days a week: Forget to use it
YES


1 => Checked
CGMUseNoHelp
tinyint
Reason participant is using CGM less than 6 days a week: Does not provide information that is helpful for diabetes management
YES


1 => Checked
CGMUseOth
tinyint
Reason participant is using CGM less than 6 days a week: Other
YES


1 => Checked
CGMDiabMgmtDec
varchar
How frequently has the participant been downloading CGM data at home and viewing the data to make changes in management
NO


Never, <1 time per week, 1 time per week, 2-3 times per week, 4-7 times per week
BGMProtCompl
varchar
From review of the downloaded blood glucose meters, assess the degree of participant compliance with the BGM testing protocol for his/her intervention group
YES


Excellent => Excellent (>=90% of required testing done), Very Good => Very Good (75% to <90% of required testing done), Good => Good (60% to <75% of required testing done), Fair => Fair (45% to <60% of required testing done), Poor => Poor (<45% of required testing done), Unknown => Unknown (BGM download not available)
HbA1cCollected
varchar
Was an HbA1c sample collected
YES


Yes, No
StandBGMProtCompl
varchar
From review of the downloaded Standard blood glucose meters, assess the degree of participant compliance with the BGM testing protocol for his/her intervention group
YES


Excellent => Excellent (>=90% of required testing done), Very Good => Very Good (75% to <90% of required testing done), Good => Good (60% to <75% of required testing done), Fair => Fair (45% to <60% of required testing done), Poor => Poor (<45% of required testing done), Unknown => Unknown (BGM download not available)
BlindBGMProtCompl
varchar
From review of the downloaded Blinded blood glucose meters, assess the degree of participant compliance with the BGM testing protocol for his/her intervention group
YES


Excellent => Excellent (>=90% of required testing done), Very Good => Very Good (75% to <90% of required testing done), Good => Good (60% to <75% of required testing done), Fair => Fair (45% to <60% of required testing done), Poor => Poor (<45% of required testing done), Unknown => Unknown (BGM download not available)

HHypoEvent
Description - One record per Hypoglycemic Event submitted
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



PtID
varchar
Participant ID
NO



SiteId
Int
Site Identifier
NO



HypoOccurDtDaysFromEnroll
int
Hypo occur date days from enroll date




HypoOccurDtApprox
tinyint
Estimated: Date of Event
YES


1 => Checked
HypoApproxTime
varchar
Indicate the approximate time of day of the event
NO


00:01 - 03:00, 03:01 - 06:00, 06:01 - 09:00, 09:01 - 12:00, 12:01 - 15:00, 15:01 - 18:00, 18:01 - 21:00, 21:01 - 00:00, Unknown
GlucMeterCk
varchar
Was the glucose level checked on a home blood glucose meter
NO


Yes, No, Unknown
GlucMeterRes
decimal
Result of glucose level checked on a home blood glucose meter
YES
0.00
500.00

GlucMeterResUnk
tinyint
Unknown: Result of glucose level checked on a home blood glucose meter
YES


1 => Checked
SensorWear
varchar
Was the participant wearing a CGM sensor at the time of the event
NO


Yes, No, Unknown
SensorGluc
decimal
Glucose reading at the time the event was identified
YES
0.00
500.00

SensorGlucUnk
tinyint
Unknown: Glucose reading at the time the event was identified
YES


1 => Checked
LastInsDoseDtDaysFromEnroll
int
Last Insulin Dose Days from Enroll
YES



LastInsDoseApprox
tinyint
Estimated: Date of last insulin dose prior to the hypoglycemia event
YES


1 => Checked
LastInsDoseUnk
tinyint
Unknown: Date of last insulin dose prior to the hypoglycemia event
YES


1 => Checked
LastInsApproxTime
varchar
Last insulin dose prior to the hypoglycemia event: Indicate the approximate time
YES


00:01 - 03:00, 03:01 - 06:00, 06:01 - 09:00, 09:01 - 12:00, 12:01 - 15:00, 15:01 - 18:00, 18:01 - 21:00, 21:01 - 00:00, Unknown
LastInsPriorToHypo
varchar
Was the last insulin dose prior to the event based off the CGM reading
YES


Yes, No, Unknown
HypoSeizure
tinyint
Please select all of the following that apply for this event: Seizure
YES


1 => Checked
HypoLossCons
tinyint
Please select all of the following that apply for this event: Loss of consciousness
YES


1 => Checked
HypoReqAssist
tinyint
Please select all of the following that apply for this event: Required assistance
YES


1 => Checked
HypoAmbulance
tinyint
Please select all of the following that apply for this event: Ambulance Called
YES


1 => Checked
HypoEMT
tinyint
Please select all of the following that apply for this event: EMT Assistance
YES


1 => Checked
HypoHthCareProv
tinyint
Please select all of the following that apply for this event: Evaluated or treated by healthcare provider (not EMT)
YES


1 => Checked
GlucGiven
varchar
Was glucagon given
NO


Yes, No, Unknown
HospOrER
varchar
Was the participant hospitalized or treated in the Emergency Room
NO


Yes, No, Unknown
HospERTrtLoc
varchar
Where was the participant treated
YES


ICU only, Floor only, ICU and Floor, Emergency Room only, Unknown
HospNumDays
tinyint
If hospitalized, duration (days)
YES



HospNumDaysUnk
tinyint
Unknown: Duration of hospitalization
YES


1 => Checked
HypoOutcome
varchar
Outcome
NO


Fully recovered, Other, Unknown
EventCauseStdyDev
varchar
Is there any evidence that a study device (e.g., blood glucose meter and/or CGM) contributed to the event (either device malfunction or improper use by user)
YES


Yes, No
EventCauseBGM
tinyint
Indicate any study device that may have contributed to the event: Blood glucose meter
YES


1 => Checked
EventCauseCGM
tinyint
Indicate any study device that may have contributed to the event: CGM
YES


1 => Checked
EventCauseExpl
varchar
Cause of Event: What is thought to be the explanation
YES


User error, Problem with the study device, Both user error and problem with the study device
EventCauseNonStdy
varchar
Is there any indication of non-study-device-related factors that contributed to the occurrence of the event
YES


Yes, No

HInitialStudyCGM 
Description - One record per Initial Study CGM form submitted
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



PtID
varchar
Participant ID
NO



SiteId
Int
Site Identifier
NO



CGMTypeProvided
varchar
What type of study CGM was provided
NO


Blinded, Standard, None => None (participant not eligible)
DtTmSyncConfirm
tinyint
If a study CGM was provided, confirm date time synchronization
YES


1 => Checked

HInsulin 
Description - One record per Insulin type per patient
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



PtID
varchar
Patient ID
NO



SiteId
Int
Site Identifier
NO



InsName
Varchar
Insulin Name
NO



InsRoute
varchar
Route
NO


Pump, Injection, Inhaled
InsInjectionFreq
varchar
If injection or inhaled, what is the usual frequency of injections or inhaled per day
YES


1, 2, 3, 4, 5, 6, 7, 8, 9, Unknown
InsTypeStart
varchar
Start Date of Insulin Type
NO


In use at time of enrollment, Started after enrollment, Unknown
InsTypeStartDtDaysFromEnroll
Int
Insulin type start days from enroll
YES



InsTypeStartUnknown
tinyint
If started after enrollment, start date: Unknown
YES


1 => Checked
InsTypeStopDtDaysFromEnroll
Int
Insulin type stop days from enroll
YES



InsTypeStopUnknown
tinyint
Stop Date of Insulin Type: Unknown
YES


1 => Checked
InsTypeStartEstimate
tinyint
If started after enrollment, start date: Estimated
YES


1 => Checked
InsTypeStopEstimate
tinyint
Stop Date of Insulin Type: Estimated
YES


1 => Checked

HLocalHbA1c
Description - One record per Local HbA1c form submitted
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



PtID
varchar
Participant ID
NO



SiteId
Int
Site Identification
NO



Visit
varchar
Visit
NO



HbA1cTestDtDaysAfterEnroll
Int
HbA1c test date number of days after enrollment
NO



HbA1cTestMethod
varchar
Method of testing
YES


Point of Care => Point of Care (POC), Local Lab
HbA1cTestRes
decimal
HbA1C Results
YES
4.0
15.0

HbA1cNotDone
tinyint
Local HbA1c not done
YES


1 => Checked

HMedicalCondition
Description - One record per medical condition form
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



PtID
varchar
Participant ID
NO



SiteId
Int
Site Identification
NO



MedCond
Varchar
Medical Condition
NO



MedCondPreStart
varchar
Medical condition present prior to study enrollment
NO


Yes, No
MedCondPreStartCat
varchar
If present prior to enrollment, approximate duration (prior to enrollment)
YES


<=30 days, >30 days to < 3 months, 3 months to < 6 months, 6 months to < 1 year, 1 year to < 5 years, 5 years to < 10 years, >=10 years, Unknown
MedCondPreStartTreat
varchar
If present prior to enrollment, was the medical condition treated with medication
YES


Current, Past, Never
MedCondDiagDtDaysFromEnroll
Int
Diagnosis date number of days from enrollment
YES



MedCondDiagDtApprox
tinyint
Date of diagnosis is approximate
YES


1 => Checked
MedCondDiagDtUnk
tinyint
Date of diagnosis is unknown
YES


1 => Checked
MedCondTrt
varchar
If condition started after enrollment, treatment of the medical condition
YES


None, Medication, Surgery, Medication and Surgery, Dietary Management, Unknown, Other
MedCondResDtDaysFromEnroll
Int
Recovery date number of days from enrollment.
YES



MedCondResDtApprox
tinyint
Recovery date of medical condition is approximate
YES


1 => Checked
MedCondStatus
varchar
Medical condition status
YES


Ongoing (further improvement / worsening possible) => Ongoing (further improvement or worsening possible), Ongoing, medically stable => Ongoing, medically stable (further change not expected), Complete Recovery, Recovered with Sequelae
MedCondDiagMonthsAfterEnroll
Int
Number of months after enrollment medical condition diagnosed
YES



MedCondDiagYearsAfterEnroll
Int
Number of years after enrollment medical condition diagnosed
YES



MedCondCurrTreatMed
varchar
Current treatment with medications
YES


Yes, No

HMedication
Description - One record per medications form
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



PtID
varchar
Subject ID
NO



SiteId
Int
Site Identifier
NO



MedDose
varchar
Dose per administration
YES



MedUnit
varchar
Dose per administration unit
YES


aerosol, ampules, capsules, cream, dl => dl-deciliter, elixir, g => g-gram, gal => gal-gallon, gtt-drops, IU => IU-International unit, kg => kg-kilogram, L => L-liter, lbs => lbs-pounds, M => M-molar, mcg => mcg-microgram, meq => meq-milliequivalent, mg => mg-milligram, mL => mL-milliliter, Ointment, pills, pt => pt-pint, puff, ounces, qt => qt-quart, tablet, tbs => tbs-tablespoon, tsp => tsp-teaspoon, ul => ul-microliter, units, vials
MedDoseUnk
tinyint
Dose per administration is unknown
YES


1 => Checked
MedRoute
varchar
Route
NO


SC => S.C.-subcutaneous, IV => I.V.-intravenous, Gtt => Gtt-drops, ID => I.D.-intradermal, IM => I.M.-intramuscular, PO => P.O.-by mouth, PR => P.R.-by rectum, Topical - ocular, Topical - skin, Vaginal, Transurethral, Oral Inhalation, Nasal, Sublingual, Intravitreal, Peribulbar, Intra-articular => Intra-articular injection, Retrobulbar, Transdermal, Subconjunctival, Subtenons, Intrauterine, Topical, Epidural
MedLocSide
varchar
If treatment is for eye or ear, which was treated with medication
YES


Right, Left, Both
MedFreqType
varchar
Frequency
NO


Fixed Regimen, As Needed, One Time Treatment
MedFreqNum
tinyint
Frequency number
YES


1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50
MedFreqPer
varchar
Frequency period
YES


Day, Week, Month, Year
MedFreqUnk
tinyint
Medication frequency is unknown
YES


1 => Checked
MedInd
varchar
Indication
NO


Prior to enrollment => Medical condition prior to enrollment, New => New medical condition/adverse event, Prevention
MedStartTrtCat
varchar
Start date of treatment category
NO


On treatment at time of enrollment, Treatment started after enrollment
MedStartDtDaysFromEnroll
Int
Number of days from enrollment medication started
YES



MedStartDtApprox
tinyint
Medication Start Date is approximate
YES


1 => Checked
MedStopDtDaysFromEnroll
int
Number of days from enrollment medication stopped
YES



MedStopDtApprox
tinyint
Medication Stop Date is approximate
YES


1 => Checked
MedOngoing
tinyint
Medication is ongoing
YES


1 => Checked
MedStartPreEnrRange
varchar
If on treatment at time of enrollment, Medication Start Range
YES


<=30 days, >30 days to < 3 months, 3 months to < 6 months, 6 months to < 1 year, 1 year to < 5 years, 5 years to < 10 years, >=10 years, Unknown
MedStartMonthsAfterEnroll
Int
Number of months after enrollment medication started
YES



MedStartYearsAfterEnroll
Int
Number of years after enrollment medication started
YES



MedStopMonthsAfterEnroll
Int
Number of months after enrollment medication stopped
YES



MedStopYearsAfterEnroll
Int
Number of years after enrollment medication stopped
YES



MedStopDtUnk
tinyint
Medication stop date unknown
YES


1 => Checked
MedStartDtUnk
tinyint
Medication start date unknown
YES


1 => Checked
MedCondNotReqd
tinyint
Condition not required to be reported on medical condition form
YES


1 => Checked
PreExistCondNotReqd
tinyint
Condition not required to be reported on pre-existing condition form
YES


1 => Checked
AdvEventNotReqd
tinyint
Condition not required to be reported on adverse event form
YES


1 => Checked

HPostRandPtFinalStatus
Description - One record per Post Rand Final Status form submitted
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



PtID
varchar
Participant ID
NO



SiteId
Int
Site identifier
NO



HPostRandFinalStatReas
varchar
Reason participant's participation in the study has ended
NO


Participant requests to withdraw, in writing => Participant requests to withdraw - participant formally withdrew consent in writing, Participant requests to withdraw, not in writing => Participant requests to withdraw - did not withdraw consent in writing, Lost to follow up => Lost to follow up - detail efforts to contact participant in COMMENTS, Site withdraws participant => Site withdraws participant - indicate reason in COMMENTS, Death
PtWithdrawReas
varchar
Reason for participant withdrawal
YES


Adverse event, Changed doctor, Does not want study treatment, Finances, Moved, Other treatment requested, Poor health, Poor outcome, Travel difficulty, Unknown, Visit too lengthy
DeathDtDaysAfterEnroll
Int
Number of days after enrollment death occurred
YES




tblHPtRoster
Description - One record per Protocol H PtID obtained
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



PtID
varchar
Unique Patient Identifier
NO



SiteOrig
smallint
Original Site ID
YES



SiteID
smallint
Site Identifier
YES



RandDtDaysAfterEnroll
Int
Number 
No



PtStatus
varchar
Patient Status
NO


Active, Completed, Dropped
TrtGroup
varchar
Treatment group randomization assignment
YES


CGM+BGM
CGM Only

AgeAsOfEnrollDt
Int
Age as of enrollment
NO




HQuestDiabTech
Description - One record per Diabetes Technology Questionnaire submitted
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



PtID
varchar
Participant ID
NO



SiteId
Int
Site Identifier
NO



Visit
varchar
Visit
NO



WorryHighBGNow
tinyint
Worry or fear about high blood sugar: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
WorryHighBGChg
tinyint
Worry or fear about high blood sugar: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
LowBGEffortNow
tinyint
Effort to keep low blood sugar from happening: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
LowBGEffortChg
tinyint
Effort to keep low blood sugar from happening: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
LowBGSleepNow
tinyint
Worry or fear about low blood sugar during sleep: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
LowBGSleepChg
tinyint
Worry or fear about low blood sugar during sleep: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
FeelDiffNow
tinyint
Feeling different from others: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
FeelDiffChg
tinyint
Feeling different from others: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
DiabTimeNow
tinyint
Amount of time spent thinking about diabetes: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
DiabTimeChg
tinyint
Amount of time spent thinking about diabetes: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
EatBGNow
tinyint
Not knowing how eating affects blood sugar: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
EatBGChg
tinyint
Not knowing how eating affects blood sugar: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
DiabEffortNow
tinyint
Amount of time and effort needed for diabetes from my family or me: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
DiabEffortChg
tinyint
Amount of time and effort needed for diabetes from my family or me: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
LTHealthNow
tinyint
Worry or fear about long term health: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
LTHealthChg
tinyint
Worry or fear about long term health: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
DayLowBGNow
tinyint
Worry or fear about daytime low blood sugar: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
DayLowBGChg
tinyint
Worry or fear about daytime low blood sugar: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
HighBGNow
tinyint
Effort to keep high blood sugar from happening: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
HighBGChg
tinyint
Effort to keep high blood sugar from happening: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
FingStkPainNow
tinyint
Pain or discomfort from finger sticks or monitors: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
FindStkPainChg
tinyint
Pain or discomfort from finger sticks or monitors: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
PumpInjPainNow
tinyint
Pain or discomfort from insulin injections or pump sets: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
PumpInjPainChg
tinyint
Pain or discomfort from insulin injections or pump sets: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
FamWorryNow
tinyint
Family arguments or worries about diabetes: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
FamWorryChg
tinyint
Family arguments or worries about diabetes: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
TroubleSleepNow
tinyint
Trouble sleeping well: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
TroubleSleepChg
tinyint
Trouble sleeping well: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
StrictMealNow
tinyint
Strictness of the meal plan: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
StrictMealChg
tinyint
Strictness of the meal plan: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
WorkSchNow
tinyint
Coping with work or school along with diabetes: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
WorkSchChg
tinyint
Coping with work or school along with diabetes: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
SportExerNow
tinyint
Taking part in sports, exercise or playing despite diabetes: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
SportExerChg
tinyint
Taking part in sports, exercise or playing despite diabetes: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
InsAmtNow
tinyint
Knowing how much insulin to take: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
InsAmtChg
tinyint
Knowing how much insulin to take: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
KeepUpPeersNow
tinyint
Keeping up with friends or peers who don't have diabetes: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
KeepUpPeersChg
tinyint
Keeping up with friends or peers who don't have diabetes: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
BGReactNow
tinyint
Reacting to all of the blood sugar results that I get: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
BGReactChg
tinyint
Reacting to all of the blood sugar results that I get: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
DiabQuestNow
tinyint
Dealing with others who ask about diabetes: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
DiabQuestChg
tinyint
Dealing with others who ask about diabetes: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
DiabRespNow
tinyint
My amount of responsibility for taking care of diabetes: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
DiabRespChg
tinyint
My amount of responsibility for taking care of diabetes: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
PreMealInsNow
tinyint
Being sure that pre-meal insulin covers the amount of carbohydrates eaten: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
PreMealInsChg
tinyint
Being sure that pre-meal insulin covers the amount of carbohydrates eaten: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
SkipMealInsNow
tinyint
Getting the right amount of insulin when meals are skipped or delayed: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
SkipMealInsChg
tinyint
Getting the right amount of insulin when meals are skipped or delayed: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
AlarmReactNow
tinyint
Reacting to all of the alarms from diabetes devices: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
AlarmReactChg
tinyint
Reacting to all of the alarms from diabetes devices: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
InsSickDayNow
tinyint
Getting the right amount of insulin on sick days: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
InsSickDayChg
tinyint
Getting the right amount of insulin on sick days: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
DeviceRunLifeNow
tinyint
Feeling that diabetes devices run my life: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
DeviceRunLifeChg
tinyint
Feeling that diabetes devices run my life: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
ExerInsAmtNow
tinyint
Getting the right amount of insulin after exercising more than usual: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
ExerInsAmtChg
tinyint
Getting the right amount of insulin after exercising more than usual: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
SeveralDeviceNow
tinyint
Coping with carrying and using several devices: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
SeveralDeviceChg
tinyint
Coping with carrying and using several devices: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
LookDiffNow
tinyint
Looking different because of diabetes and using devices: Is this a problem now
YES


1 => 1 - Very Much, 2, 3 => 3 - Just a Little, 4, 5 => 5 - Not At All
LookDiffChg
tinyint
Looking different because of diabetes and using devices: How has it changed compared to your treatment before the study
YES


1 => 1 - Much Worse, 2 => 2 - A Little Worse, 3 => 3 - Same, 4 => 4 - A Little Better, 5 => 5 - Much Better
QuestNotDone
tinyint
Diabetes Technology Questionnaire will not be completed
YES


1 => Checked

HQuestHypoFear 
Description - One record per Hypoglycemia Fear Survey submitted
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



PtID
varchar
Participant ID
NO



SiteId
Int
Site Identifier
NO



Visit
varchar
Visit
NO



LgSnackBed
tinyint
Eat large snacks at bedtime
YES


0 => 0 - Never, 1 => 1 - Rarely, 2 => 2 - Sometimes, 3 => 3 - Often, 4 => 4 - Almost Always
AvoidAloneLowBG
tinyint
Avoid being alone when my sugar is likely to be low
YES


0 => 0 - Never, 1 => 1 - Rarely, 2 => 2 - Sometimes, 3 => 3 - Often, 4 => 4 - Almost Always
TestBGRunHigh
tinyint
If test blood glucose, run a little high to be on the safe side
YES


0 => 0 - Never, 1 => 1 - Rarely, 2 => 2 - Sometimes, 3 => 3 - Often, 4 => 4 - Almost Always
HighBGAlone
tinyint
Keep my sugar high when I will be alone for a while
YES


0 => 0 - Never, 1 => 1 - Rarely, 2 => 2 - Sometimes, 3 => 3 - Often, 4 => 4 - Almost Always
EatFirstSignLowBG
tinyint
Eat something as soon as I feel the first sign of low blood sugar
YES


0 => 0 - Never, 1 => 1 - Rarely, 2 => 2 - Sometimes, 3 => 3 - Often, 4 => 4 - Almost Always
RedInsThinkLowBG
tinyint
Reduce my insulin when I think my sugar is low
YES


0 => 0 - Never, 1 => 1 - Rarely, 2 => 2 - Sometimes, 3 => 3 - Often, 4 => 4 - Almost Always
KeepHighBGMtg
tinyint
Keep my sugar high when I plan to be in a long meeting or at a party
YES


0 => 0 - Never, 1 => 1 - Rarely, 2 => 2 - Sometimes, 3 => 3 - Often, 4 => 4 - Almost Always
CarryFastActSug
tinyint
Carry fast-acting sugar with me
YES


0 => 0 - Never, 1 => 1 - Rarely, 2 => 2 - Sometimes, 3 => 3 - Often, 4 => 4 - Almost Always
AvoidExThinkLowBG
tinyint
Avoid exercise when I think my sugar is low
YES


0 => 0 - Never, 1 => 1 - Rarely, 2 => 2 - Sometimes, 3 => 3 - Often, 4 => 4 - Almost Always
CkSugOftMtg
tinyint
Check my sugar often when I plan to be in a long meeting or out to a party
YES


0 => 0 - Never, 1 => 1 - Rarely, 2 => 2 - Sometimes, 3 => 3 - Often, 4 => 4 - Almost Always
WorryNotRecLowBG
tinyint
I worry about not recognizing/realizing I am having low blood sugar
YES


0 => 0 - Never, 1 => 1 - Rarely, 2 => 2 - Sometimes, 3 => 3 - Often, 4 => 4 - Almost Always
WorryNoFood
tinyint
I worry about not having food, fruit, or juice with me
YES


0 => 0 - Never, 1 => 1 - Rarely, 2 => 2 - Sometimes, 3 => 3 - Often, 4 => 4 - Almost Always
WorryPassOut
tinyint
I worry about passing out in public
YES


0 => 0 - Never, 1 => 1 - Rarely, 2 => 2 - Sometimes, 3 => 3 - Often, 4 => 4 - Almost Always
WorryEmbarSocial
tinyint
I worry about embarrassing myself or my friends in a social situation
YES


0 => 0 - Never, 1 => 1 - Rarely, 2 => 2 - Sometimes, 3 => 3 - Often, 4 => 4 - Almost Always
WorryReacAlone
tinyint
I worry about having a reaction while alone
YES


0 => 0 - Never, 1 => 1 - Rarely, 2 => 2 - Sometimes, 3 => 3 - Often, 4 => 4 - Almost Always
WorryAppStupDrunk
tinyint
I worry about appearing stupid or drunk
YES


0 => 0 - Never, 1 => 1 - Rarely, 2 => 2 - Sometimes, 3 => 3 - Often, 4 => 4 - Almost Always
WorryLoseCntrl
tinyint
I worry about losing control
YES


0 => 0 - Never, 1 => 1 - Rarely, 2 => 2 - Sometimes, 3 => 3 - Often, 4 => 4 - Almost Always
WorryNoHelp
tinyint
I worry about no one being around to help me during a reaction
YES


0 => 0 - Never, 1 => 1 - Rarely, 2 => 2 - Sometimes, 3 => 3 - Often, 4 => 4 - Almost Always
WorryReactDrive
tinyint
I worry about having a reaction while driving
YES


0 => 0 - Never, 1 => 1 - Rarely, 2 => 2 - Sometimes, 3 => 3 - Often, 4 => 4 - Almost Always
WorryMistAcc
tinyint
I worry about making a mistake or having an accident
YES


0 => 0 - Never, 1 => 1 - Rarely, 2 => 2 - Sometimes, 3 => 3 - Often, 4 => 4 - Almost Always
WorryBadEvalCrit
tinyint
I worry about getting a bad evaluation or being criticized
YES


0 => 0 - Never, 1 => 1 - Rarely, 2 => 2 - Sometimes, 3 => 3 - Often, 4 => 4 - Almost Always
WorryRespForOthers
tinyint
I worry about difficulty thinking clearly when responsible for others
YES


0 => 0 - Never, 1 => 1 - Rarely, 2 => 2 - Sometimes, 3 => 3 - Often, 4 => 4 - Almost Always
WorryDizzy
tinyint
I worry about feeling lightheaded or dizzy
YES


0 => 0 - Never, 1 => 1 - Rarely, 2 => 2 - Sometimes, 3 => 3 - Often, 4 => 4 - Almost Always
QuestNotDone
tinyint
Hypoglycemia Fear Survey will not be completed
YES


1 => Checked

HQuestHypoUnaware
Description - One record per Clarke Hypoglycemia Unawareness Survey completed
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



PtID
varchar
Participant ID
NO



SiteId
Int
Site Identifier
NO



LowBGSympCat
varchar
Select the category that best describes you
NO


Always have symptoms when blood sugar is low => I always have symptoms when my blood sugar is low, Sometimes have symptoms when blood sugar is low => I sometimes have symptoms when my blood sugar is low, No longer have symptoms when blood sugar is low => I no longer have symptoms when my blood sugar is low
LowBGLostSymp
varchar
Have you lost some of the symptoms that used to occur when your blood sugar was low
NO


Yes, No
ModHypoEpPast6Mon
varchar
In the past six months how often have you had moderate hypoglycemia episodes
NO


Never, Once or twice, Every other month, Once a month, More than once a month
SevHypoEpPastYear
varchar
In the past year how often have you had severe hypoglycemic episodes
NO


Never, 1 time, 2 times, 3 times, 4 times, 5 times, 6 times, 7 times, 8 times, 9 times, 10 times, 11 times, 12 or more times
Bel70PastMonWSymp
varchar
How often in the last month have you had readings <70 mg/dL with symptoms
NO


Never, 1 to 3 times, 1 time/week, 2 to 3 times/week, 4 to 5 times/week, Almost daily
Bel70PastMonNoSymp
varchar
How often in the last month have you had readings <70 mg/dL without any symptoms
NO


Never, 1 to 3 times, 1 time/week, 2 to 3 times/week, 4 to 5 times/week, Almost daily
FeelSympLowBG
varchar
How low does your blood sugar need to go before you feel symptoms
NO


60-69 mg/dL, 50-59 mg/dL, 40-49 mg/dL, <40 mg/dL
ExtentSympLowBG
varchar
To what extent can you tell by your symptoms that your blood sugar is low
NO


Never, Rarely, Sometimes, Often, Always

HRandomization
Description - One record per Randomization form submitted
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



PtID
varchar
Participant ID
NO



SiteId
Int
Site Identifier
NO



NoExclEventOccur
tinyint
Verify that participant did not meet any of the exclusion criteria since enrollment
NO


1 => Checked
EligCritMet
tinyint
Participant meets eligibility criteria
NO


1 => Checked
MedicalCondsEntered
varchar
Medical Conditions entered
NO


None to enter, Completed
MedicationEntered
varchar
Medications entered
NO


None to enter, Completed
HbA1cCollected
varchar
Was an HbA1c sample collected
YES


Yes, No

HRunInVisitStatus
Description - One record per Run In Visit Status form submitted
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



PtID
varchar
Participant ID
NO



SiteId
Int
Site Identifier
NO



Visit
varchar
Visit
NO



RunInStatus
varchar
Select status of participant
NO


Complete => Standard CGM run-in complete, ready for randomization, Continuing => Standard CGM run-in continuing, Discontinued => Standard CGM run-in discontinued (complete a Pre-randomization Final Status Form)

tblSample
Description - One record per sample per participant per draw type
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecId
Int
Unique record ID in table
NO



PtID
Varchar
Participant ID
NO



Visit
Varchar
Visit
NO



SiteID
Smallint
Site identifying number
YES



ContainerType
Varchar
Type of container that the sample comes in
NO



CollectionDtDaysFromEnroll
Int
Collection date, user-entered date, number of days from enrollment
NO



SampleCountActual
Tinyint
Number of samples user said they are entering
NO



SampleStatus
Varchar
Sample status
NO



CourierName
Varchar
Courier name
YES


FedEx
ShipDtDaysFromEnroll
Int
Date of shipment number of days from enrollment
YES



ShipmentLabRecvDt
Datetime
Date shipment of samples received at lab
YES



Analyte
Varchar
Name of the analysis
YES



Value
Varchar
Value of analysis
YES



ResultStatus
Varchar
Result status
YES





HScreening
Description - One record per Screening form submitted
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



PtID
varchar
Participant ID
NO



SiteId
Int
Site Identifier
NO



EligCritMet
tinyint
Eligibility criteria has been met by the participant
YES


1 => Checked
ExclCritAbsent
tinyint
Exclusion criteria is absent for the participant
YES


1 => Checked
Gender
varchar
Gender
NO


M => Male, F => Female
Ethnicity
varchar
Ethnicity
NO


Hispanic or Latino, Not Hispanic or Latino, Unknown/not reported
Race
varchar
Race
NO


White, Black/African American, Asian, Native Hawaiian/Other Pacific Islander, American Indian/Alaskan Native, More than one race, Unknown/not reported
DiagAge
tinyint
Age at diagnosis of diabetes
NO



DiagAgeApprox
tinyint
Age at diagnosis of diabetes is Approximate
YES


1 => Checked
SHMostRec
varchar
Estimate of when most recent severe hypoglycemic event occurred
NO


Never, < 3 months ago, 3-<6 months ago, 6-12 months ago, More than 12 months ago
SHNumLast12Mon
varchar
Estimated number of  severe hypoglycemic events in the last 12 months
NO


0, 1, 2, 3, 4, >=5
DKAMostRec
varchar
Estimate of when most recent definite or probable DKA event occurred
NO


Never, < 3 months ago, 3-<6 months ago, 6-12 months ago, More than 12 months ago
DKANumLast12Mon
varchar
Estimated number of definite or probable DKA events in the last 12 months
NO


0, 1, 2, 3, 4, >=5
OthGlucLowerMed
varchar
Is participant using glucose-lowering medication other than insulin
NO


Yes, No
Fingerstick7DayAve
tinyint
What is the average number of fingerstick readings the participant reports having done each day over the last 7 days
NO
0
30

EduLevel
varchar
Please select the highest level of education completed by the participant
YES


Less than 1st Grade, 1st, 2nd, 3rd, or 4th grade, 5th or 6th grade, 7th or 8th Grade, 9th Grade, 10th Grade, 11th Grade, 12th Grade - no diploma, High school graduate/diploma/GED, Some college but no degree, Associate Degree => Associate Degree (AA), Bachelor's Degree => Bachelor's Degree (BS/BA/AB), Master's Degree => Master's Degree (MA,MS,MSW,MBA,MPH), Professional Degree => Professional Degree (MD, DDS, DVM, LLB, JD), Doctorate Degree => Doctorate Degree (PhD, EdD)
EduLevelUnk
tinyint
Unknown: Highest level of education completed by the participant
YES


1 => Checked
EduLevelNoAns
tinyint
Does not wish to provide: Highest level of education completed by the participant
YES


1 => Checked
AnnualInc
varchar
In the household where the participant lives most of the time, what is the annual household income from all sources
YES


Less than $25,000, $25,000 - $35,000 => $25,000 to less than $35,000, $35,000 - less than $50,000 => $35,000 to less than $50,000, $50,000 - less than $75,000 => $50,000 to less than $75,000, $75,000 - less than $100,000 => $75,000 to less than $100,000, $100,000 - less than $200,000 => $100,000 to less than $200,000, $200,000 or more
AnnualIncUnk
tinyint
Unknown: Annual Income
YES


1 => Checked
AnnualIncNoAns
tinyint
Does not wish to provide: Annual Income
YES


1 => Checked
InsPrivate
tinyint
What kind of health insurance or health care coverage does the participant have: Private Health Insurance (e.g. commercial, fee-for-service, HMO, PPO, POS)
YES


1 => Checked
InsMedicare
tinyint
What kind of health insurance or health care coverage does the participant have: Medicare
YES


1 => Checked
InsMediGap
tinyint
What kind of health insurance or health care coverage does the participant have: MediGap
YES


1 => Checked
InsMedicaid
tinyint
What kind of health insurance or health care coverage does the participant have: Medicaid
YES


1 => Checked
InsSCHIP
tinyint
What kind of health insurance or health care coverage does the participant have: SCHIP (CHIP, Children's health insurance program)
YES


1 => Checked
InsMilitary
tinyint
What kind of health insurance or health care coverage does the participant have: Military health care (TRICARE, CHAMPUS, CHAMPVA, VA)
YES


1 => Checked
InsIndian
tinyint
What kind of health insurance or health care coverage does the participant have: Indian Health Service plan
YES


1 => Checked
InsState
tinyint
What kind of health insurance or health care coverage does the participant have: State sponsored health plan  
YES


1 => Checked
InsOtherGov
tinyint
What kind of health insurance or health care coverage does the participant have: Other government sponsored health coverage plan
YES


1 => Checked
InsSingleService
tinyint
What kind of health insurance or health care coverage does the participant have: Single service plan (e.g. dental, vision, prescriptions)
YES


1 => Checked
InsNoCoverage
tinyint
What kind of health insurance or health care coverage does the participant have: No coverage of any type 
YES


1 => Checked
InsUnknown
tinyint
What kind of health insurance or health care coverage does the participant have: Unknown
YES


1 => Checked
InsNoAns
tinyint
What kind of health insurance or health care coverage does the participant have: Does not wish to provide
YES


1 => Checked
Weight
decimal
Weight
NO
20.0
200.0

Height
decimal
Height
NO
100.0
280.0

PEAbnormal
varchar
Were any clinically significant abnormalities found on the physical exam
NO


Yes, No
CGMUseStatus
varchar
Indicate status of CGM (real-time) use
NO


Never, In past, but not current, Current
CGMUseDuration
varchar
How long has the participant been using CGM
YES


< 6 months, 6 months - < 1 year, 1 - < 2 years, 2 - < 5 years, >= 5 years
CGMUseDevice
varchar
Which CGM is being used
YES


Dexcom, Medtronic
CGMDLoadMinDays
varchar
Does the CGM download show use on at least 21 of the last 28 days
YES


Yes, No
CGMGlucUnder60
varchar
Are CGM glucose values <60 mg/dl less than 10% of the time
YES


Yes, No

HUnschedVisit 
Description - One record per Unscheduled Visit form submitted
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



PtID
varchar
Participant ID
NO



SiteId
Int
Site Identifier
NO



VisitReasCGMTrain
tinyint
Reason for Visit: Participant needed additional CGM training
YES


1 => Checked
VisitReasDiabMgmt
tinyint
Reason for Visit: Participant had a question or problem with diabetes management
YES


1 => Checked
VisitReasPotentialAE
tinyint
Reason for Visit: Participant had a potential adverse event
YES


1 => Checked
VisitReasOth
tinyint
Reason for Visit: Other
YES


1 => Checked








HVisitInfo
Description - Visit Information Form
Name
Data Type
Description
Nullable
Min
Max
Possible_Values
RecID
int
Unique record ID in table
NO



PtID
varchar
Patient Identifier
NO



SiteId
Int
Site Identifier
NO



Visit
varchar
Visit
NO



VisitDtDaysFromEnroll
Int
Number of days from enrollment visit occurred
NO



OutOfWin
tinyint
Visit was completed out of window
YES


1 => Checked
OutOfWinReason
varchar
Reason visit was completed out of window
YES


Bad weather, Travel difficulty, Financial issue, Poor health, Personal issue, Work issue, Subject on vacation, Visits too lengthy, Investigator away, Clinic appointment not available, Site forgot to schedule, Difficulty contacting subject, Poor outcome, Good outcome, Adverse event, Unknown, Other
VisitMiss
tinyint
Visit was missed
YES


1 => Checked
VisitMissReason
varchar
Reason visit was missed
YES


Bad weather, Travel difficulty, Financial issue, Poor health, Personal issue, Work issue, Subject on vacation, Visits too lengthy, Investigator away, Clinic appointment not available, Site forgot to schedule, Difficulty contacting subject, Poor outcome, Good outcome, Adverse event, Unknown, Other




