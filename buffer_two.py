import arcpy
input_feature_class = r"D:\Bharati\Sem_3\Programming_3\P1_Running_Python_Scripts\Practical_1_ProProject\Practical_1_ProProject\01_Running_Python_Scripts.gdb\Wilson_Schools"

output_buffer_path = r"C:\Users\HARSHAL\Documents\ArcGIS\Projects\MyProject3\output.gdb\buffer_500"

distance = "500 meters"

arcpy.analysis.Buffer(input_feature_class, output_buffer_path, distance)
print("--------------------------------")