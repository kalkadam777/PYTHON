movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#1
# def _imdb(l):
#     l1 = []
#     for i in l: 
#         l1.append(i["imdb"])
#     for i in l1:
#         if i>5.5:
#             print("True")
#         else:
#             print("False")
            
# print(_imdb(movies))
# 2
# def imdb(dict):
#     l = []
#     for i in dict:
#         if i["imdb"]>5.5:
#             l.append(i["name"])
#     return l
# print(imdb(movies))
# 3
# def Catg(cat):
#     l = []
#     for i,e in enumerate(movies):
#         if cat in e.values():
#             l.append(e['name'])
#     return l
# print(Catg("Thriller"))
# 4
# def MeanF(movies):
#     l = []
#     for i in movies:
#         l.append(i['imdb'])
#     return sum(l)/len(l)
# print(MeanF(movies))
#5
# def ImC(Cat):
#     l = []
#     for i,e in enumerate(movies):
#         if Cat in e.values():
#             l.append(e['imdb'])
#     return sum(l)/len(l)

# print(ImC("Romance"))
    
# print(l)