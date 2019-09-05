# Created August 1st 2019 at 8:39 am
# By Jed Ferreras for 508 Industries LLC
# Project #00223-PROMFI
# Task Family G; Task Parent S; Task Child MS; Task Code: GS-MS -- assigned to this module
# The program below is for the Task Allocation Protocol within Promfi 1.4
# The goals of this program are to:
#   1. establish a generic task structure with a dictionary
#   2. populate the dictionary with specific task descriptions over time based on the excel spreadsheet while replacing generic tasks
#   3. store the tasks in a file for permanent use
#   4. associate each description with a code
#   5. allocate task codes to projects based on user inputs
#   6. build a gui

# class TaskGenerator:
#     # def generaltaskpopulator(self, item, name):
#     #     # xx
#
#
#     # def generaltaskstructure(self, item, name):
#     #     module_dict = {'node_dict': {'sector_dict': {'element_dict': {"element_name"}}}}
#
#
#     def generictask(self): #, item, name):
#         print("To generate a task, please select a system item below: ")
#         system_list = ['module','node','sector','element',"element"]
#         print(system_list)
#         usr_sel = input("Type Selection Here: ")
#         # print("you have selected: ",usr_sel)
#         # sel_state = input("if this is correct type 'y', else type 'n'")
#         # if sel_state = 'y'
#         #     print(usr_sel, "will be added to the system")
#         # else
#         for
#         # system_dict = {'module_dict': {'node_dict': {'sector_dict': {'element_dict': {"element_name"}}}}}
#
# d = TaskGenerator()
# print(d.generictask())


# system_dict = {'module_dict': {'node_dict': {'sector_dict': {'element_dict': {"element_name"}}}}}
# system_dict.update()
# print(system_dict)

# system_dict = {'module_dict'}
# module_dict = {'node_dict'}
# node_dict = {'sector_dict'}
# sector_dict = {'element_dict'}
# # element_dict = {'element'}
#
# sector_dict.update(['element_dict'])
# node_dict.update(sector_dict)
# module_dict.update(node_dict)
# system_dict.update(module_dict)

# system_dict = {'module_dict': {'node_dict': {'sector_dict': {'element_dict': {"element_name"}}}}}


# system_dict = {}
# module_dict = {'key':'item'}
# node_dict = {'key':'item'}
# sector_dict = {}
# element_dict = {}
#
# sector_dict.update(element_dict)
# node_dict.update(sector_dict)
# module_dict.update(node_dict)
# system_dict.update(module_dict)
#
# # usr_sel =
#
# # sector_dict
# element_dict[2] = 'yolo'

element_dict = {'key':'item'}

element_dict['key']['item'] = 'yolo'

print(element_dict)
