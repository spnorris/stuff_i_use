
import pandas as pd
import numpy as np

class dt_clnr:
    def __init__(self) -> None:
        pass
    
    def cln_cl_nms(self, df):
        """Input: A pandas dataframe
            Output: Dataframe with scrubbed column names"""
        cols = df.columns.tolist()
        rnm_dict = {}

        for i in range(0, len(cols)):
            old_nm = cols[i]
            print('Old Column Name:', old_nm) 
            nw_nm = old_nm.replace(' ', '_')
            nw_nm = ''.join([c for c in nw_nm if c.lower() not in 'aeiou'])
            nw_nm = nw_nm.lower()
            print('New Name:', nw_nm)
            print('================')
            rnm_dict[cols[i]] = nw_nm 

        df2 = df.rename(columns = rnm_dict)
        return df2
    
    def whatisthis(self, df, num):
        """Input: A pandas dataframe, Top X number of columns you want
                    to see by unique value
            Output: Writes details to console letting you
            know what is being mesured in that particular dataframe"""
        print("Shape:", df.shape)
        print("===================")
        print("                   ")
        print("                   ")
        print("===================")
        cols = df.columns.tolist()
        unq_cnts = []
        for i in range(0, len(cols)):
            unq_cnts.append(df[cols[i]].nunique())
        high_card = pd.DataFrame()
        high_card['column_names'] = cols
        high_card['unq_items'] = unq_cnts
        high_card = high_card.sort_values(by = 'unq_items', ascending = False)
        print("Columns with Most Unique Items")
        print(high_card.head(num))
        print("===================")
        print("                   ")
        print("                   ")
        print("===================")
        cols = df.columns.tolist()
        print("List of All Columns:", cols)
    
    def expld_dts(self, df, dt_cols):
        """Input: A pandas dataframe, date columns
           Ouput: The dataframe with columns for yr, mth, wk
        """
        dt_cols = dt_cols
        for i in range(0, len(dt_cols)):
            df[dt_cols[i]] = pd.to_datetime(df[dt_cols[i]])
            df[f"{dt_cols[i]}_yr"] = df[dt_cols[i]].dt.year
            df[f"{dt_cols[i]}_mth"] = df[dt_cols[i]].dt.month
        return df
    