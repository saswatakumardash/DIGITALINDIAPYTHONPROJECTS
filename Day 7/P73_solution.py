######## IMMUTABLE CODE SECTION BEGIN ########

# helper library functions
import pandas as pd
import sys, os

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


######## IMMUTABLE CODE SECTION END ########

########## USER CODE SECTION BEGIN #########

def main():
    # Path to csv file
    csv_file_path = input()

    # Read the csv file in a pandas Dataframe
    iris_df = pd.read_csv(csv_file_path)

    # Get the highest frequency element for each column
    # note that we need iloc[0] since there can be more than one modes for a column and we just consider the first one
    modes = iris_df.mode().iloc[0]

    # Fill all the missing values using the respective modes.
    iris_df_highest_freq = iris_df.fillna(modes)

    # divide the columns based on the classes
    # For more details on groupby and transform : https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html
    grouped = iris_df.groupby("plant")

    # Calculate the means of each group and create a dataframe with same size as original
    class_wise_means = grouped.transform("mean")

    # Fill the missing values using the class_wise means
    iris_df_classwise_mean = iris_df.fillna(class_wise_means)


    # This is the same as the previous one, just with a different aggregation funciton
    # We can do all the operations in a single line like this as well
    iris_df_classwise_median = iris_df.fillna(iris_df.groupby("plant").transform("median"))

    # print column wise mean
    print("Column wise means:")
    print(iris_df_highest_freq.mean())
    print(iris_df_classwise_mean.mean())
    print(iris_df_classwise_median.mean())


if __name__ == "__main__":
    # Call the main function
    main()


########## USER CODE SECTION END #########