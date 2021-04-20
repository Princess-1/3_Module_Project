def create_sql_table_from_df(df, name, conn):
    '''
    Args:
        df, name, conn: Function takes in each dataframe 
    Returns: 
        table: Converts each dataframe to a sql table
    '''
    # Use try except
    # it will try to make a table
    # if a table exists the except part of the code will stop the program from making duplicates
    try:
        df.to_sql(name, conn)
        print(f"Created table {name}")
    
    # if the table exists t will tell you, and won't cause an error
    except Exception as e:
        print(f"Could not make table {name}")
        print(e)