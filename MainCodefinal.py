

import pandas as pd
import sys
import pycountry
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import wbpy


class ScorceCode:

    #User inputs in the console the product to market_
    #prod= input("enter the item you desire to sell:")


    def forWorld(product):

        pytrend = TrendReq()
        pytrend.build_payload(kw_list=[product])
        interest_by_region_df = pytrend.interest_by_region()
        related_topics = pytrend.related_topics()
        related_queries = pytrend.related_queries()
        #interest_by_region_df.values.tolist() gives us data of numbers
        dc=interest_by_region_df.loc[(interest_by_region_df!=0).any(axis=1)]
        print(related_topics)
        print(related_queries)
        return dc

    def forWorld1(product):
        kw_list = [product]
        pytrend = TrendReq()
        pytrend.build_payload(kw_list )
        interest_over_time_df = pytrend.get_historical_interest(kw_list, year_start=2017, month_start=1, day_start=1, hour_start=0, year_end=2018, month_end=1, day_end=1, hour_end=0, cat=0, geo='', gprop='', sleep=0)
        #interest_by_region_df.values.tolist() gives us data of numbers
        print(list(interest_over_time_df.columns.values))
        dc=interest_over_time_df.loc[(interest_over_time_df!=0).any(axis=1)]
        return dc



   #User enters the country value
    # somehow find a way to map the name of the country to country codes

    def forCountry(Country, product):
        pytrend = TrendReq()
        ctemp=pycountry.countries.get(name=Country.title())
        pytrend.build_payload(kw_list=[product], geo=ctemp.alpha_2)
        interest_by_region_df = pytrend.interest_by_region(resolution='REGION')
        dc = interest_by_region_df.loc[(interest_by_region_df != 0).any(axis=1)]
        return dc

    def forCountryMarketing(Country):
        pytrend = TrendReq()
        ctemp = pycountry.countries.get(name=Country.title())
        pytrend.build_payload(kw_list=['Email marketing', 'Radio Advertising', 'Mobile Marketing', 'Fliers','Newspaper Marketing'], geo=ctemp.alpha_2) #It can take maximum 5 products in kw_list
        interest_by_region_df = pytrend.interest_by_region(resolution='REGION')
        pytrend.build_payload(kw_list=['Business Card', 'Billboards', 'Bus Shelter Ads', 'Print Ads', 'Television Advertising'],geo=ctemp.alpha_2)
        interest_by_region_df1 = pytrend.interest_by_region(resolution='REGION')


        return interest_by_region_df1 , interest_by_region_df



    #User enters the state value after choosing the country
    def forState(Country, State, product):

            pytrend = TrendReq()
            cc = pycountry.countries.get(name=Country.title())
            provinces = []
            provincelist = list(pycountry.subdivisions.get(country_code=cc.alpha_2))
            for p in provincelist:
                 provinces.append((p.code.split('-')[1], p.name))
            for i in range(len(provinces)):
                for j in range(len(provinces[0])):
                    if provinces[i][j]==State.title():
                         ss=provinces[i][0]
            value=cc.alpha_2+"-"+ss

            pytrend.build_payload(kw_list=[product], geo=value )
            interest_by_region_df = pytrend.interest_by_region(resolution='REGION')
            dc = interest_by_region_df.loc[(interest_by_region_df != 0).any(axis=1)]

            return dc




    def forTotalUsers(Country,city):
        df1 = pd.read_csv("/Users/canquerydeborah/Desktop/PRI_Project/cities.csv")
        df2 = pd.read_csv("/Users/canquerydeborah/Desktop/PRI_Project/penitration.csv")
        data1 = int(df1.loc[df1['city'] == city.title(), 'pop'])
        data2 = float(df2.loc[df2['country'] == Country.title(), '2016'])



        return int(data1*data2/100)

    def forTotalPop(city):
        df1 = pd.read_csv("/Users/canquerydeborah/Desktop/PRI_Project/cities.csv")

        data1 = int(df1.loc[df1['city'] == city.title(), 'pop'])

        return int(data1)

    def forTotalPenitration(Country):
        df2 = pd.read_csv("/Users/canquerydeborah/Desktop/PRI_Project/penitration.csv")

        data2 = float(df2.loc[df2['country'] == Country.title(), '2016'])

        return int(data2)




