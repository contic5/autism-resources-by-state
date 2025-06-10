import pandas as pd

target_state="Massachusetts"

def double_print(text,target_file,end="\n"):
    print(text,end=end)
    target_file.write(text)
    target_file.write(end)

def get_useful_resources(resource_df,target_file):    
    filtered_df=resource_df[(resource_df["State"]==target_state)]
    double_print(f"{target_state} Resources",target_file)
    for index,row in filtered_df.iterrows():
        line=f"{row['Resource']}: {row['Link']}"
        double_print(line,target_file)

    double_print("\nNational Resources",target_file)
    filtered_df=resource_df[(resource_df["State"]=="National")]
    for index,row in filtered_df.iterrows():
        line=f"{row['Resource']}: {row['Link']}"
        double_print(line,target_file)

    double_print("",target_file)

def main():
    resource_df=pd.read_excel("Autism Resources by State.xlsx")
    with open("autism_resources_email.txt","w") as target_file:
        with open("intro.txt") as intro_file:
            double_print(intro_file.read(),target_file)
        
        get_useful_resources(resource_df,target_file)

        with open("outro.txt") as outro_file:
            double_print(outro_file.read(),target_file)

if __name__=="__main__":
    main()