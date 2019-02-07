

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


        list_of_related_queries = []

        for k in related_queries:
            rel_qarray = related_queries[k]['top']

        related_queries2 = rel_qarray.loc[:, 'query' ]
        df = pd.DataFrame(related_queries2, columns=['query'])
        for index, row in df.iterrows():
            list_of_related_queries.append(row["query"])

        for k in related_topics:
            related_tarray = related_topics[k]['title']

        list_of_related_topics = related_tarray.values.tolist()
        return dc, list_of_related_queries, list_of_related_topics




  #  def forWorld1(product):
  #      kw_list = [product]
  #      pytrend = TrendReq()
  #     pytrend.build_payload(kw_list )
  #      interest_over_time_df = pytrend.get_historical_interest(kw_list, year_start=2017, month_start=1, day_start=1, hour_start=0, year_end=2018, month_end=1, day_end=1, hour_end=0, cat=0, geo='', gprop='', sleep=0)
  #      #interest_by_region_df.values.tolist() gives us data of numbers
  #      print(list(interest_over_time_df.columns.values))
  #      dc=interest_over_time_df.loc[(interest_over_time_df!=0).any(axis=1)]
  #      return dc



   #User enters the country value
    # somehow find a way to map the name of the country to country codes


    def forCountry(Country, product):
        pytrend = TrendReq()
        ctemp=pycountry.countries.get(name=Country.title())
        print(Country.title())
        pytrend.build_payload(kw_list=[product], geo=ctemp.alpha_2)
        interest_by_region_df = pytrend.interest_by_region(resolution='REGION')

        related_topics = pytrend.related_topics()
        related_queries = pytrend.related_queries()

        dc = interest_by_region_df.loc[(interest_by_region_df != 0).any(axis=1)]
        column_name = dc.columns.values
        dc = dc.sort_values(by=column_name[0],ascending= False).iloc[0:10]
        list_of_related_queries = []
        list_of_related_topics = []


        for k in related_queries:
            rel_qarray = related_queries[k]['top']


        if rel_qarray is not None:
            related_queries2 = rel_qarray.loc[:, 'query']
            df = pd.DataFrame(related_queries2, columns=['query'])
            for index, row in df.iterrows():
                list_of_related_queries.append(row["query"])


            for k in related_topics:
                if related_topics[k]['title'] is not None:
                    related_tarray = related_topics[k]['title']

            list_of_related_topics = related_tarray.values.tolist()

        return dc, list_of_related_queries, list_of_related_topics





    def forCountryMarketing(Country):
        pytrend = TrendReq()
        ctemp = pycountry.countries.get(name=Country.title())
        pytrend.build_payload(kw_list=['Email marketing', 'Radio Advertising', 'Mobile Marketing', 'Television Advertising', 'Facebook Advertisement'], geo=ctemp.alpha_2) #It can take maximum 5 products in kw_list
        digital_marketing = pytrend.interest_by_region(resolution='REGION')
        pytrend.build_payload(kw_list=['Newspaper Marketing', 'Billboards', 'Bus Shelter Ads', 'Print Ads','Fliers'],geo=ctemp.alpha_2)
        analog_marketing = pytrend.interest_by_region(resolution='REGION')

        return digital_marketing , analog_marketing


    def RecommendationText(analog,digital):
        recommedantion = ''

        maxAnag = 0
        Anag_Name= ''
        typeofAnalog=0
        Digi_Name=''
        maxDigi = 0
        typeofDigital=0
        for marketing in analog:
           if(marketing>maxAnag):
               maxAnag=marketing
               typeofAnalog= analog.index(marketing);
               if typeofAnalog == 0 :
                   Anag_Name= 'Newspaper Marketing'
               elif typeofAnalog == 1:
                   Anag_Name = 'Billboards'
               elif typeofAnalog == 2:
                   Anag_Name = 'Bus Shelter Ads'
               elif typeofAnalog == 1:
                   Anag_Name = 'Print Ads'
               elif typeofAnalog == 1:
                   Anag_Name = 'Fliers'


        for marketing in digital:
           if(marketing>maxDigi):
               maxDigi=marketing
               typeofDigital = digital.index(marketing)
               if typeofDigital == 0 :
                   Digi_Name= 'Email marketing'
               elif typeofAnalog == 1:
                   Digi_Name = 'Radio Advertising'
               elif typeofAnalog == 2:
                   Digi_Name = 'Mobile Marketing'
               elif typeofAnalog == 1:
                   Digi_Name = 'Television Advertising'
               elif typeofAnalog == 1:
                   Digi_Name = 'Facebook Advertisement'


        if maxDigi > maxAnag:
            recommedantion =  'Thes most popular analog marketing in this country is ' + Anag_Name  +' and the most popular digital marketing is ' + Digi_Name + '.\n' + \
                              'As the results show the most recommended approach of marketing is the Digital marketing approach'
        else:
            recommedantion = 'Thes most popular analog marketing in this country is ' + Anag_Name + 'and the most popular digital marketing is ' + Digi_Name + '.\n' + \
                             'As the results show the most recommended approach of marketing is the Analog marketing approach'

        print(recommedantion)


        return recommedantion

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
