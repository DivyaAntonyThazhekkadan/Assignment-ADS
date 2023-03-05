# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd 
import  matplotlib.pyplot as plt

def lineplot(df,categories):
    """
    This function plots the  relation between the discount percentage 
    and rating count in the given data frame of  amazon
Arguments :
    1)df is the dataframe  with the data to plot
    2)the categories
    Returns
    -------
    None.

    """
    
    plt.figure(figsize=(15,10));
    xvalues = np.arange(0,110,10,dtype=int)
    plt.xticks(xvalues)
    print(xvalues)
    # print(pd.DataFrame.min(df["rating_count"], axis=1))
    # print(pd.DataFrame.max(df["rating_count"],axis=1))
    #yvalues = np.arange(min(df["rating_count"]),(max(df["rating_count"])+1000),1000,dtype=int)
   
    #plt.yticks(yvalues)
    #to plot favourable and unfavourable plots
    for column in categories:
        dfsub = df_amazon[df_amazon.category == column ].copy()
        pd.DataFrame.drop_duplicates(dfsub,subset = ["category","discount_percentage_n","rating_count"])
        plt.plot(dfsub["discount_percentage_n"],dfsub["rating_count"],label = str(column))
        #plt.scatter(dfsub["discount_percentage_n"],dfsub["rating_count"],label = str(column))
    #labeling
    plt.xlabel("Discount percentage")
    plt.ylabel("Rating Count")
    plt.title(("Relation b/w Discount percentage and Rating Count of the amazon product 'Electronics|Accessories|MemoryCards|MicroSD"))
    #removing white spaces left and right
    # plt.ylim(pd.DataFrame.min(df["rating_count"],1),pd.DataFrame.max(df["rating_count"],1))
    plt.legend()
    #save as png
    plt.savefig("lineplot.png")
    plt.show()
    return       


def barPlot(df):
    """
    generates the bar plot of the rating given for each item in a given category
    

    Parameters
    ----------
    
    df : dataframe.

    Returns
    -------
    None.

    """
    plt.figure(figsize=(15,10))
    plt.bar(df["product_id"],df["rating"])
    # yvalues = np.arange(0,6,5,dtype=int)
    # plt.yticks(yvalues)
    plt.xticks(rotation = 120)
    plt.xlabel("Product Code")
    plt.ylabel("Rating")
    plt.title("Rating for the various products Under "\
              "the catecgory \n Electronics|Accessories|MemoryCards|MicroSD'")
    plt.savefig("bar.png",bbox_inches = "tight")
    plt.show()
    return

def scatterplot(df,categories):
    """
    This function plots the  relation between the discount percentage 
    and rating count in the given data frame of  amazon
Arguments :
    1)df is the dataframe  with the data to plot
    2)the categories
    Returns
    -------
    None.

    """
    
    plt.figure(figsize=(15,10));
    xvalues = np.arange(0,110,10,dtype=int)
    plt.xticks(xvalues)
    print(xvalues)
    # print(pd.DataFrame.min(df["rating_count"], axis=1))
    # print(pd.DataFrame.max(df["rating_count"],axis=1))
    #yvalues = np.arange(min(df["rating_count"]),(max(df["rating_count"])+1000),1000,dtype=int)
   
    #plt.yticks(yvalues)
    #to plot favourable and unfavourable plots
    for column in categories:
        dfsub = df_amazon[df_amazon.category == column ].copy()
        pd.DataFrame.drop_duplicates(dfsub,subset = ["category","discount_percentage_n","rating_count"])
        #plt.plot(dfsub["discount_percentage_n"],dfsub["rating_count"],label = str(column))
        plt.scatter(dfsub["discount_percentage_n"],dfsub["rating_count"],label = str(column))
    #labeling
    plt.xlabel("Discount percentage")
    plt.ylabel("Rating Count")
    plt.title(("Relation b/w Discount percentage and Rating Count of the amazon product 'Electronics|Accessories|MemoryCards|MicroSD"))
    #removing white spaces left and right
    # plt.ylim(pd.DataFrame.min(df["rating_count"],1),pd.DataFrame.max(df["rating_count"],1))
    plt.legend()
    #save as png
    plt.savefig("Scatterplot.png")
    plt.show()
    return       

            
            
 #https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset?resource=download
df_amazon = pd.read_excel("amazon.xlsx")
df_comAccessories = df_amazon[df_amazon.category == 'Electronics|Accessories|MemoryCards|MicroSD'].copy()
selected_categories=[
     #'Computers&Accessories|Accessories&Peripherals|Cables&Accessories|Cables|USBCables',\
    #                   ,\
                      'Electronics|Accessories|MemoryCards|MicroSD']#,\
                       #'Electronics|Headphones,Earbuds&Accessories|Headphones|In-Ear']#,\
                    # 'Home&Kitchen|Kitchen&HomeAppliances|SmallKitchenAppliances|Kettles&HotWaterDispensers|ElectricKettles']

print(df_amazon)
lineplot(df = df_amazon, categories = selected_categories)
scatterplot(df = df_amazon, categories = selected_categories)
barPlot(df_comAccessories)
print(df_amazon)