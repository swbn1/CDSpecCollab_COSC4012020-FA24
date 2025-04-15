import pandas as pd
import os
import pathlib
import mariadb

if __name__ == '__main__':
    runs_path = pathlib.Path('/home/shared_workspace/CDSpecCollab_COSC4012020-FA24/cd_spec_viewer_web/cd_spec_viewer_web/cdspecruns')
    the_files = list(runs_path.glob('*.csv'))
    for file in the_files: 
        3
        # print(file)
        # df = pd.read_csv(file)



    try:
        connection = mariadb.connect(
            user="maria",
            password="6969",
            host="localhost",
            port=3306,
            database="mariadb"
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Example query: Create a table
        cursor.execute('SHOW COLUMNS FROM cdspec_specrun')
        columns = cursor.fetchall()
        print(columns)
        for col in columns:
            print(col[0])
        update_query = "UPDATE cdspec_specrun SET " + ", ".join([f"{column[0]} = 'MONKE'" for column in columns])
        cursor.execute(update_query)
        # Commit changes
        connection.commit()

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")

    finally:
        # Close the connection
        if connection:
            connection.close()