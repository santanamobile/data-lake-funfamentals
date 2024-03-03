#!/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

class DataLake:
    def __init__(self, db_file='datalake.db'):
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.create_table()
    
    def create_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                value FLOAT
            );
        ''')
        self.conn.commit()

    def collect_data(self, value):
        self.conn.execute('''
            INSERT INTO data (value) VALUES (?);
        ''', (value,))
        self.conn.commit()

    def retrieve_data(self):
        return pd.read_sql_query('SELECT * FROM data', self.conn)
    
    def analyze_data(self):
        data = self.retrieve_data()
        mean_value = data['value'].mean()
        std_dev = data['value'].std()
        return mean_value, std_dev

    def visualize_data(self):
        data = self.retrieve_data()
        plt.plot(data['timestamp'], data['value'])
        plt.xlabel('Timestamp')
        plt.title('Data Lake Visualization')
        plt.show()

def main():
    dl = DataLake()
    dl.collect_data(5.0)
    dl.collect_data(10.0)
    dl.collect_data(11.0)
    print(dl.retrieve_data())
    print(dl.analyze_data())
    mean, std_dev = dl.analyze_data()
    print ("\n Data Analysis : ")
    print ("Mean : ", mean)
    print ("Standard Deviation : ", std_dev)
    dl.visualize_data()

if __name__ == '__main__':
    main()
