text=input("please enter the text: \n")

# if ("subscribe my channel" in text):
#     spam=True
if(("buy now"or"click this"or"subscribe my channel") in text):
    spam=True
# elif("click this"in text):
#     spam=True
else:
    spam=False

if(spam):
    print("this is spam")
else:
    print("this is not spam")