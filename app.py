# import streamlit as st
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# import pandas as pd


# def get_data_from_spreadsheet():
#     scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
#     credentials = ServiceAccountCredentials.from_json_keyfile_name("quantum-idiom-407905-a69b27e14d3d.json", scope)
#     client = gspread.authorize(credentials)
#     sheet = client.open("Pre Sales Tasks").worksheet("Daily Report Dec") # Replace with your Google Spreadsheet name

#     # Assuming columns: Task, Email, Status (Change column numbers if needed)
#     # data = sheet.get_all_records()[3:]
#     data = sheet.get_all_values()[1:]
#     data=pd.DataFrame(data)

#     data.columns = ['Name', 'Date', 'CRM Calls', 'Telecalling Calls', 'No. of Calls', 'Target Comment', 'Target left', 'CRM Attempted', 'CRM Dead', 'Telecalling Attempted', 'Telecalling Dead', 'CRM Prospect', 'Telecalling Prospect', 'Total Prospect', 'Site Visit Done', 'Booking Done',"Task Done Status", 'MTD Calls', 'Avg Calls', 'MTD CRM Prospect', 'MTD Telecalling Prospect', 'MTD Total Prospect', 'MTD Site Visit Done', 'MTD Booking Done', 'MTD Calls22', 'MTD Average Calls222', 'MTD Prospects2222', 'MTD Site Visits22', 'MTD Booking Done22']
#     data = data.iloc[1:, :-5]
#     return data


# def main():
#     st.title("Pre Sales Telecalling Report")

#     data=get_data_from_spreadsheet()
#     unqiue=data["Name"].unique()

#     A,B,C=st.columns(3)
#     Start_Date = A.date_input("Enter your start date",value=None)
#     End_Date = B.date_input("Enter your End date",value=None)
#     Executive = C.selectbox("Choose Executive Name:", options=["All"]+list(unqiue))


#     print(Start_Date)
#     print(End_Date)
#     print(type(End_Date))
#     print(Executive)

#     data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')
#     # data['Date'] = data['Date'].dt.strftime('%Y/%m/%d')

#     if Start_Date==None and End_Date==None and Executive=="All":
#         st.write(data)
#     else:
#         if Start_Date!=None:
#             data=data[data["Date"].dt.date>=Start_Date]
#         if End_Date!=None:
#             data=data[data["Date"].dt.date<=End_Date]
#         if Executive!="All":
#             data=data[data["Name"]==Executive]
#         else:
#             pass

#     st.write(data)

# main()

import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

class SalesReportApp:
    def __init__(self):
        self.scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name("quantum-idiom-407905-a69b27e14d3d.json", self.scope)
        self.client = gspread.authorize(self.credentials)
        self.sheet = self.client.open("Pre Sales Tasks").worksheet("Daily Report Dec")  # Replace with your Google Spreadsheet name
        self.data,self.data1 = self.get_data_from_spreadsheet()

    def get_data_from_spreadsheet(self):
        data = self.sheet.get_all_values()[1:]
        data = pd.DataFrame(data)
        data.columns = ['Name', 'Date', 'CRM Calls', 'Telecalling Calls', 'No. of Calls', 'Target Comment', 'Target left', 'CRM Attempted', 'CRM Dead', 'Telecalling Attempted', 'Telecalling Dead', 'CRM Prospect', 'Telecalling Prospect', 'Total Prospect', 'Site Visit Done', 'Booking Done',"Task Done Status", 'MTD Calls', 'Avg Calls', 'MTD CRM Prospect', 'MTD Telecalling Prospect', 'MTD Total Prospect', 'MTD Site Visit Done', 'MTD Booking Done', 'MTD Calls22', 'MTD Average Calls222', 'MTD Prospects2222', 'MTD Site Visits22', 'MTD Booking Done22']
        data = data.iloc[1:, :-5]
        data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')
        return data,data

    def display_ui(self):
        st.title("Pre Sales Telecalling Report")

        unique_executives = self.data["Name"].unique()

        col_start, col_end, col_executive=st.columns(3)
        self.start_date = col_start.date_input("Enter your start date", value=None)
        self.end_date = col_end.date_input("Enter your End date", value=None)
        self.executive = col_executive.selectbox("Choose Executive Name:", options=["All"] + list(unique_executives))

        st.write(f"Start Date: {self.start_date}")
        st.write(f"End Date: {self.end_date}")
        st.write(f"Executive: {self.executive}")

    

    def filter_data(self):
        if self.start_date is not None:
            self.data = self.data[self.data["Date"].dt.date >= self.start_date]
        if self.end_date is not None:
            self.data = self.data[self.data["Date"].dt.date <= self.end_date]
        if self.executive != "All":
            self.data = self.data[self.data["Name"] == self.executive]

    def graph(self):
        # st.title("Pre Sales Telecalling Report")
        # unique_executives1 = self.data1["Name"].unique()
        # self.data1=self.data1[['Name', 'Date', 'CRM Calls', 'Telecalling Calls', 'No. of Calls']]
        # self.data1 = self.data1.sort_values(by='Date')
        # self.executive1 = st.selectbox("Choose Executive Name:", list(unique_executives1))
        # self.data1=self.data1[self.data1["Name"]==self.executive1]
        # st.line_chart(self.data1.set_index('Date'))
        # st.pyplot()
        # st.write(self.data1)
        st.title("Pre Sales Telecalling Report")
        parameter_options = ['CRM Calls', 'Telecalling Calls',"No. of Calls",'CRM Prospect', 'Telecalling Prospect', 'Total Prospect']
        # self.data1 = self.data1["CRM Calls"].astype(int)
        # self.data1 = self.data1["Telecalling Calls"].astype(int)
        chosen_parameter = st.selectbox("Choose Parameter:", parameter_options)

        unique_executives1 = self.data1["Name"].unique()
        self.data1 = self.data1[['Name', 'Date', chosen_parameter]]
        self.data1['Date'] = pd.to_datetime(self.data1['Date'])
        self.data1 = self.data1.sort_values(by='Date')

        # Choose Executive Name
        self.executive1 = st.selectbox("Choose Executive Name:", list(unique_executives1))
        self.data1 = self.data1[self.data1["Name"] == self.executive1]

        # Extract day from datetime and set it as the index
        self.data1['Day'] = self.data1['Date'].dt.day
        self.data1[chosen_parameter] = self.data1[chosen_parameter].astype(int)
        self.data1 = self.data1[['Day', chosen_parameter]]
        # self.data1 = self.data1.set_index('Day')

        print(self.data1)


        # Plot the line chart
        # st.scatter_chart(self.data1,y=chosen_parameter)
        st.scatter_chart(self.data1, x="Day",y=chosen_parameter)

        # Display the DataFrame
        st.write(self.data1)


    def display_result(self):
        st.write(self.data)

    def run(self):
        self.display_ui()
        self.filter_data()
        self.display_result()
        self.graph()

if __name__ == "__main__":
    app = SalesReportApp()
    app.run()

