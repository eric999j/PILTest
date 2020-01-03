# pip install wolframalpha
import wolframalpha

input = raw_input("Q: ")
app_id = "6RAWKL-X7529UYY4U"
client = wolframalpha.Client(app_id)

res = client.query(input)
answer = next(res.results).text

print answer
