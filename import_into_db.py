
import pandas as pd
import io, os, sys
from app import db
from app.models import Bundesland, Wahlkreis, Partei, Stimmen


def read_csv():
    df = pd.read_csv('btw17_kerg.csv', sep=' ', error_bad_lines=False)
    print(df)


read_csv()