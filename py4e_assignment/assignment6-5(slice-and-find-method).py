#method slice and find application
text = "X-DSPAM-Confidence:    0.8475"
zero=text.find("0")
slice=text[zero:]
FS=float(slice)
print(FS)