# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------------------------------------------
# Author: David Bassard
# Date: 15/11/2019
# ------------------------------------------------------------------------------------------------------------------

# Libraries

import json
from flask import render_template
from app import database_query as dq
from app import app
import plotly
import plotly.graph_objs as go
import datetime

# ------------------------------------------------------------------------------------------------------------------
# Connection to database

path_json_creds = "./.private/mysql_settings.json"
mysql_settings = json.load(open(path_json_creds, "r"))

settings = {
    "host": mysql_settings["myhost"],
    "user": mysql_settings["myuser"],
    "password": mysql_settings["mypassword"],
    "raise_on_warnings" : True
}


# ------------------------------------------------------------------------------------------------------------------
# Home

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

# ------------------------------------------------------------------------------------------------------------------
# ------------------QUESTION 1--------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# Question 1 : Global

@app.route('/survey_eco_1')
def survey_eco_1():

    data = dq.sr_eco1(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_1.html",
        graph_sr1 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='indianred')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 1 : na

@app.route('/survey_eco_na_1')
def survey_eco_na_1():

    data = dq.sr_econa1(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_na_1.html",
        graph_srna1 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='lightblue')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 1 : citizen

@app.route('/survey_eco_cc_1')
def survey_eco_cc_1():

    data = dq.sr_ecocc1(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_cc_1.html",
        graph_srcc1 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='olivedrab')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))


# ------------------------------------------------------------------------------------------------------------------
# Question 1 : Elected official and institution

@app.route('/survey_eco_eei_1')
def survey_eco_eei_1():

    data = dq.sr_ecoeei1(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_eei_1.html",
        graph_sreei1 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='mediumorchid')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 1 : for-profit organization

@app.route('/survey_eco_obl_1')
def survey_eco_obl_1():

    data = dq.sr_ecoobl1(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_obl_1.html",
        graph_srobl1 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='goldenrod')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 1 : non-profit organization

@app.route('/survey_eco_obnl_1')
def survey_eco_obnl_1():

    data = dq.sr_ecoobnl1(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_obnl_1.html",
        graph_srobnl1 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='chocolate')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))


# ------------------------------------------------------------------------------------------------------------------
# ------------------QUESTION 2--------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# Question 2 : Global

@app.route('/survey_eco_2')
def survey_eco_2():

    data = dq.sr_eco2(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_2.html",
        graph_sr2 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='indianred')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 2 : na

@app.route('/survey_eco_na_2')
def survey_eco_na_2():

    data = dq.sr_econa2(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_na_2.html",
        graph_srna2 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='lightblue')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 2 : citizen

@app.route('/survey_eco_cc_2')
def survey_eco_cc_2():

    data = dq.sr_ecocc2(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_cc_2.html",
        graph_srcc2 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='olivedrab')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 2 : Elected official and institution

@app.route('/survey_eco_eei_2')
def survey_eco_eei_2():

    data = dq.sr_ecoeei2(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_eei_2.html",
        graph_sreei2 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='mediumorchid')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))


# ------------------------------------------------------------------------------------------------------------------
# Question 2 : for-profit organization

@app.route('/survey_eco_obl_2')
def survey_eco_obl_2():

    data = dq.sr_ecoobl2(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_obl_2.html",
        graph_srobl2 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='goldenrod')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 2 : non-profit organization

@app.route('/survey_eco_obnl_2')
def survey_eco_obnl_2():

    data = dq.sr_ecoobnl2(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_obnl_2.html",
        graph_srobnl2 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='chocolate')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# ------------------QUESTION 3--------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# Question 3 : Global

@app.route('/survey_eco_3')
def survey_eco_3():

    data = dq.sr_eco3(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_3.html",
        graph_sr3 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='indianred')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 3 : na

@app.route('/survey_eco_na_3')
def survey_eco_na_3():

    data = dq.sr_econa3(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_na_3.html",
        graph_srna3 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='lightblue')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 3 : citizen

@app.route('/survey_eco_cc_3')
def survey_eco_cc_3():

    data = dq.sr_ecocc3(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_cc_3.html",
        graph_srcc3 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='olivedrab')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 3 : Elected official and institution

@app.route('/survey_eco_eei_3')
def survey_eco_eei_3():

    data = dq.sr_ecoeei3(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_eei_3.html",
        graph_sreei3 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='mediumorchid')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 3 : for-profit organization

@app.route('/survey_eco_obl_3')
def survey_eco_obl_3():

    data = dq.sr_ecoobl3(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_obl_3.html",
        graph_srobl3 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='goldenrod')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 3 : non-profit organization

@app.route('/survey_eco_obnl_3')
def survey_eco_obnl_3():

    data = dq.sr_ecoobnl3(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_obnl_3.html",
        graph_srobnl3 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='chocolate')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# ------------------QUESTION 4--------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# Question 4 : Global

@app.route('/survey_eco_4')
def survey_eco_4():

    data = dq.sr_eco4(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_4.html",
        graph_sr4 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='indianred')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 4 : na

@app.route('/survey_eco_na_4')
def survey_eco_na_4():

    data = dq.sr_econa4(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_na_4.html",
        graph_srna4 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='lightblue')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 4 : citizen

@app.route('/survey_eco_cc_4')
def survey_eco_cc_4():

    data = dq.sr_ecocc4(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_cc_4.html",
        graph_srcc4 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='olivedrab')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 4 : Elected official and institution

@app.route('/survey_eco_eei_4')
def survey_eco_eei_4():

    data = dq.sr_ecoeei4(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_eei_4.html",
        graph_sreei4 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='mediumorchid')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 4 : for-profit organization

@app.route('/survey_eco_obl_4')
def survey_eco_obl_4():

    data = dq.sr_ecoobl4(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_obl_4.html",
        graph_srobl4 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='goldenrod')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 4 : non-profit organization

@app.route('/survey_eco_obnl_4')
def survey_eco_obnl_4():

    data = dq.sr_ecoobnl4(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_obnl_4.html",
        graph_srobnl4 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='chocolate')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# ------------------QUESTION 5--------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# Question 5 : Global

@app.route('/survey_eco_5')
def survey_eco_5():

    data = dq.sr_eco5(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_5.html",
        graph_sr5 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='indianred')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 5 : na

@app.route('/survey_eco_na_5')
def survey_eco_na_5():

    data = dq.sr_econa5(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_na_5.html",
        graph_srna5 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='lightblue')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 5 : citizen

@app.route('/survey_eco_cc_5')
def survey_eco_cc_5():

    data = dq.sr_ecocc5(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_cc_5.html",
        graph_srcc5 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='olivedrab')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 5 : Elected official and institution

@app.route('/survey_eco_eei_5')
def survey_eco_eei_5():

    data = dq.sr_ecoeei5(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_eei_5.html",
        graph_sreei5 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='mediumorchid')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 5 : for-profit organization

@app.route('/survey_eco_obl_5')
def survey_eco_obl_5():

    data = dq.sr_ecoobl5(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_obl_5.html",
        graph_srobl5 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='goldenrod')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 6 : non-profit organization

@app.route('/survey_eco_obnl_5')
def survey_eco_obnl_5():

    data = dq.sr_ecoobnl5(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_obnl_5.html",
        graph_srobnl5 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='chocolate')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# ------------------QUESTION 6--------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# Question 6 : Global

@app.route('/survey_eco_6')
def survey_eco_6():

    data = dq.sr_eco6(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        if dico['nb'] > 3000:
            x_data.append(dico['reponse'])
            y_data.append(dico['nb'])

    return render_template(
        "survey_eco_6.html",
        graph_sr6 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='indianred')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 6 : na

@app.route('/survey_eco_na_6')
def survey_eco_na_6():

    data = dq.sr_econa6(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        if dico['nb'] > 600:
            x_data.append(dico['reponse'])
            y_data.append(dico['nb'])

    return render_template(
        "survey_eco_na_6.html",
        graph_srna6 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='lightblue')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 6 : citizen

@app.route('/survey_eco_cc_6')
def survey_eco_cc_6():

    data = dq.sr_ecocc6(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        if dico['nb'] > 3000:
            x_data.append(dico['reponse'])
            y_data.append(dico['nb'])

    return render_template(
        "survey_eco_cc_6.html",
        graph_srcc6 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='olivedrab')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 6 : Elected official and institution

@app.route('/survey_eco_eei_6')
def survey_eco_eei_6():

    data = dq.sr_ecoeei6(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        if dico['nb'] > 30:
            x_data.append(dico['reponse'])
            y_data.append(dico['nb'])

    return render_template(
        "survey_eco_eei_6.html",
        graph_sreei6 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='mediumorchid')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 6 : for-profit organization

@app.route('/survey_eco_obl_6')
def survey_eco_obl_6():

    data = dq.sr_ecoobl6(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        if dico['nb'] >= 1:
            x_data.append(dico['reponse'])
            y_data.append(dico['nb'])

    return render_template(
        "survey_eco_obl_6.html",
        graph_srobl6 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='goldenrod')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 6 : non-profit organization

@app.route('/survey_eco_obnl_6')
def survey_eco_obnl_6():

    data = dq.sr_ecoobnl6(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        if dico['nb'] >= 6:
            x_data.append(dico['reponse'])
            y_data.append(dico['nb'])

    return render_template(
        "survey_eco_obnl_6.html",
        graph_srobnl6 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='chocolate')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# ------------------QUESTION 7--------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# Question 7 : Global

@app.route('/survey_eco_7')
def survey_eco_7():

    data = dq.sr_eco7(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_7.html",
        graph_sr7 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='indianred')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# Question 7 : na

@app.route('/survey_eco_na_7')
def survey_eco_na_7():

    data = dq.sr_econa7(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_na_7.html",
        graph_srna7 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='lightblue')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))


# ------------------------------------------------------------------------------------------------------------------
# Question 7 : citizen

@app.route('/survey_eco_cc_7')
def survey_eco_cc_7():

    data = dq.sr_ecocc7(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_cc_7.html",
        graph_srcc7 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='olivedrab')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))


# ------------------------------------------------------------------------------------------------------------------
# Question 7 : Elected official and institution

@app.route('/survey_eco_eei_7')
def survey_eco_eei_7():

    data = dq.sr_ecoeei7(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_eei_7.html",
        graph_sreei7 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='mediumorchid')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))


# ------------------------------------------------------------------------------------------------------------------
# Question 7 : for-profit organization

@app.route('/survey_eco_obl_7')
def survey_eco_obl_7():

    data = dq.sr_ecoobl7(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_obl_7.html",
        graph_srobl7 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='goldenrod')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))


# ------------------------------------------------------------------------------------------------------------------
# Question 7 : non-profit organization

@app.route('/survey_eco_obnl_7')
def survey_eco_obnl_7():

    data = dq.sr_ecoobnl7(settings, DB_NAME = "gdn_db")
    print(data)

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['reponse'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_obnl_7.html",
        graph_srobnl7 = json.dumps(
            [
                go.Bar(x = x_data, y = y_data, marker_color='chocolate')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
# ------------------ TIME ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# Evolution of contributions : Global

@app.route('/survey_eco_time')
def survey_eco_time():

    data = dq.sr_ecotime(settings, DB_NAME = "gdn_db")

    x_data = []
    y_data = []

    for i in range(len(data)):
        dico = data[i]
        x_data.append(dico['date'])
        y_data.append(dico['nb'])

    return render_template(
        "survey_eco_time.html",
        graph_srecotime = json.dumps(
            [
                go.Scatter(x = x_data, y = y_data, marker_color='indianred')
            ],
            cls = plotly.utils.PlotlyJSONEncoder
        ))

# ------------------------------------------------------------------------------------------------------------------
