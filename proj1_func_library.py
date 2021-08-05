def conv_multiple_val_to_dict(df, variable, sep_char):
    # Create a dictionary
    dict = {}

    # Split and count distinct education
    for multipleStr in df[variable].dropna().tolist():
        arr = multipleStr.split(sep_char)

        for s in arr:
            key = s.strip()
            if key in dict:
              dict[key] = int(dict[key])+1
            else:
              dict[key] = 1

    # return the result
    return dict
    
def print_var_desc(schema_df, variable):
    print(variable, " = ", list(schema_df[schema_df["Column"]==variable]["QuestionText"])[0])

def print_var_desc_counts_plot(schema_df, df, variable):
    print_var_desc(schema_df, variable)
    
    # Population
    df[variable].value_counts().plot(kind="bar")

def conv_cat_to_ord(df, variable, mapping, is_print_bar_plot):
    df[variable + '_ord'] = df[variable].map(mapping)
    
    if (is_print_bar_plot):
        df[variable + '_ord'].value_counts().plot(kind='bar') 
        
def elbow_method(x):
    from sklearn.cluster import KMeans
    import matplotlib.pyplot as plt
    sum_of_squared_distances = []
    arr = range(1,15)
    for k in arr:
        km = KMeans(n_clusters=k)
        km = km.fit(x)
        print("k=", k, ", km.inertia_=", km.inertia_)
        sum_of_squared_distances.append(km.inertia_)


    plt.plot(arr, sum_of_squared_distances, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Sum_of_squared_distances')
    plt.title('Elbow Method For Optimal k')
    plt.show()
    