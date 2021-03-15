import math
from num2words import num2words
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
  if request.method == 'POST':
    text = request.form.get('text')
    coleman_liau_index = readability(text)
    return render_template('index.html', coleman_liau_index = coleman_liau_index)
  else:
    return render_template('index.html')


def readability(text):

  letters = 0
  words = 0
  sentences = 0

  for char in text:
    if char.isalpha():
      letters += 1
    if char.isspace():
      words += 1
    if char == '.' or char == '!' or char == '?':
      sentences += 1

  l = letters / words
  s = sentences / words
  index = 5.88 * (l) - 29.6 * (s) - 15.8

  level = {0: "Kindergarten", 1: "1st Grade", 2: "2nd Grade", 3: "3rd Grade", 4: "4th Grade", 5: "5th Grade", 6: "6th Grade", 7: "7th Grade", 9: "9th Grade", 10: "10th Grade", 11: "11th Grade", 12: "12th Grade", 13: "College: Freshman", 14: "College: Sophomore", 15: "College: Junior", 16: "College: Senior", 17: "Graduate School"}

  if index < 1:
    index = 0
  if index > 16:
    index = 17
  
  return (num2words(letters), num2words(words), num2words(sentences), level[math.ceil(index)])
