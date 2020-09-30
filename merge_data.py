#imports
import dask.dataframe as dd
from dask.diagnostics import ProgressBar
import pandas as pd


# load datadframes with pandas

# it's cconvinient to give column names yourself -> names flag, you have to disable the header if there is one -> nedaer = None
df1 = pd.read_csv('path/to/data.txt', sep=';', names = ['ID','POS','TYPE','SET'], header = None)
df2 = pd.read_csv('exon.hg19_ucsc.onlystart.txt', sep=';', names = ['POS','REGION'], header = None) #for example

#load it with dask
df1 = dd.read_csv('data.txt', sep=';', names = ['ID','POS','TYPE','SET'], header = None)
df2 = dd.read_csv('exon.hg19_ucsc.onlystart.txt', sep=';', names = ['POS','REGION'], header = None)


# two options, both do the same, buit have different syntax
# how: perform left outer join
# on: Column to merge on
#pandas
df_merge = pd.merge(df1, df2, how = 'left', on = 'POS')
df_merge = df1.merge(df2, how = 'left', on = 'POS')

#dask
df_merge = dd.merge(df1, df2, how = 'left', on = 'POS')
df_merge = df1.merge(df2, how = 'left', on = 'POS')

# if you use dask you can call a progressbar for the task
ProgressBar().register()

# write it to csv
df9.to_csv('path/to/csv', index=False, header=False)




# Data manipulation:

#read files of dir
#all_files = glob.glob(path +"/*.csv")

# alternative
#for file in file_list:
#    if(file.endswith('.csv')):
#        print(file)


#perform merge on multiple files
#for file in file_list:
#    if(file.endswith('.csv')):
        
        #df1 = ddf.read_csv('/home/mosul/Desktop/data_for_hristo/kg_exon_sorted.csv', names = ['ID','POS','TYPE','SET','AF','REGION'], header = None)
#        df_tmp = pd.read_csv(file, names = ['POS','REGION'], header = None)
#        df1 = pd.merge(df1,df_tmp, on='POS', how='left')

#        print(file)
