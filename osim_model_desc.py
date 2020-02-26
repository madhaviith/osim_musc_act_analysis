import opensim as osim
import pandas as pd
import json
import sys,math,os


#code to extract muscle names and indices of OSIM model and write to xlsx
cwd = os.getcwd()
osim_file_name = "ArnoldHamner_LegsTorsoArms_v2.1"
path_to_osim_model = cwd + "/"+ osim_file_name + ".osim"


model = osim.Model(path_to_osim_model)
joints = model.getJointSet()
muscles = model.getMuscles()

print joints.getSize()
print muscles.getSize()

#append the muscles to a list
osim_muscles_list = []
for j in range(muscles.getSize()):    
            #func = osim.Constant(1.0)
            #print("muscle index: {} and muscle name :{}".format(j,muscles.get(j).getName()))
          osim_muscles_list.append({"muscle_name":muscles.get(j).getName(),"index_number":j})      

osim_muscles_df = pd.DataFrame(osim_muscles_list)

print osim_muscles_df
#append joints to a list
osim_joints_list = []

for j in range(joints.getSize()):
          osim_joints_list.append({"joint_name":joints.get(j).getName(),"index_number":j})

osim_joints_df = pd.DataFrame(osim_joints_list)

#write muscles and joints to xlsx 
xslx_file_name = osim_file_name + ".xlsx"
writer = pd.ExcelWriter(xslx_file_name)
osim_muscles_df.to_excel(writer,sheet_name="muscles",index=False)
osim_joints_df.to_excel(writer,sheet_name="joints", index=False)
writer.save()
writer.close()
 
