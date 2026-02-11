import pandas as pd

us_states = [
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming"
]

def main():
    dvrs_arr=[]
    with open("public/state_dvrs_pages.txt","r") as dvrs_file:
        state=""
        last_state=""
        last_line_was_state=False
        resource=""
        website=""
        

        lines=dvrs_file.readlines()
        for line in lines:
            line=line.replace("\n","")
            words=line.split(" ")
            if line in us_states:
                state=line
                last_line_was_state=True
            elif last_line_was_state:
                resource=line
                last_line_was_state=False
            elif words[0]=="Website:":
                if state!=last_state:
                    website=words[1]
                    dvrs_dict={"Resource":resource,"Website":website,"State":state}
                    dvrs_arr.append(dvrs_dict)
                last_state=state
    
    dvrs_df=pd.DataFrame.from_dict(dvrs_arr)
    print(dvrs_df.head())
    dvrs_df.to_excel("DVRS Websites.xlsx")

if __name__=="__main__":
    main()