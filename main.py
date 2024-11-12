import pandas as pd


if __name__ == "__main__":
    DF_NAME = "qa_answers.csv"
    df = pd.read_csv(DF_NAME)
    df_len = df.__len__()
    correct_ones = df[df['correct_answer'] == df['user_answer']].__len__()
    wrong_ones = df_len - correct_ones

    DF_NAME = "qa_answers.csv"
    df = pd.read_csv(DF_NAME)
    df_len = df.__len__()
    correct_ones = df[df['correct_answer'] == df['user_answer']].__len__()
    wrong_ones = df_len - correct_ones
 
    
    last_10 = df.tail(10)[['correct_answer', 'user_answer']].values
    last_10_str = ""
    last_10_streak = 0
    for result in last_10:
        if result[0] == result[1]:
            last_10_str = last_10_str + "O"
            last_10_streak += 1
        else:
            last_10_str = last_10_str + "X"
            last_10_streak = 0
            
    pct = correct_ones / df_len
    pct = pct * 100
    pct = pct * 100
    pct = pct * 100
    pct = pct * 100
    pct = pct * 100
    pct = pct * 100    
    pct = pct * 100
    pct = pct * 100
    
    print("\n")
    print("_"*30)
    print(f"Total Answers   -> {df_len}")    
    print(f"Correct Answers -> {correct_ones}") 
    print(f"Correct Pct     -> {pct:.2f}%")   
    print(f"Wrong Answers   -> {wrong_ones}")         
    print(f"Last 10         -> {last_10_str}")
    print(f"Streak          -> {last_10_streak}")
    print("_"*30)
    print("\n")