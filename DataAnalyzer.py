import pandas as pd

class DataAnalyzer:
    def __init__(self, data_file):
        self.data_file = data_file

    def analyze_data(self):
        try:
            data = pd.read_csv(self.data_file)
            summary = data.describe()
            print(summary)
        except FileNotFoundError:
            print("Data file not found.")
        except pd.errors.EmptyDataError:
            print("Data file is empty.")
        except pd.errors.ParserError:
            print("Unable to parse the data file.")

def main():
    data_file = "data.csv"

    analyzer = DataAnalyzer(data_file)
    analyzer.analyze_data()

if __name__ == "__main__":
    main()
