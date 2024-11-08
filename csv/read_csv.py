from loguru import logger
import os
import pandas as pd
import plotly.express as px


__author__ = "Kelvin Philip"
__version__ = "v0.0.1"


# Function to read csv file to a pandas dataframe
def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df

# Main entrypoint for the script
if __name__ == '__main__':
    csvfile = 's3_cel_hc_allocation.csv'
    # Get full file path for csvfile
    csvfile = os.path.join(os.path.dirname(__file__), csvfile)
    # Check if csvfile exists
    if not os.path.exists(csvfile):
        logger.error(f"File {csvfile} not found")
        exit()

    # Read csv file
    logger.info(f"Reading csv file {csvfile}")
    df = read_csv(csvfile)
    logger.info(f"File read successfully")

    # Get rows with the text 'HC' in the column 'Category'
    logger.info(f"Getting rows with 'HC' in the column 'category'")
    hc_df = df[df['Category'].str.contains('HC')]
    logger.info(f"Rows with 'HC' in the column 'category' found successfully")

    # Melt the dataframe to convert all datetime columns to rows
    logger.info(f"Melting the dataframe")
    hc_df = hc_df.melt(id_vars=['Category'], var_name='Date', value_name='Allocation')

    # Set Allocation to 0 if NaN
    logger.info(f"Setting Allocation to 0 if NaN")
    hc_df['Allocation'] = hc_df['Allocation'].fillna(0)
    logger.info(f"Allocation set to 0 if NaN successfully")

    # Combine Category names based on project names
    logger.info(f"Combining category names based on project names")
    project_names = hc_df['Category'].str.replace(' HC', '').str.strip()
    hc_df['Project'] = project_names
    print(hc_df)
    logger.info(f"Category names combined successfully")

    # Convert Allocatioin to float
    logger.info(f"Converting Allocation to float")
    hc_df['Allocation'] = hc_df['Allocation'].astype(float)
    logger.info(f"Allocation converted to float successfully")

    # Format Date to show mm/yy
    logger.info(f"Formatting Date to show mm/yy")
    hc_df['Date'] = pd.to_datetime(hc_df['Date']).dt.strftime('%m/%y')
    logger.info(f"Date formatted successfully")

    # Plot the data using plotly-express area chart
    logger.info(f"Plotting the data")
    fig = px.bar(hc_df, x='Date', y='Allocation', color='Project', title='HC Allocation')
    fig.update_xaxes(rangeslider_visible=True)
    fig.show()
    logger.info(f"Data plotted successfully")