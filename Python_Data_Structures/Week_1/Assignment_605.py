text = "X-DSPAM-Confidence:    0.8475"
ntext = text.find("0")
ntext1= text.find("5")
print(float(text[ntext:ntext1+1]))
