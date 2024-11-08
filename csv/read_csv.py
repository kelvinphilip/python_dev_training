from loguru import logger
import os
import pandas as pd
import plotly.express as px


__author__ = "Kelvin Philip"
__version__ = "v0.0.2"


# Function to read csv file to a pandas dataframe
def read_csv(file_path):
    logger.info(f"Reading csv file {file_path}")
    df = pd.read_csv(file_path)
    logger.info(f"File read successfully")
    return df

def get_hc_rows(df):
    logger.info(f"Getting rows with 'HC' in the column 'category'")
    hc_df = df[df['Category'].str.contains('HC')]
    logger.info(f"Rows with 'HC' in the column 'category' found successfully")
    return hc_df

def melt_dataframe(df):
    logger.info(f"Melting the dataframe")
    melted_df = df.melt(id_vars=['Category'], var_name='Date', value_name='Allocation')
    return melted_df

def set_allocation_to_zero(df):
    logger.info(f"Setting Allocation to 0 if NaN")
    df['Allocation'] = df['Allocation'].fillna(0)
    logger.info(f"Allocation set to 0 if NaN successfully")
    return df

def combine_category_names(df):
    logger.info(f"Combining category names based on project names")
    project_names = df['Category'].str.replace(' HC', '').str.strip()
    df['Project'] = project_names
    logger.info(f"Category names combined successfully")
    return df

def convert_allocation_to_float(df):
    logger.info(f"Converting Allocation to float")
    df['Allocation'] = df['Allocation'].astype(float)
    logger.info(f"Allocation converted to float successfully")
    return df

def format_date(df):
    logger.info(f"Formatting Date to show mm/yy")
    df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%m/%y')
    logger.info(f"Date formatted successfully")
    return df

def plot_data(df):
    logger.info(f"Plotting the data")
    fig = px.bar(df, x='Date', y='Allocation', color='Project', title='HC Allocation')
    fig.update_xaxes(rangeslider_visible=True)
    fig.show()
    logger.info(f"Data plotted successfully")
    return fig

def save_plot(fig, filename):
    logger.info(f"Saving the plot as html")
    fig.write_html(filename)
    logger.info(f"Plot saved successfully")


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
    df = read_csv(csvfile)

    # Get rows with the text 'HC' in the column 'Category'
    hc_df = get_hc_rows(df)

    # Melt the dataframe to convert all datetime columns to rows
    hc_df = melt_dataframe(hc_df)

    # Set Allocation to 0 if NaN
    hc_df = set_allocation_to_zero(hc_df)

    # Combine Category names based on project names
    hc_df = combine_category_names(hc_df)

    # Convert Allocation to float
    hc_df = convert_allocation_to_float(hc_df)

    # Format Date to show mm/yy
    hc_df = format_date(hc_df)

    # Plot the data using plotly-express area chart
    fig = plot_data(hc_df)

    # Save the plot as html
    save_plot(fig, 'hc_allocation.html')