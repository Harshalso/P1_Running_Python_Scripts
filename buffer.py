import arcpy
arcpy.env.workspace = r"D:\Bharati\Sem_3\Programming_3\P1_Running_Python_Scripts\Practical_1_ProProject\Practical_1_ProProject\01_Running_Python_Scripts.gdb"
arcpy.analysis.Buffer("Wilson_Schools", "Wilson_Schools_Buffer", "500 meters")