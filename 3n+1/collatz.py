import csv
import os
from streamlit.runtime.scriptrunner import get_script_run_ctx
import streamlit as st
import pandas as pd


all_x_points = []
all_y_points = []


def main():
    Stremlit = is_streamlit()

    if Stremlit:
        streamlit_app()
    
    
    

    
def collatz(start: int | None = None, end: int | None = None):
    get_range = (start, end)
    strt_value = get_range[0]
    file_remover()

    for i in range(get_range[0], get_range[1]):
        x_points = []
        y_points = []
        y_point = strt_value
        counter = 1

        while y_point != 1:
            if y_point == strt_value:
                y_points.append(y_point)
                x_points.append(counter)
                counter += 1

            y_point = rules(y_point)
            y_points.append(y_point)
            x_points.append(counter)
            counter += 1
        
        strt_value += 1
        all_x_points.append(x_points)
        all_y_points.append(y_points)

    save_files()

def rules(n: int):
    if n % 2 == 0:
        return int(n/2)
    elif n % 2 == 1:
        return int(n*3+1)
    else:
        raise Exception(f"n % 2 = {n % 2}")

def fget_range(start: int | None = None, end: int | None = None):
    if is_streamlit():
        st.write("Choose a range.")
        start = st.number_input("Number to start", value=None, placeholder="Type a number...")
        end = st.number_input("Number to end", value=None, placeholder="Type a number...")
        return (start, end)
    else:
        try:
            start = int(input("Number to start: "))
            end = int(input("Number to end: "))
        except ValueError:
            raise
    return (start, end+1)


def save_files():
    for i in range(len(all_x_points)):
        with open(f"./data/{i+1}_x_data_points.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows([[x] for x in all_x_points[i]])
        
        with open(f"./data/{i+1}_y_data_points.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows([[y] for y in all_y_points[i]])

def is_streamlit():
    return get_script_run_ctx() is not None

def file_remover():
    csv_files = list_files()

    for file in csv_files:
        if file.endswith(".csv"):
            os.remove(f"./data/{file}")

def list_files():
    files = os.listdir("./data/")
    csv_files = []
    for f in files:
        if f.endswith(".csv"):
            csv_files.append(f)
    
    if csv_files is not None:
        return csv_files
    else:
        raise Exception("There are no csv files. Create ones first.")

def streamlit_app():
    st.markdown("# The Collatz Conjecture")
    st.write("***This file showcases The Collatz Conjecture!***")
    st.write("""
    The Collatz Conjecture, or (3n+1) problem, states that starting with any positive integer (n) and repeating
    the rules—if (n) is even, divide by 2; if (n) is odd, multiply by 3 and add 1—the sequence will always eventually reach 1.
    """)

    st.markdown("___")

    st.write("""
    You can try it yourself. Choose a range, e.g. 3-20, and for every number in this range the rules of 
    the Collatz Conjecture described above will be applied. 
    Based on this, you will receive file lists containing the x and y points for each number. 
    If you want to visualize the path each number took until it reached 1, select the corresponding x and y data points 
    from the file lists and you will be able to see it.
    """)

    # This problem below gave me a headache. 
    # I had a problem to stop continuous error messages because streamlit tried to
    # execute v_range[0] and v_range[1] while they were None, before inputting any number.
    v_range = fget_range()

    # if v_range[0] is None or v_range[1] is None:
    #     st.info("Enter range values")
    #     st.stop()

    if st.button("Run"):
        if v_range[1] < v_range[0]:
            st.warning("Number end can't be smaller than number start!")
        collatz(int(v_range[0]), int(v_range[1])+1)
    else:
        st.warning("Enter range values before running!")

    csv_files = list_files()
    if csv_files:
        st.warning("The .csv files with the x and y data points have been created")
    else:
        st.info("There are no csv files created yet enter range values.")
        st.stop()
    
    st.markdown("___")

    st.markdown("### Choose from the files.")
    st.write("Select two files containing x and y data points. It is important to select only the corresponding x and y files.")

    x_data_points = pd.read_csv(f"./data/{st.selectbox(label='select x data points', options=csv_files)}", header=None)[0].tolist()
    y_data_points = pd.read_csv(f"./data/{st.selectbox(label='select y data points', options=csv_files)}", header=None)[0].tolist()
    

    if st.button("Chart"):
        df = pd.DataFrame({"y": y_data_points}, index=x_data_points)
        st.line_chart(df)
    else:
        st.warning("Select files before running!")
    
    st.markdown("___")
    st.write("You can remove and clear the files if you wish.")
    
    if st.button("Delete files"):
        file_remover()
        st.rerun()




    


if __name__ == "__main__":
    main()