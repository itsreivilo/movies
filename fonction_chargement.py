import pandas as pd 
import ast 
def fonction_charge(path) :
    df = pd.read_csv(path)
    df_f = df.drop_duplicates()
    df_f['release_date'] = pd.to_datetime(df_f['release_date'])
    # De la même façon on convertit la colonne 'budget' qui est composée de chaînes de caractères et non de valeurs numériques
    df_f['budget'] = pd.to_numeric(df_f['budget'], errors='coerce')
    df_f['genres_list'] = df_f['genres_list'].apply(ast.literal_eval)
    return df_f 

