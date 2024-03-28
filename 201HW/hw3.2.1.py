import pandas as pd

# 2.1
def prepare_monster_data(file):
    #file = "2_1_sample.csv"
    data = pd.read_csv(file, engine="c", on_bad_lines="skip")
    
    # removes rows with any columns with missing values 
    data = data.dropna()
    
    counts = data['Environment'].value_counts()
    print(f"FOREST COUNT1: {counts.get('forest', 0)}")
    # removes rows with any columsn with too many values 
    
    
    #removes duplicates
    data = data.drop_duplicates()
    
    counts = data['Environment'].value_counts()
    print(f"FOREST COUNT2: {counts.get('forest', 0)}")
    
    # separates environmnts into multiple rows if possible 
    data = data.assign(Environment=data['Environment'].str.split(',')).explode('Environment').apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    counts = data['Environment'].value_counts()
    print(f"FOREST COUNT3: {counts.get('forest', 0)}")
    '''
    rowsExpandedByEnvironmentData = []
    for index, row in data.iterrows():
        curEnvironments = row["Environment"].split(",")
        for singleEnv in curEnvironments:
            rowsExpandedByEnvironmentData.append({"Name": row["Name"], "Size": row["Size"], "Type": row["Type"], "Environment": singleEnv})
    data = pd.DataFrame(rowsExpandedByEnvironmentData)
    '''
    
    #fixes Size 
    for index, row in data.iterrows():
        rowSize = row["Size"]
        match rowSize:
            case "T":
                rowSize = "tiny"
            case "S":
                rowSize = "small"
            case "M":
                rowSize = "medium"
            case "L":
                rowSize = "large"
            case "H":
                rowSize = "huge"
            case "G":
                rowSize = "gargantuan"
        row["Size"] = rowSize
        
    # all values to lowercase except Name
    
    for columnName in data.columns:
        if columnName != "Name":
            data[columnName] = data[columnName].str.lower()
    
    counts = data['Environment'].value_counts()
    print(f"\"FOREST\" COUNT4: {counts.get('forest', 0)}")
    print(f"\" FOREST\" COUNT4: {counts.get(' forest', 0)}")
    print(f"\"FORESTS\" COUNT4: {counts.get('forests', 0)}")
    print(f"\" FORESTS\" COUNT4: {counts.get(' forests', 0)}")
    
    data.to_csv("hw3Output.txt", index=False)
    
    return data

# 2.2
def monster_type_analysis(monster_df):
    
    output = {}
    
    uniqueNamesPerType = {}  # dictionary of unique names per type

    for _, row in monster_df.iterrows():
        monsterType = row["Type"]
        monsterName = row["Name"]

        if monsterName not in uniqueNamesPerType.get(monsterType, []):
            # Append name to the list of unique names for this type
            uniqueNamesPerType.setdefault(monsterType, []).append(monsterName)

    # Find the type with the largest unique names array
    typeWithMostUniqueNames = "ERROR"
    typeWithLeastUniqueNames = "ERROR"
    largestArrSize = 0
    smallestArrSize = 9999999
    for key, value in uniqueNamesPerType.items():
        if len(value) > largestArrSize:
            largestArrSize = len(value)
            typeWithMostUniqueNames = key
        if len(value) < smallestArrSize:
            smallestArrSize = len(value)
            typeWithLeastUniqueNames = key
    
    output["most_monster_type"] = typeWithMostUniqueNames
    output["most_monster_count"] = largestArrSize
    output["least_monster_type"] = typeWithLeastUniqueNames
    output["least_monster_count"] = smallestArrSize
    
    print(output) 
    
    return output
    
#2.3
def top_three_env_to_see_monsters(monster_df):
    # find the top environments with the most unique monsters in them 
    # return the top 3 
    
    counts = monster_df['Environment'].value_counts()
    print(f"FOREST COUNT: {counts.get('forest', 0)}")

    uniquePerEnv = {}  # dictionary of unique names per type

    for _, row in monster_df.iterrows():
        env = row["Environment"]
        monsterName = row["Name"]

        if monsterName not in uniquePerEnv.get(env, []):
            # Append name to the list of unique names for this type
            uniquePerEnv.setdefault(env, []).append(monsterName)
        
    # Group by 'Environment', calculate the number of unique 'Name' values in each group
    unique_names = monster_df.groupby('Environment')['Name'].nunique()
    
    # Sort in descending order and take the top 3
    print(f"forests count: {len(uniquePerEnv["forest"])}")
    top_three = unique_names.sort_values(ascending=False).head(3)
    
    # Convert to a tuple of tuples
    return tuple((index, value) for index, value in top_three.items())
    
#2.4
def most_gargantuan_monsters_env(monster_df):
    pass


preppedData = prepare_monster_data("monsters.csv")
top_three_env_to_see_monsters(preppedData)