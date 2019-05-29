from os import listdir

normal_files_path = '/media/hitkul/DATA/Acadmics/PhD_IIIT_Delhi/NII/image_hate/data/DATA_I_MADE/Images/Normal'
trolled_files_path = '/media/hitkul/DATA/Acadmics/PhD_IIIT_Delhi/NII/image_hate/data/DATA_I_MADE/Images/Trolled'
normal_file=[]

normal_file = ['file://'+normal_files_path+'/'+i+'\n' for i in listdir(normal_files_path)]
trolled_files = ['file://'+trolled_files_path+'/'+i+'\n' for i in listdir(trolled_files_path)]


# 
print(len(normal_file),len(trolled_files))

with open('data/DATA_I_MADE/normal_images_analysis.csv','w') as fout:
        fout.writelines(normal_file)

with open('data/DATA_I_MADE/troll_images_analysis.csv','w') as fout:
        fout.writelines(trolled_files)
