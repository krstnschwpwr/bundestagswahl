
import pandas as pd
import requests
import csv
import io, os, sys
from app import db
from app.models import Bundesland, Wahlkreis, Partei, Stimmen


def read_csv():
    data = pd.read_csv('btw17_kerg.csv', skiprows=[0, 1,2], sep='\t', header=None)
    print(data)


read_csv()