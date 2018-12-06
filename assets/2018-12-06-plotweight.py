from datetime import datetime, timedelta
from urllib.parse import unquote

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np


def get_image(plt):
	from ui import Image
	from io import BytesIO
	
	data = BytesIO()
	plt.savefig(data)
	data = data.getvalue()
	plt.close()
	
	return Image.from_data(data)
	

def parse_date(s):
	s = s[:-4] + s[-4:].replace(':', '')  # Timezone
	return datetime.strptime(s, '%Y-%m-%dT%H:%M:%S%z')
	
	
def trend(x_dates, y, degree=1):
	datenums = mdates.date2num(x_dates)
	polyfit = np.polyfit(datenums, y, degree)
	poly = np.poly1d(polyfit)
	return poly(datenums)


def plot(data):
	dates, weights = list(zip(*data))
	
	dates = [parse_date(s) for s in dates]
	weights = np.array(weights, dtype='float')
	trends = trend(dates, weights, degree=3)
	
	# Styling
	plt.title('Weight')
	plt.ylabel('kg')
	plt.grid()
	plt.gcf().autofmt_xdate()
	padding = timedelta(days=5)
	plt.xlim(dates[0]-padding, dates[-1]+padding)
	
	ax = plt.gca()
	ax.set_axisbelow(True)
	for spine in ax.spines.values():
		spine.set_visible(False)
	ax.xaxis.tick_bottom()
	ax.yaxis.tick_left()
	ax.tick_params(axis='both', direction='out')
	
	style = {
		'linewidth': 2,
		'color': '#9883e5',
		'markersize': 4,
		'markeredgecolor': '#4c3799'
	}
	
	trend_style = {
		'linewidth': 2,
		'color': '#49ba6f'
	}
	
	plt.plot(dates, trends, '--', **trend_style)
	plt.plot(dates, weights, 'o-', **style)
	
	return get_image(plt)
	

if __name__ == '__main__':
	import csv
	import sys
	import clipboard
	import webbrowser

	callback_url = unquote(sys.argv[1])
	data = unquote(sys.argv[2]).split('\n')
	
	reader = csv.reader(data, delimiter=';')
	data = list(reader)[1:]  # Skip header
	image = plot(data)
	
	clipboard.set_image(image)
	webbrowser.open(callback_url)
