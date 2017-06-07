from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def query(request):
	return render(request, 'database/query.html')

def query_result(request):
	sql = request.POST['query']
	if sql:
		rows = _my_custom_sql(sql=sql)
		print(rows)
	else:
		rows = 'error'
	return render(request, 'database/query.html', context = {'rows':rows, 'sql':sql})
	
def button(request):
	return render(request, 'database/button.html')

def button_result(request):
	from_list = request.POST.getlist('from')
	from_list = ["database_" + table for table in from_list]
	select_list = request.POST.getlist('select')
	select_list = ["database_" + field for field in select_list]
	where = request.POST['where']
	
	sql = "SELECT {select_sql} FROM {from_sql};".format(
		select_sql=', '.join(select_list),
		from_sql=', '.join(from_list),
	)
	if where:
		sql = sql + "WHERE" + where

	rows = _my_custom_sql(sql)
	return render(request, 'database/button.html', context = {'rows':rows, 'sql':sql})


def _my_custom_sql(sql):
	cursor = connection.cursor()
	try:
		cursor.execute(sql)
		row = cursor.fetchall()
	except:
		row = 'error'
	finally:
		cursor.close()
		return row