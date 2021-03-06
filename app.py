from flask import render_template, Flask, request
from datetime import time
from mysql_to_sqlite import DButil
import os
#http://tobiasahlin.com/blog/chartjs-charts-to-get-you-started


app = Flask(__name__)


@app.route("/simple_chart")
def chart():
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template('chart.html', values=values, labels=labels, legend=legend)


@app.route("/line_chart")
def line_chart():
    legend = 'Temperatures'
    temperatures = [73.7, 73.4, 73.8, 72.8, 68.7, 65.2,
                    61.8, 58.7, 58.2, 58.3, 60.5, 65.7,
                    70.2, 71.4, 71.2, 70.9, 71.3, 71.1]
    times = ['12:00PM', '12:10PM', '12:20PM', '12:30PM', '12:40PM', '12:50PM',
             '1:00PM', '1:10PM', '1:20PM', '1:30PM', '1:40PM', '1:50PM',
             '2:00PM', '2:10PM', '2:20PM', '2:30PM', '2:40PM', '2:50PM']
    return render_template('line_chart.html', values=temperatures, labels=times, legend=legend)


@app.route("/time_chart")
def time_chart():
    legend = 'Temperatures'
    temperatures = [73.7, 73.4, 73.8, 72.8, 68.7, 65.2,
                    61.8, 58.7, 58.2, 58.3, 60.5, 65.7,
                    70.2, 71.4, 71.2, 70.9, 71.3, 71.1]
    times = [time(hour=11, minute=14, second=15),
             time(hour=11, minute=14, second=30),
             time(hour=11, minute=14, second=45),
             time(hour=11, minute=15, second=00),
             time(hour=11, minute=15, second=15),
             time(hour=11, minute=15, second=30),
             time(hour=11, minute=15, second=45),
             time(hour=11, minute=16, second=00),
             time(hour=11, minute=16, second=15),
             time(hour=11, minute=16, second=30),
             time(hour=11, minute=16, second=45),
             time(hour=11, minute=17, second=00),
             time(hour=11, minute=17, second=15),
             time(hour=11, minute=17, second=30),
             time(hour=11, minute=17, second=45),
             time(hour=11, minute=18, second=00),
             time(hour=11, minute=18, second=15),
             time(hour=11, minute=18, second=30)]
    return render_template('time_chart.html', values=temperatures, labels=times, legend=legend)

@app.route("/bar_chart")
def bar_chart(): 
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    colors = [ "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC"  ]
    return render_template('bar_chart.html', values=values,labels=labels, colors=colors)

@app.route("/group_chart")
def group_chart():
    labels=["1900", "1950", "1999", "2050"]
    countries={'Africa': { 'color': "#3e95cd", 'values': [133,221,783,2478]}, 'Europe': { 'color': "#8e5ea2", 'values': [408,547,675,734]} }
    return render_template('group_chart.html', labelss=labels, countries=countries)

@app.route("/dbcache",methods=['GET','POST'])
def dbcache():
    if request.method == 'POST':
        if not os.path.isfile('test.db'):
            DButil()
    return render_template('clean_cache.html')

if __name__ == "__main__":
    app.run(debug=True,port=8000)
