import ProjectNumberSequenceGenerator as PN
from ResourceNumberSequenceGenerator import resource_number as rn
import TaskCodeSequenceGenerator as TC
PN.project_number()
rn()
TC.task_code()

# 190504 Promfi2 output below:
# "F:\00085-PROGRAMMING & CODING PROJECTS\Python Programming\venv\Scripts\python.exe" "F:/00085-PROGRAMMING & CODING PROJECTS/Python Programming/190422_python tutorial - programming with Mosh/PROMFI 2/Promfi2.py"
# F:\00085-PROGRAMMING & CODING PROJECTS\Python Programming\venv\lib\site-packages\openpyxl\worksheet\_reader.py:296: UserWarning: Data Validation extension is not supported and will be removed
#   warn(msg)
# F:\00085-PROGRAMMING & CODING PROJECTS\Python Programming\venv\lib\site-packages\openpyxl\worksheet\header_footer.py:49: UserWarning: Cannot parse header or footer so it will be ignored
#   warn("""Cannot parse header or footer so it will be ignored""")
# F:\00085-PROGRAMMING & CODING PROJECTS\Python Programming\venv\lib\site-packages\openpyxl\worksheet\_reader.py:296: UserWarning: Unknown extension is not supported and will be removed
#   warn(msg)
# F:\00085-PROGRAMMING & CODING PROJECTS\Python Programming\venv\lib\site-packages\openpyxl\worksheet\_reader.py:296: UserWarning: Conditional Formatting extension is not supported and will be removed
#   warn(msg)
# ['0-personal', '1-company', '2-unassigned', '3-unassigned', '5-library', '6-jobs4-unassigned', '7-unassigned', '8-unassigned', '9-incubator']
# select a family from the list: 2
# Family selected: 2
# 2
# The next vacant project id is: 20001
# 0 1 2 3 4 5 6 7 8 9
#
# Select a series value: 0
# You have chosen series: 0000
# 0 1 2 3 4 5 6 7 8 9
#
# Select a Resource range: 9
# You have chosen Resource range: 900
# 0 1 2 3 4 5 6 7 8 9
#
# Select a Resource instance: 5
# You have chosen Resource instance: 50
# The Resource ID# is: 0950
# guess a family task code: D
# guess a parent task code: D
# Task Code Options are:
# {'DD': None}
# {'DD-MD': 'MASTER INFORMATION MODEL (MIM)'}
# {'DD-FD': 'FAMILY INFORMATION MODEL (FIM)'}
# {'DD-XD': 'PARENT INFORMATION MODEL (PIM)'}
# {'DD-CD': 'CHILD INFORMATION MODEL (CIM)'}
# {'DD-ID': 'GENERAL INFORMATION MODEL (GIM)'}
# {'DD-ZD': 'GLOBAL DESIGN INTENT LAYOUT (GDIL)'}
# {'DD-ND': 'LOCAL DESIGN INTENT LAYOUT (LDIL)'}
# {'DD-GD': 'GHOST DESIGN INTENT MODEL (GDIM)'}
# {'DD-RD': 'MODIFIED RESILLIENT MODELING STRATEGY (MRMS)'}
# {'DD-KD': 'BACKGROUND'}
# {'DD-SD': 'SKELETON/LAYOUT'}
# {'DD-OD': 'CORE'}
# {'DD-UD': 'SURFACE'}
# {'DD-TD': 'DETAIL'}
# {'DD-HD': 'HOLES'}
# {'DD-YD': 'MODIFY'}
# {'DD-QD': 'QUARANTINE'}
# {'DD-VD': 'VARIANTS'}
# {'DD-AD': 'PARTS, COMPONENTS, AND MODULES'}
#
# Process finished with exit code 0
