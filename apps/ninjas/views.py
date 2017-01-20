from django.shortcuts import render, HttpResponse, redirect

# Create your views here. THIS IS THE CONTROLLER

def index(request):
	something = "this is somethin"
	imgtag = "imageloc"
	context = {
		'turtle': something,
		'imgtag': imgtag
	}
	return render(request, 'ninjas/index.html', context)

def whichTurtle(request, color):
	print ("**************************")
	# if /ninjas display all four
	if color == "" :
		return render(request, 'ninjas/all.html')
	# if /ninjas/red ==> raph
	elif color == "red":
		return render(request, 'ninjas/raph.html')
			# if /ninjas/organe ====> Mikey
	elif color == "orange":
		return render(request, 'ninjas/mikey.html')
			# if /ninjas/purple ====> Donnie
	elif color == "purple":
		return render(request, 'ninjas/don.html')
			# if /ninjas/blue ====> leo
	elif color == "blue":
		return render(request, 'ninjas/leo.html')
	# else megan fox
	else :
		return render(request, 'ninjas/april.html')
