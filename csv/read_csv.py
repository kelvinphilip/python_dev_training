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

def get_hc_rows(df):
    return df[df['Category'].str.contains('HC')]

def melt_dataframe(df):
    return df.melt(id_vars=['Category'], var_name='Date', value_name='Allocation')

def set_allocation_to_zero(df):
    df['Allocation'] = df['Allocation'].fillna(0)
    return df

def combine_category_names(df):
    project_names = df['Category'].str.replace(' HC', '').str.strip()
    df['Project'] = project_names
    return df

def convert_allocation_to_float(df):
    df['Allocation'] = df['Allocation'].astype(float)
    return df

def format_date(df):
    df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%m/%y')
    return df

def plot_data(df):
    fig = px.bar(df, x='Date', y='Allocation', color='Project', title='HC Allocation')
    fig.update_xaxes(rangeslider_visible=True)
    fig.show()
    return fig

def save_plot(fig, filename):
    fig.write_html(filename)


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
    hc_df = get_hc_rows(df)
    logger.info(f"Rows with 'HC' in the column 'category' found successfully")

    # Melt the dataframe to convert all datetime columns to rows
    logger.info(f"Melting the dataframe")
    hc_df = melt_dataframe(hc_df)

    # Set Allocation to 0 if NaN
    logger.info(f"Setting Allocation to 0 if NaN")
    hc_df = set_allocation_to_zero(hc_df)
    logger.info(f"Allocation set to 0 if NaN successfully")

    # Combine Category names based on project names
    logger.info(f"Combining category names based on project names")
    hc_df = combine_category_names(hc_df)
    print(hc_df)
    logger.info(f"Category names combined successfully")

    # Convert Allocation to float
    logger.info(f"Converting Allocation to float")
    hc_df = convert_allocation_to_float(hc_df)
    logger.info(f"Allocation converted to float successfully")

    # Format Date to show mm/yy
    logger.info(f"Formatting Date to show mm/yy")
    hc_df = format_date(hc_df)
    logger.info(f"Date formatted successfully")

    # Plot the data using plotly-express area chart
    logger.info(f"Plotting the data")
    fig = plot_data(hc_df)
    logger.info(f"Data plotted successfully")

    # Save the plot as html
    logger.info(f"Saving the plot as html")
    save_plot(fig, 'hc_allocation.html')
    logger.info(f"Plot saved successfully")