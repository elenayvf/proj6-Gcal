import arrow
import datetime 

present = arrow.utcnow()
future = present.replace(days =+ 2)
hello = future.date()

new = present.replace(hour= future.hour)

start = arrow.get(2013, 5, 5, 12, 30)
end = arrow.get(2013, 5, 12, 17, 15)

for r in arrow.Arrow.span_range('day', start, end):
	q = r[0]
	p = q.minute
	#j = p.hour()
	#l = p.minute()
	s = r[1] 
	print(r)
	print (type(p))
	#print(j)
	#print(p)
	
	print(type(r))
	