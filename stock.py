import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait



def downloadStockHistoryCSV(stock_name): #incomplete
	#open chrome and direct to yahoo finance
	chrome_driver_path = "/mnt/d/bash/WebDrivers/chromedriver"
	browser = webdriver.Chrome(chrome_driver_path)
	yahoo_finance_url = "https://finance.yahoo.com/lookup"
	browser.get(yahoo_finance_url)
	#enter quote name into searchbox then wait for browser to redirect to new url
	search_box = browser.find_element_by_css_selector("input[name=p]")
	search_box.send_keys(stock_name)
	search_box.send_keys(Keys.ENTER)
	WebDriverWait(browser, 15).until(lambda driver : driver.current_url != yahoo_finance_url)
	#click on "historical data" tag and wait for correct section to appear

	#click on time period's dropdown button and wait for drop-down list to appear

	#click on "1Y" button in drop-down list

	#click on "Done" button and wait for drop-down list to disappear

	#click on "Apply" button and wait for data on web page to change

	#click on "download Data"

	#move csv file to correct dir
	url = browser.current_url
	acronym_start = url.find("p=")+2
	acronym_end = url.find("&")
	file_name = url[acronym_start:acronym_end]+".csv"
	print(file_name)
	return "StockData/"+file_name

def loadStockHistory(csv_path): #incomplete
	#
	return []

def splitTraining(history):
	size = len(history)
	end = math.floor(0.5*size)
	return history[:end]

def splitValidation(history):
	size = len(history)
	start = math.floor(0.5*size)
	end = math.floor(0.7*size)
	return history[start:end]

def splitTest(history):
	size = len(history)
	start = math.floor(0.7*size)
	return history[start:]

def trainModel(training, validation, test): #incomplete
	return (2, 3)

def plotModel(weight, bias): #incomplete
	print("weight is", weight)
	print("bias is", bias)

def main():
	csv_path = downloadStockHistoryCSV("IBM")
	stock_history = loadStockHistory(csv_path)
	training_set = splitTraining(stock_history) #0~0.5
	validation_set = splitValidation(stock_history) #0.5~0.7
	test_set = splitTest(stock_history)
	(weight, bias) = trainModel(training_set, validation_set, test_set)
	plotModel(weight, bias)

if __name__ == "__main__":
	main()
